# App Tkinter para consultar y calcular con tipos de cambio del dólar en Argentina (Actual e Histórico) – Versión 1.5 (10/2025)
 # Importación de librerías
import requests
import pandas as pd
import numpy as np
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import font
from datetime import datetime
import os
import sys
from funciones_TC  import *


'''IMPORTACIÓN DE FUNCIONES PROPIAS'''
from operaciones_math import *


# Inicio de la interfaz de usuario (ventana raíz)
#CREACIÓN DE VENTANAS:
raiz=Tk()
# raiz.title("Tipo de Cambio del Dolar Oficial en Argentina")
raiz.title("Tipo de Cambio del Dolar en Argentina")

# Configuración de la ventana raíz
ancho_ventana = 510
alto_ventana = 280

x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

# raiz.geometry("700x750"+100,100)

# Variables globales de estado/texto
comentario=StringVar()

# Parámetro para efecto de parpadeo en la etiqueta de VENTA
flash_delay = 250  # msec between colour change


# Menú principal (Acerca de / Información)
barra_menu=Menu(raiz)
raiz.config(menu=barra_menu)

#COMANDO PARA ELIMINAR LA LÍNEA DE LÁGRIMA DEL MENÚ:
raiz.option_add("*tearOff",False)

#CREANDO LAS PESTAÑAS DEL MENÚ PRINCIPAL:
menu_Acerca=Menu(barra_menu)

#AGREGANDO LAS PESTAÑAS AL MENÚ PRINCIPAL:
barra_menu.add_cascade(menu=menu_Acerca,label="Información de contacto")

#CREANDO LAS PESTAÑAS DEL MENÚ PRINCIPAL:
menu_Personalizacion=Menu(barra_menu)

#AGREGANDO LAS PESTAÑAS AL MENÚ PRINCIPAL:
barra_menu.add_cascade(menu=menu_Personalizacion,label="Personalización")

#CREANDO Y AGREGANDO LOS SUB MENÚS DE LA PESTAÑA "Acerca de":
menu_Acerca.add_command(label="Contáctanos",command=lambda:mensajeContacto())
menu_Acerca.add_command(label="Versión",command=lambda:mensajeVersion())

#CREANDO Y AGREGANDO LOS SUB MENÚS DE LA PESTAÑA "Personalización":
menu_Personalizacion.add_command(label="Configurar colores y fuentes",command=lambda:ventanaPersonalizacion())


# Muestra datos de contacto
def mensajeContacto():
    messagebox.showinfo("Contáctanos","Para mayor información favor escribir al siguiente email:\n\nrodriguezcolmenaresl@gmail.com")

# Muestra la versión actual
def mensajeVersion():
    # messagebox.showinfo("Info. Versión","Versión 1.0 \n \nMes/Año: 09/2024")
    # messagebox.showinfo("Info. Versión","Versión 1.3 \n \nMes/Año: 03/2025")
    # messagebox.showinfo("Info. Versión","Versión 1.4 \n \nMes/Año: 10/2025")
    messagebox.showinfo("Info. Versión","Versión 1.5 \n \nMes/Año: 10/2025")


# Función para obtener la ruta del directorio donde guardar/cargar configuración
def get_config_dir():
    """Obtiene la ruta del directorio donde guardar la configuración (compatible con .exe)"""
    try:
        # Si estamos ejecutando desde un .exe (PyInstaller)
        if getattr(sys, 'frozen', False):
            # sys.executable contiene la ruta al .exe
            base_path = os.path.dirname(sys.executable)
        else:
            # Si estamos ejecutando desde un script .py
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        return base_path
    except Exception as e:
        print(f"Error al determinar directorio de configuración: {e}")
        return os.path.dirname(os.path.abspath(__file__))


# Función para guardar la configuración de personalización
def guardar_configuracion():
    """Guarda la configuración de colores y fuentes en un archivo JSON"""
    try:
        config = {
            'colorRaiz': colorRaiz,
            'colorGeneral': colorGeneral,
            'colorSeleccion': colorSeleccion,
            'colorComentario': colorComentario,
            'colorDbgBoton': colorDbgBoton,
            'colorAbgBoton': colorAbgBoton,
            'fuenteGeneral': fuenteGeneral
        }
        
        # Guardar en el directorio correcto (compatible con .exe)
        config_file = os.path.join(get_config_dir(), 'config_personalizacion.json')
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"Configuración guardada en: {config_file}")
    except Exception as e:
        print(f"Error al guardar configuración: {e}")


# Función para cargar la configuración de personalización
def cargar_configuracion():
    """Carga la configuración de colores y fuentes desde un archivo JSON"""
    global colorRaiz, colorGeneral, colorSeleccion, colorComentario
    global colorDbgBoton, colorAbgBoton, fuenteGeneral
    
    try:
        config_file = os.path.join(get_config_dir(), 'config_personalizacion.json')
        
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Aplicar configuración cargada
            colorRaiz = config.get('colorRaiz', colorRaiz)
            colorGeneral = config.get('colorGeneral', colorGeneral)
            colorSeleccion = config.get('colorSeleccion', colorSeleccion)
            colorComentario = config.get('colorComentario', colorComentario)
            colorDbgBoton = config.get('colorDbgBoton', colorDbgBoton)
            colorAbgBoton = config.get('colorAbgBoton', colorAbgBoton)
            fuenteGeneral = config.get('fuenteGeneral', fuenteGeneral)
            
            print(f"Configuración cargada desde: {config_file}")
            return True
        else:
            print(f"Archivo de configuración no encontrado: {config_file}")
            return False
    except Exception as e:
        print(f"Error al cargar configuración: {e}")
        return False


