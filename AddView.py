# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AddFrame
###########################################################################

class AddFrame ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 571,456 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"First Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.txtfName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txtfName, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Last Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txtlName, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Report Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtrNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txtrNum, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer4.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Link to report:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtfPath = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txtfPath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnBrowse = wx.Button( self, wx.ID_ANY, u"Browse...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnBrowse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnOK, 2, wx.ALL, 5 )
		
		
		bSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnCancel, 2, wx.ALL, 5 )
		
		
		bSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer6, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

