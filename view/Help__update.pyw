from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class menuupdate(QDialog):
	def __init__(self, controler):
		self.__do = controler
		QDialog.__init__(self)
		uic.loadUi("view/ui/Help__update.ui", self)

		self.v1 = 'https://github.com/albertolicea00/CRUD-PyQt/archive/refs/tags/01-28-2022v1.zip'
		self.v2 = 'https://github.com/albertolicea00/CRUD-PyQt/archive/refs/tags/01-28-2023v2.zip'
		self.vz = 'https://github.com/albertolicea00/CRUD-PyQt/archive/refs/heads/main.zip'


# ------------------------------------------------------
#			BUTTONS ACTIONS
# ------------------------------------------------------
		self.btn_v1.clicked.connect(lambda: self.__do.connect_web(self.v1))
		self.btn_v2.clicked.connect(lambda: self.__do.connect_web(self.v2))
		self.btn_vz.clicked.connect(lambda: self.__do.connect_web(self.vz))
