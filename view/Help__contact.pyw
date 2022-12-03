from PyQt5.QtWidgets import QDialog
from PyQt5 import uic



class menu_contact(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("view/ui/Help__contact.ui",self)
		