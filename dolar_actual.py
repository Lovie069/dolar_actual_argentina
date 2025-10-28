'''Como OBTENER el VALOR del DOLAR BLUE con PYTHON
https://www.youtube.com/watch?v=dPnZaWYqiIM'''

'''PAGINA PARA CORREGIR EL ERROR DE IMPORTACIÓN DE DATOS DE AMBITO
https://stackoverflow.com/questions/38489386/how-to-fix-403-forbidden-errors-when-calling-apis-using-python-requests'''

'''Agregar Data Frame en Tkinter
https://es.stackoverflow.com/questions/340278/como-mostrar-un-dataframe-en-tkinter'''

'''Adding validation to an Entry widget
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-validation.html'''

'''Python String Methods
https://www.w3schools.com/python/python_ref_string.asp'''


'''IMPORTACIÓN DE LIBRERIAS'''
import requests
import pandas as pd
import numpy as np
# import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import os
from datetime import datetime
from funciones_TC  import *


'''IMPORTACIÓN DE FUNCIONES PROPIAS'''
from operaciones_math import *


'''INCIAMOS LA INTERFAZ DE USUARIO'''
#CREACIÓN DE VENTANAS:
raiz=Tk()
# raiz.title("Tipo de Cambio del Dolar Oficial en Argentina")
raiz.title("Tipo de Cambio del Dolar en Argentina")

#CONFIGURACION DE LA VENTANA RAIZ:
ancho_ventana = 510
alto_ventana = 280

x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

# raiz.geometry("700x750"+100,100)

colorRaiz = '#E0BFE0'
raiz.config(bg=colorRaiz,padx=10,pady=10)
raiz.resizable(0,0)


'''VARIABLES GLOBALES'''
comentario=StringVar()

'''VARIABLE PARA EFECTO PARPADEO:'''
flash_delay = 250  # msec between colour change


#CONFIGURACION DEL MENU PRINCIPAL:
barra_menu=Menu(raiz)
raiz.config(menu=barra_menu)

#COMANDO PARA ELIMINAR LA LÍNEA DE LÁGRIMA DEL MENÚ:
raiz.option_add("*tearOff",False)

#CREANDO LAS PESTAÑAS DEL MENÚ PRINCIPAL:
menu_Acerca=Menu(barra_menu)

#AGREGANDO LAS PESTAÑAS AL MENÚ PRINCIPAL:
barra_menu.add_cascade(menu=menu_Acerca,label="Información de contacto")

#CREANDO Y AGREGANDO LOS SUB MENÚS DE LA PESTAÑA "Acerca de":
menu_Acerca.add_command(label="Contáctanos",command=lambda:mensajeContacto())
menu_Acerca.add_command(label="Versión",command=lambda:mensajeVersion())


#Mensaje de contacto:
def mensajeContacto():
    messagebox.showinfo("Contáctanos","Para mayor información favor escribir al siguiente email:\n\nrodriguezcolmenaresl@gmail.com")

#Mensaje de versión info:
def mensajeVersion():
    # messagebox.showinfo("Info. Versión","Versión 1.0 \n \nMes/Año: 09/2024")
    # messagebox.showinfo("Info. Versión","Versión 1.3 \n \nMes/Año: 03/2025")
    # messagebox.showinfo("Info. Versión","Versión 1.4 \n \nMes/Año: 10/2025")
    messagebox.showinfo("Info. Versión","Versión 1.5 \n \nMes/Año: 10/2025")


'''GENERAMOS CARACTERISTICAS DE LA INTERFAZ QUE SE USARAN EN MULTIPLES PARTES'''
# DIMENSIONES

#PADDING:
x1=15 #Padx
y1=1 #Pady

x2=x1 #Padx
y2=5 #Pady

x3=x1 #Padx
y3= (5,1) #Pady

#ANCHO DE GIDGETS EN VENTANA DE ÁREAS:
h1=80 #Alto de botones
h2=1 #Alto filas frame áreas y volúmenes
w1=100 #Ancho botones
w2=400 #Ancho pantalla de cálculo
w3=100 #Ancho imágenes
w4=15 #Ancho label datos


'''BORDES'''
# TIPOS: raised, sunken, flat, groove, ridge, solid
bordeTitulo = "flat"
bordeSubtitulo = "flat"

# ANCHO
b1 = 1
b2 = 10

#ORIENTACION:
u1="nsew" #Ubicación figuras geométricas
u2="e"    #Ubicación de Gitgets en frame calculos de áreas y volúmenes


'''BOTONES'''
# COLORES
# FONDOS POR DEFECTO:
colorDbgBoton = "#E0BFE0"

# FONDOS AL PRESIONAR
colorAbgBoton = "#E075DF"

# COLOR DE TEXTO POR DEFECTO
colorDfBoton = "blue"

# COLOR DE TEXTO AL PRESIONAR
colorAfBoton = "white"


