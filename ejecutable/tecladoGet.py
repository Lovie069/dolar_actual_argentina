'''https://www.codigopiton.com/detectar-pulsacion-de-tecla-en-python/'''

from pynput import keyboard as kb

'''METODO UNO'''

def pulsa(tecla):
	print('Se ha pulsado la tecla ' + str(tecla))

with kb.Listener(pulsa) as escuchador:
	escuchador.join()
	
# '''METODO DOS'''

# def pulsa(tecla):
# 	print('Se ha pulsado la tecla ' + str(tecla))

# def suelta(tecla):
# 	print('Se ha soltado la tecla ' + str(tecla))

# with kb.Listener(pulsa, suelta) as escuchador:
# 	escuchador.join()

# '''METODO 3'''

# from pynput import keyboard as kb

# def pulsa(tecla):
# 	print('Se ha pulsado la tecla ' + str(tecla))

# def suelta(tecla):
# 	print('Se ha soltado la tecla ' + str(tecla))
# 	if tecla == kb.KeyCode.from_char('q'):
# 		return False

# kb.Listener(pulsa, suelta).run()