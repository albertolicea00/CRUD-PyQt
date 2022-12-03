from unittest import TestCase
from model.studentClass import *

class Student_Test (TestCase):
	std1 = Student ("98010742326" , ["Walter" , "Mendives"] , "Male" , ["Cristo",409, "Camagüey" , "Jimaguayú"] , ["Guantanamo-672" , "This is a little description1..." , False] ,"Informatica" , 1 , 90.90)
	std2 = Student ("97021744529" , ["Daniella" , "Gimenez"] , "Famale" , ["Cielo","15a", "Camagüey" , "Minas"] , ["Guantanamo-672" , "This is a little description2..." , False] ,"Informatica" , 2 , 95.88)
	std3 = Student ("00010947739" , ["Jorge" , "Placeres"] , "Male" , ["Avenida",2499, "Camagüey" , "Camagüey"] , ["Guantanamo-672" , "This is a little description3..." , False] ,"Informatica" , 3 , 56.01)
	
	def test_getters (self):
		self.assertEqual(self.std1.carrer, "Informatica" )
		self.assertEqual(self.std1.year_of_carrer, 1 )
		self.assertEqual(self.std1.average, 90.90 )
		self.assertEqual(self.std1.degree_acttitude, 11.177)

		self.assertEqual(self.std2.carrer, "Informatica" )
		self.assertEqual(self.std2.year_of_carrer, 2  )
		self.assertEqual(self.std2.average, 95.88 )
		self.assertEqual(self.std2.degree_acttitude, 11.0764 )

		self.assertEqual(self.std3.carrer, "Informatica" )
		self.assertEqual(self.std3.year_of_carrer, 3 )
		self.assertEqual(self.std3.average, 56.01 )
		self.assertEqual(self.std3.degree_acttitude, 10.0303 )

	def test_setters (self):
		self.std1.carrer = "Economia"
		self.std1.year_of_carrer = 1
		self.std1.average = 91.00
		self.assertEqual(self.std1.carrer, "Economia" )
		self.assertEqual(self.std1.year_of_carrer, 1 )
		self.assertEqual(self.std1.average, 91.00 )

		self.std2.carrer = "Informatica"
		self.std2.year_of_carrer = 3
		self.std2.average =  96.00
		self.assertEqual(self.std2.carrer, "Informatica" )
		self.assertEqual(self.std2.year_of_carrer, 3 )
		self.assertEqual(self.std2.average, 96.00 )

		self.std3.carrer = "Ciencias de la Informacion"
		self.std3.year_of_carrer = 3
		self.std3.average = 55.00
		self.assertEqual(self.std3.carrer, "Ciencias de la Informacion" )
		self.assertEqual(self.std3.year_of_carrer, 3 )
		self.assertEqual(self.std3.average, 55.00 )