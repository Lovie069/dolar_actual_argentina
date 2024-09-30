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


'''INCIAMOS LA INTERFAZ DE USUARIO'''
#CREACIÓN DE VENTANAS:
raiz=Tk()
raiz.title("Tipo de Cambio del Dolar Oficial en Argentina")

#CONFIGURACION DE LA VENTANA RAIZ:
ancho_ventana = 500
alto_ventana = 280

x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

# raiz.geometry("700x750"+100,100)

colorRaiz = '#E0BFE0'
raiz.config(bg=colorRaiz,padx=15,pady=15)
raiz.resizable(0,0)

miFrame=Frame(raiz) #width=200, height=300
miFrame.pack()

# VARIABLES GLOBALES
caracter=StringVar()

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

texto_resultado = StringVar()

valor_fecha = ""
valor_compra = 0
valor_venta = 0
valor_variacion = ""

    # if listadoUnidades.get()=="mm" and listadoUnidades1.get()=="cc (ml)":
    #     resultado0 = float(digito9.get())*(10**3)
    #     volumen.set(resultado0)
    #     unidadesFinalesVolumen.set("mm^3")

    # elif listadoUnidades.get()=="mm" and listadoUnidades1.get()=="m^3":
    #     resultado0 = float(digito9.get())*(10**9)
    #     volumen.set(resultado0)
    #     unidadesFinalesVolumen.set("mm^3")

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


datoIngreso1 = StringVar()
# valorSalida1 = StringVar()


def calcularPesosARS(precioVenta,montoEnUSD):
    global valor_venta, valor_compra, valor_fecha, valor_variacion

    if montoEnUSD == "":
        texto_resultado.set("")

    else:
        montoEnUSD.replace('.',',').replace('','.')
        resultado = precioVenta * float(montoEnUSD)
        texto_resultado.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
    
    

def limpiarCalculos():
    datoIngreso1.set("")
    texto_resultado.set("")





'''GENERAMOS CARACTERISTICAS DE LA INTERFAZ QUE SE USARAN EN MULTIPLES PARTES'''
# DIMENSIONES

#PADDING:
x1=15 #Padx
y1=1 #Pady

x2=15 #Padx
y2=10 #Pady

x3=15 #Padx
y3= (15,1) #Pady

#ANCHO DE GIDGETS EN VENTANA DE ÁREAS:
h1=80 #Alto de botones
h2=1 #Alto filas frame áreas y volúmenes
w1=100 #Ancho botones
w2=400 #Ancho pantalla de cálculo
w3=100 #Ancho imágenes
w4=15 #Ancho label datos

#ALTO DE SEPARACIÓN ENTRE GIDGETS
factor1=20
factor2=62

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
letraBotones= (fuenteGeneral, 9, 'bold')
letraDatos= (fuenteGeneral, 10)
letraIngresos= (fuenteGeneral, 10)
letraResultados= (fuenteGeneral, 10)

# FONDOS
fondoIngresos = "white"











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

ancho2=6
alto2=2


#********* BOTÓN = FILA 1 ***************************************
# botonActualizar=Button(miFrame, text="ACTUALIZAR", width=ancho, height=alto)
Label(miFrame,text="DOLAR OFICIAL", fg=fuenteTitulo,font=letraTitulo, relief=bordeTitulo,borderwidth=b1).grid(column=0,row=fila1,sticky=u1, padx=x1,pady=y1, columnspan=4)


