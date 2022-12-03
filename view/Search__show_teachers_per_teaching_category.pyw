from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic



class Search__show_teachers_per_teaching_category(QDialog):
	def __init__(self, controler):
		self.__do = controler
		QDialog.__init__(self)
		uic.loadUi("view/ui/Search__show_teachers_per_teaching_category.ui",self)

# -----------------------------------------------------------------------------------------------
#			Declarando las acciones para los botones 
# ----------------------------------------------------------------------------------------------
		self.btn_search.clicked.connect(self.__do.search)
		self.btn_cancel.clicked.connect(self.close)
# ------------------------------------------------------
#			GETTERS 
# ------------------------------------------------------
	@property
	def value_teaching_category (self):
		return self.box_teaching_category.currentText()	
# ------------------------------------------------------
#			SETTERS  
# ------------------------------------------------------
	@value_teaching_category.setter
	def value_teaching_category (self, value):
		self.box_teaching_category.setCurrentText(value)
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