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
from funciones_TC  import *


'''IMPORTACIÓN DE FUNCIONES PROPIAS'''
from operaciones_math import *


'''INCIAMOS LA INTERFAZ DE USUARIO'''
#CREACIÓN DE VENTANAS:
raiz=Tk()
raiz.title("Tipo de Cambio del Dolar Oficial en Argentina")

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


# VARIABLES GLOBALES
comentario=StringVar()

# resultado=0
# operacion=""
# reset_pantalla=False
# d=0

#VARIABLE PARA EFECTO PARPADEO:

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
    messagebox.showinfo("Info. Versión","Versión 1.1 \n \nMes/Año: 10/2024")


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
# url_nacion = "https://mercados.ambito.com//dolarnacion//variacion"
# url_informal = "https://mercados.ambito.com//dolar/informal/variacion"
# https://mercados.ambito.com//euro//variacion
# https://mercados.ambito.com//dolarturista/variacion
# https://mercados.ambito.com//dolarcripto/variacion
# https://mercados.ambito.com//dolarrava/cl/variacion
# https://mercados.ambito.com//dolarrava/mep/variacion
# https://mercados.ambito.com//euro/informal/variacion
# https://mercados.ambito.com//dolar/mayorista/variacion
# https://mercados.ambito.com//dolarfuturo/variacion

'''URL DE LAS COTIZACIONES HISTORICAS DE DOLAR OFICIAL EN ARGENTINA (ÚLTIMO MES)'''
url_oficial_historico = "https://mercados.ambito.com//dolar/oficial/historico-general/2024-10-09/2024-11-09"

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


def extraccionDatosDolarOficialHistorico(url,usuario):
    global table

    '''EXTRACCIÓN DE LA INFORMACIÓN DE LA PÁGINA WEB'''
    response = requests.get(url, headers=usuario)
    valor = response.json()
    # print(response.json())
    # print(response.status_code)
    datos = np.array(valor, dtype=object)
    df = pd.DataFrame(data=datos[1:,1:], columns=datos[0,1:], index=datos[1:,0])
    table.delete("1.0", "end")
    table.insert(tk.INSERT, df.to_string())
    
    print(df.to_string())

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


def validation0(digito):
    lista = ["+","-","*","/"]
    
    return not digito in lista


def validation(digito):
    lista = ["+","-","*","/"]
    for n in range(0, 10):
        lista.append(str(n))

    return not digito in lista
    


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
Label(tipoCambio,text="DOLAR OFICIAL", fg=fuenteTitulo,font=letraTitulo, relief=bordeTitulo,borderwidth=b1).grid(column=0,row=fila1,sticky=u1, padx=x1,pady=y1, columnspan=4)


