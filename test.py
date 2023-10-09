import wx
class Interfaz(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Bienvenido a nuestra lavanderia, ¿Que servicio dese al dia de hoy?", pos=(10, 10))
        self.lblname1 = wx.StaticText(self, label="Inserta numero de la maquina:", pos=(20,50))
        self.maquina = wx.TextCtrl(self, value="", pos=(185, 50), size=(30,20))
        self.lblname2 = wx.StaticText(self, label="Tipo de Maquina:", pos=(250,50))
        self.lblname3 = wx.StaticText(self, label="Tipo", pos=(350,50))
        self.lblname4 = wx.StaticText(self, label="¿Cuantos kilos de ropa se van a lavar?", pos=(20,80))
        self.maquina = wx.TextCtrl(self, value="", pos=(225, 80), size=(30,20))
        self.lblname5 = wx.StaticText(self, label="Agregue extra al servicio:", pos=(20,110))
        self.serv1 = wx.CheckBox(self, label = 'Detergente',pos = (30,130))
        self.serv2 = wx.CheckBox(self, label = 'Suavizante',pos = (120,130))
        self.lblname6 = wx.StaticText(self, label="Total a Pagar:", pos=(250,110))
        self.tpagar1 = wx.TextCtrl(self, value="", pos=(325, 110), size=(80,20))
        self.lblname7 = wx.StaticText(self, label="Importe:", pos=(250,130))
        self.tpagar2 = wx.TextCtrl(self, value="", pos=(325, 130), size=(80,20))
        self.lblname8 = wx.StaticText(self, label="Cambio:", pos=(250,150))
        self.tpagar3 = wx.TextCtrl(self, value="", pos=(325, 150), size=(80,20))
        self.lblname9 = wx.StaticText(self, label="Datos del Cliente:", pos=(20,180))
        self.lblname10 = wx.StaticText(self, label="ID:", pos=(20,210))
        self.Dclient1 = wx.TextCtrl(self, value="", pos=(35, 210), size=(30,20))
        self.lblname11 = wx.StaticText(self, label="Nombre:", pos=(80,210))
        self.Dclient2 = wx.TextCtrl(self, value="", pos=(130, 210), size=(200,20))
        self.lblname12 = wx.StaticText(self, label="Fecha de Registro:", pos=(350,210))
        self.Dclient3 = wx.TextCtrl(self, value="", pos=(450, 210), size=(150,20))
        self.lblname13 = wx.StaticText(self, label="Fecha de Vencimiento:", pos=(30,240))
        self.Dclient4 = wx.TextCtrl(self, value="", pos=(150, 240), size=(150,20))
        self.lblname14 = wx.StaticText(self, label="Descuento (%):", pos=(320,240))
        self.Dclient5 = wx.TextCtrl(self, value="", pos=(400, 240), size=(30,20))
        self.button1 =wx.Button(self, label="Realizar\nCobro", pos=(620, 10),size=(150,30))
        self.button2 =wx.Button(self, label="Calcular\nTotal", pos=(620, 45),size=(150,30))
        self.button3 =wx.Button(self, label="Activar / Desactivar\nMantenimiento", pos=(620, 80),size=(150,30))
        self.button4 =wx.Button(self, label="Buscar\nCliente", pos=(620, 115),size=(150,30))
        self.button5 =wx.Button(self, label="Alta\nCliente", pos=(620, 150),size=(150,30))
        self.button6 =wx.Button(self, label="Modificar\nCliente", pos=(620, 185),size=(150,30))
        self.button7 =wx.Button(self, label="Baja\nCliente", pos=(620, 220),size=(150,30))
        self.nummaq1 = wx.StaticText(self, label="M1:", pos=(20,300))
        self.statmaq1 = wx.StaticText(self, label="Libre", pos=(50,300))
        self.nummaq2 = wx.StaticText(self, label="M2:", pos=(100,300))
        self.statmaq2 = wx.StaticText(self, label="Libre", pos=(130,300))
        self.nummaq3 = wx.StaticText(self, label="M3:", pos=(180,300))
        self.statmaq3 = wx.StaticText(self, label="Libre", pos=(210,300))
        self.nummaq4 = wx.StaticText(self, label="M4:", pos=(260,300))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(290,300))
        self.nummaq4 = wx.StaticText(self, label="M5:", pos=(340,300))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(370,300))
        self.nummaq1 = wx.StaticText(self, label="M6:", pos=(20,330))
        self.statmaq1 = wx.StaticText(self, label="Libre", pos=(50,330))
        self.nummaq2 = wx.StaticText(self, label="M7:", pos=(100,330))
        self.statmaq2 = wx.StaticText(self, label="Libre", pos=(130,330))
        self.nummaq3 = wx.StaticText(self, label="M8:", pos=(180,330))
        self.statmaq3 = wx.StaticText(self, label="Libre", pos=(210,330))
        self.nummaq4 = wx.StaticText(self, label="M9:", pos=(260,330))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(290,330))
        self.nummaq4 = wx.StaticText(self, label="M10:", pos=(340,330))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(370,330))
        self.nummaq1 = wx.StaticText(self, label="M11:", pos=(20,360))
        self.statmaq1 = wx.StaticText(self, label="Libre", pos=(50,360))
        self.nummaq2 = wx.StaticText(self, label="M12:", pos=(100,360))
        self.statmaq2 = wx.StaticText(self, label="Libre", pos=(130,360))
        self.nummaq3 = wx.StaticText(self, label="M13:", pos=(180,360))
        self.statmaq3 = wx.StaticText(self, label="Libre", pos=(210,360))
        self.nummaq4 = wx.StaticText(self, label="M14:", pos=(260,360))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(290,360))
        self.nummaq4 = wx.StaticText(self, label="M15:", pos=(340,360))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(370,360))
        
        #Eventos de Boton
        self.Bind(wx.EVT_BUTTON, self.OnClick1, self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.button2)
        self.Bind(wx.EVT_BUTTON, self.OnClick3, self.button3)
        self.Bind(wx.EVT_BUTTON, self.OnClick4, self.button4)
        self.Bind(wx.EVT_BUTTON, self.OnClick5, self.button5)
        self.Bind(wx.EVT_BUTTON, self.OnClick6, self.button6)
        self.Bind(wx.EVT_BUTTON, self.OnClick7, self.button7)

    #Definicion de evnetos
    def OnClick1(self,event):
        self.statmaq1 = wx.StaticText(self, label="Ocupado", pos=(50,300))
    def OnClick2(self,event):
        self.statmaq2 = wx.StaticText(self, label="Ocupado", pos=(130,300))
    def OnClick3(self,event):
        self.statmaq3 = wx.StaticText(self, label="Ocupado", pos=(210,300))
    def OnClick4(self,event):
        self.statmaq1 = wx.StaticText(self, label="Ocupado", pos=(50,300))
    def OnClick5(self,event):
        self.statmaq2 = wx.StaticText(self, label="Ocupado", pos=(130,300))
    def OnClick6(self,event):
        self.statmaq3 = wx.StaticText(self, label="Ocupado", pos=(210,300))
    def OnClick7(self,event):
        self.statmaq3 = wx.StaticText(self, label="Ocupado", pos=(210,300))
            

#Creamos la App como objeto wx.App
app = wx.App(False)
#Definimos el frame con titulo y tamaño de 700 x 500
frame = wx.Frame(None,title="Lavanderia MISTI",size=(800,500))
#Creamos el panel de la interfaz con objeto padre al frame
panel = Interfaz(frame)
#Mostramos el Frame
frame.Show()
#Ponemos la app en loop para ejecutarse
app.MainLoop()
