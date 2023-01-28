from view.Help__contact import menu_contact
from model.extraServices import extraService

class Help__contactControler ():
	def __init__ (self):
		pass

	def run (self):
		self.__view = menu_contact(self)
		
		self.__view.show()
		self.__view.exec()

	def connect_web(self, url):
		extraService.openWeb(url)
