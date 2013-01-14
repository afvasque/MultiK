#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Frame2

modules ={u'BasicOperacion': [0, '', u'BasicOperacion'],
 'Frame2': [1, 'Main frame of Application', u'Frame2.py'],
 'Panel1': [0, '', u'Panel1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame2.create(None)
        self.main.ShowFullScreen(True, style= wx.DEFAULT_FRAME_STYLE | 
                         wx.NO_FULL_REPAINT_ON_RESIZE | wx.FULLSCREEN_ALL)
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
