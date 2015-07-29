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
        self.mainWindow.Bind(wx.EVT_CLOSE, self.onExit, self.mainWindow)

        # setup view
        self.mainWindow.reportList.InsertColumn(0, 'Last Name')
        self.mainWindow.reportList.InsertColumn(1, 'First Name')
        self.mainWindow.reportList.InsertColumn(2, 'Report Number')#, width=wx.COL_WIDTH_AUTOSIZE)

        # setup member vars
        self.appModel = ExpenseModel()

    def show(self, *args):
        self.mainWindow.Show(*args)

    def onExit(self, event):
        self.appModel.reportDict.close()
        sys.exit(0)

    def onAdd(self, event):
        addController = AddController(self.mainWindow, self.appModel)
        addController.show()
        if not self.appModel.addInfoDict: return
        index = self.mainWindow.reportList.InsertStringItem(self.mainWindow.reportList.GetItemCount(), self.appModel.addInfoDict['lName'])
        self.mainWindow.reportList.SetStringItem(index, 1, self.appModel.addInfoDict['fName'])
        self.mainWindow.reportList.SetStringItem(index, 2, self.appModel.addInfoDict['rNum'])
        self.mainWindow.reportList.SetItemData(index, self.appModel.addInfoDict['fPath'])
        self.appModel.reportDict.update(self.appModel.addInfoDict)