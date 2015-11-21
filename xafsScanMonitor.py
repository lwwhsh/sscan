#!/usr/bin/python
"""
Epics MCA Display application
"""
import numpy as np
import wx
from wxmplot.plotpanel import PlotPanel

ICON_FILE = 'stripchart.ico'
FILECHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

BGCOL = (250, 250, 240)

MENU_EXIT = wx.NewId()
MENU_SAVE_IMG = wx.NewId()
MENU_SAVE_DAT = wx.NewId()
MENU_CONFIG = wx.NewId()
MENU_UNZOOM = wx.NewId()
MENU_HELP = wx.NewId()
MENU_ABOUT = wx.NewId()
MENU_PRINT = wx.NewId()
MENU_PSETUP = wx.NewId()
MENU_PREVIEW = wx.NewId()
MENU_CLIPB = wx.NewId()
MENU_SELECT_COLOR = wx.NewId()
MENU_SELECT_SMOOTH = wx.NewId()


def get_bound(val):
    """return float value of input string or None"""
    val = val.strip()
    if len(val) == 0 or val is None:
        return None
    try:
        val = float(val)
    except:
        val = None
    return val


class MyChoice(wx.Choice):
    """Simplified wx Choice"""

    def __init__(self, parent, choices=('No', 'Yes'),
                 defaultyes=True, size=(75, -1)):
        wx.Choice.__init__(self, parent, -1, size=size)
        self.choices = choices
        self.Clear()
        self.SetItems(self.choices)
        self.SetSelection({False: 0, True: 1}[defaultyes])

    def SetChoices(self, choices):
        self.Clear()
        self.SetItems(choices)
        self.choices = choices

    def Select(self, choice):
        if isinstance(choice, int):
            self.SetSelection(choice)
        elif choice in self.choices:
            self.SetSelection(self.choices.index(choice))


