'''PAGINA PARA CORREGIR EL ERROR DE IMPORTACIÓN DE DATOS DE AMBITO
https://stackoverflow.com/questions/38489386/how-to-fix-403-forbidden-errors-when-calling-apis-using-python-requests'''


'''IMPORTACIÓN DE LIBRERIAS'''
import pandas as pd
import requests
# import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from funciones_TC  import *


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
caracter=StringVar()
comentario=StringVar()

resultado=0
operacion=""
reset_pantalla=False


#CONFIGURACION DEL MENU PRINCIPAL:
barra_menu=Menu(raiz)
# raiz["menu"]=barra_menu
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
    messagebox.showinfo("Info. Versión","Versión 1.0 \n \nMes/Año: 09/2024")




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

#FUENTES:
# fuenteGeneral = 'Tahoma'
fuenteGeneral = 'Comic Sans MS'
'''https://blog.hubspot.es/website/fuentes-html'''
letraTitulo = (fuenteGeneral, 11, 'bold')
letraSubtitulos= (fuenteGeneral, 10, 'bold')
letraBotones= (fuenteGeneral, 8, 'bold')
letraDatos= (fuenteGeneral, 9)
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


'''CREACIÓN DE VENTANA TIPO NOTEBOOK'''
#NOTEBOOK:
notebook1 = ttk.Notebook(miFrame,padding=10)
notebook1.grid(column=0,row=0,sticky='nsew')

tipoCambio = ttk.Frame(notebook1,padding=(1,1)) #PRIMERA PÁGINA
verificacionValores = ttk.Frame(notebook1,padding=(1,1)) #SEGUNDA PÁGINA

notebook1.add(tipoCambio, text='TC')
notebook1.add(verificacionValores, text='Verificación')



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

'''PERMISOS DE LA PÁGINA WEB AMBITO'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}


texto_fecha = StringVar()
texto_compra = StringVar()
texto_venta = StringVar()
texto_variacion = StringVar()

texto_resultado1 = StringVar()

texto_resultado2 = StringVar()
texto_resultado3 = StringVar()
texto_resultado4 = StringVar()

valor_fecha = ""
valor_compra = 0
valor_venta = 0
valor_variacion = ""


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
    
    # TEXTOS
    texto_fecha.set(str(valor_fecha))
    texto_compra.set(str(valor_compra))
    texto_venta.set(str(valor_venta))
    texto_variacion.set(str(valor_variacion))


    # return valor, valor_fecha, valor_compra, valor_venta, valor_variacion
    # return texto_fecha, texto_compra, texto_venta, texto_variacion

'''VERIFICAMOS SI LOS VALORES COICIDEN CON EL .json de la PÁGINA WEB'''
# print(f'Valor de compra: '+str(valor_compra))
# print(f'Valor de venta: '+str(valor_venta))
# print(f'% de variación: '+valor_variacion)
# print(f'Última actualización: '+valor_fecha)

'''VERIFICAMOS SI EL TIPO DE DATOS OBTENIDO SE PUEDE TRATAR COMO NÚMERO'''
# monto_en_pesos = input("Ingrese el valor en USD:")
# valor_en_usd = valor_venta * float(monto_en_pesos)
# print(f'Debes cobrar: '+str(valor_en_usd)+f' $')

'''PANTALLA 1'''
datoIngreso1 = StringVar()

'''PANTALLA 2'''
datoIngreso2 = StringVar()
datoIngreso3 = StringVar()
datoIngreso4 = StringVar()


def calcularPesosARS(precioVenta,montoEnUSD):
    global valor_venta, valor_compra, valor_fecha, valor_variacion

    if montoEnUSD == "":
        texto_resultado1.set("")

    else:
        montoEnUSD.replace('.',',').replace('','.')
        resultado = precioVenta * float(montoEnUSD)
        texto_resultado1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
    

def limpiarCalculos():
    datoIngreso1.set("")
    texto_resultado1.set("")

def limpiarCalculos2():
    datoIngreso2.set("")
    datoIngreso3.set("")
    datoIngreso4.set("")

    texto_resultado2.set("")
    texto_resultado3.set("")
    texto_resultado4.set("")
    comentario.set("")


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
Label(tipoCambio,textvariable=texto_compra, fg=fuenteDatos,font=letraDatos).grid(column=0,row=fila4,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,textvariable=texto_venta, fg=fuenteDatos,font=letraDatos).grid(column=1,row=fila4,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,textvariable=texto_variacion, fg=fuenteDatos,font=letraDatos).grid(column=2,row=fila4,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,textvariable=texto_fecha, fg=fuenteDatos,font=letraDatos).grid(column=3,row=fila4,sticky=u1,padx=x1,pady=y1)


#********* FILA 5 *************************************************
Label(tipoCambio,text="Ingrese el valor (en USD)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila5,sticky=u1, columnspan=2,padx=x3,pady=y3)
Label(tipoCambio,text="Resultado (en $ ARS)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=2,row=fila5,sticky=u1, columnspan=2,padx=x3,pady=y3)

#********* FILA 6 *************************************************
pantalla1=Entry(tipoCambio, textvariable=datoIngreso1, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
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
pantalla3=Entry(verificacionValores, textvariable=datoIngreso2, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso, width=23)
pantalla3.grid(column=1,row=fila3,sticky=u1,padx=x1,pady=y1)


#********* FILA 4 *************************************************
Label(verificacionValores,text="PESOS ($)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila4,sticky=u1,padx=x1,pady=y1)
pantalla4=Entry(verificacionValores, textvariable=datoIngreso3, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
pantalla4.grid(column=1,row=fila4,sticky=u1,padx=x1,pady=y1)

#********* FILA 5 *************************************************
Label(verificacionValores,text="DOLARES (USD)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila5,sticky=u1,padx=x1,pady=y1)
pantalla5=Entry(verificacionValores, textvariable=datoIngreso4, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
pantalla5.grid(column=1,row=fila5,sticky=u1,padx=x1,pady=y1)


#********* FILA 6 *************************************************
botonCalcular1=Button(verificacionValores, text="CALCULAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho2, height=alto1, command=lambda:funcionCalcular(comentario,F1,F2,F3,F4,datoIngreso2,datoIngreso3,datoIngreso4))
botonCalcular1.grid(row=fila7, column=0,padx=x2,pady=y2) #sticky=u1

botonLimpiar2=Button(verificacionValores, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho2, height=alto1, command=lambda:limpiarCalculos2())
botonLimpiar2.grid(row=fila7, column=1,padx=x2) #sticky=u1


#********* FILA 7 *************************************************
Label(verificacionValores,textvariable=comentario, fg=colorComentario,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1, height = 1).grid(column=0, row=fila6, sticky=u1, columnspan=2, padx=x2,pady=y2)



raiz.mainloop()