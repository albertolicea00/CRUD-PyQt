
from view.Help__update import about


class Help__updateControler ():
	def __init__ (self):
		pass

	def run (self):
		self.__view = about()
		
		self.__view.show()
		self.__view.exec()