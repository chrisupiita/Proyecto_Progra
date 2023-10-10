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


class VentanaUsuario(wx.Frame):
    def __init__(self, parent):
        super(VentanaUsuario, self).__init__(parent, title="Acciones de Usuario", size=(450, 250))
        panel = wx.Panel(self)
        
        btn_alta_cliente = wx.Button(panel, label="Alta de Cliente", pos=(30, 20),size=(150, 30))
        btn_busqueda_cliente = wx.Button(panel, label="Búsqueda de Cliente", pos=(30, 100),size=(150, 30))
        btn_modificar_cliente = wx.Button(panel, label="Modificar Cliente", pos=(250, 20),size=(150, 30))
        btn_eliminar_cliente = wx.Button(panel, label="Eliminar Cliente", pos=(250, 100),size=(150, 30))
        btn_cancelar = wx.Button(panel, label="Cancelar", pos=(320, 160), size=(80, 30))
        
        btn_cancelar.Bind(wx.EVT_BUTTON, self.OnCancelar)
        btn_alta_cliente.Bind(wx.EVT_BUTTON, self.OnAltaCliente)
        btn_busqueda_cliente.Bind(wx.EVT_BUTTON, self.OnBusquedaCliente)
        btn_modificar_cliente.Bind(wx.EVT_BUTTON, self.OnModificarCliente)
        btn_eliminar_cliente.Bind(wx.EVT_BUTTON, self.OnEliminarCliente)
        
        self.Show()

    def OnAltaCliente(self, event):
        # Llama a la ventana de alta de cliente aquí
        ventana_alta = VentanaRegistro(self)
        ventana_alta.Center()
        ventana_alta.Show()

    def OnBusquedaCliente(self, event):
        # Llama a la ventana de búsqueda de cliente aquí
        ventana_busqueda = VentanaBusqueda(self)
        ventana_busqueda.Center()
        ventana_busqueda.Show()

    def OnModificarCliente(self, event):
        # Llama a la ventana de modificación de cliente aquí
        ventana_modificar = VentanaModificar(self)
        ventana_modificar.Center()
        ventana_modificar.Show()

    def OnEliminarCliente(self, event):
        # Llama a la ventana de eliminación de cliente aquí
        ventana_eliminar = VentanaEliminar(self)
        ventana_eliminar.Center()
        ventana_eliminar.Show()
        
    def OnCancelar(self, event):
        self.Destroy()

