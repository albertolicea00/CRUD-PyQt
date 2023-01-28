from view.Help__update import menuupdate
from model.extraServices import extraService

class Help__updateControler ():
	def __init__ (self):
		pass

	def run (self):
		self.__view = menuupdate(self)
		self.__view.show()
		self.__view.exec()

	def connect_web(self, url):
		extraService.openWeb(url)