#********* PANTALLA = FILA 2 ***************************************
botonActualizar=Button(tipoCambio, text="ACTUALIZAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:extraccionDatosDolarOficial(url_oficial,headers))
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




'''VENTANA DOLAR HISTÓRICO'''
#********* BOTÓN = FILA 1 ***************************************
Label(dolarHistorico,text="DOLAR HISTÓRICO", fg=fuenteTitulo,font=letraTitulo, relief=bordeTitulo,borderwidth=b1).place(x=15, y=0,width=437, height=28)

#********* PANTALLA = FILA 2 ***************************************
botonActualizar=Button(dolarHistorico, text="ACTUALIZAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:extraccionDatosDolarOficialHistorico(url_oficial_historico,headers))
# botonActualizar.grid( column=0, row=fila2, columnspan=4,sticky=u1,padx=x2,pady=y2)
botonActualizar.place(x=15, y=33,width=437, height=28)

#********* FILA 3*************************************************
response = requests.get(url_oficial_historico, headers=headers)
valor = response.json()
# print(response.json())
# print(response.status_code)
datos = np.array(valor, dtype=object)
df = pd.DataFrame(data=datos[1:,1:], columns=datos[0,1:], index=datos[1:,0])

table = tk.Text(dolarHistorico)
# table.insert(tk.INSERT, df.to_string())
table.config(width=50, height=30)
table.place(x=100, y=75,width=230, height=130)

scrollbar = ttk.Scrollbar(dolarHistorico,orient=tk.VERTICAL, command=table.yview)
table.config(yscrollcommand=scrollbar.set)
scrollbar.place(x=340, y=75, height=130)




'''FUNCIONES PARA SUMAR VARIOS VALORES DENTRO DEL CAMPO [PESOS ($)]
ANTES DE REALIZAR LA CONVERSIÓN A [TC ($ / USD)] O A [DOLARES (USD)]'''


# FUNCIÓN PARA INSERTAR DIGITOS EN LA PANTALLA
# def presionarBoton(digito):

#     global operacion, resultado, reset_pantalla, d

#     if reset_pantalla==True:
#         if datoIngreso3.get()!="INF" or datoIngreso3.get()!="COMPLEJO":
#             resultado= resultado
#             operacion=operacion            
            
#         elif datoIngreso3.get()=="INF" or datoIngreso3.get()=="COMPLEJO":
#             resultado= 0
#             operacion=""

#         datoIngreso3.set(digito)
#         reset_pantalla=False        

#     elif reset_pantalla==False:

#         if d==0:

#             if digito==".":
#                 datoIngreso3.set(datoIngreso3.get() + digito)

#                 d+=1

#             elif digito!=".":
#                 datoIngreso3.set(datoIngreso3.get() + digito)

#         else:
#             if digito==".":
#                 datoIngreso3.set(datoIngreso3.get())

#             elif digito!=".":
#                 datoIngreso3.set(datoIngreso3.get() + digito)
    
#     pantalla4.icursor(END)

      
#     print(resultado)
#     print(operacion)
#     print(reset_pantalla)



# FUNCIÓN SUMAR:
    
# def suma():

#     global operacion, resultado, reset_pantalla, d

#     d=0

#     if reset_pantalla==False and datoIngreso3.get()!="":

#         if operacion=="sumar":
#             resultado=resultado + float(datoIngreso3.get())
        
#         elif operacion=="restar":
#             resultado= resultado - float(datoIngreso3.get())

#         elif operacion=="multiplicar":
#             resultado= resultado * float(datoIngreso3.get())
        
#         elif operacion=="":
#             resultado= float(datoIngreso3.get())

#         elif operacion=="dividir":
#             try:
#                 resultado= resultado / float(datoIngreso3.get())
        
#             except ZeroDivisionError:
#                 resultado="INF"

# #RESULTA:
#         operacion="sumar"
#         reset_pantalla=True
#         datoIngreso3.set(resultado)

#     elif reset_pantalla==False and datoIngreso3.get()=="":
#         resultado=resultado
#         operacion="sumar"
#         reset_pantalla=True
#         datoIngreso3.set(resultado)
        
# #SI NO:
#     elif reset_pantalla==True:
#         if datoIngreso3.get()!="INF" or datoIngreso3.get()!="COMPLEJO":
#             resultado= float(datoIngreso3.get())
#             operacion="sumar"
#             reset_pantalla=True
#             datoIngreso3.set(resultado)

#         elif datoIngreso3.get()=="INF" or datoIngreso3.get()=="COMPLEJO":
#             resultado= 0
#             operacion=""
#             reset_pantalla=False
#             datoIngreso3.set("")

#     pantalla4.icursor(END)

#     print(resultado)
#     print(operacion)
#     print(reset_pantalla)
    
  
# # FUNCIÓN RESTAR:
    
# def resta():

#     global operacion, resultado, reset_pantalla, d

#     d=0

#     if reset_pantalla==False  and datoIngreso3.get()!="":

#         if operacion=="sumar":
#             resultado=resultado + float(datoIngreso3.get())
        
#         elif operacion=="restar":
#             resultado= resultado - float(datoIngreso3.get())

#         elif operacion=="multiplicar":
#             resultado= resultado * float(datoIngreso3.get())
        
#         elif operacion=="":
#             resultado= float(datoIngreso3.get())

#         elif operacion=="dividir":
#             try:
#                 resultado= resultado / float(datoIngreso3.get())
        
#             except ZeroDivisionError:
#                 resultado="INF"

# #RESULTA:
#         operacion="restar"
#         reset_pantalla=True
#         datoIngreso3.set(resultado)

#     elif reset_pantalla==False and datoIngreso3.get()=="":
#         resultado=resultado
#         operacion="restar"
#         reset_pantalla=True
#         datoIngreso3.set(resultado)
            
# #SI NO:
#     elif reset_pantalla==True:
#         if datoIngreso3.get()!="INF" or datoIngreso3.get()!="COMPLEJO":
#             resultado= float(datoIngreso3.get())
#             operacion="restar"
#             reset_pantalla=True
#             datoIngreso3.set(resultado)

#         elif datoIngreso3.get()=="INF" or datoIngreso3.get()=="COMPLEJO":
#             resultado= 0
#             operacion=""
#             reset_pantalla=False
#             datoIngreso3.set("")

#     pantalla4.icursor(END)

#     print(resultado)
#     print(operacion)
#     print(reset_pantalla)



# def subTotal():

#     global operacion, resultado, reset_pantalla, d

#     d=0

#     if reset_pantalla==False and datoIngreso3.get()!="":

#         if operacion=="sumar":
#             resultado= resultado + float(datoIngreso3.get())

#         elif operacion=="restar":
#             resultado= resultado - float(datoIngreso3.get())

#         elif operacion=="multiplicar":
#             resultado= resultado * float(datoIngreso3.get())
           
#         elif operacion=="":
#             resultado= float(datoIngreso3.get())
                  
#         elif operacion=="dividir":
#                 try:
#                     resultado= resultado / float(datoIngreso3.get())
            
#                 except ZeroDivisionError:
#                     resultado= "INF"

# #RESULTA:       
#         reset_pantalla=True
#         datoIngreso3.set(resultado)

#     elif reset_pantalla==False and datoIngreso3.get()=="":
#         resultado=resultado
#         operacion=""
#         reset_pantalla=True
#         datoIngreso3.set(resultado)
        

# #RESULTA (en True con todas las operaciones):

#     elif reset_pantalla==True:
#         if datoIngreso3.get()!="INF" or datoIngreso3.get()!="COMPLEJO":
#             resultado= float(datoIngreso3.get())
#             reset_pantalla=True
#             datoIngreso3.set(resultado)
        
#         elif datoIngreso3.get()=="INF" or datoIngreso3.get()=="COMPLEJO":
#             resultado= 0
#             reset_pantalla=False
#             datoIngreso3.set("")

#     operacion=""

#     pantalla4.icursor(END)

#     print(resultado)
#     print(operacion)
#     print(reset_pantalla)





#BORRAR ULTIMO DIGITO:
    
# def borrar_ultimo():

#     global operacion, resultado, reset_pantalla, d

#     d=0

#     if datoIngreso3.get()!="":
#         datoIngreso3.set(datoIngreso3.get()[:-1])

#     else:
#         datoIngreso3.set("")
    
#     pantalla4.icursor(END)


# widget = 0

# def focus(event):
#     global widget
#     widget = verificacionValores.focus_get() 
#     # print(widget, "has focus")
#     print(widget)

# Here function focus() is binded with Mouse Button-1 
# so every time you click mouse, it will call the 
# focus method, defined above 
# verificacionValores.bind_all("<Button-1>", lambda e: focus(e))
# verificacionValores.bind_all("<Select>", lambda e: focus(e)) 


# def handleReturn(event):
#     test = verificacionValores.focus_get()
#     print(test.get())


# verificacionValores.bind("<Return>",handleReturn)





'''CÓDIGO PARA INGRESAR DATOS POR TECLADO:'''
#widget.bind(evento, callback)

# Numeros
for n in range(0, 10):
    # pantalla4.bind(str(n), lambda event: presionarBoton(event.char))
    pantalla4.bind(str(n), lambda event: presionarBoton(event.char,datoIngreso3, pantalla4, END))
    # pantalla4.bind(f"<KP_{n}>", lambda event: presionarBoton(event.char))
    pantalla5.bind(str(n), lambda event: presionarBoton(event.char,datoIngreso4, pantalla5, END))
    
    # verificacionValores.bind_all(str(n),lambda e: focus(e))

# Punto decimal
# pantalla4.bind(".", lambda event: presionarBoton(event.char))
# pantalla4.bind("<KP_Decimal>", lambda event: presionarBoton(event.char))

# Operadores
# raiz.bind("*", lambda _: multiplica())
# raiz.bind("<KP_Multiply>", lambda _:  multiplica())
# raiz.bind("/", lambda _: divide())
# raiz.bind("<KP_Divide>", lambda _: divide())
pantalla4.bind("+", lambda _: suma(datoIngreso3, pantalla4, END))
# pantalla4.bind("<KP_Add>", lambda _: suma())
pantalla4.bind("-", lambda _: resta(datoIngreso3, pantalla4, END))
# pantalla4.bind("-", lambda _: resta())
# pantalla4.bind("<KP_Subtract>", lambda _: resta())
pantalla5.bind("+", lambda _: suma(datoIngreso4, pantalla5, END))
# pantalla4.bind("<KP_Add>", lambda _: suma())
pantalla5.bind("-", lambda _: resta(datoIngreso4, pantalla5, END))


# Clear (SUPR)
# raiz.bind("<Delete>", lambda _: borrar_todo())


# Delete (BackSpace)
pantalla4.bind("<BackSpace>", lambda _: borrar_ultimo(datoIngreso3, pantalla4, END))
# pantalla4.bind("<BackSpace>", lambda _: borrar_ultimo())
pantalla5.bind("<BackSpace>", lambda _: borrar_ultimo(datoIngreso4, pantalla5, END))


# = (Return/Intro)
pantalla4.bind("<Return>", lambda _: subTotal(datoIngreso3, pantalla4, END))
# pantalla4.bind("<Return>", lambda _: subTotal())
# pantalla4.bind("<KP_Enter>", lambda _: subTotal())
pantalla5.bind("<Return>", lambda _: subTotal(datoIngreso4, pantalla5, END))



raiz.mainloop()