class Interfaz(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.titulo = wx.StaticText(self, label="Lavandería MISTI", pos=(300, 10))
        self.titulo.SetFont(font)
        
        self.lbl_id_cliente = wx.StaticText(self, label="ID del Cliente:", pos=(20, 50))
        self.txt_id_cliente = wx.TextCtrl(self, value="", pos=(225, 50), size=(100, 25))

        self.lbl_nombre_cliente = wx.StaticText(self, label="Nombre del Cliente:", pos=(20, 80))
        self.txt_nombre_cliente = wx.TextCtrl(self, value="", pos=(225, 80), size=(200, 25))
        
        self.btn_verificar_cliente = wx.Button(self, label="Verificar Cliente", pos=(20, 110), size=(150, 30))
        self.Bind(wx.EVT_BUTTON, self.OnVerificarCliente, self.btn_verificar_cliente)
        
        self.lblname1 = wx.StaticText(self, label="Inserta numero de la maquina:", pos=(20, 150))
        self.maquina = wx.TextCtrl(self, value="", pos=(225, 150), size=(30, 20))
        
        self.lblname4 = wx.StaticText(self, label="¿Cuantos kilos de ropa se van a lavar?", pos=(20,180))
        self.maquina = wx.TextCtrl(self, value="", pos=(225, 180), size=(30,20))
        
        self.precio = wx.StaticText(self, label="$20 por kilo", pos=(270,183))
        
        self.lblname5 = wx.StaticText(self, label="Selecciona servicio adicional:", pos=(20, 210))
        self.servicios_adicionales = ["Ninguno", "Detergente", "Suavizante"]
        self.cmb_servicios_adicionales = wx.ComboBox(self, pos=(225, 210), size=(150, 25), choices=self.servicios_adicionales, style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.cmb_servicios_adicionales.SetSelection(0)  # Establece la selección inicial
        
        self.lbltipo = wx.StaticText(self, label="Tipo de Máquina:", pos=(20, 240))
        self.tipos_maquina = ["Lavadora", "Secadora", "Mixta"]
        self.cmb_tipo_maquina = wx.ComboBox(self, pos=(225, 240), size=(100, 25), choices=self.tipos_maquina, style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.cmb_tipo_maquina.SetSelection(0)  # Establece la selección inicial
        
        self.lblname6 = wx.StaticText(self, label="Total a Pagar:", pos=(20,270))
        self.tpagar1 = wx.TextCtrl(self, value="", pos=(225, 270), size=(80,20))
        self.lblname7 = wx.StaticText(self, label="Importe:", pos=(20,300))
        self.tpagar2 = wx.TextCtrl(self, value="", pos=(225, 300), size=(80,20))
        self.lblname8 = wx.StaticText(self, label="Cambio:", pos=(20,330))
        self.tpagar3 = wx.TextCtrl(self, value="", pos=(225, 330), size=(80,20))

    
        self.button_usuario = wx.Button(self, label="Acciones \nUsuario", pos=(620, 400), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.OnMostrarVentanaUsuario, self.button_usuario)
        
        self.button1 =wx.Button(self, label="Realizar\nCobro", pos=(310, 400),size=(150,40))
        self.button2 =wx.Button(self, label="Calcular\nTotal", pos=(155, 400),size=(150,40))
        self.button3 =wx.Button(self, label="Activar / Desactivar\nMantenimiento", pos=(465, 400),size=(150,40))
        #self.button4 =wx.Button(self, label="Buscar\nCliente", pos=(620, 115),size=(150,30))
        
        #self.button6 =wx.Button(self, label="Modificar\nCliente", pos=(620, 185),size=(150,30))
        #self.button7 =wx.Button(self, label="Baja\nCliente", pos=(620, 220),size=(150,30))
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.maqs = wx.StaticText(self, label="Listado de maquinas:", pos=(525,100))
        self.maqs.SetFont(font)
        
        self.nummaq1 = wx.StaticText(self, label="M1:", pos=(500,150))
        self.statmaq1 = wx.StaticText(self, label="Libre", pos=(530,150))
        self.nummaq2 = wx.StaticText(self, label="M2:", pos=(500,170))
        self.statmaq2 = wx.StaticText(self, label="Libre", pos=(530,170))
        self.nummaq3 = wx.StaticText(self, label="M3:", pos=(500,190))
        self.statmaq3 = wx.StaticText(self, label="Libre", pos=(530,190))
        self.nummaq4 = wx.StaticText(self, label="M4:", pos=(500,210))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(530,210))
        self.nummaq4 = wx.StaticText(self, label="M5:", pos=(500,230))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(530,230))
        self.nummaq1 = wx.StaticText(self, label="M6:", pos=(500,250))
        self.statmaq1 = wx.StaticText(self, label="Libre", pos=(530,250))
        self.nummaq2 = wx.StaticText(self, label="M7:", pos=(500,270))
        self.statmaq2 = wx.StaticText(self, label="Libre", pos=(530,270))
        
        self.nummaq3 = wx.StaticText(self, label="M8:", pos=(600,150))
        self.statmaq3 = wx.StaticText(self, label="Libre", pos=(630,150))
        self.nummaq4 = wx.StaticText(self, label="M9:", pos=(600,170))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(630,170))
        self.nummaq4 = wx.StaticText(self, label="M10:", pos=(600,190))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(630,190))
        self.nummaq1 = wx.StaticText(self, label="M11:", pos=(600,210))
        self.statmaq1 = wx.StaticText(self, label="Libre", pos=(630,210))
        self.nummaq2 = wx.StaticText(self, label="M12:", pos=(600,230))
        self.statmaq2 = wx.StaticText(self, label="Libre", pos=(630,230))
        self.nummaq3 = wx.StaticText(self, label="M13:", pos=(600,250))
        self.statmaq3 = wx.StaticText(self, label="Libre", pos=(630,250))
        self.nummaq4 = wx.StaticText(self, label="M14:", pos=(600,270))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(630,270))
        self.nummaq4 = wx.StaticText(self, label="M15:", pos=(600,290))
        self.statmaq4 = wx.StaticText(self, label="Libre", pos=(630,290))
        
        self.det = wx.StaticText(self, label="Detergente $20", pos=(500,330))
        self.det = wx.StaticText(self, label="Suavizante $25", pos=(500,350))
        
        # ... Otros elementos de la interfaz ...

    def OnMostrarVentanaUsuario(self, event):
        ventana_usuario = VentanaUsuario(self)
        ventana_usuario.Center()
        ventana_usuario.Show()
        
    def OnVerificarCliente(self, event):
        id_cliente = self.txt_id_cliente.GetValue()
        nombre_cliente = self.txt_nombre_cliente.GetValue()

        # Realiza la verificación del cliente aquí
        usuario_encontrado = self.buscar_usuario(id_cliente, nombre_cliente)

        if usuario_encontrado:
            mensaje = "Información del cliente:\n\n" \
                      f"ID: {usuario_encontrado[0]}\n" \
                      f"Nombre(s): {usuario_encontrado[1]}\n" \
                      f"Apellido Paterno: {usuario_encontrado[2]}\n" \
                      f"Apellido Materno: {usuario_encontrado[3]}\n" \
                      f"Fecha de Registro: {usuario_encontrado[4]}\n" \
                      f"Fecha de Vencimiento: {usuario_encontrado[5]}\n" \
                      f"Descuento: {usuario_encontrado[6]}"
        else:
            mensaje = "Usuario no encontrado."

        dlg = wx.MessageDialog(self, mensaje, "Verificación de Cliente", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def buscar_usuario(self, id_buscar, nombre_buscar):
        # Abre el archivo CSV y busca al usuario
        nombre_archivo = "usuarios.csv"

        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Salta la primera fila (encabezados)
            for fila in lector_csv:
                id_usuario = fila[0]
                nombre = fila[1]
                if id_buscar == id_usuario and nombre_buscar == nombre:
                    return fila  # Retorna los datos del usuario encontrado

        return None  # Retorna None si el usuario no se encuentra


# Crear una aplicación de wxPython
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Lavandería MISTI", size=(800, 500))
interfaz = Interfaz(frame)
frame.Show()
app.MainLoop()