class ScanDisplay(wx.Frame):
    help_msg = """Quick help:

 Left-Click:   to display X,Y coordinates
 Left-Drag:    to zoom in on plot region
 Right-Click:  display popup menu with choices:
                Zoom out 1 level
                Zoom all the way out
                --------------------
                Configure
                Save Image

Also, these key bindings can be used
(For Mac OSX, replace 'Ctrl' with 'Apple'):

  Ctrl-S:     save plot image to file
  Ctrl-C:     copy plot image to clipboard
  Ctrl-K:     Configure Plot
  Ctrl-Q:     quit

"""

    about_msg = """Epics MCA Display version 1.0
PLS XAFS Beamline.>
"""

    def __init__(self, parent=None, *args, **kwargs):
        self.parent = None
        self.plotpanel = None
        self.plot_en = None  # check first plot

        self.needs_refresh = False
        self.create_frame(parent)

    def create_frame(self, parent, size=(900, 540), **kwds):  # (900,540), (750, 450)
        self.parent = parent

        kwds['style'] = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL
        kwds['size'] = size
        wx.Frame.__init__(self, parent, -1, 'XAFS Scan viewer', **kwds)
        self.Show()

        self.build_statusbar()
        self.plotpanel = PlotPanel(self,
                                   #trace_color_callback=self.onTraceColor,
                                   axissize=[0.08, 0.06, 0.91, 0.92])
        self.plotpanel.messenger = self.write_message
        self.build_menus()
        self.SetBackgroundColour(wx.Colour(*BGCOL))

        mainsizer = wx.BoxSizer(wx.VERTICAL)

        mainsizer.Add(self.plotpanel, 1, wx.EXPAND, 5)
        self.SetAutoLayout(True)
        self.SetSizer(mainsizer)
        self.Fit()

        try:
            self.SetIcon(wx.Icon(ICON_FILE, wx.BITMAP_TYPE_ICO))
        except:
            pass

        self.Refresh()

    def build_statusbar(self):
        sbar = self.CreateStatusBar(2, wx.CAPTION | wx.THICK_FRAME)
        sfont = sbar.GetFont()
        sfont.SetWeight(wx.BOLD)
        sfont.SetPointSize(10)
        sbar.SetFont(sfont)
        self.SetStatusWidths([-5, -2])
        self.SetStatusText('', 0)

    def write_message(self, s, panel=0):
        """write a message to the Status Bar"""
        self.SetStatusText(s, panel)

    def build_menus(self):
        mbar = wx.MenuBar()

        mfile = wx.Menu()
        mfile.Append(MENU_SAVE_DAT, "&Save Data\tCtrl+S",
                     "Save PNG Image of Plot")
        mfile.Append(MENU_SAVE_IMG, "Save Plot Image\t",
                     "Save PNG Image of Plot")
        mfile.Append(MENU_CLIPB, "&Copy Image to Clipboard\tCtrl+C",
                     "Copy Plot Image to Clipboard")
        mfile.AppendSeparator()
        mfile.Append(MENU_PSETUP, 'Page Setup...', 'Printer Setup')
        mfile.Append(MENU_PREVIEW, 'Print Preview...', 'Print Preview')
        mfile.Append(MENU_PRINT, "&Print\tCtrl+P", "Print Plot")
        mfile.AppendSeparator()
        mfile.Append(MENU_EXIT, "E&xit\tCtrl+Q", "Exit the 2D Plot Window")

        mopt = wx.Menu()
        mopt.Append(MENU_CONFIG, "Configure Plot\tCtrl+K",
                    "Configure Plot styles, colors, labels, etc")
        mopt.AppendSeparator()
        mopt.Append(MENU_UNZOOM, "Zoom Out\tCtrl+Z",
                    "Zoom out to full data range")

        mhelp = wx.Menu()
        mhelp.Append(MENU_HELP, "Quick Reference", "Quick Reference for MPlot")
        mhelp.Append(MENU_ABOUT, "About", "About MPlot")

        mbar.Append(mfile, "File")
        mbar.Append(mopt, "Options")
        mbar.Append(mhelp, "&Help")

        self.SetMenuBar(mbar)
        self.Bind(wx.EVT_MENU, self.onHelp, id=MENU_HELP)
        self.Bind(wx.EVT_MENU, self.onAbout, id=MENU_ABOUT)
        self.Bind(wx.EVT_MENU, self.onExit, id=MENU_EXIT)
        self.Bind(wx.EVT_CLOSE, self.onExit)

        pp = self.plotpanel
        self.Bind(wx.EVT_MENU, pp.configure, id=MENU_CONFIG)
        self.Bind(wx.EVT_MENU, pp.unzoom_all, id=MENU_UNZOOM)
        self.Bind(wx.EVT_MENU, pp.save_figure, id=MENU_SAVE_IMG)
        self.Bind(wx.EVT_MENU, pp.Print, id=MENU_PRINT)
        self.Bind(wx.EVT_MENU, pp.PrintSetup, id=MENU_PSETUP)
        self.Bind(wx.EVT_MENU, pp.PrintPreview, id=MENU_PREVIEW)
        self.Bind(wx.EVT_MENU, pp.canvas.Copy_to_Clipboard, id=MENU_CLIPB)
    '''
    def onTraceColor(self, trace, color, **kws):
        irow = self.get_current_traces()[trace][0] - 1
        self.colorsels[irow].SetColour(color)
    '''
    def onAbout(self, event=None):
        dlg = wx.MessageDialog(self, self.about_msg,
                               "About Epics MCA Display",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def onHelp(self, event=None):
        dlg = wx.MessageDialog(self, self.help_msg, "XAFS scan viewer help",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def onExit(self, event=None):
        try:
            self.plotpanel.win_config.Close(True)
            self.plotpanel.win_config.Destroy()
        except:
            pass

        self.Destroy()
    '''
    def get_current_traces(self):
        """return list of current traces"""
        traces = []  # to be shown

        for irow, s in enumerate(self.pvchoices):
            if s is not None:
                ix = s.GetSelection()
                if ix > 0:
                    name = self.pvlist[ix]
                    logs = 1 == self.pvwids[irow][0].GetSelection()
                    color = self.pvwids[irow][1].GetColour()
                    ymin = get_bound(self.pvwids[irow][2].GetValue())
                    ymax = get_bound(self.pvwids[irow][3].GetValue())
                    traces.append((irow, name, logs, color, ymin, ymax))

        return traces
    '''
    def onUpdatePlot(self, **kwargs):
        if len(kwargs['plotXdata']) < 3:
            return

        Xdata = np.asarray(kwargs['plotXdata'])
        Ydata = np.asarray(kwargs['plotYdata'])

        ppanel = self.plotpanel
        did_update = False

        if self.plot_en is None or False:  # first plot!
            self.plot_en = True

            ppanel.plot(Xdata, Ydata,
                        linewidth=0.5, marker='o',
                        markersize=4, xlabel='energy[eV]',
                        ylabel='[count]')
            did_update = True

        else:  # update line(s)!.
            try:
                ppanel.update_line(0, Xdata, Ydata,
                                   draw=True, update_limits=True)

                did_update = True
            except Exception as e:
                print 'XAFS scan viewer have exception!!!\n %s\n' % e.message
                pass

        if did_update:  # update plot xy limits!
            ppanel.set_xylims((Xdata[0], Xdata[len(Xdata)-1],
                               Ydata.min(), Ydata.max()))
            ppanel.canvas.draw()

        self.needs_refresh = not did_update

        #print ' PLOT Complete in ScanDiaplay class : %s' % (time.ctime())
        return

if __name__ == '__main__':
    app = wx.App()
    f = ScanDisplay(None, -1)
    f.Show(True)
    app.MainLoop()
