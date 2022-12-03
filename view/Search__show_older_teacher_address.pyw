from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic



class Search__show_older_teacher_address(QDialog):
	def __init__(self, controler):
		self.__do = controler
		QDialog.__init__(self)
		uic.loadUi("view/ui/Search__show_older_teacher_address.ui",self)	
# -----------------------------------------------------------------------------------------------
#			Declarando las acciones para los botones 
# ----------------------------------------------------------------------------------------------
		self.btn_search.clicked.connect(self.__do.search)
		self.btn_cancel.clicked.connect(self.close)

		self.box_province.currentTextChanged.connect(self.__do.assigOption2)
# ------------------------------------------------------
#			GETTERS 
# ------------------------------------------------------
	@property
	def value_province (self):
		return self.box_province.currentText()

	@property
	def value_municipality (self):
		return self.box_municipality.currentText()		
# ------------------------------------------------------
#			SETTERS  
# ------------------------------------------------------
	@value_province.setter
	def value_province (self, value):
		box_province.setCurrentText(value)

	@value_municipality.setter
	def value_municipality (self, value):
		box_municipality.setCurrentText(value)
# ------------------------------------------------------   
# 			RESULT
# ------------------------------------------------------
	def showResult(self, msg):
		QMessageBox.information(self, "Found", msg)
# ------------------------------------------------------   
			# ERROR
# ------------------------------------------------------
	def showError(self, msg):
		QMessageBox.critical(self, "Error", msg)