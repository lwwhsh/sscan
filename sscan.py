# -----------------------------------------------------------------------------
#   EPICS SSCAN,
#      XAFS scan program
#      (currently built for the XAFS Beamline at Pohang Light Source(South Korea)
# -----------------------------------------------------------------------------
#   Authors:
#   Woulwoo Lee, XAS Beamline
#   I got many ideas(codes) from Sakura and epicsStepScan software
#   Many thanks Peter and Matt Newvil
#   Pohang Light Source Korea, 2014
# -*- coding: utf-8 -*-

import wx   # suppress import warning    @UnusedImport
from scan_ui import SscanBaseMainFrame
import wx.lib.mixins.inspection


class SscanWxApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    """
    The main application class - added a wxPython inspection tool
       http://wiki.wxpython.org/Widget%20Inspection%20Tool
    """

    def OnInit(self):
        self.Init()  # initialize the inspection tool
        self.m_frame = SscanBaseMainFrame(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

if __name__ == '__main__':
    app = SscanWxApp(0)
    app.MainLoop()
