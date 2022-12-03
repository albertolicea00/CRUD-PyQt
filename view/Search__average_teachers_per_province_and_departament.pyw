from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic



class Search__average_teachers_per_province_and_departament(QDialog):
	def __init__(self, controler):
		self.__do = controler
		QDialog.__init__(self)
		uic.loadUi("view/ui/Search__average_teachers_per_province_and_departament.ui",self)
# -----------------------------------------------------------------------------------------------
#			Declarando las acciones para los botones 
# ----------------------------------------------------------------------------------------------
		self.btn_search.clicked.connect(self.__do.search)
		self.btn_cancel.clicked.connect(self.close)

		self.box_province.currentTextChanged.connect(self.__do.assigOption2)
		# self.box_departament.currentTextChanged.connect(self.__do.assigOption3)	o assigOption1 con parametro de ("province" , "departament") por si queria hacerlo vicebersa 	*pero seria un lio terrible (es una idea)
# ------------------------------------------------------
#			GETTERS 
# ------------------------------------------------------
	@property
	def value_province (self):
		return self.box_province.currentText()

	@property
	def value_departament (self):
		return self.box_departament.currentText()		
# ------------------------------------------------------
#			SETTERS  
# ------------------------------------------------------
	@value_province.setter
	def value_province (self, value):
		box_province.setCurrentText(value)

	@value_departament.setter
	def value_departament (self, value):
		box_departament.setCurrentText(value)
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