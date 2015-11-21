# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"-- EPICS sscan --", pos = wx.DefaultPosition, size = wx.Size( 998,819 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bMainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_MainPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bMainFrameSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_LeftPanel = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_LeftPanel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_LeftPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.m_LeftPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Scan Status", wx.DefaultPosition, wx.Size( 400,-1 ), wx.ALIGN_CENTRE|wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 22, 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_staticText3.SetToolTipString( u"Display scan status" )
		
		bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 4, 5, 0, 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.AddGrowableCol( 2 )
		fgSizer3.AddGrowableCol( 3 )
		fgSizer3.AddGrowableCol( 4 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.m_staticStatus = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticStatus.Wrap( -1 )
		fgSizer3.Add( self.m_staticStatus, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextColIo = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Io(Incident)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextColIo.Wrap( -1 )
		self.m_staticTextColIo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticTextColIo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticTextColIf = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"If(fluorescence)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextColIf.Wrap( -1 )
		self.m_staticTextColIf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticTextColIf, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextColIt = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"It(transmittance)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextColIt.Wrap( -1 )
		self.m_staticTextColIt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticTextColIt, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextCorIr = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Ir(reference)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticTextCorIr.Wrap( -1 )
		self.m_staticTextCorIr.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticTextCorIr, 0, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticStatusGain = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Gain:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusGain.Wrap( -1 )
		self.m_staticStatusGain.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusGain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticStatusGainIo = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"IoGain", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusGainIo.Wrap( -1 )
		self.m_staticStatusGainIo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusGainIo, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticStatusGainIf = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"IfGain", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusGainIf.Wrap( -1 )
		self.m_staticStatusGainIf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusGainIf, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticStatusGainIt = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"ItGain", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusGainIt.Wrap( -1 )
		self.m_staticStatusGainIt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusGainIt, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticStatusGainIr = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"IrGain", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusGainIr.Wrap( -1 )
		self.m_staticStatusGainIr.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusGainIr, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticStatusOffset = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Offset:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusOffset.Wrap( -1 )
		self.m_staticStatusOffset.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusOffset, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticStatusOffsetIo = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"IoBG", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusOffsetIo.Wrap( -1 )
		self.m_staticStatusOffsetIo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusOffsetIo, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticStatusOffsetIf = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"IfBG", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusOffsetIf.Wrap( -1 )
		self.m_staticStatusOffsetIf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusOffsetIf, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticStatusOffsetIt = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"ItBG", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusOffsetIt.Wrap( -1 )
		self.m_staticStatusOffsetIt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusOffsetIt, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticStatusOffsetIr = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"IrBG", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusOffsetIr.Wrap( -1 )
		self.m_staticStatusOffsetIr.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusOffsetIr, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticStatusCount = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Count:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticStatusCount.Wrap( -1 )
		self.m_staticStatusCount.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusCount, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticStatusCountIo = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"01234567890", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticStatusCountIo.Wrap( -1 )
		self.m_staticStatusCountIo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusCountIo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticStatusCountIf = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"01234567890", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticStatusCountIf.Wrap( -1 )
		self.m_staticStatusCountIf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusCountIf, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticStatusCountIt = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"01234567890", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticStatusCountIt.Wrap( -1 )
		self.m_staticStatusCountIt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusCountIt, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticStatusCountIr = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"01234567890", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.m_staticStatusCountIr.Wrap( -1 )
		self.m_staticStatusCountIr.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer3.Add( self.m_staticStatusCountIr, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( fgSizer3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 7, 7, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.AddGrowableCol( 2 )
		fgSizer4.AddGrowableCol( 3 )
		fgSizer4.AddGrowableCol( 4 )
		fgSizer4.AddGrowableCol( 5 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextColRegion = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Region", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextColRegion.Wrap( -1 )
		self.m_staticTextColRegion.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextColRegion, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticTextColStart = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextColStart.Wrap( -1 )
		self.m_staticTextColStart.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextColStart, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextColStop = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextColStop.Wrap( -1 )
		self.m_staticTextColStop.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextColStop, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextColStep = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Step", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextColStep.Wrap( -1 )
		self.m_staticTextColStep.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextColStep, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextColNpts = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Npts", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextColNpts.Wrap( -1 )
		self.m_staticTextColNpts.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextColNpts, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextColTime = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Time (s)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextColTime.Wrap( -1 )
		self.m_staticTextColTime.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextColTime, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextColUnits = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextColUnits.Wrap( -1 )
		self.m_staticTextColUnits.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextColUnits, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextRawPreEdge = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Pre-Edge", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextRawPreEdge.Wrap( -1 )
		self.m_staticTextRawPreEdge.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextRawPreEdge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_PreEdgeStart = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"-200", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_PreEdgeStart.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_PreEdgeStart, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_PreEdgeStop = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"-50", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_PreEdgeStop.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_PreEdgeStop, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_PreEdgeStep = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"5.0", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_PreEdgeStep.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_PreEdgeStep, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_PreEdgeNpts = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"30", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_PreEdgeNpts.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_PreEdgeNpts, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_PreEdgeTime = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_PreEdgeTime.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_PreEdgeTime, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_PreEdgeUnits = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"eV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_PreEdgeUnits.Wrap( -1 )
		self.m_PreEdgeUnits.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_PreEdgeUnits, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextRawXanes = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"XANES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextRawXanes.Wrap( -1 )
		self.m_staticTextRawXanes.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextRawXanes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_XanesStart = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"-50", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_XanesStart.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_XanesStart, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_XanesStop = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"-10", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_XanesStop.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_XanesStop, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_XanesStep = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_XanesStep.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_XanesStep, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_XanesNpts = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"40", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_XanesNpts.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_XanesNpts, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_XanesTime = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_XanesTime.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_XanesTime, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_XanesUnits = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"eV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_XanesUnits.Wrap( -1 )
		self.m_XanesUnits.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_XanesUnits, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextRawXAFS1 = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"XAFS1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextRawXAFS1.Wrap( -1 )
		self.m_staticTextRawXAFS1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextRawXAFS1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_Xafs1Start = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"-10", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs1Start.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs1Start, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_Xafs1Stop = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"40", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs1Stop.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs1Stop, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_Xafs1Step = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"0.4", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs1Step.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs1Step, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_Xafs1Npts = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"125", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs1Npts.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs1Npts, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_Xafs1Time = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs1Time.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs1Time, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_Xafs1UnitsChoices = [ u"eV", u"K" ]
		self.m_Xafs1Units = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_Xafs1UnitsChoices, 0 )
		self.m_Xafs1Units.SetSelection( 0 )
		self.m_Xafs1Units.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_Xafs1Units.SetMinSize( wx.Size( 40,-1 ) )
		
		fgSizer4.Add( self.m_Xafs1Units, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticTextRawXAFS2 = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"XAFS2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextRawXAFS2.Wrap( -1 )
		self.m_staticTextRawXAFS2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextRawXAFS2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_Xafs2Start = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"40", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs2Start.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs2Start, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_Xafs2Stop = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"550", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs2Stop.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs2Stop, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Xafs2Step = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"0.035", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs2Step.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs2Step, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_Xafs2Npts = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"250", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs2Npts.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs2Npts, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_Xafs2Time = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs2Time.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs2Time, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		m_Xafs2UnitsChoices = [ u"eV", u"K" ]
		self.m_Xafs2Units = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_Xafs2UnitsChoices, 0 )
		self.m_Xafs2Units.SetSelection( 1 )
		self.m_Xafs2Units.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_Xafs2Units.SetMinSize( wx.Size( 40,-1 ) )
		
		fgSizer4.Add( self.m_Xafs2Units, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticTextRawXAFS3 = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"XAFS3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextRawXAFS3.Wrap( -1 )
		self.m_staticTextRawXAFS3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextRawXAFS3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_Xafs3Start = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"550", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs3Start.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs3Start, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_Xafs3Stop = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"980", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs3Stop.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs3Stop, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_Xafs3Step = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"0.045", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs3Step.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs3Step, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Xafs3Npts = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"89", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs3Npts.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs3Npts, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Xafs3Time = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs3Time.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs3Time, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_Xafs3UnitsChoices = [ u"eV", u"K" ]
		self.m_Xafs3Units = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_Xafs3UnitsChoices, 0 )
		self.m_Xafs3Units.SetSelection( 1 )
		self.m_Xafs3Units.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_Xafs3Units.SetMinSize( wx.Size( 40,-1 ) )
		
		fgSizer4.Add( self.m_Xafs3Units, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticTextRawXAFS4 = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"XAFS4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextRawXAFS4.Wrap( -1 )
		self.m_staticTextRawXAFS4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_staticTextRawXAFS4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_Xafs4Start = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"980", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs4Start.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs4Start, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Xafs4Stop = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1525", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs4Stop.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs4Stop, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Xafs4Step = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"0.05", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs4Step.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs4Step, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Xafs4Npts = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"79", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs4Npts.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs4Npts, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_Xafs4Time = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_Xafs4Time.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer4.Add( self.m_Xafs4Time, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		m_Xafs4UnitsChoices = [ u"eV", u"K" ]
		self.m_Xafs4Units = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_Xafs4UnitsChoices, 0 )
		self.m_Xafs4Units.SetSelection( 1 )
		self.m_Xafs4Units.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_Xafs4Units.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer4.Add( self.m_Xafs4Units, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer10.Add( fgSizer4, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer7 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer7.AddGrowableCol( 0 )
		fgSizer7.AddGrowableCol( 1 )
		fgSizer7.AddGrowableCol( 2 )
		fgSizer7.AddGrowableCol( 3 )
		fgSizer7.AddGrowableCol( 4 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_setGain = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Set Gain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_setGain.Wrap( -1 )
		self.m_setGain.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, wx.EmptyString ) )
		
		fgSizer7.Add( self.m_setGain, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_setGainIoChoices = [ u"1E-4", u"1E-5", u"1E-6", u"1E-7", u"1E-8", u"1E-9" ]
		self.m_setGainIo = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_setGainIoChoices, 0 )
		self.m_setGainIo.SetSelection( 3 )
		self.m_setGainIo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer7.Add( self.m_setGainIo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		m_setGainIfChoices = [ u"1E-4", u"1E-5", u"1E-6", u"1E-7", u"1E-8", u"1E-9" ]
		self.m_setGainIf = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_setGainIfChoices, 0 )
		self.m_setGainIf.SetSelection( 3 )
		self.m_setGainIf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer7.Add( self.m_setGainIf, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_setGainItChoices = [ u"1E-4", u"1E-5", u"1E-6", u"1E-7", u"1E-8", u"1E-9" ]
		self.m_setGainIt = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_setGainItChoices, 0 )
		self.m_setGainIt.SetSelection( 3 )
		self.m_setGainIt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer7.Add( self.m_setGainIt, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		m_setGainIrChoices = [ u"1E-4", u"1E-5", u"1E-6", u"1E-7", u"1E-8", u"1E-9" ]
		self.m_setGainIr = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_setGainIrChoices, 0 )
		self.m_setGainIr.SetSelection( 3 )
		self.m_setGainIr.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer7.Add( self.m_setGainIr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer10.Add( fgSizer7, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 2, 6, 0, 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.AddGrowableCol( 2 )
		fgSizer5.AddGrowableCol( 3 )
		fgSizer5.AddGrowableCol( 4 )
		fgSizer5.AddGrowableCol( 5 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextEdgeEnergy = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Edge Energy", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextEdgeEnergy.Wrap( -1 )
		self.m_staticTextEdgeEnergy.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, wx.EmptyString ) )
		
		fgSizer5.Add( self.m_staticTextEdgeEnergy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_SetEdgeEnergy = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"7112.0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.m_SetEdgeEnergy.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_SetEdgeEnergy.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		
		fgSizer5.Add( self.m_SetEdgeEnergy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextElement = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Element", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextElement.Wrap( -1 )
		self.m_staticTextElement.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer5.Add( self.m_staticTextElement, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_choiceElementChoices = [ u"H", u"He", u"Li", u"Be", u"B", u"C", u"N", u"O", u"F", u"Ne", u"Na", u"Mg", u"Al", u"Si", u"P", u"S", u"Cl", u"Ar", u"K", u"Ca", u"Sc", u"Ti", u"V", u"Cr", u"Mn", u"Fe", u"Co", u"Ni", u"Cu", u"Zn", u"Ga", u"Ge", u"As", u"Se", u"Br", u"Kr", u"Rb", u"Sr", u"Y", u"Zr", u"Nb", u"Mo", u"Tc", u"Ru", u"Rh", u"Pd", u"Ag", u"Cd", u"In", u"Sn", u"Sb", u"Te", u"I", u"Xe", u"Cs", u"Ba", u"La", u"Ce", u"Pr", u"Nd", u"Pm", u"Sm", u"Eu", u"Gd", u"Tb", u"Dy", u"Ho", u"Er", u"Tm", u"Yb", u"Lu", u"Hf", u"Ta", u"W", u"Re", u"Os", u"Ir", u"Pt", u"Au", u"Hg", u"Tl", u"Pb", u"Bi", u"Po", u"At", u"Rn", u"Fr", u"Ra", u"Ac", u"Th", u"Pa", u"U", u"Np", u"Pu", u"Am", u"Cm", u"Bk", u"Cf" ]
		self.m_choiceElement = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,-1 ), m_choiceElementChoices, 0 )
		self.m_choiceElement.SetSelection( 25 )
		self.m_choiceElement.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer5.Add( self.m_choiceElement, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticTextCurrentEnergy = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Current Energy:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextCurrentEnergy.Wrap( -1 )
		self.m_staticTextCurrentEnergy.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer5.Add( self.m_staticTextCurrentEnergy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticStatusGainE = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"7000.0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticStatusGainE.Wrap( -1 )
		self.m_staticStatusGainE.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_staticStatusGainE.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		fgSizer5.Add( self.m_staticStatusGainE, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextTimePoint = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Time/Point(sec)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextTimePoint.Wrap( -1 )
		self.m_staticTextTimePoint.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer5.Add( self.m_staticTextTimePoint, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_setCountTime = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_CENTRE )
		self.m_setCountTime.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_setCountTime.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		
		fgSizer5.Add( self.m_setCountTime, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextMode = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMode.Wrap( -1 )
		self.m_staticTextMode.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer5.Add( self.m_staticTextMode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_absRelChoices = [ u"Relative", u"Absolute" ]
		self.m_absRel = wx.Choice( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_absRelChoices, 0 )
		self.m_absRel.SetSelection( 0 )
		self.m_absRel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer5.Add( self.m_absRel, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.moveEo_button = wx.Button( self.m_LeftPanel, wx.ID_ANY, u"&Move Eo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.moveEo_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.moveEo_button.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.moveEo_button.SetToolTipString( u"Move to Edge Energy Position" )
		
		fgSizer5.Add( self.moveEo_button, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( fgSizer5, 0, wx.EXPAND, 5 )
		
		self.m_staticline211 = wx.StaticLine( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline211, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextNumberOfScans = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Number of Scans:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNumberOfScans.Wrap( -1 )
		self.m_staticTextNumberOfScans.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		bSizer71.Add( self.m_staticTextNumberOfScans, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_numberOfScans = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( 40,-1 ), wx.TE_CENTRE )
		self.m_numberOfScans.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		bSizer71.Add( self.m_numberOfScans, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer71.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextScanPoints = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Scan Point:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextScanPoints.Wrap( -1 )
		self.m_staticTextScanPoints.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		bSizer71.Add( self.m_staticTextScanPoints, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_currentScanPoint = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_currentScanPoint.Wrap( -1 )
		self.m_currentScanPoint.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_currentScanPoint.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer71.Add( self.m_currentScanPoint, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextSeparate = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSeparate.Wrap( -1 )
		self.m_staticTextSeparate.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		bSizer71.Add( self.m_staticTextSeparate, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_totalScanPoint = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"850", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_totalScanPoint.Wrap( -1 )
		self.m_totalScanPoint.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_totalScanPoint.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer71.Add( self.m_totalScanPoint, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer10.Add( bSizer71, 0, wx.EXPAND, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextFileName = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"File Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextFileName.Wrap( -1 )
		self.m_staticTextFileName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer8.Add( self.m_staticTextFileName, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_fileName = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"ddd", wx.DefaultPosition, wx.Size( 390,-1 ), 0 )
		self.m_fileName.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer8.Add( self.m_fileName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextComments = wx.StaticText( self.m_LeftPanel, wx.ID_ANY, u"Comments:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextComments.Wrap( -1 )
		self.m_staticTextComments.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer8.Add( self.m_staticTextComments, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_comment = wx.TextCtrl( self.m_LeftPanel, wx.ID_ANY, u"enter comments", wx.DefaultPosition, wx.Size( 390,60 ), wx.TE_MULTILINE )
		self.m_comment.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		
		fgSizer8.Add( self.m_comment, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		self.m_staticline2111 = wx.StaticLine( self.m_LeftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline2111, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.scan_button = wx.Button( self.m_LeftPanel, wx.ID_ANY, u"&Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.scan_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.scan_button.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		self.scan_button.SetToolTipString( u"start scan" )
		
		bSizer4.Add( self.scan_button, 0, wx.ALL, 5 )
		
		self.pause_button = wx.Button( self.m_LeftPanel, wx.ID_ANY, u"&Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pause_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.pause_button.SetToolTipString( u"start scan" )
		
		bSizer4.Add( self.pause_button, 0, wx.ALL, 5 )
		
		self.resume_button = wx.Button( self.m_LeftPanel, wx.ID_ANY, u"&Resume", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.resume_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.resume_button.SetToolTipString( u"start scan" )
		
		bSizer4.Add( self.resume_button, 0, wx.ALL, 5 )
		
		self.m_buttonAbort = wx.Button( self.m_LeftPanel, wx.ID_ANY, u"&Abort", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonAbort.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.m_buttonAbort.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer4.Add( self.m_buttonAbort, 0, wx.ALL, 5 )
		
		self.plot_button = wx.Button( self.m_LeftPanel, wx.ID_ANY, u"&Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.plot_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 92, False, "Swis721 LtEx BT" ) )
		self.plot_button.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer4.Add( self.plot_button, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_RIGHT, 5 )
		
		
		self.m_LeftPanel.SetSizer( bSizer10 )
		self.m_LeftPanel.Layout()
		bSizer10.Fit( self.m_LeftPanel )
		bSizer12.Add( self.m_LeftPanel, 1, wx.ALL, 5 )
		
		
		bMainFrameSizer.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		self.m_RightPanel = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_RightPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel7 = wx.Panel( self.m_RightPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )
		
		spectrumSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_plotTrans = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spectrumSizer.Add( self.m_plotTrans, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_plotFluo = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		spectrumSizer.Add( self.m_plotFluo, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( spectrumSizer )
		self.m_panel7.Layout()
		spectrumSizer.Fit( self.m_panel7 )
		bSizer9.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_RightPanel.SetSizer( bSizer9 )
		self.m_RightPanel.Layout()
		bSizer9.Fit( self.m_RightPanel )
		bMainFrameSizer.Add( self.m_RightPanel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_MainPanel.SetSizer( bMainFrameSizer )
		self.m_MainPanel.Layout()
		bMainFrameSizer.Fit( self.m_MainPanel )
		bMainSizer.Add( self.m_MainPanel, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bMainSizer )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClick_Exit )
		self.m_PreEdgeStart.Bind( wx.EVT_TEXT_ENTER, self.onStart )
		self.m_PreEdgeStop.Bind( wx.EVT_TEXT_ENTER, self.onStop )
		self.m_PreEdgeStep.Bind( wx.EVT_TEXT_ENTER, self.onStep )
		self.m_PreEdgeNpts.Bind( wx.EVT_TEXT_ENTER, self.onNpts )
		self.m_XanesStart.Bind( wx.EVT_TEXT_ENTER, self.onStart )
		self.m_XanesStop.Bind( wx.EVT_TEXT_ENTER, self.onStop )
		self.m_XanesStep.Bind( wx.EVT_TEXT_ENTER, self.onStep )
		self.m_XanesNpts.Bind( wx.EVT_TEXT_ENTER, self.onNpts )
		self.m_Xafs1Start.Bind( wx.EVT_TEXT_ENTER, self.onStart )
		self.m_Xafs1Stop.Bind( wx.EVT_TEXT_ENTER, self.onStop )
		self.m_Xafs1Step.Bind( wx.EVT_TEXT_ENTER, self.onStep )
		self.m_Xafs1Npts.Bind( wx.EVT_TEXT_ENTER, self.onNpts )
		self.m_Xafs1Units.Bind( wx.EVT_CHOICE, self.onUnits )
		self.m_Xafs2Start.Bind( wx.EVT_TEXT_ENTER, self.onStart )
		self.m_Xafs2Stop.Bind( wx.EVT_TEXT_ENTER, self.onStop )
		self.m_Xafs2Step.Bind( wx.EVT_TEXT_ENTER, self.onStep )
		self.m_Xafs2Npts.Bind( wx.EVT_TEXT_ENTER, self.onNpts )
		self.m_Xafs2Units.Bind( wx.EVT_CHOICE, self.onUnits )
		self.m_Xafs3Start.Bind( wx.EVT_TEXT_ENTER, self.onStart )
		self.m_Xafs3Stop.Bind( wx.EVT_TEXT_ENTER, self.onStop )
		self.m_Xafs3Step.Bind( wx.EVT_TEXT_ENTER, self.onStep )
		self.m_Xafs3Npts.Bind( wx.EVT_TEXT_ENTER, self.onNpts )
		self.m_Xafs3Units.Bind( wx.EVT_CHOICE, self.onUnits )
		self.m_Xafs4Start.Bind( wx.EVT_TEXT_ENTER, self.onStart )
		self.m_Xafs4Stop.Bind( wx.EVT_TEXT_ENTER, self.onStop )
		self.m_Xafs4Step.Bind( wx.EVT_TEXT_ENTER, self.onStep )
		self.m_Xafs4Npts.Bind( wx.EVT_TEXT_ENTER, self.onNpts )
		self.m_Xafs4Units.Bind( wx.EVT_CHOICE, self.onUnits )
		self.m_SetEdgeEnergy.Bind( wx.EVT_TEXT_ENTER, self.enterE0 )
		self.m_choiceElement.Bind( wx.EVT_CHOICE, self.OnChoiceElement )
		self.moveEo_button.Bind( wx.EVT_BUTTON, self.moveEoButton )
		self.scan_button.Bind( wx.EVT_BUTTON, self.StartScan )
		self.pause_button.Bind( wx.EVT_BUTTON, self.PauseScan )
		self.resume_button.Bind( wx.EVT_BUTTON, self.ResumeScan )
		self.m_buttonAbort.Bind( wx.EVT_BUTTON, self.AbortScan )
		self.plot_button.Bind( wx.EVT_BUTTON, self.ShowPlot )
		self.m_plotTrans.Bind( wx.EVT_SIZE, self.OnSize_TransCanvas )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClick_Exit( self, event ):
		event.Skip()
	
	def onStart( self, event ):
		event.Skip()
	
	def onStop( self, event ):
		event.Skip()
	
	def onStep( self, event ):
		event.Skip()
	
	def onNpts( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	def onUnits( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def enterE0( self, event ):
		event.Skip()
	
	def OnChoiceElement( self, event ):
		event.Skip()
	
	def moveEoButton( self, event ):
		event.Skip()
	
	def StartScan( self, event ):
		event.Skip()
	
	def PauseScan( self, event ):
		event.Skip()
	
	def ResumeScan( self, event ):
		event.Skip()
	
	def AbortScan( self, event ):
		event.Skip()
	
	def ShowPlot( self, event ):
		event.Skip()
	
	def OnSize_TransCanvas( self, event ):
		event.Skip()
	

