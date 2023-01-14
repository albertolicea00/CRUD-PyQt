from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCloseEvent
from PyQt5 import uic
import sys



class MainWindow (QMainWindow):
	def __init__ (self, controler):
		self.__do = controler
		QMainWindow.__init__(self)
		uic.loadUi("view/ui/MainWindow.ui",self)

# ------------------------------------------------------
#			BUTTONS ACTIONS
# ------------------------------------------------------
		self.actmenu_open.triggered.connect(self.__do.File__open)
		self.actmenu_save.triggered.connect(self.__do.File__save)
		self.actmenu_save_as.triggered.connect(self.__do.File__save_as)

		self.actmenu_exit.triggered.connect(self.close)

		self.actmenu_placetolocationCRUD.triggered.connect(self.__do.CRUD__Placetolocation)
		self.actmenu_studentsCRUD.triggered.connect(self.__do.CRUD__Students)
		self.actmenu_seachersCRUD.triggered.connect(self.__do.CRUD__Teachers)

		self.actmenu_average_teachers_per_provinceNdepartament.triggered.connect(self.__do.Search__average_teachers_per_province_and_departament)
		self.actmenu_show_teachers_teaching_category.triggered.connect(self.__do.Search__show_teachers_per_teaching_category)
		self.actmenu_show_older_teacher_address.triggered.connect(self.__do.Search__show_older_teacher_address)
		self.actmenu_count_students_per_provinceNyear.triggered.connect(self.__do.Search__count_students_per_province_and_year)

		self.actmenu_about.triggered.connect(self.__do.Help__about)
		self.actmenu_contact.triggered.connect(self.__do.Help__contact)
		self.actmenu_update.triggered.connect(self.__do.Help__update)
# ******************************************************
#			TABLES
# ******************************************************
		self.table_Student.resizeColumnsToContents()
		self.table_Teacher.resizeColumnsToContents()

		self.table_Student.itemClicked.connect(self.__do.load_StudentForm)
		self.table_Teacher.itemClicked.connect(self.__do.load_TeacherForm)
# ------------------------------------------------------
#			EXIT
# ------------------------------------------------------
	def closeEvent(self, event):
		# Esta funcion ya no es necesaria ya que almacena los datos en una BBDD
		# reply = QMessageBox.question(self,
		# 	 "QUIT", "If you close the main window, all data in the repository will be cleaned\nAre you sure you wanna close the aplication ?",
		# 	QMessageBox.Yes | QMessageBox.No
		# )
		# if reply == QMessageBox.Yes:
		# 	# event.accept() 		# cierra la ventana self
			sys.exit()				# cierratodo el programa 		(el otro metodo mas tosco es un try de cierra para cada una de las ventanas del proyecto)
		# else:
		# 	event.ignore()
		# pass

# ------------------------------------------------------
#			CLEAN
# ------------------------------------------------------
	def clean_StudentTable(self):
		while self.table_Student.rowCount() > 0:
			self.table_Student.removeRow(0)

	def clean_TeacherTable(self):
		while self.table_Teacher.rowCount() > 0:
			self.table_Teacher.removeRow(0)
# ------------------------------------------------------
#			ADD
# ------------------------------------------------------
	def add_StudentTable(self, row, column, text):
		self.table_Student.setItem(row , column , QTableWidgetItem(text))

	def add_TeacherTable(self, row, column, text):
		self.table_Teacher.setItem(row , column , QTableWidgetItem(text))




