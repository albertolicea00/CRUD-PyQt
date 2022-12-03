from PyQt5.QtWidgets import QTableWidgetItem
from view.CRUD__Teachers import menu_crudTeacher
from model.teacherClass import Teacher

class CRUD__TeachersControler ():
	def __init__ (self, tableTeacher, repository):
		self.__table = tableTeacher 
		self.__repository = repository

	@property
	def view (self):
		return self.__view

	def run (self):
		try:
			self.__table.Table.setCurrentIndex(1)
			self.__view = menu_crudTeacher(self)
			self.assigPlaces() 
			self.__validatePlace()
			self.__view.show()
		except Exception as e:
			self.__view.showError(e.args[0])
# ------------------------------------------------------   
#			CRUD
# ------------------------------------------------------
	def insertTeacher (self):
		try :
			self.__view.validateForm()
			value_id = self.__view.value_id
			value_name = self.__view.value_name
			value_lastname = self.__view.value_lastname
			value_gender = self.__view.value_gender
			value_leftCuba = self.__view.value_leftCuba
			value_address_street = self.__view.value_address_street
			value_address_number = self.__view.value_address_number
			value_address_province = self.__view.value_address_province
			value_address_municipality = self.__view.value_address_municipality
			value_place_name = self.__view.value_place_name
			value_place_description = self.__view.value_place_description
			value_place_inWork = self.__view.value_place_inWork
			value_departament = self.__view.value_departament
			value_teachingCategory = self.__view.value_teachingCategory
			value_scientificCategory = self.__view.value_scientificCategory

			tch = Teacher(value_id, 
						[value_name, value_lastname], 
						value_gender,
						[value_address_street, value_address_number, value_address_province, value_address_municipality],
						[value_place_name ,	value_place_description , value_place_inWork],
						
						value_departament,
						value_leftCuba,
						value_teachingCategory,
						value_scientificCategory)

			self.__repository.insertTeacher(tch)
			self.__table.Table.setCurrentIndex(1)
			self.load_TeacherTable()
			self.__view.cleanForm()
		except Exception as e:
			self.__view.showError(e.args[0])

	def updateTeacher (self):
		try :
			index = self.__table.table_Teacher.currentRow()
			if index == -1: 
				raise Exception("Must be select a teacher to update")
			old_tch_ID = self.__table.table_Teacher.item(index, 0).text()

			self.__view.validateForm()
			value_id = self.__view.value_id
			value_name = self.__view.value_name
			value_lastname = self.__view.value_lastname
			value_gender = self.__view.value_gender
			value_leftCuba = self.__view.value_leftCuba
			value_address_street = self.__view.value_address_street
			value_address_number = self.__view.value_address_number
			value_address_province = self.__view.value_address_province
			value_address_municipality = self.__view.value_address_municipality
			value_place_name = self.__view.value_place_name
			value_place_description = self.__view.value_place_description
			value_place_inWork = self.__view.value_place_inWork
			value_departament = self.__view.value_departament
			value_teachingCategory = self.__view.value_teachingCategory
			value_scientificCategory = self.__view.value_scientificCategory

			new_tch = Teacher(value_id, 
						[value_name, value_lastname], 
						value_gender,
						[value_address_street, value_address_number, value_address_province, value_address_municipality],
						[value_place_name ,	value_place_description , value_place_inWork],
						
						value_departament,
						value_leftCuba,
						value_teachingCategory,
						value_scientificCategory)
			
			self.__repository.updateTeacher(old_tch_ID , new_tch)
			self.__table.Table.setCurrentIndex(1)
			self.load_TeacherTable()
			self.__view.cleanForm()
		except Exception as e:
			self.__view.showError(e.args[0])

	def deleteTeacher (self):
		try:
			index = self.__table.table_Teacher.currentRow()
			if index == -1:
				raise Exception("Must be select a teacher to delete")
			tch_ID = self.__table.table_Teacher.item(index, 0).text()

			self.__repository.removeTeacher( tch_ID )
			self.__table.Table.setCurrentIndex(1)
			self.load_TeacherTable()
			self.__view.cleanForm()

		except Exception as e:
			self.__view.showError(e.args[0])
# ------------------------------------------------------   
#			Load Table
# ------------------------------------------------------
	def load_TeacherTable (self):
		self.__table.clean_TeacherTable()
		for tch in self.__repository.Teachers:

			left_cuba = "No"
			place_in_university = "No"
			if tch.left_cuba:
				left_cuba = "Yes" 
			if tch.place_to_location.place_in_university:
				place_in_university = "Yes"
			
			i = self.__table.table_Teacher.rowCount()
			self.__table.table_Teacher.insertRow(i)
 
			self.__table.add_TeacherTable(i, 0, tch.ID)
			self.__table.add_TeacherTable(i, 1, str(tch.degree_acttitude))
			self.__table.add_TeacherTable(i, 2, tch.fullname.name)
			self.__table.add_TeacherTable(i, 3, tch.fullname.last_name)
			self.__table.add_TeacherTable(i, 4, tch.gender)
			self.__table.add_TeacherTable(i, 5,  f"{tch.birthday.day}-{tch.birthday.month}-{tch.birthday.year}")
			self.__table.add_TeacherTable(i, 6, tch.departament)
			self.__table.add_TeacherTable(i, 7, tch.teaching_category)
			self.__table.add_TeacherTable(i, 8, tch.scientific_category)
			self.__table.add_TeacherTable(i, 9, tch.address.address_street) 
			self.__table.add_TeacherTable(i, 10, str(tch.address.address_number))
			self.__table.add_TeacherTable(i, 11, tch.address.address_province)
			self.__table.add_TeacherTable(i, 12, tch.address.address_municipality)
			self.__table.add_TeacherTable(i, 13, tch.place_to_location.place_name)
			self.__table.add_TeacherTable(i, 14, tch.place_to_location.place_description)
			self.__table.add_TeacherTable(i, 15, place_in_university)
			self.__table.add_TeacherTable(i, 16, left_cuba)
		self.__table.table_Teacher.resizeColumnsToContents()

# ------------------------------------------------------   
#			Load Places
# ------------------------------------------------------
	def assigPlaces (self):
		for i in range(len(self.__repository.Places)):
			place_name = self.__repository.Places[i].place_name
			self.__view.box_place_name.addItem(str(place_name))
	
	def loadingPlaces (self, opt):
		index = self.__repository.indexPlace(opt)
		self.__view.value_place_description = self.__repository.Places[index].place_description
		self.__view.value_place_inWork = self.__repository.Places[index].place_in_university
# ------------------------------------------------------
#			VALIDATIONS 
# ------------------------------------------------------
	def __validatePlace (self):
		if self.__view.value_place_name == "":
			raise Exception("You must input a Place to Location before any Teacher") 
