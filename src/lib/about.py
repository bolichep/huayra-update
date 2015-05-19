# -*- coding: utf-8 -*-

import wx
import wx.html
import os.path

import webbrowser


class wxHTML(wx.html.HtmlWindow):
    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())


class AboutDialog(wx.Frame):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(
            parent=parent,
            title=u'Acerca de',
        )

        html = wxHTML(self)
        html.LoadPage(
            os.path.join(
            wx.GetApp().app_path,
            'media',
            'about.html'
        ))

        self.SetMinSize((350, 250))
        self.SetMaxSize((350, 250))

        w, h = wx.DisplaySize()
        x = (w / 2) - (350 / 2)
        y = (h / 2) - (250 / 2)

        self.SetPosition((x,y))

    def OnClose(self, evt):
        self.Close()
