import os
import wx
import wx.aui as aui
import wx.stc as stc

from subWindow import SubWindow


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.frame = wx.Frame.__init__(self, parent, title=title, size=(800,600))
        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)
 
        
        text1 = stc.StyledTextCtrl(self, size=wx.Size(400, 300))
        text2 = stc.StyledTextCtrl(self, size=wx.Size(400, 300))
        
        self._mgr.AddPane(text1, aui.AuiPaneInfo().Caption("Text 1").Center())
        self._mgr.AddPane(text2, aui.AuiPaneInfo().Caption("Text 2").Bottom())
        self._mgr.Update()
        
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuSub = filemenu.Append(wx.ID_ABOUT, "Sub"," New sub window")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onSub, menuSub)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.Show(True)

    def onAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.
        
    def onSub(self,e):
        SubWindow(self, "Test");

    def onExit(self,e):
        self.Close(True)  # Close the frame.
        
    def onClose(self, e):
        self._mgr.UnInit()
        del self._mgr
        self.Destroy()
 

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()