# Función para aplicar cambios de personalización a todos los widgets
def aplicarPersonalizacion():
    global colorRaiz, colorGeneral, colorSeleccion, colorComentario
    global colorDbgBoton, colorAbgBoton
    global fuenteGeneral, fuenteTitulo, fuenteSubtitulo, fuenteBotones, fuenteDatos, fuenteIngreso, fuenteResultados
    global letraTitulo, letraSubtitulos, letraBotones, letraDatos, letraDatos2, letraIngresos, letraResultados
    global new_colour
    
    # Actualizar variables de fuente (mantener tamaños originales)
    letraTitulo = (fuenteGeneral, 11, 'bold')
    letraSubtitulos = (fuenteGeneral, 10, 'bold')
    letraBotones = (fuenteGeneral, 8, 'bold')
    letraDatos = (fuenteGeneral, 9)
    letraDatos2 = (fuenteGeneral, 7, 'bold')
    letraIngresos = (fuenteGeneral, 9)
    letraResultados = (fuenteGeneral, 9)
    
    # Actualizar colores de fuente
    fuenteTitulo = colorGeneral
    fuenteSubtitulo = colorGeneral
    fuenteBotones = colorGeneral
    fuenteDatos = colorGeneral
    fuenteIngreso = colorGeneral
    fuenteResultados = colorGeneral
    new_colour = colorGeneral
    
    # Actualizar ventana raíz
    raiz.config(bg=colorRaiz)
    
    # Actualizar frame principal
    miFrame.config(bg=colorRaiz)
    
    # Actualizar estilo de Notebook
    s1.configure("TNotebook.Tab", foreground=colorGeneral, font=(fuenteGeneral, 8, 'bold'))
    s1.map("TNotebook.Tab", foreground=[("active", colorSeleccion)])
    
    # Actualizar todos los widgets hijos de las pestañas
    actualizar_widgets_tipoCambio()
    actualizar_widgets_verificacion()
    actualizar_widgets_historico()
    
    # Guardar configuración
    guardar_configuracion()
    
    # Forzar actualización de la ventana
    raiz.update_idletasks()


def actualizar_widgets_tipoCambio():
    """Actualiza todos los widgets de la pestaña TipoCambio"""
    def actualizar_recursivo(widget):
        # Actualizar Labels de tkinter
        if isinstance(widget, Label):
            try:
                widget_text = widget.cget('text')
                textvar = str(widget.cget('textvariable'))
                
                if widget_text in ["COMPRA", "VENTA", "VARIACIÓN", "FECHA (Últ. Act.)", "Ingrese el valor (en USD)", "Resultado (en $ ARS)"]:
                    widget.config(fg=fuenteSubtitulo, font=letraSubtitulos)
                elif textvar == str(texto_compra):
                    widget.config(fg=fuenteDatos, font=letraDatos)
                elif textvar == str(texto_variacion):
                    widget.config(fg=fuenteDatos, font=letraDatos)
                elif textvar == str(texto_fecha):
                    widget.config(fg=fuenteDatos, font=letraDatos)
            except:
                pass
        # Actualizar Buttons de tkinter
        elif isinstance(widget, Button):
            try:
                widget.config(fg=fuenteBotones, font=letraBotones, bg=colorDbgBoton, activebackground=colorAbgBoton)
            except:
                pass
        # Actualizar Entry de tkinter
        elif isinstance(widget, Entry):
            try:
                textvar = str(widget.cget('textvariable'))
                if textvar == str(texto_resultado1):
                    widget.config(fg=fuenteResultados, font=letraResultados)
                else:
                    widget.config(fg=fuenteIngreso, font=letraIngresos)
            except:
                pass
        
        # Actualizar widgets hijos recursivamente
        try:
            for child in widget.winfo_children():
                actualizar_recursivo(child)
        except:
            pass
    
    for widget in tipoCambio.winfo_children():
        actualizar_recursivo(widget)
    
    # Actualizar Label_venta específicamente
    try:
        Label_venta.config(fg=new_colour, font=letraDatos)
    except:
        pass


