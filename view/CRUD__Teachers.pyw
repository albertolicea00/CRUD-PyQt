from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from model.util.CubaProvinces.mainQt import *


class menu_crudTeacher(QWidget):
	def __init__(self, controler):
		self.__do = controler
		QWidget.__init__(self)
		uic.loadUi("view/ui/CRUD__Teachers.ui",self)
		self.cleanForm()
		self.__validateUI()	
# ------------------------------------------------------
#		GROUPING PROVINCES PER MUNICIPAYS
# ------------------------------------------------------
		self.groupCubaProvinces = CubaProvinces_BoxGroup(provinceBox=self.box_address_province , municipalyBox=self.box_address_municipality)
		self.groupCubaProvinces.exec_()
# ------------------------------------------------------
#			BUTTONS ACTIONS
# ------------------------------------------------------
		self.btn_insert.clicked.connect(self.__do.insertTeacher)
		self.btn_update.clicked.connect(self.__do.updateTeacher)
		self.btn_delete.clicked.connect(self.__do.deleteTeacher)
		self.btn_cancel.clicked.connect(self.close)

		self.box_place_name.currentTextChanged.connect(self.__do.loadingPlaces)
# ------------------------------------------------------
#				GETTERS 
# ------------------------------------------------------
	@property
	def value_id (self):
		return self.txt_ID.text().strip()	

	@property
	def value_name (self):
		return self.txt_name.text().strip()

	@property
	def value_lastname (self):
		return self.txt_lastname.text().strip()

	@property
	def value_gender (self):
		if self.rbtn_male.isChecked():
			gender = "Male"
		elif self.rbtn_famale.isChecked():
			gender = "Famale"
		else:					# self.rbtn_other.isChecked():
			gender = "Other" 
		return gender

	@property
	def value_leftCuba (self):
		return self.cbtn_leftCuba.isChecked()

	@property
	def value_address_street (self):
		return self.txt_address_street.text().strip()

	@property
	def value_address_number (self):
		return self.txt_address_number.text().strip()

	@property
	def value_address_province (self):
		return self.box_address_province.currentText()

	@property
	def value_address_municipality (self):
		return self.box_address_municipality.currentText()

	@property
	def value_place_name (self):
		return self.box_place_name.currentText()

	@property
	def value_place_description (self):
		return self.txt_place_description.toPlainText()

	@property
	def value_place_inWork (self):
		return self.cbtn_place_inUiversity.isChecked()

	@property
	def value_departament (self):
		return self.txt_departament.text().strip()

	@property
	def value_teachingCategory (self):
		return self.box_teaching_category.currentText()

	@property
	def value_scientificCategory (self):
		return self.box_scientific_category.currentText()

# ------------------------------------------------------
#				SETTERS  
# ------------------------------------------------------
	@value_id.setter
	def value_id (self, value):
		self.txt_ID.setText(value)

	@value_name.setter
	def value_name (self, value):
		self.txt_name.setText(value)

	@value_lastname.setter
	def value_lastname (self, value):
		self.txt_lastname.setText(value)

	@value_gender.setter
	def value_gender (self, value):
		if value == "Male":
			self.rbtn_male.setChecked(True)
		elif value == "Famale":
			self.rbtn_famale.setChecked(True)
		else:					#value == "Other"
			self.rbtn_other.setChecked(True)

	@value_leftCuba.setter
	def value_leftCuba (self, value):
		if value == "Yes":
			value = True
		elif value == "No":
			value = False
		self.cbtn_leftCuba.setChecked(value)

	@value_address_street.setter
	def value_address_street (self, value):
		self.txt_address_street.setText(value)

	@value_address_number.setter
	def value_address_number (self, value):
		self.txt_address_number.setText(value)

	@value_address_province.setter
	def value_address_province (self, value):
		self.box_address_province.setCurrentText(value) 

	@value_address_municipality.setter
	def value_address_municipality (self, value):
		self.box_address_municipality.setCurrentText(value) 

	@value_place_name.setter
	def value_place_name (self, value):
		self.box_place_name.setCurrentText(value)

	@value_place_description.setter
	def value_place_description (self, value):
		self.txt_place_description.setPlainText(value)

	@value_place_inWork.setter
	def value_place_inWork (self, value):
		if value == "Yes":
			value = True
		elif value == "No":
			value = False
		self.cbtn_place_inUiversity.setCheckable(True)
		self.cbtn_place_inUiversity.setChecked(value)
		# self.cbtn_place_inUiversity.setCheckable(False)	yo queria este y no el enable para mas estetico, pero al ponerlo de esta forma impide ingresarle contenido al chbox
		self.cbtn_place_inUiversity.setEnabled(False)


	@value_departament.setter
	def value_departament (self, value):
		self.txt_departament.setText(value)

	@value_teachingCategory.setter
	def value_teachingCategory (self, value):
		self.box_teaching_category.setCurrentText(value)

	@value_scientificCategory.setter
	def value_scientificCategory (self, value):
		self.box_scientific_category.setCurrentText(value)

# ------------------------------------------------------
#			CLEAN
# ------------------------------------------------------
	def cleanForm (self):
		self.value_id = ''
		self.value_name = ''
		self.value_lastname = ''
		self.value_gender = 'Male'
		self.value_leftCuba = False
		self.value_address_street = ''
		self.value_address_number = ''
		self.value_address_province = 'Isla de la Juventud**'
		self.value_address_municipality = 'Nueva Gerona'
		# self.value_place_name = ''
		# self.value_place_description = ''
		# self.value_place_inCollege = False
		self.value_departament = ''
		self.value_teachingCategory = 'Titular'
		self.value_scientificCategory = 'None'
# ------------------------------------------------------   
#			ERROR
# ------------------------------------------------------
	def showError(self, msg):
		QMessageBox.critical(self, "Error", msg)
# ------------------------------------------------------
#			VALIDATIONS 
# ------------------------------------------------------
# no necesito tantas validaciones ya que valide bastante en el modelo
	def validateForm (self):
		self.__validateEmptys()
		# try :
		# 	int(self.value_address_number) 
		# except:	
		# 	raise Exception("The address number format must be a number")


	def __validateUI(self):
		pass

	def __validateEmptys (self):
		msg = "The {} value is necesary"
		if len(self.value_id) == 0:
			raise Exception (msg.format("id")) 
		if len(self.value_name) == 0:
			raise Exception (msg.format("name")) 
		if len(self.value_lastname) == 0:
			raise Exception (msg.format("lastname")) 
		if len(self.value_address_street) == 0:
			raise Exception (msg.format("address_street")) 
		if len(self.value_address_number) == 0:
			raise Exception (msg.format("address_number")) 
		if len(self.value_departament) == 0:
			raise Exception (msg.format("carrer")) 

		if self.box_place_name.count() == 0:
			raise Exception ("You must input a Place to Location before any Teacher") 