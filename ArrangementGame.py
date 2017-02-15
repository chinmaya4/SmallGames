import wx
import random

class Arrangement (wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Arrangement', pos=(600, 250), size=(305, 400))
        panel=wx.Panel(self)
        
        button1 = wx.Button(panel, label='1', pos=(10, 10), size=(60, 60), name='One')
        button2 = wx.Button(panel, label='2', pos=(10, 80), size=(60, 60), name='Two')
        button3 = wx.Button(panel, label='3', pos=(10, 150), size=(60, 60), name='Three')
        button4 = wx.Button(panel, label='4', pos=(10, 220), size=(60, 60), name='Four')
        button5 = wx.Button(panel, label='5', pos=(80, 10), size=(60, 60), name='Five')
        button6 = wx.Button(panel, label='6', pos=(80, 80), size=(60, 60), name='Six')
        button7 = wx.Button(panel, label='7', pos=(80, 150), size=(60, 60), name='Seven')
        button8 = wx.Button(panel, label='8', pos=(80, 220), size=(60, 60), name='Eight')
        button9 = wx.Button(panel, label='9', pos=(150, 10), size=(60, 60), name='Nine')
        button10 = wx.Button(panel, label='10', pos=(150, 80), size=(60, 60), name='Ten')
        button11 = wx.Button(panel, label='11', pos=(150, 150), size=(60, 60), name='Eleven')
        button12 = wx.Button(panel, label='12', pos=(150, 220), size=(60, 60), name='Twelve')
        button13 = wx.Button(panel, label='13', pos=(220, 10), size=(60, 60), name='Thirteen')
        button14 = wx.Button(panel, label='14', pos=(220, 80), size=(60, 60), name='Fourteen')
        button15 = wx.Button(panel, label='15', pos=(220, 150), size=(60, 60), name='Fifteen')
        button16 = wx.Button(panel, label='15', pos=(220, 220), size=(60, 60), name='Sixteen')
        button16.Hide()

        self.buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16]

        for button in self.buttons:
            self.buildButtons(button)

        buttonShuffle = wx.Button(panel, label='Shuffle', pos=(40, 300), size=(80, 50))
        self.Bind(wx.EVT_BUTTON, self.Shuffle, buttonShuffle)
            
        buttonExit = wx.Button(panel, label='Exit', pos=(170, 300), size=(80, 50))
        self.Bind(wx.EVT_BUTTON, self.closebutton, buttonExit)
        self.Bind(wx.EVT_CLOSE, self.closewindow)

    def buildButtons(self, btn):
        """"""
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        
    def Shuffle(self, event):
        data = range(15)
        i = 0
        random.shuffle(data)
        for button in self.buttons:
            hideStatus = button.Hide()
            if hideStatus == True:
                button.SetLabel(str(data[i]+1))
                i += 1
                button.Show()
            else:
                button.Hide()
        
    def closebutton(self, event):
        self.Close(True)

    def closewindow(self, event):
        self.Destroy()

    def onButton(self, event):
        for button in self.buttons:
            hideStatus = button.Hide()
            button.Show()
            if hideStatus == False:
                button.SetLabel(event.GetEventObject().GetLabel())
                button.Show()
                                     
        event.GetEventObject().Hide()
                    
if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=Arrangement(parent=None, id = 1)
    frame.Show()
    app.MainLoop()
