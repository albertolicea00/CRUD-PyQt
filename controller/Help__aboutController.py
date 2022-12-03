
from view.Help__about import menu_about


class Help__aboutControler ():
	def __init__ (self):
		pass

	def run (self):
		self.__view = menu_about()
		
		self.__view.show()
		self.__view.exec()