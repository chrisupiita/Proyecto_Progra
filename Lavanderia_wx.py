import wx
import csv
from datetime import datetime
import os

class VentanaRegistro(wx.Dialog):
    def __init__(self, parent):
        super(VentanaRegistro, self).__init__(parent, title="Registro", size=(450, 350))
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.titulo = wx.StaticText(self, label="Alta de usuario", pos=(160,10))
        self.titulo.SetFont(font)
        
        #dimensiones para cuadros de ingreso de texto
        pos_camp_x = 220
        pos_camp_y = 60
        
        pos_inter = 60
        
        pos_tex_x = 70
        
        self.ingr_id = wx.StaticText(self, label="ID del usuario", pos=(pos_tex_x,pos_inter))
        self.id = wx.TextCtrl(self, value="", pos=(pos_camp_x, pos_camp_y), size=(30,20))
        
        self.ingr_nom = wx.StaticText(self, label="Nombre(s)", pos=(pos_tex_x,pos_inter+20))
        self.nombre = wx.TextCtrl(self, value="", pos=(pos_camp_x, pos_camp_y+20), size=(110,20))
        
        self.ingr_ap = wx.StaticText(self, label="Apellido Pat.", pos=(pos_tex_x,pos_inter+40))
        self.ap_pat = wx.TextCtrl(self, value="", pos=(pos_camp_x, pos_camp_y+40), size=(110,20))
        
        self.ingr_am = wx.StaticText(self, label="Apellido Mat.", pos=(pos_tex_x,pos_inter+60))
        self.ap_mat = wx.TextCtrl(self, value="", pos=(pos_camp_x, pos_camp_y+60), size=(110,20))
        
        self.fecha = wx.StaticText(self, label="Fecha registro", pos=(pos_tex_x,pos_inter+110))
        
        self.dia = wx.StaticText(self, label="dia", pos=(220,pos_inter+90))
        self.d = wx.TextCtrl(self, value="", pos=(pos_camp_x, pos_camp_y+110), size=(20,20))
        
        self.mes = wx.StaticText(self, label="mes", pos=(255,pos_inter+90))
        self.m = wx.TextCtrl(self, value="", pos=(pos_camp_x+35, pos_camp_y+110), size=(20,20))
        
        self.anio = wx.StaticText(self, label="año", pos=(290,pos_inter+90))
        self.a = wx.TextCtrl(self, value="", pos=(pos_camp_x+70, pos_camp_y+110), size=(40,20))
        
        
        self.vecimiento = wx.StaticText(self, label="Vencimiento", pos=(pos_tex_x,pos_inter+150))
        
        self.dia_v = wx.StaticText(self, label="dia", pos=(220,pos_inter+130))
        self.d_v = wx.TextCtrl(self, value="", pos=(pos_camp_x, pos_camp_y+150), size=(20,20))
        
        self.mes_v = wx.StaticText(self, label="mes", pos=(255,pos_inter+130))
        self.m_v = wx.TextCtrl(self, value="", pos=(pos_camp_x+35, pos_camp_y+150), size=(20,20))
        
        self.anio_v = wx.StaticText(self, label="año", pos=(290,pos_inter+130))
        self.a_v = wx.TextCtrl(self, value="", pos=(pos_camp_x+70, pos_camp_y+150), size=(40,20))
        
        
        self.descuento = wx.StaticText(self, label="Descuento", pos=(pos_tex_x,pos_inter+180))
        self.desc = wx.TextCtrl(self, value="", pos=(pos_camp_x, pos_camp_y+180), size=(40,20))
        
        #botones 
        self.b_cancelar =wx.Button(self, label="Cancelar", pos=(330, 270),size=(80,30))
        self.b_regist =wx.Button(self, label="Registrar", pos=(240, 270),size=(80,30))
        
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.b_cancelar)
        self.Bind(wx.EVT_BUTTON, self.OnAlta, self.b_regist)
        
    def OnAlta(self, event):
        id_us = self.id.GetValue()
        nom =self.nombre.GetValue()
        ap_p = self.ap_pat.GetValue()
        ap_m = self.ap_mat.GetValue()
        di = int(self.d.GetValue())
        me = int(self.m.GetValue())
        an = int(self.a.GetValue())
        di_v = int(self.d_v.GetValue())
        me_v = int(self.m_v.GetValue())
        an_v = int(self.a_v.GetValue())
        des = self.desc.GetValue()
        
        fecha_reg= datetime(an, me, di)
        fecha_venc = datetime(an_v, me_v, di_v)
        
        #usuarios = [id_us,nom,ap_p,ap_p,ap_m,datetime(an, me, di),datetime(an_v,me_v,di_v),des]
        nombre_archivo = "usuarios.csv"
        archivo_existe = os.path.isfile(nombre_archivo)
        
        with open(nombre_archivo, mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)

            # Si el archivo no existe, escribe los encabezados de las columnas
            if not archivo_existe:
                escritor_csv.writerow(["ID", "Nombre(s)", "Apellido Paterno", "Apellido Materno", "Fecha registro", "Fecha vencimiento", "Descuento"])

            # Escribe los datos de los usuarios en filas separadas
            fecha_reg_str = fecha_reg.strftime("%Y-%m-%d")
            fecha_venc_srt = fecha_venc.strftime("%Y-%m-%d")
            escritor_csv.writerow([id_us, nom, ap_p, ap_m, fecha_reg_str, fecha_venc_srt, des])
            
        mensaje = "Usuario registrado con éxito."
        dlg = wx.MessageDialog(self, mensaje, "Registro Exitoso", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()  # Destruye el diálogo después de cerrarlo

        # Cerrar la ventana de alta de usuario
        self.Destroy()
        
    def OnCancelar(self, event):
        self.Destroy()
        
class VentanaBusqueda(wx.Dialog):
    def __init__(self, parent):
        super(VentanaBusqueda, self).__init__(parent, title="Buscar cliente", size=(400, 200))
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.titulo = wx.StaticText(self, label="Buscar cliente", pos=(120, 10))
        self.titulo.SetFont(font)

        self.lbl_nombre = wx.StaticText(self, label="Nombre:", pos=(20, 50))
        self.txt_nombre = wx.TextCtrl(self, value="", pos=(100, 50), size=(150, 25))

        self.lbl_id = wx.StaticText(self, label="ID:", pos=(20, 90))
        self.txt_id = wx.TextCtrl(self, value="", pos=(100, 90), size=(100, 25))

        self.btn_buscar = wx.Button(self, label="Buscar", pos=(270, 50), size=(80, 30))
        self.btn_cancelar = wx.Button(self, label="Cancelar", pos=(270, 90), size=(80, 30))

        self.Bind(wx.EVT_BUTTON, self.OnBuscar, self.btn_buscar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.btn_cancelar)

    def OnBuscar(self, event):
        nombre_buscar = self.txt_nombre.GetValue()
        id_buscar = self.txt_id.GetValue()

        # Abre el archivo CSV y busca al usuario
        nombre_archivo = "usuarios.csv"
        usuario_encontrado = None

        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Salta la primera fila (encabezados)
            for fila in lector_csv:
                id_usuario = fila[0]
                nombre = fila[1]
                if id_buscar == id_usuario and nombre_buscar == nombre:
                    usuario_encontrado = fila
                    break

        if usuario_encontrado:
            mensaje = "Información del usuario:\n\n" \
                      f"ID: {usuario_encontrado[0]}\n" \
                      f"Nombre(s): {usuario_encontrado[1]}\n" \
                      f"Apellido Paterno: {usuario_encontrado[2]}\n" \
                      f"Apellido Materno: {usuario_encontrado[3]}\n" \
                      f"Fecha de Registro: {usuario_encontrado[4]}\n" \
                      f"Fecha de Vencimiento: {usuario_encontrado[5]}\n" \
                      f"Descuento: {usuario_encontrado[6]}"
        else:
            mensaje = "Usuario no encontrado."

        dlg = wx.MessageDialog(self, mensaje, "Resultado de la Búsqueda", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnCancelar(self, event):
        self.Destroy()

        
#Modificar usuario
class VentanaModificar(wx.Dialog):
    def __init__(self, parent):
        super(VentanaModificar, self).__init__(parent, title="Modificar Usuario", size=(400, 300))
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.titulo = wx.StaticText(self, label="Modificar Usuario", pos=(120, 10))
        self.titulo.SetFont(font)

        self.lbl_nombre = wx.StaticText(self, label="Nombre:", pos=(20, 50))
        self.txt_nombre = wx.TextCtrl(self, value="", pos=(100, 50), size=(150, 25))

        self.lbl_id = wx.StaticText(self, label="ID:", pos=(20, 90))
        self.txt_id = wx.TextCtrl(self, value="", pos=(100, 90), size=(100, 25))

        self.lbl_parametro = wx.StaticText(self, label="Parámetro a Modificar:", pos=(20, 130))
        self.cmb_parametro = wx.ComboBox(self, pos=(200, 130), size=(150, 25),
                                         choices=["Nombre(s)", "Apellido Paterno", "Apellido Materno", "Fecha registro", "Fecha vencimiento", "Descuento"])

        self.lbl_nuevo_valor = wx.StaticText(self, label="Nuevo Valor:", pos=(20, 170))
        self.txt_nuevo_valor = wx.TextCtrl(self, value="", pos=(150, 170), size=(200, 25))

        self.btn_buscar = wx.Button(self, label="Buscar", pos=(270, 50), size=(80, 30))
        self.btn_modificar = wx.Button(self, label="Modificar", pos=(270, 90), size=(80, 30))
        self.btn_cancelar = wx.Button(self, label="Cancelar", pos=(270, 210), size=(80, 30))

        self.Bind(wx.EVT_BUTTON, self.OnBuscar, self.btn_buscar)
        self.Bind(wx.EVT_BUTTON, self.OnModificar, self.btn_modificar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.btn_cancelar)

    def OnBuscar(self, event):
        nombre_buscar = self.txt_nombre.GetValue()
        id_buscar = self.txt_id.GetValue()

        # Abre el archivo CSV y busca al usuario
        nombre_archivo = "usuarios.csv"
        usuario_encontrado = None

        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Salta la primera fila (encabezados)
            for fila in lector_csv:
                id_usuario = fila[0]
                nombre = fila[1]
                if id_buscar == id_usuario and nombre_buscar == nombre:
                    usuario_encontrado = fila
                    break

        if usuario_encontrado:
            mensaje = "Información del usuario a modificar:\n\n" \
                      f"ID: {usuario_encontrado[0]}\n" \
                      f"Nombre(s): {usuario_encontrado[1]}\n" \
                      f"Apellido Paterno: {usuario_encontrado[2]}\n" \
                      f"Apellido Materno: {usuario_encontrado[3]}\n" \
                      f"Fecha de Registro: {usuario_encontrado[4]}\n" \
                      f"Fecha de Vencimiento: {usuario_encontrado[5]}\n" \
                      f"Descuento: {usuario_encontrado[6]}"
        else:
            mensaje = "Usuario no encontrado."

        dlg = wx.MessageDialog(self, mensaje, "Resultado de la Búsqueda", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnModificar(self, event):
        nombre_buscar = self.txt_nombre.GetValue()
        id_buscar = self.txt_id.GetValue()
        parametro_modificar = self.cmb_parametro.GetValue()
        nuevo_valor = self.txt_nuevo_valor.GetValue()

        # Abre el archivo CSV y busca al usuario
        nombre_archivo = "usuarios.csv"
        usuarios = []

        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            encabezados = next(lector_csv)  # Lee los encabezados
            for fila in lector_csv:
                id_usuario = fila[0]
                nombre = fila[1]
                if id_buscar == id_usuario and nombre_buscar == nombre:
                    fila[encabezados.index(parametro_modificar)] = nuevo_valor
                usuarios.append(fila)

        # Escribe los usuarios actualizados en el archivo CSV
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(encabezados)
            for usuario in usuarios:
                escritor_csv.writerow(usuario)

        self.txt_nombre.SetValue("")
        self.txt_id.SetValue("")
        self.cmb_parametro.SetValue("")
        self.txt_nuevo_valor.SetValue("")
        mensaje = f"Parámetro '{parametro_modificar}' modificado exitosamente."
        dlg = wx.MessageDialog(self, mensaje, "Resultado de la Modificación", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnCancelar(self, event):
        self.Destroy()


#baja de usuario
class VentanaEliminar(wx.Dialog):
    def __init__(self, parent):
        super(VentanaEliminar, self).__init__(parent, title="Eliminar Usuario", size=(400, 220))
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.titulo = wx.StaticText(self, label="Eliminar Usuario", pos=(120, 10))
        self.titulo.SetFont(font)

        self.lbl_nombre = wx.StaticText(self, label="Nombre:", pos=(20, 50))
        self.txt_nombre = wx.TextCtrl(self, value="", pos=(100, 50), size=(150, 25))

        self.lbl_id = wx.StaticText(self, label="ID:", pos=(20, 90))
        self.txt_id = wx.TextCtrl(self, value="", pos=(100, 90), size=(100, 25))

        self.btn_buscar = wx.Button(self, label="Buscar", pos=(90, 130), size=(80, 30))
        self.btn_borrar = wx.Button(self, label="Borrar", pos=(180, 130), size=(80, 30))
        self.btn_cancelar = wx.Button(self, label="Cancelar", pos=(270, 130), size=(80, 30))

        self.Bind(wx.EVT_BUTTON, self.OnBuscar, self.btn_buscar)
        self.Bind(wx.EVT_BUTTON, self.OnBorrar, self.btn_borrar)
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.btn_cancelar)

    def OnBuscar(self, event):
        nombre_buscar = self.txt_nombre.GetValue()
        id_buscar = self.txt_id.GetValue()

        # Abre el archivo CSV y busca al usuario
        nombre_archivo = "usuarios.csv"
        usuario_encontrado = None

        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Salta la primera fila (encabezados)
            for fila in lector_csv:
                id_usuario = fila[0]
                nombre = fila[1]
                if id_buscar == id_usuario and nombre_buscar == nombre:
                    usuario_encontrado = fila
                    break

        if usuario_encontrado:
            mensaje = "Información del usuario a borrar:\n\n" \
                      f"ID: {usuario_encontrado[0]}\n" \
                      f"Nombre(s): {usuario_encontrado[1]}\n" \
                      f"Apellido Paterno: {usuario_encontrado[2]}\n" \
                      f"Apellido Materno: {usuario_encontrado[3]}\n" \
                      f"Fecha de Registro: {usuario_encontrado[4]}\n" \
                      f"Fecha de Vencimiento: {usuario_encontrado[5]}\n" \
                      f"Descuento: {usuario_encontrado[6]}"
        else:
            mensaje = "Usuario no encontrado."

        dlg = wx.MessageDialog(self, mensaje, "Resultado de la Búsqueda", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnBorrar(self, event):
        nombre_buscar = self.txt_nombre.GetValue()
        id_buscar = self.txt_id.GetValue()

        # Abre el archivo CSV y busca al usuario
        nombre_archivo = "usuarios.csv"
        usuarios = []

        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            encabezados = next(lector_csv)  # Lee los encabezados
            for fila in lector_csv:
                id_usuario = fila[0]
                nombre = fila[1]
                if id_buscar != id_usuario or nombre_buscar != nombre:
                    usuarios.append(fila)

        # Escribe los usuarios restantes en el archivo CSV
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(encabezados)
            for usuario in usuarios:
                escritor_csv.writerow(usuario)

        self.txt_nombre.SetValue("")
        self.txt_id.SetValue("")
        mensaje = "Usuario borrado exitosamente."
        dlg = wx.MessageDialog(self, mensaje, "Resultado del Borrado", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnCancelar(self, event):
        self.Destroy()



class Interfaz(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Bienvenido a nuestra lavanderia, ¿Que servicio desea al dia de hoy?", pos=(10, 10))
        self.lblname1 = wx.StaticText(self, label="Inserta numero de la maquina:", pos=(20,50))
        self.maquina = wx.TextCtrl(self, value="", pos=(225, 50), size=(30,20))
        self.lblname2 = wx.StaticText(self, label="Tipo de Maquina:", pos=(300,50))
        self.lbltipo = wx.StaticText(self, label="Lavadora", pos=(400,50))
        self.lbltipo1 = wx.StaticText(self, label="Secadora", pos=(400,75))
        self.lbltipo2 = wx.StaticText(self, label="Mixta", pos=(400,25))
        
        self.lblname4 = wx.StaticText(self, label="¿Cuantos kilos de ropa se van a lavar?", pos=(20,80))
        self.maquina = wx.TextCtrl(self, value="", pos=(225, 80), size=(30,20))
        self.lblname5 = wx.StaticText(self, label="Agregue extra al servicio:", pos=(20,110))
        self.serv1 = wx.CheckBox(self, label = 'Detergente',pos = (30,130))
        self.serv2 = wx.CheckBox(self, label = 'Suavizante',pos = (120,130))
        self.lblname6 = wx.StaticText(self, label="Total a Pagar:", pos=(300,110))
        self.tpagar1 = wx.TextCtrl(self, value="", pos=(400, 110), size=(80,20))
        self.lblname7 = wx.StaticText(self, label="Importe:", pos=(300,130))
        self.tpagar2 = wx.TextCtrl(self, value="", pos=(400, 130), size=(80,20))
        self.lblname8 = wx.StaticText(self, label="Cambio:", pos=(300,150))
        self.tpagar3 = wx.TextCtrl(self, value="", pos=(400, 150), size=(80,20))
        
        """
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
        """
        
        self.button1 =wx.Button(self, label="Realizar\nCobro", pos=(620, 10),size=(150,30))
        self.button2 =wx.Button(self, label="Calcular\nTotal", pos=(620, 45),size=(150,30))
        self.button3 =wx.Button(self, label="Activar / Desactivar\nMantenimiento", pos=(620, 80),size=(150,30))
        #self.button4 =wx.Button(self, label="Buscar\nCliente", pos=(620, 115),size=(150,30))
        
        #self.button6 =wx.Button(self, label="Modificar\nCliente", pos=(620, 185),size=(150,30))
        #self.button7 =wx.Button(self, label="Baja\nCliente", pos=(620, 220),size=(150,30))
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
        
        #Definicion de botones y llamadas a funciones
        self.button_alta =wx.Button(self, label="Alta\nCliente", pos=(620, 265),size=(150,40))
        self.Bind(wx.EVT_BUTTON, self.OnMostrarRegistro, self.button_alta)
        
        self.button_bus =wx.Button(self, label="Busqueda\nCliente", pos=(620, 310),size=(150,40))
        self.Bind(wx.EVT_BUTTON, self.OnBusqueda, self.button_bus)
        
        self.button_mod =wx.Button(self, label="Modificar\nCliente", pos=(620, 355),size=(150,40))
        self.Bind(wx.EVT_BUTTON, self.OnModificar, self.button_mod)
        
        self.button_elim =wx.Button(self, label="Eliminar\nCliente", pos=(620, 400),size=(150,40))
        self.Bind(wx.EVT_BUTTON, self.OnEliminar, self.button_elim)
        
        #Eventos de Boton
        self.Bind(wx.EVT_BUTTON, self.OnClick1, self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.button2)
        self.Bind(wx.EVT_BUTTON, self.OnClick3, self.button3)
        #self.Bind(wx.EVT_BUTTON, self.OnClick4, self.button4)
        #self.Bind(wx.EVT_BUTTON, self.OnClick5, self.button5) alta cliente
        #self.Bind(wx.EVT_BUTTON, self.OnClick6, self.button6)
        #self.Bind(wx.EVT_BUTTON, self.OnClick7, self.button7)

    #Definicion de eventos
    
    #evento de boton alta usuario
    def OnMostrarRegistro(self, event):
        ventana_registro = VentanaRegistro(self)
        ventana_registro.Center()
        ventana_registro.ShowModal()
        ventana_registro.Destroy()  # Destruye la ventana emergente cuando se cierra
    
    def OnBusqueda(self, event):
        ventana_busq = VentanaBusqueda(self)
        ventana_busq.Center()
        ventana_busq.ShowModal()
        ventana_busq.Destroy()  # Destruye la ventana emergente cuando se cierra
        
    def OnModificar(self, event):
        ventana_busq = VentanaModificar(self)
        ventana_busq.Center()
        ventana_busq.ShowModal()
        ventana_busq.Destroy()
        
    def OnEliminar(self, event):
        ventana_busq = VentanaEliminar(self)
        ventana_busq.Center()
        ventana_busq.ShowModal()
        ventana_busq.Destroy()  # Destruye la ventana emergente cuando se cierra
    
    def OnClick1(self,event): #evento realizar cobro
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
frame.Center()
frame.Show()
#Ponemos la app en loop para ejecutarse
app.MainLoop()