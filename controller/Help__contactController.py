
from view.Help__contact import menu_contact


class Help__contactControler ():
	def __init__ (self):
		pass

	def run (self):
		self.__view = menu_contact()
		
		self.__view.show()
		self.__view.exec()