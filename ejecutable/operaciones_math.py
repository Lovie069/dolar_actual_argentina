'''VARIABLES GLOBALES'''
resultado=0
operacion=""
reset_pantalla=False
d=0


'''FUNCIONES PARA SUMAR (O RESTAR) VARIOS VALORES DENTRO DEL CAMPO [PESOS ($)] Y [DOLARES (USD)]
ANTES DE REALIZAR LA CONVERSIÓN A [TC ($ / USD)], A [DOLARES (USD)] O A [PESOS ($)]'''


# FUNCIÓN PARA INSERTAR DIGITOS EN LA PANTALLA
def presionarBoton(digito, datoIngreso, pantalla, END):

    global operacion, resultado, reset_pantalla, d

    if reset_pantalla==True:
        if datoIngreso.get()!="INF" or datoIngreso.get()!="COMPLEJO":
            resultado= resultado
            operacion=operacion            
            
        elif datoIngreso.get()=="INF" or datoIngreso.get()=="COMPLEJO":
            resultado= 0
            operacion=""

        datoIngreso.set(digito)
        reset_pantalla=False        

    elif reset_pantalla==False:

        if d==0:

            if digito==".":
                datoIngreso.set(datoIngreso.get() + digito)

                d+=1

            elif digito!=".":
                datoIngreso.set(datoIngreso.get() + digito)

        else:
            if digito==".":
                datoIngreso.set(datoIngreso.get())

            elif digito!=".":
                datoIngreso.set(datoIngreso.get() + digito)
    
    pantalla.icursor(END)

      
    # print(resultado)
    # print(operacion)
    # print(reset_pantalla)



# FUNCIÓN SUMAR:
def suma(datoIngreso, pantalla, END):

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and datoIngreso.get()!="":

        if operacion=="sumar":
            resultado=resultado + float(datoIngreso.get())
        
        elif operacion=="restar":
            resultado= resultado - float(datoIngreso.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(datoIngreso.get())
        
        elif operacion=="":
            resultado= float(datoIngreso.get())

        elif operacion=="dividir":
            try:
                resultado= resultado / float(datoIngreso.get())
        
            except ZeroDivisionError:
                resultado="INF"

#RESULTA:
        operacion="sumar"
        reset_pantalla=True
        datoIngreso.set(resultado)

    elif reset_pantalla==False and datoIngreso.get()=="":
        resultado=resultado
        operacion="sumar"
        reset_pantalla=True
        datoIngreso.set(resultado)
        
#SI NO:
    elif reset_pantalla==True:
        if datoIngreso.get()!="INF" or datoIngreso.get()!="COMPLEJO":
            resultado= float(datoIngreso.get())
            operacion="sumar"
            reset_pantalla=True
            datoIngreso.set(resultado)

        elif datoIngreso.get()=="INF" or datoIngreso.get()=="COMPLEJO":
            resultado= 0
            operacion=""
            reset_pantalla=False
            datoIngreso.set("")

    pantalla.icursor(END)

    # print(resultado)
    # print(operacion)
    # print(reset_pantalla)




# FUNCIÓN RESTAR:
def resta(datoIngreso, pantalla, END):

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False  and datoIngreso.get()!="":

        if operacion=="sumar":
            resultado=resultado + float(datoIngreso.get())
        
        elif operacion=="restar":
            resultado= resultado - float(datoIngreso.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(datoIngreso.get())
        
        elif operacion=="":
            resultado= float(datoIngreso.get())

        elif operacion=="dividir":
            try:
                resultado= resultado / float(datoIngreso.get())
        
            except ZeroDivisionError:
                resultado="INF"

#RESULTA:
        operacion="restar"
        reset_pantalla=True
        datoIngreso.set(resultado)

    elif reset_pantalla==False and datoIngreso.get()=="":
        resultado=resultado
        operacion="restar"
        reset_pantalla=True
        datoIngreso.set(resultado)
            
#SI NO:
    elif reset_pantalla==True:
        if datoIngreso.get()!="INF" or datoIngreso.get()!="COMPLEJO":
            resultado= float(datoIngreso.get())
            operacion="restar"
            reset_pantalla=True
            datoIngreso.set(resultado)

        elif datoIngreso.get()=="INF" or datoIngreso.get()=="COMPLEJO":
            resultado= 0
            operacion=""
            reset_pantalla=False
            datoIngreso.set("")

    pantalla.icursor(END)

    # print(resultado)
    # print(operacion)
    # print(reset_pantalla)


#FUNCIÓN SUB TOTAL (O IGUAL):
def subTotal(datoIngreso, pantalla, END):

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and datoIngreso.get()!="":

        if operacion=="sumar":
            resultado= resultado + float(datoIngreso.get())

        elif operacion=="restar":
            resultado= resultado - float(datoIngreso.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(datoIngreso.get())
           
        elif operacion=="":
            resultado= float(datoIngreso.get())
                  
        elif operacion=="dividir":
                try:
                    resultado= resultado / float(datoIngreso.get())
            
                except ZeroDivisionError:
                    resultado= "INF"

#RESULTA:       
        reset_pantalla=True
        datoIngreso.set(resultado)

    elif reset_pantalla==False and datoIngreso.get()=="":
        resultado=resultado
        operacion=""
        reset_pantalla=True
        datoIngreso.set(resultado)
        

#RESULTA (en True con todas las operaciones):

    elif reset_pantalla==True:
        if datoIngreso.get()!="INF" or datoIngreso.get()!="COMPLEJO":
            resultado= float(datoIngreso.get())
            reset_pantalla=True
            datoIngreso.set(resultado)
        
        elif datoIngreso.get()=="INF" or datoIngreso.get()=="COMPLEJO":
            resultado= 0
            reset_pantalla=False
            datoIngreso.set("")

    operacion=""

    pantalla.icursor(END)

    # print(resultado)
    # print(operacion)
    # print(reset_pantalla)


#FUNCIÓN BORRAR ÚLTIMO DÍGITO:
def borrar_ultimo(datoIngreso, pantalla, END):

    global operacion, resultado, reset_pantalla, d

    d=0

    if datoIngreso.get()!="":
        datoIngreso.set(datoIngreso.get()[:-1])

    else:
        datoIngreso.set("")
    
    pantalla.icursor(END)