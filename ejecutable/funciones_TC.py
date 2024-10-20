'''FUNCIONES PARA EL TANTEO DE TASAS DE CAMBIO:'''

def tasaCambio(pesos,usd):
    return pesos/usd

def pesos(tc,usd):
    return tc * usd

def usd(tc,pesos):
    return pesos / tc


def funcionCalcular(comentario,F1,F2,F3,F4,datoIngreso2,datoIngreso3,datoIngreso4):
    if datoIngreso2.get()=="" and datoIngreso3.get()=="" and datoIngreso4.get()=="":
        comentario.set(F1)


    elif datoIngreso2.get()=="" and datoIngreso3.get()=="" and datoIngreso4.get()!="":
        comentario.set(F2)
    elif datoIngreso2.get()=="" and datoIngreso3.get()!="" and datoIngreso4.get()=="":
        comentario.set(F2)
    elif datoIngreso2.get()!="" and datoIngreso3.get()=="" and datoIngreso4.get()=="":
        comentario.set(F2)


    elif datoIngreso2.get()!="" and datoIngreso3.get()!="" and datoIngreso4.get()=="":   
        resultado = usd(float(datoIngreso2.get()),float(datoIngreso3.get()))
        datoIngreso4.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_","."))
        comentario.set(F3)

    elif datoIngreso2.get()!="" and datoIngreso3.get()=="" and datoIngreso4.get()!="":
        resultado = pesos(float(datoIngreso2.get()),float(datoIngreso4.get()))
        datoIngreso3.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_","."))
        comentario.set(F3)


    elif datoIngreso2.get()=="" and datoIngreso3.get()!="" and datoIngreso4.get()!="":
        resultado = tasaCambio(float(datoIngreso3.get()),float(datoIngreso4.get()))
        datoIngreso2.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_","."))
        comentario.set(F3)


    else:
        comentario.set(F4)

