import wx

from AddView import AddFrame

class AddController:
    def __init__(self, parent=None, appModel=None):
        self.MainWindow = AddFrame(parent)
        self.MainWindow.SetMaxSize(self.MainWindow.GetSize())
        self.MainWindow.SetMinSize(map(lambda x: x/1.5, self.MainWindow.GetSize()))

        self.MainWindow.Bind(wx.EVT_BUTTON, self.onAdd, self.MainWindow.btnOK)
        self.MainWindow.Bind(wx.EVT_BUTTON, self.onClose, self.MainWindow.btnCancel)

        self.appModel = appModel
    def show(self):
        self.MainWindow.ShowModal()

    def onClose(self, event=None):
        self.appModel.addInfoDict = {}
        self.MainWindow.Destroy()

    def onAdd(self, event):
        self.appModel.addInfoDict = {
            'fName' : self.MainWindow.txtfName.GetValue(),
            'lName' : self.MainWindow.txtlName.GetValue(),
            'fPath' : self.MainWindow.txtfPath.GetValue(),
            'rNum'  : self.MainWindow.txtrNum.GetValue(),
        }
        self.MainWindow.Destroy()