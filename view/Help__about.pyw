from PyQt5.QtWidgets import QDialog
from PyQt5 import uic



class menu_about(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi('view/ui/Help__about.ui',self)
		