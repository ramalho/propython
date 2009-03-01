#!/usr/bin/env python

import wx

class CriarJanela(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, 
            parent=None, 
            id=-1, 
            title='CONSOLIP: Brincando com Python', 
            pos=wx.DefaultPosition, 
            size=wx.Size(800,600)
        )
        menuArquivo = wx.Menu()
        menuArquivo.Append(1,'&Abrir...')
        menuArquivo.Append(2,'&Salvar')
        
        menuBar = wx.MenuBar()
        menuBar.Append(menuArquivo,'&Arquivo')
        
        self.Bind(wx.EVT_MENU, self.AbrirTexto, id=1)
        #self.Bind(wx.EVT_MENU, self.AbrirTexto, 2)
        
        self.SetMenuBar(menuBar)
        
        self.texto = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        
    def AbrirTexto(self, event):
        dlg = wx.FileDialog(self, 'Selecione um arquivo', '.', '', '*.txt;*.py', wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            caminho = dlg.GetPath()
            self.texto.LoadFile(caminho)
            #self.SetStatusText(caminho)
        dlg.Destroy()
        event.Skip()
            
class Inicia(wx.App):
    def OnInit(self):
        janela = CriarJanela()
        janela.Show(True)
        #self.SetTopWindow(janela)
        return True
        
app = Inicia()
app.MainLoop()