'''LETRAS'''
#COLORES:
# colorGeneral = '#723b71'
colorGeneral = '#502A4F'
colorSeleccion = '#944D93'
colorComentario = '#E075DF'

fuenteTitulo = colorGeneral
fuenteSubtitulo = colorGeneral
fuenteBotones= colorGeneral
fuenteDatos = colorGeneral
fuenteIngreso = colorGeneral
fuenteResultados = colorGeneral

new_colour = colorGeneral

#FUENTES:
# fuenteGeneral = 'Tahoma'
fuenteGeneral = 'Comic Sans MS'
'''https://blog.hubspot.es/website/fuentes-html'''
letraTitulo = (fuenteGeneral, 11, 'bold')
letraSubtitulos= (fuenteGeneral, 10, 'bold')
letraBotones= (fuenteGeneral, 8, 'bold')
letraDatos= (fuenteGeneral, 9)
letraDatos2= (fuenteGeneral, 7, 'bold')
letraIngresos= (fuenteGeneral, 9)
letraResultados= (fuenteGeneral, 9)

# FONDOS
fondoIngresos = "white"

#AVISOS:
F1 = "Debes insertar al menos 2 datos"
F2 = "Faltan 1 campo por llenar"
F3 = "Operación realizada"
F4 = "Recuerda limpiar los campos antes de operar"


'''CREACION DE VENTANA PRINCIPAL'''
# miFrame=Frame(raiz) #width=200, height=300
# miFrame.pack()
miFrame=Frame(raiz, relief="solid",borderwidth=0,padx=1,pady=1)
miFrame.pack()
#TIPOS DE BORDES: raised, sunken, flat, groove, ridge, solid
# TIPOS DE CURSOR , cursor='cross'

# recuadro1=ttk.LabelFrame(miFrame,text="Geométricos",padding=(10,5))
# recuadro1.pack(fill="both",expand=1)
'''CREACIÓN DE ESTILOS'''
# s = ttk.Style()
# # s.theme_use("classic")
# s.configure("TNotebook", background="blue")

s1 = ttk.Style()
# s1.theme_use("classic")
# print(ttk.Style().theme_names())
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
# s1.configure("TNotebook.Tab", foreground="black", background="green", font=('fuenteGeneral', '11', 'bold'))
s1.configure("TNotebook.Tab", foreground=colorGeneral, font=('fuenteGeneral', '8', 'bold'))
s1.map("TNotebook.Tab", foreground=[("active", colorSeleccion)])

s2 = ttk.Style()

'''CREACIÓN DE VENTANA TIPO NOTEBOOK'''
#NOTEBOOK:
notebook1 = ttk.Notebook(miFrame,padding=10)
notebook1.grid(column=0,row=0,sticky='nsew')

tipoCambio = ttk.Frame(notebook1,padding=(1,1)) #PRIMERA PÁGINA
verificacionValores = ttk.Frame(notebook1,padding=(1,1)) #SEGUNDA PÁGINA
dolarHistorico = ttk.Frame(notebook1,padding=(1,1)) #TERCERA PÁGINA

notebook1.add(tipoCambio, text='TC')
notebook1.add(verificacionValores, text='Verificación')
notebook1.add(dolarHistorico, text='Histórico')



'''URL DE TODAS LAS COTIZACIONES DE DOLAR EN ARGENTINA'''
url_oficial = "https://mercados.ambito.com//dolar/oficial/variacion"
url_nacion = "https://mercados.ambito.com//dolarnacion//variacion"
url_informal = "https://mercados.ambito.com//dolar/informal/variacion"
url_dolar_turista = "https://mercados.ambito.com//dolarturista/variacion"
url_dolar_cripto = "https://mercados.ambito.com//dolarcripto/variacion"
url_dolar_mayorista = "https://mercados.ambito.com//dolar/mayorista/variacion"
url_dolar_rava_ccl = "https://mercados.ambito.com//dolarrava/cl/variacion"
url_dolar_rava_mep = "https://mercados.ambito.com//dolarrava/mep/variacion"
# url_dolar_futuro = "https://mercados.ambito.com//dolarfuturo/variacion"
# url_euro = "https://mercados.ambito.com//euro//variacion"
# url_euro_informal = "https://mercados.ambito.com//euro/informal/variacion"

'''URL DE LA COTIZACIÓN DE DOLAR  EN ARGENTINA QUE VAMOS A USAR EN ESTA APP'''

# Lista de opciones de cotizaciones y nombres legibles
opciones_dolar = [
    ("Dólar Oficial", url_oficial),
    ("Dólar Nación", url_nacion),
    ("Dólar Blue/Informal", url_informal),
    ("Dólar Mayorista", url_dolar_mayorista),
    ("Dólar Turista", url_dolar_turista),
    ("Dólar Mep", url_dolar_rava_mep),
    ("Dólar CCL", url_dolar_rava_ccl),
    ("Dólar Cripto", url_dolar_cripto),
]