#********* PANTALLA = FILA 2 ***************************************
botonActualizar=Button(miFrame, text="ACTUALIZAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:extraccionDatosDolarOficial(url_oficial,headers))
botonActualizar.grid(row=fila2, column=0, columnspan=4,sticky=u1,padx=x2,pady=y2)

#********* TEXTOS = FILA 3 ***************************************
Label(miFrame,text="COMPRA", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(miFrame,text="VENTA", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=1,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(miFrame,text="VARIACIÓN", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=2,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(miFrame,text="FECHA (Últ. Act.)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=3,row=fila3,sticky=u1,padx=x1,pady=y1)


#********* FILA 4 *************************************************
Label(miFrame,textvariable=texto_compra, fg=fuenteDatos,font=letraDatos).grid(column=0,row=fila4,sticky=u1,padx=x1,pady=y1)
Label(miFrame,textvariable=texto_venta, fg=fuenteDatos,font=letraDatos).grid(column=1,row=fila4,sticky=u1,padx=x1,pady=y1)
Label(miFrame,textvariable=texto_variacion, fg=fuenteDatos,font=letraDatos).grid(column=2,row=fila4,sticky=u1,padx=x1,pady=y1)
Label(miFrame,textvariable=texto_fecha, fg=fuenteDatos,font=letraDatos).grid(column=3,row=fila4,sticky=u1,padx=x1,pady=y1)


#********* FILA 5 *************************************************
Label(miFrame,text="Ingrese el valor (en USD)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila5,sticky=u1, columnspan=2,padx=x3,pady=y3)
Label(miFrame,text="Resultado (en $ ARS)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=2,row=fila5,sticky=u1, columnspan=2,padx=x3,pady=y3)

#********* FILA 6 *************************************************
pantalla1=Entry(miFrame, textvariable=datoIngreso1, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
pantalla1.grid(column=0, row=fila6, sticky=u1, columnspan=2, padx=x2,pady=y2)

pantalla2 =Entry(miFrame,textvariable=texto_resultado,state="readonly", justify="center", fg=fuenteResultados,font=letraResultados, relief=bordeSubtitulo,borderwidth=b1)
pantalla2.grid(column=2, row=fila6, sticky=u1, columnspan=2, padx=x2,pady=y2)


#********* FILA 7 *************************************************
# botonCalcular=Button(miFrame, text="Calcular", width=ancho, height=alto)
# botonLimpiar=Button(miFrame, text="Limpiar", width=ancho, height=alto)

botonCalcular=Button(miFrame, text="CALCULAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:calcularPesosARS(valor_venta,datoIngreso1.get()))
botonCalcular.grid(row=fila7, column=0, columnspan=2,sticky=u1,padx=x2,pady=y2)

botonLimpiar=Button(miFrame, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, activeforeground=colorAfBoton, width=ancho1, height=alto1, command=lambda:limpiarCalculos())
botonLimpiar.grid(row=fila7, column=2, columnspan=2,sticky=u1,padx=x2,pady=y2)








#CÓDIGO PARA INGRESAR DATOS POR TECLADO:
#widget.bind(evento, callback)

# # Numeros
# for n in range(0, 10):
#     raiz.bind(str(n), lambda event: presionarBoton(event.char))
#     raiz.bind(f"<KP_{n}>", lambda event: presionarBoton(event.char))

# # Punto decimal
# raiz.bind(".", lambda event: presionarBoton(event.char))
# raiz.bind("<KP_Decimal>", lambda event: presionarBoton(event.char))

# # Operadores
# raiz.bind("*", lambda _: multiplica())
# raiz.bind("<KP_Multiply>", lambda _:  multiplica())
# raiz.bind("/", lambda _: divide())
# raiz.bind("<KP_Divide>", lambda _: divide())
# raiz.bind("+", lambda _: suma())
# raiz.bind("<KP_Add>", lambda _: suma())
# raiz.bind("-", lambda _: resta())
# raiz.bind("<KP_Subtract>", lambda _: resta())


# # Clear (SUPR)
# raiz.bind("<Delete>", lambda _: borrar_todo())


# # Delete (BackSpace)
# raiz.bind("<BackSpace>", lambda _: borrar_ultimo())


# # = (Return/Intro)
# raiz.bind("<Return>", lambda _: subTotal())
# raiz.bind("<KP_Enter>", lambda _: subTotal())





raiz.mainloop()