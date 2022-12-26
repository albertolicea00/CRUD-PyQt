from controller.MainController import *
from testing.model_main_test import *


# Hay muchos comentarios que nada tienen que ver con el funcionamiento de la app
#	mas bien son idean random que surguieron en su momento, para mejorar la app 	
#					(que algunas quedaron como una utopia y otras ya que sustituyeron por algo mejor)


if __name__ == "__main__":
	# test = Testing()
	# test.start()
	# app = mainControler ()
	# app.run()
	pass
	
# -----------------------------------------
# 		TO DO (Extra) :
# -----------------------------------------
# -	comentar cada cosa en el codigo, faltan la vista y el controlador ->> pruebas doctest
# + modificar y obtimizar el funcionamiento de buscar al profesor mas viejo (Enves de un bucle for anidado: (la longitud) que solo compruebe con el primer elemento (para en caso de que hallan 10 o 20 peronas iguales, ahorrar memoria y tiempo de ejecucion) )
# + hacer que la vista de las operaciones tengan un values  para devolver una lista 
# 	y que en el controlador no tenga que utilizar el elemento directamente del ui 	
# 	(luego revisar y arreglar el assigOption con una logica diferente y mas privada)
# + areglar el checkBox de en la universidad, estudiantes y profesores, en la vista (ir al comentario)
# + agregar una funcionalidad de primera ejecucion o how do i do it 
# 	(tips para usar la app) que se cargan dentro del menu de diapositivas en un about (como usar la app),  
# 	(los eventos de los tips se cargan (por un btn en un label (con el cursor en ?mode) )  
# 	escogiendo, visualiza el tip1, tip2....)
# + agregar las funcionalidades del about 
# + poner un disegno a los widgets
# + poner un btn de modo obscuro 
# 	(concatenarlo con un modulo que cambia toda los stylesheet) o 
# 	(con condicionales si la variable darkmode is True or not)
# + las funcionalidades para guardar y cargar las tablas a 
# (bbdd o ficheros externos sin extencion)
