from PyQt5.QtWidgets import QTableWidgetItem
from view.CRUD__Students import menu_crudStudent
from model.studentClass import Student 

class CRUD__StudentsControler ():
	def __init__ (self, tableStudent , repository):
		self.__table = tableStudent 
		self.__repository = repository

	@property
	def view (self):
		return self.__view

	def run (self):
		try:
			self.__table.Table.setCurrentIndex(0)
			self.__view = menu_crudStudent(self)
			self.assigPlaces() 
			self.__validateOpen()
			self.__view.show()
		except Exception as e:
			self.__view.showError(e.args[0])
# ------------------------------------------------------   
#			CRUD
# ------------------------------------------------------
	def insertStudent (self):
		try :
			self.__view.validateForm()
			value_id = self.__view.value_id
			value_name = self.__view.value_name
			value_lastname = self.__view.value_lastname
			value_gender = self.__view.value_gender
			# value_leftCuba = self.__view.value_leftCuba			No disponible 
			value_address_street = self.__view.value_address_street
			value_address_number = self.__view.value_address_number
			value_address_province = self.__view.value_address_province
			value_address_municipality = self.__view.value_address_municipality
			value_place_name = self.__view.value_place_name
			value_place_description = self.__view.value_place_description
			value_place_inCollege = self.__view.value_place_inCollege
			value_carrer = self.__view.value_carrer
			value_yearofcarrer = self.__view.value_yearofcarrer
			value_average = self.__view.value_average

			std = Student (value_id, 
					[value_name, value_lastname], 
					value_gender,
					[value_address_street, value_address_number, value_address_province, value_address_municipality],
					[value_place_name ,	value_place_description , value_place_inCollege],
					value_carrer,
					value_yearofcarrer,
					value_average
			)

			self.__repository.insertStudent( std )
			self.__table.Table.setCurrentIndex(0)
			self.load_StudentTable()
			self.__view.cleanForm()
		except Exception as e:
			self.__view.showError(e.args[0])
			
	def updateStudent (self):
		index = self.__table.table_Student.currentRow()
		try:
			if index == -1: 
				raise Exception("Must be select a student to update")
			old_std_ID = self.__table.table_Student.item(index, 0).text()

			self.__view.validateForm()
			value_id = self.__view.value_id
			value_name = self.__view.value_name
			value_lastname = self.__view.value_lastname
			value_gender = self.__view.value_gender
			# value_leftCuba = self.__view.value_leftCuba			No disponible 
			value_address_street = self.__view.value_address_street
			value_address_number = self.__view.value_address_number
			value_address_province = self.__view.value_address_province
			value_address_municipality = self.__view.value_address_municipality
			value_place_name = self.__view.value_place_name
			value_place_description = self.__view.value_place_description
			value_place_inCollege = self.__view.value_place_inCollege
			value_carrer = self.__view.value_carrer
			value_yearofcarrer = self.__view.value_yearofcarrer
			value_average = self.__view.value_average

			new_std = Student (value_id, 
					[value_name, value_lastname], 
					value_gender,
					[value_address_street, value_address_number, value_address_province, value_address_municipality],
					[value_place_name ,	value_place_description , value_place_inCollege],
					value_carrer,
					value_yearofcarrer,
					value_average)
			self.__repository.updateStudent(old_std_ID, new_std)
			self.__table.Table.setCurrentIndex(0)
			self.load_StudentTable()		
			self.__view.cleanForm()
		except Exception as e:
			self.__view.showError(e.args[0])

	def deleteStudent (self):
		try:
			index = self.__table.table_Student.currentRow()
			if index == -1:
				raise Exception("Must be select a file to update")
			std_ID = self.__table.table_Student.item(index, 0).text()

			self.__repository.removeStudent( std_ID )
			self.__table.Table.setCurrentIndex(0)
			self.load_StudentTable()
			self.__view.cleanForm()

		except Exception as e:
			self.__view.showError(e.args[0])

# ------------------------------------------------------   
#			Load Table
# ------------------------------------------------------
	def load_StudentTable (self):
		self.__table.clean_StudentTable()
		for std in self.__repository.Students:
			
			place_in_university = "No"
			if std.place_to_location.place_in_university:
				place_in_university = "Yes"
			
			i = self.__table.table_Student.rowCount()
			self.__table.table_Student.insertRow(i)
			 
			self.__table.add_StudentTable(i, 0, std.ID)
			self.__table.add_StudentTable(i, 1, str(std.degree_acttitude))
			self.__table.add_StudentTable(i, 2, std.fullname.name)
			self.__table.add_StudentTable(i, 3, std.fullname.last_name)
			self.__table.add_StudentTable(i, 4, std.gender)
			self.__table.add_StudentTable(i, 5, f"{std.birthday.day}-{std.birthday.month}-{std.birthday.year}")
			self.__table.add_StudentTable(i, 6, str(std.carrer))
			self.__table.add_StudentTable(i, 7, str(std.year_of_carrer))
			self.__table.add_StudentTable(i, 8, str(std.average))
			self.__table.add_StudentTable(i, 9, std.address.address_street) 
			self.__table.add_StudentTable(i, 10, str(std.address.address_number))
			self.__table.add_StudentTable(i, 11, std.address.address_province)
			self.__table.add_StudentTable(i, 12, std.address.address_municipality)
			self.__table.add_StudentTable(i, 13, std.place_to_location.place_name)
			self.__table.add_StudentTable(i, 14, std.place_to_location.place_description)
			self.__table.add_StudentTable(i, 15, place_in_university)
		self.__table.table_Student.resizeColumnsToContents()

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
		self.__view.value_place_inCollege = self.__repository.Places[index].place_in_university
# ------------------------------------------------------
#			VALIDATIONS 
# ------------------------------------------------------
	def __validateOpen (self):
		if self.__view.value_place_name == "":
			raise Exception("You must input a Place to Location before any Student") 
