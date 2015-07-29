import wx
import shelve, sys

from ExpenseView import MainFrame as MainView
from AddController import AddController
from ExpenseModel import ExpenseModel

class ExpenseController:
    def __init__(self):
        self.mainWindow = MainView(None)

        # setup bindings
        self.mainWindow.Bind(wx.EVT_MENU, self.onExit, self.mainWindow.menuExit)
        self.mainWindow.Bind(wx.EVT_MENU, self.onAdd, self.mainWindow.menuAdd)

        # setup view
        self.mainWindow.reportList.InsertColumn(0, 'Last Name')
        self.mainWindow.reportList.InsertColumn(1, 'First Name')
        self.mainWindow.reportList.InsertColumn(2, 'Report Number')#, width=wx.COL_WIDTH_AUTOSIZE)

        # setup member vars
        self.appModel = ExpenseModel()

    def show(self):
        self.mainWindow.Show()

    def onExit(self, event):
        sys.exit(0)

    def onAdd(self, event):
        addController = AddController(self.mainWindow, self.appModel)
        addController.show()
        print self.appModel.addInfoDict