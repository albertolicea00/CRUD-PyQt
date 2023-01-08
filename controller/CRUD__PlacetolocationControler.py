from PyQt5.QtWidgets import QTableWidgetItem
from view.CRUD__Placetolocation import menu_crudPlacetolocation
from model.util.placetolocationClass import Place_to_location 

class CRUD__PlacetolocationControler ():
	def __init__ (self , repository):
		self.__repository = repository

	def run (self):
		self.__view = menu_crudPlacetolocation(self)
		self.load_PlacetolocationTable()
		self.__view.show()

# ------------------------------------------------------   
#			CRUD
# ------------------------------------------------------
	def insertPlace (self):
		try :
			self.__view.validateForm()
			value_place_name = self.__view.value_place_name
			value_place_description = self.__view.value_place_description
			value_place_inUniversity = self.__view.value_place_inUniversity

			plc = Place_to_location ([	value_place_name ,
										value_place_description ,
										value_place_inUniversity  ]
			)

			self.__repository.insertPlace( plc )
			self.load_PlacetolocationTable()
			self.__view.cleanForm()
		except Exception as e:
			self.__view.showError(e.args[0])

	def updatePlace (self):
		index = self.__view.tablePlacetolocation.currentRow()
		try:
			if index == -1: 
				raise Exception("Must be select a place to update")
			old_plc_ID = self.__view.tablePlacetolocation.item(index, 0).text()

			self.__view.validateForm()
			value_place_name = self.__view.value_place_name
			value_place_description = self.__view.value_place_description
			value_place_inUniversity = self.__view.value_place_inUniversity
			new_plc = Place_to_location (	[value_place_name ,
											value_place_description ,
											value_place_inUniversity]
			)

			self.__repository.updatePlace(old_plc_ID, new_plc)
			self.load_PlacetolocationTable()
			self.__view.cleanForm()
		except Exception as e:
			self.__view.showError(e.args[0])

	def deletePlace (self):
		try:
			index = self.__view.tablePlacetolocation.currentRow()
			if index == -1:
				raise Exception("Must be select a place to delete")
			plc_ID = self.__view.tablePlacetolocation.item(index, 0).text()

			self.__repository.removePlace( plc_ID )
			self.load_PlacetolocationTable()
			self.__view.cleanForm()

		except Exception as e:
			self.__view.showError(e.args[0])


# ------------------------------------------------------   
#			Load Table
# ------------------------------------------------------
	def load_PlacetolocationTable (self):
		self.__view.clean_PlacetolocationTable()
		for q in self.__repository.Places:

			plc = Place_to_location([q[1], q[2], q[3]])

			in_university = "No"
			if plc.place_in_university:
				in_university = "Yes"

			i = self.__view.tablePlacetolocation.rowCount()
			self.__view.tablePlacetolocation.insertRow(i)
			 
			self.__view.add_PlaceTable(i, 0, plc.place_name)
			self.__view.add_PlaceTable(i, 1, in_university)
			self.__view.add_PlaceTable(i, 2, plc.place_description)

		self.__view.tablePlacetolocation.resizeColumnsToContents()
# ------------------------------------------------------   
#			Load Form
# ------------------------------------------------------
	def load_PlacetolocationForm (self):
		index = self.__view.tablePlacetolocation.currentRow()

		if index != -1:
			value_place_name = self.__view.tablePlacetolocation.item(index, 0).text()
			value_place_inUniversity = self.__view.tablePlacetolocation.item(index, 1).text()
			value_place_description = self.__view.tablePlacetolocation.item(index, 2).text()
			self.__view.value_place_name = value_place_name
			self.__view.value_place_description = value_place_description
			self.__view.value_place_inUniversity = value_place_inUniversity
			