opcion_dolar_var = StringVar()
opcion_dolar_var.set("Dólar Nación")  # Valor por defecto en el desplegable

# Map para obtener la URL en base al nombre mostrado
mapa_opciones_dolar = {nombre: url for nombre, url in opciones_dolar}
url_dolar = mapa_opciones_dolar[opcion_dolar_var.get()]

def actualizar_url_dolar(*args):
    global url_dolar
    url_dolar = mapa_opciones_dolar[opcion_dolar_var.get()]

opcion_dolar_var.trace_add('write', actualizar_url_dolar)

# Crea la lista desplegable en la pestaña TipoCambio
# from tkinter import ttk
opciones_nombres = [nombre for nombre, _ in opciones_dolar]
lista_dolar = ttk.Combobox(tipoCambio, textvariable=opcion_dolar_var, values=opciones_nombres, state="readonly")
# lista_dolar.grid(row=0, column=0, padx=5, pady=5, sticky="w")




'''URL DE LAS COTIZACIONES HISTORICAS DEL DOLAR "ESCOGIDO EN ESTA APP" EN ARGENTINA'''
# url_oficial_historico = "https://mercados.ambito.com//dolar/oficial/historico-general/2024-10-09/2024-11-09"
# url_dolarnacion_historico = https://mercados.ambito.com//dolarnacion/historico-general/2024-10-09/2024-11-09
# url_mep_historico = "https://mercados.ambito.com//dolar/mep/historico-general/2024-10-09/2024-11-09"

url_oficial_historico = "https://mercados.ambito.com//dolar/oficial/historico-general/"
url_dolarnacion_historico = "https://mercados.ambito.com//dolarnacion/historico-general/"
url_mep_historico = "https://mercados.ambito.com//dolar/mep/historico-general/"

url_informal_historico = "https://mercados.ambito.com//dolar/informal/historico-general/"
url_dolarturista_historico = "https://mercados.ambito.com//dolar/dolarturista/historico-general/"
url_dolar_cripto_historico = "https://mercados.ambito.com//dolar/dolarcripto/historico-general/"
url_dolar_mayorista_historico = "https://mercados.ambito.com//dolar/mayorista/historico-general/"
url_dolar_rava_ccl_historico = "https://mercados.ambito.com//dolarrava/cl/historico-general/"
url_dolar_rava_mep_historico = "https://mercados.ambito.com//dolarrava/mep/historico-general/"




# Crear lista de opciones para la selección de dólar histórico
opciones_dolar_historico = [
    ("Dólar Oficial", url_oficial_historico),
    ("Dólar Nación", url_dolarnacion_historico),
    ("Dólar Blue/Informal", url_informal_historico),
    ("Dólar Turista", url_dolarturista_historico),
    ("Dólar Mayorista", url_dolar_mayorista_historico),
    ("Dólar Mep", url_mep_historico),
    ("Dólar CCL", url_dolar_rava_ccl_historico),
    ("Dólar Cripto", url_dolar_cripto_historico),
]

opcion_dolar_historico_var = StringVar()
opcion_dolar_historico_var.set("Dólar Nación")  # Valor por defecto

# Map para obtener la URL en base al nombre mostrado
mapa_opciones_dolar_historico = {nombre: url for nombre, url in opciones_dolar_historico}
url_dolar_historico = mapa_opciones_dolar_historico[opcion_dolar_historico_var.get()]

def actualizar_url_dolar_historico(*args):
    global url_dolar_historico
    url_dolar_historico = mapa_opciones_dolar_historico[opcion_dolar_historico_var.get()]

opcion_dolar_historico_var.trace_add('write', actualizar_url_dolar_historico)

# Crea la lista desplegable en la pestaña dolarHistorico
opciones_historico_nombres = [nombre for nombre, _ in opciones_dolar_historico]
lista_dolar_historico = ttk.Combobox(dolarHistorico, textvariable=opcion_dolar_historico_var, values=opciones_historico_nombres, state="readonly")
# lista_dolar_historico.grid(row=0, column=0, padx=5, pady=5, sticky="w")






