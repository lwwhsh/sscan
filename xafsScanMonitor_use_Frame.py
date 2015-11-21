"""
XAFS Plot
Designed by LWW
2014.10.5
some change for zoom-in at plotpanel.py, config.py in wxmplot module Ver0.9.4
wxmplot compiled on matplotlib version 1.4

"""
import sys
import wx
import time
import numpy as np
from wxmplot.plotframe import PlotFrame
from epics import PV


class XAFSviewerFrame(wx.Frame):
    def __init__(self, parent=None, *args, **kwds):

        #kwds["style"] = wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, parent, wx.NewId(), '', wx.DefaultPosition, wx.Size(-1, -1), **kwds)
        #self.SetTitle(" WXMPlot Plotting Demo")
        """
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
        """
        self.plotframe = None
        """
        framesizer = wx.BoxSizer(wx.VERTICAL)

        panel = wx.Panel(self, -1, size=(-1, -1))
        panelsizer = wx.BoxSizer(wx.VERTICAL)

        panelsizer.Add(wx.StaticText(panel, -1, 'XAFS Spectra viewer '),
                       0, wx.ALIGN_LEFT | wx.ALIGN_CENTER | wx.LEFT | wx.EXPAND, 10)

        b40 = wx.Button(panel, -1, 'Start Timed Plot',    size=(-1, -1))
        #b40.Bind(wx.EVT_BUTTON,self.onStartTimer)
        panelsizer.Add(b40, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER | wx.LEFT, 5)

        panel.SetSizer(panelsizer)
        panelsizer.Fit(panel)

        framesizer.Add(panel, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER | wx.EXPAND, 2)
        self.SetSizer(framesizer)
        framesizer.Fit(self)
        """

        #----------- added by LWW -----------------------------
        #====== self.showPlotFrame(do_raise=False, clear=False)
        """
        self.plotYdata = []
        self.plotXdata = []

        # ----------epics PVs-----------------------
        self.i0 = PV('BL10C:scaler1_calc2.VAL')
        self.it = PV('BL10C:scaler1_calc3.VAL')
        self.iF = PV('BL10C:scaler1_calc4.VAL')
        self.trans = PV('BL10C:scaler1_calc8.VAL')
        self.motorPos = PV('mobiis:m2.RBV')
        
        self.scanStart = PV('lww:scan2.EXSC.VAL', callback=self.scanStartCALLBACK)

        while self.motorPos.get() is None:
            print self.motorPos.get()

        self.countDonePV = PV('BL10C:scaler1.CNT', callback=self.countDoneCALLBACK)
        """

        self.time0 = time.time()
        self.datrange = None
        #----------- end of add by LWW -----------------------
        
        #wx.EVT_TIMER(self, ID_TIMER, self.onTimer)
        #self.timer = wx.Timer(self, ID_TIMER)
        """
        self.Refresh()
        """

    # --------------epics callback method---------------------
    def scanStartCALLBACK(self, **kwargs):
        if kwargs['value'] is 1:  # 0:Done, 1: scanning
            self.showPlotFrame(do_raise=True, clear=False)
            print 'New Scan Started!!!'
        else:
            print 'scan stopped!!!'
        return
    
    def countDoneCALLBACK(self, **kwargs):
        """
        if kwargs['value'] is 1:  # 0:Done, 1:Counting
            return

        ## self._flag = True
        self.plotYdata.append(self.trans.get())
        self.plotXdata.append(self.motorPos.get())
        ## self._flag = False
        """
        self.plotXdata = kwargs['plotXdata']
        self.plotYdata = kwargs['plotYdata']
        print 'X:%s, Y:%s' % (len(self.plotXdata), len(self.plotYdata))
        
        # Todo: we need new scan start sequence.
        #       new list, graph clear, data save...,
        # print 'timer ', self.count, time.time()
        ## self.count += 1
        #self.showPlotFrame(do_raise=False, clear=False)
        ## n = self.count
        if len(self.plotXdata) < 2:
            return
        # Todo: implementation of scan finish sequence.
        '''
        if n >= self.npts:
            self.timer.Stop()
            self.timer_results()
        elif n <= 3:
        '''
        if len(self.plotXdata) <= 3:
            self.plotframe.plot(self.plotXdata, self.plotYdata,
                                linewidth=0.5, marker='o',
                                markersize=6, xlabel='energy[eV]',
                                ylabel='[count]')
                                # , grid=False)

        else:
            xx = np.array(self.plotXdata)
            yy = np.array(self.plotYdata)
            
            self.plotframe.update_line(0, xx, yy, update_limits=len(xx) < 10, draw=True)
            
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
            self.plotframe.panel.set_xylims(self.datrange)
            
    def showPlotFrame(self, do_raise=True, clear=True):
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
        '''
        if clear:
            self.plotframe.panel.clear()
            self.plotframe.reset_config()

            self.plotYdata = []
            self.plotXdata = []
        '''
        if clear is True:
            self.clearPlot()

    def clearPlot(self):
        self.plotframe.panel.clear()
        self.plotframe.reset_config()

        self.plotYdata = []
        self.plotXdata = []

    '''    
    def onStartTimer(self,event=None):
        self.count    = 0
        self.up_count = 0
        self.n_update = 1
        self.datrange = None
        self.time0    = time.time()
        ### LWW self.start_mem= self.report_memory()
        self.timer.Start(10)
        # self.timer.Start(500)
    
    def timer_results(self):
        if (self.count < 2): return
        etime = time.time() - self.time0
        tpp   = etime/max(1,self.count)
        s = "drew %i points in %8.3f s: time/point= %8.4f s" % (self.count,etime,tpp)
        self.plotframe.write_message(s)
        self.time0 = 0
        self.count = 0
        self.datrange = None
    '''
    '''
    def onTimer(self, event):
        # print 'timer ', self.count, time.time()
        self.count += 1
        self.showPlotFrame(do_raise=False, clear=False)
        n = self.count
        if n < 2:
            return
        if n >= self.npts:
            self.timer.Stop()
            self.timer_results()
        elif n <= 3:
            self.plotframe.plot(self.x[:n], self.y1[:n])# , grid=False)

        else:
            self.plotframe.update_line(0, self.x[:n], self.y1[:n], update_limits=n<10, draw=True)

            etime = time.time() - self.time0
            s = " %i / %i points in %8.4f s" % (n,self.npts,etime)
            self.plotframe.write_message(s)

        if self.datrange is None:
            self.datrange = [min(self.x[:n]), max(self.x[:n]),
                             min(self.y1[:n]),max(self.y1[:n])]

        dr = [min(self.x[:n]),  max(self.x[:n]),
              min(self.y1[:n]), max(self.y1[:n])]
        
        lims = self.plotframe.panel.get_viewlimits()
        if dr[0] < lims[0] or dr[1] > lims[1] or dr[2] < lims[2] or dr[3] > lims[3]:
            self.datrange = dr
            if n < len(self.x):
                nmax = min(int(n*1.6), len(self.x)-1)
                self.datrange[1] = self.x[nmax]
            self.plotframe.panel.set_xylims(self.datrange)
    '''
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "This program shows MCA Spectra\n"
                                     "message dialog.",
                                     "About MPlot test", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        """
        # 1st. disconnect PV(s)
        self.countDonePV.clear_callbacks()
        self.i0.disconnect()
        self.it.disconnect()
        self.iF.disconnect()
        self.trans.disconnect()
        self.motorPos.disconnect()
        """
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