def actualizar_widgets_verificacion():
    """Actualiza todos los widgets de la pestaña Verificación"""
    def actualizar_recursivo(widget):
        # Actualizar Labels de tkinter
        if isinstance(widget, Label):
            try:
                widget_text = widget.cget('text')
                textvar = str(widget.cget('textvariable'))
                
                if widget_text == "VERIFICACIÓN":
                    widget.config(fg=fuenteTitulo, font=letraTitulo)
                elif widget_text in ["TC ($ / USD)", "PESOS ($)", "DOLARES (USD)"]:
                    widget.config(fg=fuenteSubtitulo, font=letraSubtitulos)
                elif textvar == str(comentario):
                    widget.config(fg=colorComentario, font=letraSubtitulos)
            except:
                pass
        # Actualizar Buttons de tkinter
        elif isinstance(widget, Button):
            try:
                widget.config(fg=fuenteBotones, font=letraBotones, bg=colorDbgBoton, activebackground=colorAbgBoton)
            except:
                pass
        # Actualizar Entry de tkinter
        elif isinstance(widget, Entry):
            try:
                widget.config(fg=fuenteIngreso, font=letraIngresos)
            except:
                pass
        
        # Actualizar widgets hijos recursivamente
        try:
            for child in widget.winfo_children():
                actualizar_recursivo(child)
        except:
            pass
    
    for widget in verificacionValores.winfo_children():
        actualizar_recursivo(widget)


def actualizar_widgets_historico():
    """Actualiza todos los widgets de la pestaña Histórico"""
    def actualizar_recursivo(widget):
        # Actualizar Labels de tkinter
        if isinstance(widget, Label):
            try:
                widget_text = widget.cget('text')
                if widget_text in ["Fecha", "Compra", "Venta"]:
                    widget.config(fg=fuenteTitulo, font=letraTitulo)
            except:
                pass
        # Actualizar Buttons de tkinter
        elif isinstance(widget, Button):
            try:
                widget.config(fg=fuenteBotones, font=letraBotones, bg=colorDbgBoton, activebackground=colorAbgBoton)
            except:
                pass
        # Actualizar Entry de tkinter
        elif isinstance(widget, Entry):
            try:
                widget.config(fg=fuenteIngreso, font=letraIngresos)
            except:
                pass
        # Actualizar Text de tkinter (excepto la tabla de histórico que usa fuente fija)
        elif isinstance(widget, tk.Text):
            try:
                # Solo actualizar color, pero mantener la fuente original (Courier para tabla histórica)
                current_font = widget.cget('font')
                widget.config(fg=colorGeneral)
                # Si la fuente ya es Courier, no la cambiamos (es la tabla histórica)
                if not current_font or 'Courier' not in str(current_font):
                    widget.config(font=(fuenteGeneral, 11))
            except:
                pass
        
        # Actualizar widgets hijos recursivamente
        try:
            for child in widget.winfo_children():
                actualizar_recursivo(child)
        except:
            pass
    
    for widget in dolarHistorico.winfo_children():
        actualizar_recursivo(widget)


