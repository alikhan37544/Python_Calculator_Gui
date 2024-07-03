import wx
from wx.lib.mixins.listctrl import TextCtrlMixin

class Calculator(wx.Frame):
    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title, size=(200, 
150))

        self.InitUI()
        self.value = ''

    def InitUI(self):
        self.panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.result_text = wx.TextCtrl(self.panel, style=wx.TE_READONLY | 
wx.TE_MULTILINE)
        result_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_sizer.Add(self.result_text, 1, wx.EXPAND)
        sizer.Add(result_sizer, 0, wx.EXPAND)

        self.button_sizer = wx.BoxSizer(wx.VERTICAL)

        button_names = ['7', '8', '9', '/', 'C']
        for name in button_names:
            button = wx.Button(self.panel, label=name)
            self.button_sizer.Add(button, 1, wx.ALL | wx.EXPAND, 5)

        sizer.Add(self.button_sizer, 0, wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.Show()

    def handle_button_click(self, event):
        button = event.GetEventObject()
        if button.GetLabel() == 'C':
            self.value = ''
            self.result_text.Clear()
        else:
            if button.GetLabel() == '/':
                self.value += '/'
            elif button.GetLabel() == '7' or button.GetLabel() == '8' or 
button.GetLabel() == '9':
                self.value += button.GetLabel()
            self.result_text.AppendText(self.value)

    def OnClose(self, event):
        if wx.MessageBox("Really quit?", "Message Box", wx.YES_NO | 
wx.CANCEL | wx.ICON_INFORMATION) != wx.YES:
            return
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = Calculator(None, title="Calculator")
    frame.Show()
    app.MainLoop()