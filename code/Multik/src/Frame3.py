# coding=utf-8
#Boa:Frame:Frame2

import wx
from Panel1 import *

def create(parent):
    return Frame2(parent)

[wxID_FRAME2] = [wx.NewId() for _init_ctrls in range(1)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        wx.Frame.__init__(self, style=wx.DEFAULT_FRAME_STYLE, name='', parent=prnt, title='Frame2', pos=(341, 167), id=wxID_FRAME2, size=(911, 445))
        
        self.child= Panel1(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(519, 234),
              style=wx.TAB_TRAVERSAL)

    def __init__(self, parent):
        self._init_ctrls(parent)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
