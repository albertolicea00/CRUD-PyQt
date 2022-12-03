from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic



# la idea era hacerlo con una pantalla LCD (oculta) con un id personal para que al asignarle un lugar a una persona se disminuyan la cantidad de plazas de dicho lugar
# tambian habria que crear un atributo de plazas a las ubicaciones  
class menu_crudPlacetolocation(QWidget):
	def __init__(self, controler):
		self.__do = controler
		QWidget.__init__(self)
		uic.loadUi("view/ui/CRUD__Placetolocation.ui",self)
		self.cleanForm()
		self.__validateUI()

		self.tablePlacetolocation.itemClicked.connect(self.__do.load_PlacetolocationForm)
# ------------------------------------------------------
#			BUTTONS ACTIONS
# ------------------------------------------------------
		self.btn_insert.clicked.connect(self.__do.insertPlace)
		self.btn_update.clicked.connect(self.__do.updatePlace)
		self.btn_delete.clicked.connect(self.__do.deletePlace)
		self.btn_cancel.clicked.connect(self.close)
# ------------------------------------------------------
#				GETTERS 
# ------------------------------------------------------
	@property
	def value_place_name (self):
		return self.txt_place_name.text().strip()

	@property
	def value_place_description (self):
		return self.txt_place_description.toPlainText()

	@property
	def value_place_inUniversity (self):
		return self.cbtn_place_inUiversity.isChecked() 
# ------------------------------------------------------
#				SETTERS  
# ------------------------------------------------------

	@value_place_name.setter
	def value_place_name (self, value):
		self.txt_place_name.setText(value)

	@value_place_description.setter
	def value_place_description (self, value):
		self.txt_place_description.setPlainText(value)

	@value_place_inUniversity.setter
	def value_place_inUniversity (self, value):
		if value == "Yes":
			value = True
		if value == "No":
			value = False
		self.cbtn_place_inUiversity.setChecked(value)

# ------------------------------------------------------
#			CLEAN
# ------------------------------------------------------
	def cleanForm (self):
		self.value_place_name = ''
		self.value_place_description = ''
		self.value_place_inUniversity = False
# ------------------------------------------------------   
#			ERROR
# ------------------------------------------------------
	def showError(self, msg):
		QMessageBox.critical(self, "Error", msg)
# ------------------------------------------------------
#			VALIDATIONS 
# ------------------------------------------------------
	def validateForm (self):
		self.__validateEmptys()

	def __validateUI(self):
		pass
		# validar el id_number o hacer una operacion automatica (con otro metodo) para que se aumente en 1 el LCD_id_number 
		# 		y asi luego de esto  cuando valla a llamar al nombre de un place to location
		# que me salga en el comboBox Students y Teachers "{id_number} - {name_place}" para cada uno de los lugares existentes


	def __validateEmptys (self):
		msg = "The {} value is necesary"

		if len(self.value_place_name) == 0:
			raise Exception (msg.format("place_name"))
		# if len(self.txt_place_description) == 0:
		# 	raise Exception (msg.format("place_name"))



	def clean_PlacetolocationTable(self):
		while self.tablePlacetolocation.rowCount() > 0:
			self.tablePlacetolocation.removeRow(0)

	def add_PlaceTable(self, fila, columna, texto):
		self.tablePlacetolocation.setItem(fila, columna, QTableWidgetItem(texto))

