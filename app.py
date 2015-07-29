import wx
from ExpenseController import ExpenseController


class SplashScreen(wx.SplashScreen):
    def __init__(self, parent=None):
        aBitmap = wx.Image('logo.jpg').ConvertToBitmap()
        splashStyle = wx.SPLASH_CENTER_ON_SCREEN | wx.SPLASH_TIMEOUT
        splashDuration = 1500 # milliseconds
        wx.SplashScreen.__init__(self, aBitmap, splashStyle, splashDuration, parent)
        self.Bind(wx.EVT_CLOSE, self.onExit)
        wx.Yield()

    def onExit(self, event):
       self.Hide()

       controller = ExpenseController()
       controller.show(True)

       event.Skip()

def main():
    app = wx.App(None)
    splash = SplashScreen()
    splash.Show()
    app.MainLoop()

if __name__ == '__main__': main()