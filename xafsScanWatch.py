"""
XAFS Plot
Designed by LWW
2014.10.5
some change for zoom-in at plotpanel.py, config.py in wxmplot module Ver0.9.4
wxmplot compiled on matplotlib version 1.4

"""
import sys
if not hasattr(sys, 'frozen'):
    import wxversion
    wxversion.ensureMinimal('2.8')

import wx
import time
import numpy as np
from wxmplot.plotframe import PlotFrame
from epics import PV, poll
from epics.wx import EpicsFunction, DelayedEpicsCallback


class XAFSviewerFrame(wx.Frame):
    def __init__(self, parent=None, *args, **kwds):

        kwds["style"] = wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL

        wx.Frame.__init__(self, parent, wx.NewId(), '', wx.DefaultPosition, wx.Size(-1, -1), **kwds)
        self.SetTitle(" WXMPlot Plotting Demo")

        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        menu = wx.Menu()
        ID_EXIT = wx.NewId()
        ID_TIMER = wx.NewId()

        menu.Append(ID_EXIT, "E&xit", "Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        wx.EVT_MENU(self, ID_EXIT, self.OnExit)

        self.Bind(wx.EVT_CLOSE, self.OnExit)
        
        self.plotframe = None

        framesizer = wx.BoxSizer(wx.VERTICAL)

        panel = wx.Panel(self, -1, size=(-1, -1))
        panelsizer = wx.BoxSizer(wx.VERTICAL)

        panelsizer.Add(wx.StaticText(panel, -1, 'XAFS Spectra viewer '),
                       0, wx.ALIGN_LEFT | wx.ALIGN_CENTER | wx.LEFT | wx.EXPAND, 10)

        b40 = wx.Button(panel, -1, 'Start Timed Plot',    size=(-1, -1))
        b40.Bind(wx.EVT_BUTTON,self.onStartTimer)
        panelsizer.Add(b40, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER | wx.LEFT, 5)

        panel.SetSizer(panelsizer)
        panelsizer.Fit(panel)

        framesizer.Add(panel, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER | wx.EXPAND, 2)
        self.SetSizer(framesizer)
        framesizer.Fit(self)

        #----------------------------------------------------------------------
        self.dxpPrefix = 'dxpXMAP:'
        self.NofDet = 13
        # 1st make mca name list
        # string list [mca0, mca1, mca2, ..., mca12]
        self.mcaList = ['mca%i' % (i+1) for i in range(self.NofDet)]
        # text name: dxpXMAP:mca1, dxpXMAP:mca2, ...., is not PV
        self.mcaNetNameList = ['%s%s.R0' % (self.dxpPrefix, self.mcaList[i])
                               for i in range(self.NofDet)]

        self.plotYdata = []
        self.plotXdata = []
        self.plotMCAdata = []

        self.ShowPlotFrame(do_raise=False, clear=False)

        self.time0 = time.time()

        wx.EVT_TIMER(self, ID_TIMER, self.onTimer)
        self.timer = wx.Timer(self, ID_TIMER)

        self.init_epics()

        self.Refresh()

    @EpicsFunction
    def init_epics(self):
        # make PV object.
        #  for scaler
        self.i0 = PV('BL10C:scaler1_calc2.VAL')
        self.it = PV('BL10C:scaler1_calc3.VAL')
        self.iF = PV('BL10C:scaler1_calc4.VAL')
        self.trans = PV('BL10C:scaler1_calc8.VAL')

        # for Energy
        self.energyPV = PV('BL10C:SM1.RBV')

        # for scan
        # self.scanStart = PV('BL10C:scan2.EXSC.VAL', callback=self.scanStartCALLBACK)

        while self.energyPV.get() is None:
            print self.energyPV.get()

        self.mcaNetPV = [PV(self.mcaNetNameList[i]) for i in range(self.NofDet)]
        print [self.mcaNetPV[i].get() for i in range(self.NofDet)]

        # for XMAP
        self.dxpEraseStartPV = PV('dxpXMAP:EraseStart')
        self.dxpAcquiringPV = PV('dxpXMAP:Acquiring', callback=self.onMCADataCALLBACK)

        self.energyDonePV = PV('BL10C:SM1.DMOV', callback=self.bl10cEnergyDoneCALLBACK)
        self.countDonePV = PV('BL10C:scaler1.CNT') # , callback=self.countDoneCALLBACK)

        poll()

        #  self.mcaPV = [PV(self.mcaNameList[i]) for i in range(self.NofDet)]

    def bl10cEnergyDoneCALLBACK(self, **kwargs):
        if kwargs['value'] is 0:  # 1:Done, 0: moving
            return

        self.moveDoneFlag = True
        print 'move done callback'
        return

    def onMCADataCALLBACK(self, **kwargs):
        if kwargs['value'] is 1:  # 0:Done, 1: Acquiring
            return

        self.countDoneFlag = True

        return

    def countDoneCALLBACK(self, **kwargs):
        if kwargs['value'] is 1:  # 0:Done, 1:Counting
            return

        # self.countDoneFlag = True
        print 'count done callback'
            
    def ShowPlotFrame(self, do_raise=True, clear=True):
        """make sure plot frame is enabled, and visible"""
        if self.plotframe is None:
            self.plotframe = PlotFrame(self, axissize=[0.08, 0.06, 0.91, 0.92])
            # self.has_plot = False
        try:
            self.plotframe.Show()
        except wx.PyDeadObjectError:
            self.plotframe = PlotFrame(self, axissize=[0.08, 0.06, 0.91, 0.92])
            self.plotframe.Show()

        if do_raise:
            self.plotframe.Raise()
        if clear:
            self.plotframe.panel.clear()
            self.plotframe.reset_config()
            
            self.plotYdata = []
            self.plotXdata = []
            self.plotMCAdata = []

    def onStartTimer(self,event=None):
        self.count    = 0
        self.up_count = 0
        self.n_update = 1
        self.datrange = None
        self.moveDoneFlag = False
        self.countDoneFlag = False
        self.eraseStartValue = False
        self.time0 = time.time()
        self.timer.Start(10)

    def onTimer(self, event):
        if not self.moveDoneFlag and not self.countDoneFlag:
            return

        if self.moveDoneFlag:
            self.dxpEraseStartPV.put(not self.eraseStartValue)  # XMAP start!
            self.countDonePV.put(1)  # count start!

            #  self.plotXdata.append(self.energyPV.get())  # read energy

            self.moveDoneFlag = not self.moveDoneFlag
            self.eraseStartValue = not self.eraseStartValue

            print 'Energy move done! Count/DXP Start Triggered!!!'

        if self.countDoneFlag:  # and self._flag
            if self.count == 0:  # 1st time in callback
                self.count += 1
                self.countDoneFlag = not self.countDoneFlag
                return

            self.countDoneFlag = not self.countDoneFlag

            # read energy
            self.plotXdata.append(self.energyPV.get())

            # for Trans.
            self.plotYdata.append(self.trans.get())

            # for MCA
            #mcaNetAll = [self.mcaNetPV[i].get() for i in range(self.NofDet)]
            #norm = sum(mcaNetAll) / self.NofDet / self.i0.get()
            #self.plotYdata.append(norm)

            print 'mca get: %s' % (self.plotYdata[-1:])
            print 'X:%s,  Y:%s' % (len(self.plotXdata), len(self.plotYdata))

            # Todo: we need new scan start sequence.
            #       new list, graph clear, data save...,
            # print 'timer ', self.count, time.time()
            ## self.count += 1
            #self.ShowPlotFrame(do_raise=False, clear=False)
            ## n = self.count
            if len(self.plotXdata) < 2:
                return
            # Todo: implementation of scan finish sequence.

            if len(self.plotXdata) <= 3:
                self.plotframe.plot(self.plotXdata, self.plotYdata,
                                    linewidth=0.5, marker='o',
                                    markersize=6, xlabel='energy[eV]',
                                    ylabel='[count]')
                                    # , grid=False)

            else:
                xx = np.array(self.plotXdata)
                yy = np.array(self.plotYdata)

                # Todo: Xdata, Ydata must be same length(need threding)
                try:
                    self.plotframe.update_line(0, xx, yy, update_limits=len(xx) < 10, draw=True)
                except Exception:
                    pass

                etime = time.time() - self.time0
                s = " %i / %i points in %8.4f s" % (len(self.plotXdata), len(self.plotYdata), etime)
                self.plotframe.write_message(s)

            if self.datrange is None:
                self.datrange = [min(self.plotXdata), max(self.plotXdata), min(self.plotYdata), max(self.plotYdata)]

            dr = [min(self.plotXdata), max(self.plotXdata),
                  min(self.plotYdata), max(self.plotYdata)]

            lims = self.plotframe.panel.get_viewlimits()
            if dr[0] < lims[0] or dr[1] > lims[1] or dr[2] < lims[2] or dr[3] > lims[3]:
                self.datrange = dr
                ## if len(self.plotXdata) < len(self.x):
                ##     nmax = min(int(n*1.6), len(self.x)-1)
                ##     self.datrange[1] = self.x[nmax]
                try:
                    self.plotframe.panel.set_xylims(self.datrange)
                except Exception:
                    pass

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "This program shows MCA Spectra\n"
                                     "message dialog.",
                                     "About MPlot test", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        # 1st. disconnect PV(s)
        self.countDonePV.clear_callbacks()
        self.i0.disconnect()
        self.it.disconnect()
        self.iF.disconnect()
        self.trans.disconnect()
        self.energyPV.disconnect()
        
        try:
            if self.plotframe is not None:
                self.plotframe.onExit()
        except:
            pass
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    f = XAFSviewerFrame(None, -1)
    f.Show(True)
    app.MainLoop()