'''PERMISOS DE LA PÁGINA WEB AMBITO'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}



'''DECLARACIÓN DE VARIABLES'''
df = pd.DataFrame()

'''PANTALLA 1'''
datoIngreso1 = StringVar()

'''PANTALLA 2'''
datoIngreso2 = StringVar()
datoIngreso3 = StringVar()
datoIngreso4 = StringVar()

texto_fecha = StringVar()
texto_compra = StringVar()
texto_venta = StringVar()
texto_variacion = StringVar()

texto_resultado1 = StringVar()

texto_resultado2 = StringVar()
texto_resultado3 = StringVar()
texto_resultado4 = StringVar()

texto_resultado5 = StringVar()

valor_fecha = ""
valor_compra = 0
valor_venta = 0
valor_variacion = ""

'''PANTALLA 3'''
datoIngreso5 = StringVar()
datoIngreso6 =StringVar()


'''EFECTO PARPADEANTE AL ACTUALIZAR LOS VALORES DE LA PÁGINA DE ÁMBITO'''
def color_label():
    global colorGeneral, colorSeleccion, colorComentario, new_colour, letraDatos

    color_actual = Label_venta.cget('foreground')
    fuente_actual = Label_venta.cget('font')

    if color_actual == colorGeneral:
        new_colour = colorSeleccion
        fuente_actual = letraDatos2
    else:
        new_colour = colorGeneral
        fuente_actual = letraDatos
    
    Label_venta.configure(foreground=new_colour, font=fuente_actual)
    # print(color_actual)
    # print(fuente_actual)


def extraccionDatosDolarOficial(url,usuario):
    global valor_venta, valor_compra, valor_fecha, valor_variacion

    '''EXTRACCIÓN DE LA INFORMACIÓN DE LA PÁGINA WEB'''
    response = requests.get(url, headers=usuario)
    valor = response.json()
    # print(response.json())
    # print(response.status_code)

    '''CREAMOS LAS VARIABLES QUE GUARDAN LOS VALORES DESEADOS'''
    # VALORES PARA CALCULOS
    valor_fecha = valor['fecha']
    valor_compra = float(str(valor['compra']).replace('.','').replace(',','.'))
    valor_venta = float(str(valor['venta']).replace('.','').replace(',','.'))
    valor_variacion = valor['variacion']
    
    # TEXTOS QUE REALMENTE SE MUESTRAN EN LA PANTALLA
    texto_fecha.set(str(valor_fecha))

    texto_compra.set(("{:_.2f}".format(valor_compra)).replace(".",",").replace("_", "."))
    texto_venta.set(("{:_.2f}".format(valor_venta)).replace(".",",").replace("_", "."))
 
    texto_variacion.set(str(valor_variacion))


    for i in range (0,4):
        Label_venta.after(flash_delay + i*flash_delay,color_label)
        


'''VERIFICAMOS SI LOS VALORES COICIDEN CON EL .json de la PÁGINA WEB'''
# print(f'Valor de compra: '+str(valor_compra))
# print(f'Valor de venta: '+str(valor_venta))
# print(f'% de variación: '+valor_variacion)
# print(f'Última actualización: '+valor_fecha)

'''VERIFICAMOS SI EL TIPO DE DATOS OBTENIDO SE PUEDE TRATAR COMO NÚMERO'''
# monto_en_pesos = input("Ingrese el valor en USD:")
# valor_en_usd = valor_venta * float(monto_en_pesos)
# print(f'Debes cobrar: '+str(valor_en_usd)+f' $')


def extraccionDatosDolarHistorico(url,usuario):
    global table

# url_oficial_historico = "https://mercados.ambito.com//dolar/oficial/historico-general/"
# 2024-10-09/2024-11-09

    url_requerido = url + datoIngreso5.get() + "/" + datoIngreso6.get()


    '''EXTRACCIÓN DE LA INFORMACIÓN DE LA PÁGINA WEB'''
    response = requests.get(url_requerido, headers=usuario)
    valor = response.json()
    # print(response.json())
    # print(response.status_code)
    datos = np.array(valor, dtype=object)
    df = pd.DataFrame(data=datos[1:,1:], columns=datos[0,1:], index=datos[1:,0])
    table.delete("1.0", "end")
    table.insert(tk.INSERT, df.to_string())
    
    # print(df.to_string())

    return df


def calcularPesosARS(precioVenta,montoEnUSD):
    global valor_venta, valor_compra, valor_fecha, valor_variacion

    if montoEnUSD == "":
        texto_resultado1.set("")

    else:
        resultado = precioVenta * float(montoEnUSD)
        texto_resultado1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
    

def limpiarCalculos():
    datoIngreso1.set("")
    texto_resultado1.set("")

def limpiarCalculos2():
    global resultado

    datoIngreso2.set("")
    datoIngreso3.set("")
    datoIngreso4.set("")

    texto_resultado2.set("")
    texto_resultado3.set("")
    texto_resultado4.set("")
    comentario.set("")

    resultado = 0

def limpiarCalculos3():
    datoIngreso5.set("")
    datoIngreso6.set("")
    table.delete("1.0", "end")
    

def validation0(digito):
    lista = ["+","-","*","/"]
    
    return not digito in lista


def validation(digito):
    lista = ["+","-","*","/"]
    for n in range(0, 10):
        lista.append(str(n))

    return not digito in lista
    

'''FUNCIÓN PARA MOSTRAR CALENDARIO'''
def mostrar_calendario(entry_widget):
    """Función para mostrar un calendario y seleccionar una fecha"""
    
    # Crear ventana del calendario
    calendario_window = tk.Toplevel(raiz)
    calendario_window.title("Seleccionar Fecha")
    calendario_window.geometry("300x300")
    calendario_window.resizable(0, 0)
    calendario_window.config(bg=colorRaiz)
    
    # Centrar la ventana en la pantalla principal
    calendario_window.transient(raiz)
    calendario_window.grab_set()
    
    # Obtener posición de la ventana principal
    raiz.update_idletasks()
    x_main = raiz.winfo_x()
    y_main = raiz.winfo_y()
    width_main = raiz.winfo_width()
    height_main = raiz.winfo_height()
    
    # Calcular posición centrada
    x_centered = x_main + (width_main // 2) - 150  # 150 es la mitad del ancho del calendario
    y_centered = y_main + (height_main // 2) - 150  # 150 es la mitad del alto del calendario
    
    # Posicionar el calendario en el centro de la ventana principal
    calendario_window.geometry(f"300x300+{x_centered}+{y_centered}")
    
    # Obtener fecha actual
    fecha_actual = datetime.now()
    año_actual = fecha_actual.year
    mes_actual = fecha_actual.month
    
    # Variables para el calendario
    año_var = tk.StringVar(value=año_actual)
    mes_var = tk.StringVar(value=mes_actual)
    dia_var = tk.StringVar()
    
    # Frame para controles
    frame_controles = tk.Frame(calendario_window, bg=colorRaiz)
    frame_controles.pack(pady=10)
    
    # Botones para navegar año
    tk.Button(frame_controles, text="◀◀", font=('Arial', 10, 'bold'),
              command=lambda: año_var.set(int(año_var.get()) - 1),
              bg=colorDbgBoton, fg=fuenteBotones, width=3).pack(side=tk.LEFT, padx=2)
    
    tk.Label(frame_controles, textvariable=año_var, font=('Arial', 12, 'bold'),
             bg=colorRaiz, fg=colorGeneral).pack(side=tk.LEFT, padx=10)
    
    tk.Button(frame_controles, text="▶▶", font=('Arial', 10, 'bold'),
              command=lambda: año_var.set(int(año_var.get()) + 1),
              bg=colorDbgBoton, fg=fuenteBotones, width=3).pack(side=tk.LEFT, padx=2)
    
    # Frame para mes
    frame_mes = tk.Frame(calendario_window, bg=colorRaiz)
    frame_mes.pack(pady=5)
    
    tk.Button(frame_mes, text="◀", font=('Arial', 10, 'bold'),
              command=lambda: cambiar_mes(-1),
              bg=colorDbgBoton, fg=fuenteBotones, width=3).pack(side=tk.LEFT, padx=2)
    
    tk.Label(frame_mes, textvariable=mes_var, font=('Arial', 12, 'bold'),
             bg=colorRaiz, fg=colorGeneral).pack(side=tk.LEFT, padx=10)
    
    tk.Button(frame_mes, text="▶", font=('Arial', 10, 'bold'),
              command=lambda: cambiar_mes(1),
              bg=colorDbgBoton, fg=fuenteBotones, width=3).pack(side=tk.LEFT, padx=2)
    
    def cambiar_mes(direccion):
        mes_actual = int(mes_var.get())
        año_actual = int(año_var.get())
        
        mes_actual += direccion
        if mes_actual > 12:
            mes_actual = 1
            año_actual += 1
            año_var.set(año_actual)
        elif mes_actual < 1:
            mes_actual = 12
            año_actual -= 1
            año_var.set(año_actual)
        
        mes_var.set(mes_actual)
        actualizar_calendario()
    
    # Frame para el calendario
    frame_calendario = tk.Frame(calendario_window, bg=colorRaiz)
    frame_calendario.pack(pady=10)
    
    # Labels para días de la semana
    dias_semana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    for i, dia in enumerate(dias_semana):
        tk.Label(frame_calendario, text=dia, font=('Arial', 9, 'bold'),
                 bg=colorRaiz, fg=colorGeneral, width=4).grid(row=0, column=i, padx=1, pady=1)
    
    def actualizar_calendario():
        # Limpiar botones existentes
        for widget in frame_calendario.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        
        # Recrear labels de días de la semana
        for i, dia in enumerate(dias_semana):
            tk.Label(frame_calendario, text=dia, font=('Arial', 9, 'bold'),
                     bg=colorRaiz, fg=colorGeneral, width=4).grid(row=0, column=i, padx=1, pady=1)
        
        año = int(año_var.get())
        mes = int(mes_var.get())
        
        # Obtener primer día del mes y número de días
        primer_dia = datetime(año, mes, 1).weekday()
        num_dias = (datetime(año, mes + 1, 1) - datetime(año, mes, 1)).days
        
        # Ajustar primer día (lunes = 0)
        primer_dia = (primer_dia + 1) % 7
        
        fila = 1
        columna = 0
        
        # Espacios vacíos para el primer día
        for _ in range(primer_dia):
            tk.Label(frame_calendario, text="", width=4).grid(row=fila, column=columna, padx=1, pady=1)
            columna += 1
        
        # Botones para cada día del mes
        for dia in range(1, num_dias + 1):
            if columna >= 7:
                columna = 0
                fila += 1
            
            def seleccionar_dia(d=dia):
                fecha_seleccionada = f"{año:04d}-{mes:02d}-{d:02d}"
                entry_widget.delete(0, tk.END)
                entry_widget.insert(0, fecha_seleccionada)
                calendario_window.destroy()
            
            tk.Button(frame_calendario, text=str(dia), font=('Arial', 9),
                     command=seleccionar_dia, bg='white', fg='black',
                     width=4, height=1).grid(row=fila, column=columna, padx=1, pady=1)
            columna += 1
    
    # Actualizar calendario inicial
    actualizar_calendario()
    
    # Botones de acción
    frame_botones = tk.Frame(calendario_window, bg=colorRaiz)
    frame_botones.pack(pady=5)
    
    tk.Button(frame_botones, text="Cancelar", font=('Arial', 10),
              command=calendario_window.destroy,
              bg=colorDbgBoton, fg=fuenteBotones, width=10, height=2).pack(side=tk.LEFT, padx=5)
    
    tk.Button(frame_botones, text="Hoy", font=('Arial', 10),
              command=lambda: [entry_widget.delete(0, tk.END), 
                              entry_widget.insert(0, datetime.now().strftime("%Y-%m-%d")),
                              calendario_window.destroy()],
              bg=colorDbgBoton, fg=fuenteBotones, width=10, height=2).pack(side=tk.LEFT, padx=5)


############################################################

#UBICACIÓN DE CADA BOTÓN:

#ORDEN DE FILAS
fila1=1
fila2=2
fila3=3
fila4=4
fila5=5
fila6=6
fila7=7
# fila8=8
# fila9=9
# fila10=10

# DIMENSION DE LOS BOTONES
ancho1=1
alto1=1

ancho2=20
alto2=2

'''VENTANA TIPO DE CAMBIO'''
#********* BOTÓN = FILA 1 ***************************************
# Label(tipoCambio,text="DOLAR BANCO NACIÓN", fg=fuenteTitulo,font=letraTitulo, relief=bordeTitulo,borderwidth=b1).grid(column=0,row=fila1,sticky=u1, padx=x1,pady=y1, columnspan=4)
# .grid(column=0,row=fila1,sticky=u1, padx=x1,pady=y1, columnspan=4)
lista_dolar.grid(row=fila1, column=0, padx=x1, pady=y1, sticky="nsew", columnspan=4)
lista_dolar.configure(justify='center')


#********* PANTALLA = FILA 2 ***************************************
botonActualizar=Button(tipoCambio, text="ACTUALIZAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:extraccionDatosDolarOficial(url_dolar,headers))
botonActualizar.grid( column=0, row=fila2, columnspan=4,sticky=u1,padx=x2,pady=y2)

#********* TEXTOS = FILA 3 ***************************************
Label(tipoCambio,text="COMPRA", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,text="VENTA", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=1,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,text="VARIACIÓN", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=2,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,text="FECHA (Últ. Act.)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=3,row=fila3,sticky=u1,padx=x1,pady=y1)


#********* FILA 4 *************************************************
# background = flash_colours[0]
Label(tipoCambio,textvariable=texto_compra, fg=fuenteDatos,font=letraDatos).grid(column=0,row=fila4,sticky=u1,padx=x1,pady=y1)

Label_venta=Label(tipoCambio,textvariable=texto_venta, foreground=new_colour,font=letraDatos)
Label_venta.grid(column=1,row=fila4,sticky=u1,padx=x1,pady=y1)

Label(tipoCambio,textvariable=texto_variacion, fg=fuenteDatos,font=letraDatos).grid(column=2,row=fila4,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,textvariable=texto_fecha, fg=fuenteDatos,font=letraDatos).grid(column=3,row=fila4,sticky=u1,padx=x1,pady=y1)


#********* FILA 5 *************************************************
Label(tipoCambio,text="Ingrese el valor (en USD)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila5,sticky=u1, columnspan=2,padx=x3,pady=y3)
Label(tipoCambio,text="Resultado (en $ ARS)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=2,row=fila5,sticky=u1, columnspan=2,padx=x3,pady=y3)

#********* FILA 6 *************************************************
pantalla1=Entry(tipoCambio, textvariable=datoIngreso1, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso, validate="all", validatecommand=(verificacionValores.register(validation0), "%S"))
pantalla1.grid(column=0, row=fila6, sticky=u1, columnspan=2, padx=x2,pady=y2)

pantalla2 =Entry(tipoCambio,textvariable=texto_resultado1,state="readonly", justify="center", fg=fuenteResultados,font=letraResultados, relief=bordeSubtitulo,borderwidth=b1)
pantalla2.grid(column=2, row=fila6, sticky=u1, columnspan=2, padx=x2,pady=y2)


#********* FILA 7 *************************************************
botonCalcular=Button(tipoCambio, text="CALCULAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho2, height=alto1, command=lambda:calcularPesosARS(valor_venta,datoIngreso1.get()))
botonCalcular.grid(row=fila7, column=0, columnspan=2,padx=x2,pady=y2) #,sticky=u1

botonLimpiar=Button(tipoCambio, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho2, height=alto1, command=lambda:limpiarCalculos())
botonLimpiar.grid(row=fila7, column=2, columnspan=2,padx=x2,pady=y2) #,sticky=u1


'''VENTANA VERIFICACIÓN'''
#********* BOTÓN = FILA 1 ***************************************
Label(verificacionValores,text="VERIFICACIÓN", fg=fuenteTitulo,font=letraTitulo, relief=bordeTitulo,borderwidth=b1).grid(column=0,row=fila1,sticky=u1, padx=x1,pady=y1, columnspan=2)


#********* PANTALLA = FILA 2 ***************************************
Label(verificacionValores,text="", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1, height = 0).grid(column=0, row=fila2, sticky=u1,padx=x2,pady=y2, columnspan=2)

#********* TEXTOS = FILA 3 ***************************************
Label(verificacionValores,text="TC ($ / USD)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1, width=25).grid(column=0,row=fila3,sticky=u1,padx=x1,pady=y1)
pantalla3=Entry(verificacionValores, textvariable=datoIngreso2, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso, width=23, validate="all", validatecommand=(verificacionValores.register(validation0), "%S"))
pantalla3.grid(column=1,row=fila3,sticky=u1,padx=x1,pady=y1)


#********* FILA 4 *************************************************
Label(verificacionValores,text="PESOS ($)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila4,sticky=u1,padx=x1,pady=y1)
pantalla4=Entry(verificacionValores, textvariable=datoIngreso3, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso, validate="all", validatecommand=(verificacionValores.register(validation), "%S"))
pantalla4.grid(column=1,row=fila4,sticky=u1,padx=x1,pady=y1)

#********* FILA 5 *************************************************
Label(verificacionValores,text="DOLARES (USD)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila5,sticky=u1,padx=x1,pady=y1)
pantalla5=Entry(verificacionValores, textvariable=datoIngreso4, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso, validate="all", validatecommand=(verificacionValores.register(validation), "%S"))
pantalla5.grid(column=1,row=fila5,sticky=u1,padx=x1,pady=y1)


#********* FILA 6 *************************************************
botonCalcular1=Button(verificacionValores, text="CALCULAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho2, height=alto1, command=lambda:funcionCalcular(comentario,F1,F2,F3,F4,datoIngreso2,datoIngreso3,datoIngreso4))
botonCalcular1.grid(row=fila7, column=0,padx=x2,pady=y2) #sticky=u1

botonLimpiar2=Button(verificacionValores, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho2, height=alto1, command=lambda:limpiarCalculos2())
botonLimpiar2.grid(row=fila7, column=1,padx=x2) #sticky=u1


#********* FILA 7 *************************************************
Label(verificacionValores,textvariable=comentario, fg=colorComentario,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1, height = 1).grid(column=0, row=fila6, sticky=u1, columnspan=2, padx=x2,pady=y2)


# def on_entry_click(event):
#     """function that gets called whenever entry is clicked"""
#     if entryFechaInicial.get() == 'aaaa-mm-dd':
#        entryFechaInicial.delete(0, "end") # delete all the text in the entry
#        entryFechaInicial.insert(0, '') #Insert blank for user input



'''VENTANA DOLAR HISTÓRICO'''
#********* BOTÓN = FILA 1 ***************************************
# Label(dolarHistorico,text="DOLAR HISTÓRICO", fg=fuenteTitulo,font=letraTitulo, relief=bordeTitulo,borderwidth=b1).place(x=15, y=0,width=437, height=28)


# lista_dolar_historico.grid(row=fila1, column=0, padx=x1, pady=y1, sticky="nsew", columnspan=4)
lista_dolar_historico.place(x=15, y=0,width=437, height=20)
# lista_dolar.grid(row=fila1, column=0, padx=x1, pady=y1, sticky="nsew", columnspan=4)
lista_dolar_historico.configure(justify='center')

#********* PANTALLA = FILA 2 ***************************************
'''MOSTRAR UN VALOR GRIS TEMPORAL POR DEFECTO EN EL ENTRY
https://stackoverflow.com/questions/30491721/how-to-insert-a-temporary-text-in-a-tkinter-entry-widget/39677021#39677021'''
entryFechaInicial = Entry(dolarHistorico, textvariable=datoIngreso5, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
# entryFechaInicial.insert(END, '2024-10-19')
entryFechaInicial.insert(0, 'AAAA-MM-DD')
entryFechaInicial.bind("<FocusIn>", lambda event: entryFechaInicial.delete(0,"end") if datoIngreso5.get() == "AAAA-MM-DD" else None)
entryFechaInicial.bind("<FocusOut>", lambda event: entryFechaInicial.insert(0, "AAAA-MM-DD") if datoIngreso5.get() == "" else None)
entryFechaInicial.bind("<Button-1>", lambda event: mostrar_calendario(entryFechaInicial))
entryFechaInicial.place(x=100, y=33,width=100, height=28)
# entryFechaInicial.configure(show="aaaa-mm-dd")

entryFechaFinal = Entry(dolarHistorico, textvariable=datoIngreso6, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
entryFechaFinal.insert(0, 'AAAA-MM-DD')
entryFechaFinal.bind("<FocusIn>", lambda event: entryFechaFinal.delete(0,"end") if datoIngreso6.get() == "AAAA-MM-DD" else None)
entryFechaFinal.bind("<FocusOut>", lambda event: entryFechaFinal.insert(0, "AAAA-MM-DD") if datoIngreso6.get() == "" else None)
entryFechaFinal.bind("<Button-1>", lambda event: mostrar_calendario(entryFechaFinal))
entryFechaFinal.place(x=230, y=33,width=100, height=28)

botonActualizar=Button(dolarHistorico, text="ACTUALIZAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:extraccionDatosDolarHistorico(url_dolar_historico,headers))
# botonActualizar.grid( column=0, row=fila2, columnspan=4,sticky=u1,padx=x2,pady=y2)
botonActualizar.place(x=360, y=33,width=100, height=28)

botonLimpiar3=Button(dolarHistorico, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:limpiarCalculos3())
# botonActualizar.grid( column=0, row=fila2, columnspan=4,sticky=u1,padx=x2,pady=y2)
botonLimpiar3.place(x=360, y=80,width=100, height=28)

#********* FILA 3*************************************************

Label(dolarHistorico,text="Fecha", fg=fuenteTitulo,font=letraTitulo).place(x=100, y=75,width=50, height=20)
Label(dolarHistorico,text="Compra", fg=fuenteTitulo,font=letraTitulo).place(x=200, y=75,width=50, height=20)
Label(dolarHistorico,text="Venta", fg=fuenteTitulo,font=letraTitulo).place(x=280, y=75,width=50, height=20)


table = tk.Text(dolarHistorico)
table.config(width=50, height=30)
table.place(x=100, y=105,width=230, height=100)

scrollbar = ttk.Scrollbar(dolarHistorico,orient=tk.VERTICAL, command=table.yview)
table.config(yscrollcommand=scrollbar.set)
scrollbar.place(x=340, y=105, height=100)



'''CÓDIGO PARA INGRESAR DATOS POR TECLADO:'''
#widget.bind(evento, callback)

# Numeros
for n in range(0, 10):
    pantalla4.bind(str(n), lambda event: presionarBoton(event.char,datoIngreso3, pantalla4, END))
    pantalla5.bind(str(n), lambda event: presionarBoton(event.char,datoIngreso4, pantalla5, END))
    # verificacionValores.bind_all(str(n),lambda e: focus(e))

'''Punto decimal'''
# pantalla4.bind(".", lambda event: presionarBoton(event.char))
# pantalla4.bind("<KP_Decimal>", lambda event: presionarBoton(event.char))

'''Operadores'''
# raiz.bind("*", lambda _: multiplica())
# raiz.bind("<KP_Multiply>", lambda _:  multiplica())

# raiz.bind("/", lambda _: divide())
# raiz.bind("<KP_Divide>", lambda _: divide())

# pantalla4.bind("+", lambda _: suma())
# pantalla4.bind("<KP_Add>", lambda _: suma())

# pantalla4.bind("-", lambda _: resta())
# pantalla4.bind("<KP_Subtract>", lambda _: resta())

pantalla4.bind("+", lambda _: suma(datoIngreso3, pantalla4, END))
pantalla4.bind("-", lambda _: resta(datoIngreso3, pantalla4, END))
# pantalla5.bind("+", lambda _: suma(datoIngreso4, pantalla5, END))
# pantalla5.bind("-", lambda _: resta(datoIngreso4, pantalla5, END))


'''Clear (SUPR)'''
# raiz.bind("<Delete>", lambda _: borrar_todo())

# Delete (BackSpace)
pantalla4.bind("<BackSpace>", lambda _: borrar_ultimo(datoIngreso3, pantalla4, END))
pantalla5.bind("<BackSpace>", lambda _: borrar_ultimo(datoIngreso4, pantalla5, END))


'''= (Return/Intro)'''
# pantalla4.bind("<KP_Enter>", lambda _: subTotal())

pantalla4.bind("<Return>", lambda _: subTotal(datoIngreso3, pantalla4, END))
# pantalla5.bind("<Return>", lambda _: subTotal(datoIngreso4, pantalla5, END))



raiz.mainloop()



