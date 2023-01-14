import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from view.MainWindow import MainWindow

from controller.CRUD__PlacetolocationControler import *
from controller.CRUD__StudentsController	import * 
from controller.CRUD__TeachersController	import *
from controller.Help__aboutController	import * 
from controller.Help__contactController	import * 
from controller.Help__updateController	import * 

from controller.Search__show_teachers_per_teaching_categoryController import * 
from controller.Search__average_teachers_per_province_and_departamentController	import * 
from controller.Search__show_older_teacher_addressController import *
from controller.Search__count_students_per_province_and_yearController	import * 

from model.repository import Repository
from model.repositoryServices import RepositoryService





class mainControler ():
	def __init__ (self):
		self.__repository = Repository()
		self.__repositoryService = RepositoryService(self.__repository)



	def run (self):
		self.__app = QApplication(sys.argv)
		self.__mainview = MainWindow(self)
		self.__mainview.show()

		CRUD__StudentsControler(self.__mainview, self.__repository).load_StudentTable()
		# CRUD__TeachersControler(self.__mainview, self.__repository).load_TeacherTable()

		self.__app.exec()

# ******************************************************
#		CRUD menu
# ******************************************************
	def CRUD__Placetolocation(self):
		self.__view_plc = CRUD__PlacetolocationControler(self.__repository)
		self.__view_plc.run()

	def CRUD__Students(self):
		self.__view_std = CRUD__StudentsControler(self.__mainview, self.__repository) 
		self.__view_std.run()	

	def CRUD__Teachers(self):
		self.__view_tch = CRUD__TeachersControler(self.__mainview, self.__repository)
		self.__view_tch.run()

	# -------------------------------------
	#		Loading tables to CRUDs
	# -------------------------------------
	def load_StudentForm (self):
		try:
			if self.__view_std.view.isVisible() == False:
				self.CRUD__Students()
		except:
			self.CRUD__Students()
		index = self.__mainview.table_Student.currentRow()
		if index != -1:
			value_id = self.__mainview.table_Student.item(index, 0).text()
			value_name = self.__mainview.table_Student.item(index, 2).text()
			value_lastname = self.__mainview.table_Student.item(index, 3).text()
			value_gender = self.__mainview.table_Student.item(index, 4).text()
			# value_leftCuba = self.__mainview.table_Student.item(ind, )			No disponible
			value_carrer = self.__mainview.table_Student.item(index, 6).text()
			value_yearofcarrer = self.__mainview.table_Student.item(index, 7).text()
			value_average = self.__mainview.table_Student.item(index, 8).text()
			value_address_street = self.__mainview.table_Student.item(index, 9).text()
			value_address_number = self.__mainview.table_Student.item(index, 10).text()
			value_address_province = self.__mainview.table_Student.item(index, 11).text()
			value_address_municipality = self.__mainview.table_Student.item(index, 12).text()
			value_place_name = self.__mainview.table_Student.item(index, 13).text()
			value_place_description = self.__mainview.table_Student.item(index, 14).text()
			value_place_inCollege = self.__mainview.table_Student.item(index, 15).text()

			self.__view_std.view.value_id = value_id
			self.__view_std.view.value_name = value_name
			self.__view_std.view.value_lastname = value_lastname
			self.__view_std.view.value_gender = value_gender
			self.__view_std.view.value_carrer = value_carrer
			self.__view_std.view.value_yearofcarrer = int(value_yearofcarrer)
			self.__view_std.view.value_average = float(value_average)
			self.__view_std.view.value_address_street = value_address_street
			self.__view_std.view.value_address_number = value_address_number
			self.__view_std.view.value_address_province = value_address_province
			self.__view_std.view.value_address_municipality = value_address_municipality
			self.__view_std.view.value_place_name = value_place_name
			self.__view_std.view.value_place_description = value_place_description
			self.__view_std.view.value_place_inCollege = value_place_inCollege

	def load_TeacherForm (self):
		try:
			if self.__view_tch.view.isVisible() == False:
				self.CRUD__Teachers()
		except:
			self.CRUD__Teachers()
		index = self.__mainview.table_Teacher.currentRow()
		if index != -1:
			value_id = self.__mainview.table_Teacher.item(index, 0).text()
			value_name = self.__mainview.table_Teacher.item(index, 2).text()
			value_lastname = self.__mainview.table_Teacher.item(index, 3).text()
			value_gender = self.__mainview.table_Teacher.item(index, 4).text()
			
			value_departament = self.__mainview.table_Teacher.item(index, 6).text()
			value_teachingCategory = self.__mainview.table_Teacher.item(index, 7).text()
			value_scientificCategory = self.__mainview.table_Teacher.item(index, 8).text()
			
			value_address_street = self.__mainview.table_Teacher.item(index, 9).text()
			value_address_number = self.__mainview.table_Teacher.item(index, 10).text()
			value_address_province = self.__mainview.table_Teacher.item(index, 11).text()
			value_address_municipality = self.__mainview.table_Teacher.item(index, 12).text()
			value_place_name = self.__mainview.table_Teacher.item(index, 13).text()
			value_place_description = self.__mainview.table_Teacher.item(index, 14).text()
			value_place_inWork = self.__mainview.table_Teacher.item(index, 15).text()
			value_leftCuba = self.__mainview.table_Teacher.item(index, 16).text()
		
			self.__view_tch.view.value_id = value_id
			self.__view_tch.view.value_name = value_name
			self.__view_tch.view.value_lastname = value_lastname
			self.__view_tch.view.value_gender = value_gender
			self.__view_tch.view.value_departament = value_departament
			self.__view_tch.view.value_teachingCategory = value_teachingCategory
			self.__view_tch.view.value_scientificCategory = value_scientificCategory
			self.__view_tch.view.value_address_street = value_address_street
			self.__view_tch.view.value_address_number = value_address_number
			self.__view_tch.view.value_address_province = value_address_province
			self.__view_tch.view.value_address_municipality = value_address_municipality
			self.__view_tch.view.value_place_name = value_place_name
			self.__view_tch.view.value_place_description = value_place_description
			self.__view_tch.view.value_place_inWork = value_place_inWork
			self.__view_tch.view.value_leftCuba = value_leftCuba

# ******************************************************
#		Search menu
# ******************************************************

	def Search__show_teachers_per_teaching_category(self):
		view =  Search__show_teachers_per_teaching_categoryController(self.__repository, self.__repositoryService)
		view.run()

	def Search__average_teachers_per_province_and_departament(self):
		view =  Search__average_teachers_per_province_and_departamentController(self.__repository, self.__repositoryService)
		view.run()

	def Search__show_older_teacher_address(self):
		view =  Search__show_older_teacher_addressController(self.__repository, self.__repositoryService)
		view.run()

	def Search__count_students_per_province_and_year(self):
		view =  Search__count_students_per_province_and_yearController(self.__repository, self.__repositoryService)
		view.run()

# ******************************************************
#		HELP menu
# ******************************************************

	def Help__about(self):
		view = Help__aboutControler()
		view.run()

	def Help__contact(self):
		view = Help__contactControler()
		view.run()

	def Help__update(self):
		view = Help__updateControler()
		view.run()

# ******************************************************
#		IN PROGRESS
# ******************************************************
	def File__open(self):
		QMessageBox.critical(self.__mainview, "Comming soon..." , "In progress, please wait for the next UniDef version")

	def File__save(self):
		QMessageBox.critical(self.__mainview, "Comming soon..." , "In progress, please wait for the next UniDef version")

	def File__save_as(self):
		QMessageBox.critical(self.__mainview, "Comming soon..." , "In progress, please wait for the next UniDef version")