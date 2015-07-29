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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 816,465 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.stBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuExit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menuExit )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.menuEdit = wx.Menu()
		self.menuAdd = wx.MenuItem( self.menuEdit, wx.ID_ANY, u"Add Report...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuEdit.AppendItem( self.menuAdd )
		
		self.m_menubar1.Append( self.menuEdit, u"Edit" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer1.Add( self.m_searchCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.reportList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer1.Add( self.reportList, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

