import wx
from ExpenseController import ExpenseController

def main():
    app = wx.App(None)
    controller = ExpenseController()
    controller.show()
    app.MainLoop()

if __name__ == '__main__': main()