# Función para mostrar ventana de personalización
def ventanaPersonalizacion():
    global colorRaiz, colorGeneral, colorSeleccion, colorComentario
    global colorDbgBoton, colorAbgBoton, fuenteGeneral
    
    # Crear ventana de personalización
    ventana_pers = tk.Toplevel(raiz)
    ventana_pers.title("Personalización")
    ventana_pers.geometry("500x550")
    ventana_pers.resizable(0, 0)
    ventana_pers.config(bg=colorRaiz)
    ventana_pers.transient(raiz)
    ventana_pers.grab_set()
    
    # Centrar ventana
    raiz.update_idletasks()
    x_main = raiz.winfo_x()
    y_main = raiz.winfo_y()
    width_main = raiz.winfo_width()
    height_main = raiz.winfo_height()
    x_centered = x_main + (width_main // 2) - 250
    y_centered = y_main + (height_main // 2) - 275
    ventana_pers.geometry(f"500x550+{x_centered}+{y_centered}")
    
    # Frame principal
    frame_principal = tk.Frame(ventana_pers, bg=colorRaiz)
    frame_principal.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Título
    titulo = tk.Label(frame_principal, text="Personalización de Colores y Fuentes", 
                     font=(fuenteGeneral, 12, 'bold'), bg=colorRaiz, fg=colorGeneral)
    titulo.pack(pady=10)
    
    # Variables para almacenar selecciones
    color_raiz_sel = colorRaiz
    color_general_sel = colorGeneral
    color_seleccion_sel = colorSeleccion
    color_comentario_sel = colorComentario
    color_boton_bg_sel = colorDbgBoton
    color_boton_active_sel = colorAbgBoton
    fuente_general_sel = fuenteGeneral
    
    # Función para seleccionar color de fondo (se define después de las otras funciones)
    
    # Función para seleccionar color general
    def seleccionar_color_general():
        nonlocal color_general_sel
        color = colorchooser.askcolor(title="Seleccionar Color General de Texto", initialcolor=colorGeneral)[1]
        if color:
            color_general_sel = color
            preview_general.config(bg=color, text=color)
    
    # Función para seleccionar color de selección
    def seleccionar_color_seleccion():
        nonlocal color_seleccion_sel
        color = colorchooser.askcolor(title="Seleccionar Color de Selección", initialcolor=colorSeleccion)[1]
        if color:
            color_seleccion_sel = color
            preview_seleccion.config(bg=color, text=color)
    
    # Función para seleccionar color de comentario
    def seleccionar_color_comentario():
        nonlocal color_comentario_sel
        color = colorchooser.askcolor(title="Seleccionar Color de Comentario", initialcolor=colorComentario)[1]
        if color:
            color_comentario_sel = color
            preview_comentario.config(bg=color, text=color)
    
    # Función para seleccionar color de botón normal
    def seleccionar_color_boton():
        nonlocal color_boton_bg_sel
        color = colorchooser.askcolor(title="Seleccionar Color de Fondo de Botón", initialcolor=colorDbgBoton)[1]
        if color:
            color_boton_bg_sel = color
            preview_boton.config(bg=color, text=color)
    
    # Función para seleccionar color de botón activo
    def seleccionar_color_boton_active():
        nonlocal color_boton_active_sel
        color = colorchooser.askcolor(title="Seleccionar Color de Botón Presionado", initialcolor=colorAbgBoton)[1]
        if color:
            color_boton_active_sel = color
            preview_boton_active.config(bg=color, text=color)
    
    # Función para seleccionar fuente
    def seleccionar_fuente():
        nonlocal fuente_general_sel
        # Obtener fuentes disponibles
        fuentes_disponibles = sorted(list(font.families()))
        ventana_fuente = tk.Toplevel(ventana_pers)
        ventana_fuente.title("Seleccionar Fuente")
        ventana_fuente.geometry("450x450")
        ventana_fuente.config(bg=colorRaiz)
        ventana_fuente.transient(ventana_pers)
        ventana_fuente.grab_set()
        
        # Centrar ventana
        x_f = ventana_pers.winfo_x() + 50
        y_f = ventana_pers.winfo_y() + 50
        ventana_fuente.geometry(f"450x450+{x_f}+{y_f}")
        
        # Frame para el buscador
        frame_busqueda = tk.Frame(ventana_fuente, bg=colorRaiz)
        frame_busqueda.pack(fill="x", padx=10, pady=(10, 5))
        
        tk.Label(frame_busqueda, text="Buscar:", font=(fuenteGeneral, 9, 'bold'), 
                bg=colorRaiz, fg=colorGeneral).pack(side="left", padx=5)
        
        entrada_busqueda = tk.Entry(frame_busqueda, font=(fuenteGeneral, 9), width=30)
        entrada_busqueda.pack(side="left", fill="x", expand=True, padx=5)
        entrada_busqueda.focus_set()
        
        # Frame con scroll
        frame_fuente = tk.Frame(ventana_fuente, bg=colorRaiz)
        frame_fuente.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Lista de fuentes
        lista_fuentes = tk.Listbox(frame_fuente, font=(fuenteGeneral, 9), bg="white", fg=colorGeneral)
        lista_fuentes.pack(side="left", fill="both", expand=True)
        
        scrollbar_fuente = tk.Scrollbar(frame_fuente, orient="vertical", command=lista_fuentes.yview)
        scrollbar_fuente.pack(side="right", fill="y")
        lista_fuentes.config(yscrollcommand=scrollbar_fuente.set)
        
        # Función para filtrar fuentes
        def filtrar_fuentes(*args):
            busqueda = entrada_busqueda.get().lower()
            lista_fuentes.delete(0, tk.END)
            fuentes_filtradas = [f for f in fuentes_disponibles if busqueda in f.lower()]
            for fuente in fuentes_filtradas:
                lista_fuentes.insert(tk.END, fuente)
            # Si hay solo un resultado o el texto coincide exactamente, seleccionarlo
            if len(fuentes_filtradas) == 1 or busqueda and busqueda in fuente_general_sel.lower():
                if len(fuentes_filtradas) > 0:
                    lista_fuentes.selection_set(0)
                    lista_fuentes.activate(0)
        
        # Vincular el evento de escritura en el buscador
        entrada_busqueda.bind('<KeyRelease>', filtrar_fuentes)
        
        # Cargar todas las fuentes inicialmente
        for fuente in fuentes_disponibles:
            lista_fuentes.insert(tk.END, fuente)
        
        # Botón seleccionar
        def aplicar_fuente():
            seleccion = lista_fuentes.curselection()
            if seleccion:
                nonlocal fuente_general_sel
                fuente_general_sel = lista_fuentes.get(seleccion[0])
                preview_fuente.config(text=f"Fuente: {fuente_general_sel}")
                ventana_fuente.destroy()
        
        # Frame para botones
        frame_botones = tk.Frame(ventana_fuente, bg=colorRaiz)
        frame_botones.pack(pady=5)
        
        boton_aplicar_fuente = tk.Button(frame_botones, text="Aplicar", 
                                        command=aplicar_fuente, bg=colorDbgBoton, 
                                        fg=fuenteBotones, font=letraBotones, width=12)
        boton_aplicar_fuente.pack(side="left", padx=5)
        
        boton_cancelar_fuente = tk.Button(frame_botones, text="Cancelar", 
                                         command=ventana_fuente.destroy, bg=colorDbgBoton, 
                                         fg=fuenteBotones, font=letraBotones, width=12)
        boton_cancelar_fuente.pack(side="left", padx=5)
    
    # Sección de colores
    frame_colores = tk.LabelFrame(frame_principal, text="Colores", 
                                  font=(fuenteGeneral, 10, 'bold'), 
                                  bg=colorRaiz, fg=colorGeneral, padx=10, pady=10)
    frame_colores.pack(fill="x", pady=5)
    
    # Sección de fuente (se crea antes para poder referenciarla)
    frame_fuente = tk.LabelFrame(frame_principal, text="Fuente", 
                                font=(fuenteGeneral, 10, 'bold'), 
                                bg=colorRaiz, fg=colorGeneral, padx=10, pady=10)
    
    # Función para actualizar fondo de la ventana cuando cambia el color de fondo
    def actualizar_fondo_ventana():
        ventana_pers.config(bg=color_raiz_sel)
        frame_principal.config(bg=color_raiz_sel)
        frame_colores.config(bg=color_raiz_sel)
        frame_fuente.config(bg=color_raiz_sel)
        for widget in frame_principal.winfo_children():
            try:
                if isinstance(widget, (tk.Frame, tk.LabelFrame)):
                    widget.config(bg=color_raiz_sel)
                elif isinstance(widget, tk.Label):
                    if widget.cget('text') not in ["Personalización de Colores y Fuentes"]:
                        widget.config(bg=color_raiz_sel)
            except:
                pass
    
    # Función para seleccionar color de fondo
    def seleccionar_color_raiz_con_actualizacion():
        nonlocal color_raiz_sel
        color = colorchooser.askcolor(title="Seleccionar Color de Fondo", initialcolor=colorRaiz)[1]
        if color:
            color_raiz_sel = color
            preview_raiz.config(bg=color, text=color)
            actualizar_fondo_ventana()
    
    # Color de fondo
    frame_raiz = tk.Frame(frame_colores, bg=colorRaiz)
    frame_raiz.pack(fill="x", pady=2)
    tk.Label(frame_raiz, text="Color de Fondo:", font=(fuenteGeneral, 9), 
            bg=colorRaiz, fg=colorGeneral, width=20, anchor="w").pack(side="left")
    preview_raiz = tk.Label(frame_raiz, text=colorRaiz, bg=colorRaiz, 
                           fg=colorGeneral, width=15, relief="solid", borderwidth=1)
    preview_raiz.pack(side="left", padx=5)
    tk.Button(frame_raiz, text="Seleccionar", command=seleccionar_color_raiz_con_actualizacion,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=12).pack(side="left", padx=5)
    
    # Color general
    frame_general = tk.Frame(frame_colores, bg=colorRaiz)
    frame_general.pack(fill="x", pady=2)
    tk.Label(frame_general, text="Color General de Texto:", font=(fuenteGeneral, 9), 
            bg=colorRaiz, fg=colorGeneral, width=20, anchor="w").pack(side="left")
    preview_general = tk.Label(frame_general, text=colorGeneral, bg=colorGeneral, 
                              fg="white", width=15, relief="solid", borderwidth=1)
    preview_general.pack(side="left", padx=5)
    tk.Button(frame_general, text="Seleccionar", command=seleccionar_color_general,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=12).pack(side="left", padx=5)
    
    # Color de selección
    frame_seleccion = tk.Frame(frame_colores, bg=colorRaiz)
    frame_seleccion.pack(fill="x", pady=2)
    tk.Label(frame_seleccion, text="Color de Selección:", font=(fuenteGeneral, 9), 
            bg=colorRaiz, fg=colorGeneral, width=20, anchor="w").pack(side="left")
    preview_seleccion = tk.Label(frame_seleccion, text=colorSeleccion, bg=colorSeleccion, 
                                fg="white", width=15, relief="solid", borderwidth=1)
    preview_seleccion.pack(side="left", padx=5)
    tk.Button(frame_seleccion, text="Seleccionar", command=seleccionar_color_seleccion,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=12).pack(side="left", padx=5)
    
    # Color de comentario
    frame_comentario = tk.Frame(frame_colores, bg=colorRaiz)
    frame_comentario.pack(fill="x", pady=2)
    tk.Label(frame_comentario, text="Color de Comentario:", font=(fuenteGeneral, 9), 
            bg=colorRaiz, fg=colorGeneral, width=20, anchor="w").pack(side="left")
    preview_comentario = tk.Label(frame_comentario, text=colorComentario, bg=colorComentario, 
                                 fg="white", width=15, relief="solid", borderwidth=1)
    preview_comentario.pack(side="left", padx=5)
    tk.Button(frame_comentario, text="Seleccionar", command=seleccionar_color_comentario,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=12).pack(side="left", padx=5)
    
    # Color de botón normal
    frame_boton = tk.Frame(frame_colores, bg=colorRaiz)
    frame_boton.pack(fill="x", pady=2)
    tk.Label(frame_boton, text="Color Fondo Botón:", font=(fuenteGeneral, 9), 
            bg=colorRaiz, fg=colorGeneral, width=20, anchor="w").pack(side="left")
    preview_boton = tk.Label(frame_boton, text=colorDbgBoton, bg=colorDbgBoton, 
                            fg=colorGeneral, width=15, relief="solid", borderwidth=1)
    preview_boton.pack(side="left", padx=5)
    tk.Button(frame_boton, text="Seleccionar", command=seleccionar_color_boton,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=12).pack(side="left", padx=5)
    
    # Color de botón activo
    frame_boton_active = tk.Frame(frame_colores, bg=colorRaiz)
    frame_boton_active.pack(fill="x", pady=2)
    tk.Label(frame_boton_active, text="Color Botón Presionado:", font=(fuenteGeneral, 9), 
            bg=colorRaiz, fg=colorGeneral, width=20, anchor="w").pack(side="left")
    preview_boton_active = tk.Label(frame_boton_active, text=colorAbgBoton, bg=colorAbgBoton, 
                                    fg="white", width=15, relief="solid", borderwidth=1)
    preview_boton_active.pack(side="left", padx=5)
    tk.Button(frame_boton_active, text="Seleccionar", command=seleccionar_color_boton_active,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=12).pack(side="left", padx=5)
    
    # Sección de fuente (continuación)
    frame_fuente.pack(fill="x", pady=5)
    
    frame_fuente_sel = tk.Frame(frame_fuente, bg=colorRaiz)
    frame_fuente_sel.pack(fill="x", pady=2)
    tk.Label(frame_fuente_sel, text="Tipo de Letra:", font=(fuenteGeneral, 9), 
            bg=colorRaiz, fg=colorGeneral, width=20, anchor="w").pack(side="left")
    preview_fuente = tk.Label(frame_fuente_sel, text=f"Fuente: {fuenteGeneral}", 
                            font=(fuenteGeneral, 9), bg=colorRaiz, fg=colorGeneral, 
                            width=25, anchor="w")
    preview_fuente.pack(side="left", padx=5)
    tk.Button(frame_fuente_sel, text="Seleccionar", command=seleccionar_fuente,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=12).pack(side="left", padx=5)
    
    # Botones de acción
    frame_botones = tk.Frame(frame_principal, bg=colorRaiz)
    frame_botones.pack(pady=20)
    
    def aplicar_cambios():
        global colorRaiz, colorGeneral, colorSeleccion, colorComentario
        global colorDbgBoton, colorAbgBoton, fuenteGeneral
        
        colorRaiz = color_raiz_sel
        colorGeneral = color_general_sel
        colorSeleccion = color_seleccion_sel
        colorComentario = color_comentario_sel
        colorDbgBoton = color_boton_bg_sel
        colorAbgBoton = color_boton_active_sel
        fuenteGeneral = fuente_general_sel
        
        aplicarPersonalizacion()
        ventana_pers.destroy()
        messagebox.showinfo("Personalización", "Los cambios se han aplicado correctamente.")
    
    def restaurar_defaults():
        nonlocal color_raiz_sel, color_general_sel, color_seleccion_sel, color_comentario_sel
        nonlocal color_boton_bg_sel, color_boton_active_sel, fuente_general_sel
        
        color_raiz_sel = '#E0BFE0'
        color_general_sel = '#502A4F'
        color_seleccion_sel = '#944D93'
        color_comentario_sel = '#E075DF'
        color_boton_bg_sel = '#E0BFE0'
        color_boton_active_sel = '#E075DF'
        fuente_general_sel = 'Comic Sans MS'
        
        preview_raiz.config(bg=color_raiz_sel, text=color_raiz_sel)
        preview_general.config(bg=color_general_sel, text=color_general_sel)
        preview_seleccion.config(bg=color_seleccion_sel, text=color_seleccion_sel)
        preview_comentario.config(bg=color_comentario_sel, text=color_comentario_sel)
        preview_boton.config(bg=color_boton_bg_sel, text=color_boton_bg_sel)
        preview_boton_active.config(bg=color_boton_active_sel, text=color_boton_active_sel)
        preview_fuente.config(text=f"Fuente: {fuente_general_sel}")
    
    tk.Button(frame_botones, text="Aplicar Cambios", command=aplicar_cambios,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=15, height=2).pack(side="left", padx=5)
    
    tk.Button(frame_botones, text="Restaurar Defaults", command=restaurar_defaults,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=15, height=2).pack(side="left", padx=5)
    
    tk.Button(frame_botones, text="Cancelar", command=ventana_pers.destroy,
             bg=colorDbgBoton, fg=fuenteBotones, font=letraBotones, width=15, height=2).pack(side="left", padx=5)


# Características visuales reutilizadas (espaciados, colores, fuentes)
# Dimensiones

#PADDING:
x1=15 #Padx
y1=1 #Pady

x2=x1 #Padx
y2=5 #Pady

x3=x1 #Padx
y3= (5,1) #Pady

 


# Bordes y ancho por defecto
# TIPOS: raised, sunken, flat, groove, ridge, solid
bordeTitulo = "flat"
bordeSubtitulo = "flat"

# ANCHO
b1 = 1
 

#ORIENTACION:
u1="nsew" #Ubicación figuras geométricas
 


# Botones: colores por defecto
colorRaiz = '#E0BFE0'
colorDbgBoton = "#E0BFE0"

# FONDOS AL PRESIONAR
colorAbgBoton = "#E075DF"

 


# Colores y fuentes
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

# Fuentes (familia y tamaños)
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

# Cargar configuración guardada (si existe)
cargar_configuracion()

# Aplicar configuración cargada a la ventana principal
raiz.config(bg=colorRaiz,padx=10,pady=10)
raiz.resizable(0,0)

# Fondo de inputs
fondoIngresos = "white"

# Mensajes de validación para pestaña Verificación
F1 = "Debes insertar al menos 2 datos"
F2 = "Faltan 1 campo por llenar"
F3 = "Operación realizada"
F4 = "Recuerda limpiar los campos antes de operar"


# Creación de contenedor principal
# miFrame=Frame(raiz) #width=200, height=300
# miFrame.pack()
miFrame=Frame(raiz, relief="solid",borderwidth=0,padx=1,pady=1)
miFrame.pack()
#TIPOS DE BORDES: raised, sunken, flat, groove, ridge, solid
# TIPOS DE CURSOR , cursor='cross'

# recuadro1=ttk.LabelFrame(miFrame,text="Geométricos",padding=(10,5))
# recuadro1.pack(fill="both",expand=1)
# Estilos para Notebook/ pestañas

s1 = ttk.Style()
# s1.theme_use("classic")
# print(ttk.Style().theme_names())
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
# s1.configure("TNotebook.Tab", foreground="black", background="green", font=('fuenteGeneral', '11', 'bold'))
s1.configure("TNotebook.Tab", foreground=colorGeneral, font=('fuenteGeneral', '8', 'bold'))
s1.map("TNotebook.Tab", foreground=[("active", colorSeleccion)])

 

# Notebook con tres pestañas: TC, Verificación, Histórico
notebook1 = ttk.Notebook(miFrame,padding=10)
notebook1.grid(column=0,row=0,sticky='nsew')

tipoCambio = ttk.Frame(notebook1,padding=(1,1)) #PRIMERA PÁGINA
verificacionValores = ttk.Frame(notebook1,padding=(1,1)) #SEGUNDA PÁGINA
dolarHistorico = ttk.Frame(notebook1,padding=(1,1)) #TERCERA PÁGINA

notebook1.add(tipoCambio, text='TC')
notebook1.add(verificacionValores, text='Verificación')
notebook1.add(dolarHistorico, text='Histórico')



# URLs de cotizaciones del dólar en Argentina (actual)
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

# Mapeo entre nombre mostrado y URL

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




# URLs base para cotizaciones históricas del dólar

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






# Encabezado User-Agent para evitar bloqueos (Ambito)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}



# Declaración de variables y StringVar para binding en UI

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

 

valor_fecha = ""
valor_compra = 0
valor_venta = 0
valor_variacion = ""

'''PANTALLA 3'''
datoIngreso5 = StringVar()
datoIngreso6 =StringVar()


# Efecto visual: parpadeo en el valor de VENTA cuando se actualiza
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
    # Obtiene datos actuales (compra, venta, variación, fecha) y actualiza la UI
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
        


 


def extraccionDatosDolarHistorico(url,usuario):
    # Descarga datos históricos entre dos fechas y los muestra en un Text como tabla
    global table

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
    # Calcula pesos ARS = precioVenta * montoEnUSD y lo muestra formateado
    global valor_venta, valor_compra, valor_fecha, valor_variacion

    if montoEnUSD == "":
        texto_resultado1.set("")

    else:
        resultado = precioVenta * float(montoEnUSD)
        texto_resultado1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
    

def limpiarCalculos():
    # Limpia campos de la pestaña TC
    datoIngreso1.set("")
    texto_resultado1.set("")

def limpiarCalculos2():
    # Limpia campos y mensajes en pestaña Verificación
    datoIngreso2.set("")
    datoIngreso3.set("")
    datoIngreso4.set("")

    comentario.set("")
 

def limpiarCalculos3():
    # Limpia fechas y tabla en pestaña Histórico
    datoIngreso5.set("")
    datoIngreso6.set("")
    table.delete("1.0", "end")
    

def validation0(digito):
    # Valida que no se ingresen operadores en campos numéricos
    lista = ["+","-","*","/"]
    
    return not digito in lista


def validation(digito):
    # Valida que solo se ingresen dígitos/operadores permitidos
    lista = ["+","-","*","/"]
    for n in range(0, 10):
        lista.append(str(n))

    return not digito in lista
    

# Función para mostrar un calendario y seleccionar una fecha (YYYY-MM-DD)
def mostrar_calendario(entry_widget):
    
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
lista_dolar.grid(row=fila1, column=0, padx=x1, pady=y1, sticky="nsew", columnspan=4)
lista_dolar.configure(justify='center')


#********* PANTALLA = FILA 2 ***************************************
botonActualizar=Button(tipoCambio, text="ACTUALIZAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, width=ancho1, height=alto1, command=lambda:extraccionDatosDolarOficial(url_dolar,headers))
botonActualizar.grid( column=0, row=fila2, columnspan=4,sticky=u1,padx=x2,pady=y2)

#********* TEXTOS = FILA 3 ***************************************
Label(tipoCambio,text="COMPRA", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=0,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,text="VENTA", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=1,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,text="VARIACIÓN", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=2,row=fila3,sticky=u1,padx=x1,pady=y1)
Label(tipoCambio,text="FECHA (Últ. Act.)", fg=fuenteSubtitulo,font=letraSubtitulos, relief=bordeSubtitulo,borderwidth=b1).grid(column=3,row=fila3,sticky=u1,padx=x1,pady=y1)


#********* FILA 4 *************************************************
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
botonCalcular=Button(tipoCambio, text="CALCULAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, width=ancho2, height=alto1, command=lambda:calcularPesosARS(valor_venta,datoIngreso1.get()))
botonCalcular.grid(row=fila7, column=0, columnspan=2,padx=x2,pady=y2) #,sticky=u1

botonLimpiar=Button(tipoCambio, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, width=ancho2, height=alto1, command=lambda:limpiarCalculos())
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
botonCalcular1=Button(verificacionValores, text="CALCULAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, width=ancho2, height=alto1, command=lambda:funcionCalcular(comentario,F1,F2,F3,F4,datoIngreso2,datoIngreso3,datoIngreso4))
botonCalcular1.grid(row=fila7, column=0,padx=x2,pady=y2) #sticky=u1

botonLimpiar2=Button(verificacionValores, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, width=ancho2, height=alto1, command=lambda:limpiarCalculos2())
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


lista_dolar_historico.place(x=15, y=0,width=437, height=20)
lista_dolar_historico.configure(justify='center')

#********* PANTALLA = FILA 2 ***************************************
entryFechaInicial = Entry(dolarHistorico, textvariable=datoIngreso5, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
entryFechaInicial.insert(0, 'AAAA-MM-DD')
entryFechaInicial.bind("<FocusIn>", lambda event: entryFechaInicial.delete(0,"end") if datoIngreso5.get() == "AAAA-MM-DD" else None)
entryFechaInicial.bind("<FocusOut>", lambda event: entryFechaInicial.insert(0, "AAAA-MM-DD") if datoIngreso5.get() == "" else None)
entryFechaInicial.bind("<Button-1>", lambda event: mostrar_calendario(entryFechaInicial))
entryFechaInicial.place(x=100, y=33,width=100, height=28)
 

entryFechaFinal = Entry(dolarHistorico, textvariable=datoIngreso6, font= letraIngresos, justify="center", background=fondoIngresos, fg=fuenteIngreso)
entryFechaFinal.insert(0, 'AAAA-MM-DD')
entryFechaFinal.bind("<FocusIn>", lambda event: entryFechaFinal.delete(0,"end") if datoIngreso6.get() == "AAAA-MM-DD" else None)
entryFechaFinal.bind("<FocusOut>", lambda event: entryFechaFinal.insert(0, "AAAA-MM-DD") if datoIngreso6.get() == "" else None)
entryFechaFinal.bind("<Button-1>", lambda event: mostrar_calendario(entryFechaFinal))
entryFechaFinal.place(x=230, y=33,width=100, height=28)

botonActualizar=Button(dolarHistorico, text="ACTUALIZAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, width=ancho1, height=alto1, command=lambda:extraccionDatosDolarHistorico(url_dolar_historico,headers))
botonActualizar.place(x=360, y=33,width=100, height=28)

botonLimpiar3=Button(dolarHistorico, text="LIMPIAR", fg=fuenteBotones,font=letraBotones, background=colorDbgBoton, activebackground=colorAbgBoton, width=ancho1, height=alto1, command=lambda:limpiarCalculos3())
botonLimpiar3.place(x=360, y=80,width=100, height=28)

#********* FILA 3*************************************************

Label(dolarHistorico,text="Fecha", fg=fuenteTitulo,font=letraTitulo).place(x=100, y=75,width=50, height=20)
Label(dolarHistorico,text="Compra", fg=fuenteTitulo,font=letraTitulo).place(x=200, y=75,width=50, height=20)
Label(dolarHistorico,text="Venta", fg=fuenteTitulo,font=letraTitulo).place(x=280, y=75,width=50, height=20)


# Crear tabla con fuente monospace fija (Courier) para mantener formato consistente
table = tk.Text(dolarHistorico, font=('Courier', 10))
table.config(width=50, height=30)
table.place(x=100, y=105,width=230, height=100)

scrollbar = ttk.Scrollbar(dolarHistorico,orient=tk.VERTICAL, command=table.yview)
table.config(yscrollcommand=scrollbar.set)
scrollbar.place(x=340, y=105, height=100)



'''CÓDIGO PARA INGRESAR DATOS POR TECLADO:'''
 
# Numeros
for n in range(0, 10):
    pantalla4.bind(str(n), lambda event: presionarBoton(event.char,datoIngreso3, pantalla4, END))
    pantalla5.bind(str(n), lambda event: presionarBoton(event.char,datoIngreso4, pantalla5, END))

 

pantalla4.bind("+", lambda _: suma(datoIngreso3, pantalla4, END))
pantalla4.bind("-", lambda _: resta(datoIngreso3, pantalla4, END))
# pantalla5.bind("+", lambda _: suma(datoIngreso4, pantalla5, END))
# pantalla5.bind("-", lambda _: resta(datoIngreso4, pantalla5, END))


 
# Delete (BackSpace)
pantalla4.bind("<BackSpace>", lambda _: borrar_ultimo(datoIngreso3, pantalla4, END))
pantalla5.bind("<BackSpace>", lambda _: borrar_ultimo(datoIngreso4, pantalla5, END))


 
pantalla4.bind("<Return>", lambda _: subTotal(datoIngreso3, pantalla4, END))
 



raiz.mainloop()



