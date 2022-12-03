from unittest import TestCase
from model.teacherClass import *

class Teacher_Test (TestCase):
	tch1 = Teacher ("81090912312" , ["Roberto","Lopez"] , "Male"   , ["Hospital", "5A", "Camagüey", "Camagüey"] , ["RTA56", "This is a little description3..." , True] , "Veterinaria", False , "Auxiliar Docente"  , "Master of Science")
	tch2 = Teacher ("97010465789" , ["Sonia" ,"Dias"]   , "Famale" , ["San Clemente", 326 , "Camagüey" , "Camagüey"] , ["UID-72" , "This is a little description2..." , False] ,"Ciencias Aplicadas" , False , "Instructor" , "Doctor")
	tch3 = Teacher ("70010957241" , ["Jessica" ,"Alba"] , "Famale" , ["San Patricio", 76 , "Camagüey" , "Florida"] , ["Guantanamo-672" , "This is a little description3..." , False] ,"Ciencias Informaticas" , True , "Auxiliar" , "None")

	def test_getters (self):
		self.assertEqual(self.tch1.departament, "Veterinaria" )
		self.assertEqual(self.tch1.left_cuba, False )
		self.assertEqual(self.tch1.teaching_category, "Auxiliar Docente" )
		self.assertEqual(self.tch1.scientific_category, "Master of Science" )
		self.assertEqual(self.tch1.degree_acttitude, 6.0 )

		self.assertEqual(self.tch2.departament, "Ciencias Aplicadas" )
		self.assertEqual(self.tch2.left_cuba, False )
		self.assertEqual(self.tch2.teaching_category, "Instructor"  )
		self.assertEqual(self.tch2.scientific_category, "Doctor" )
		self.assertEqual(self.tch2.degree_acttitude, 7.5 )

		self.assertEqual(self.tch3.departament, "Ciencias Informaticas" )
		self.assertEqual(self.tch3.left_cuba, True )
		self.assertEqual(self.tch3.teaching_category, "Auxiliar" )
		self.assertEqual(self.tch3.scientific_category, "None" )
		self.assertEqual(self.tch3.degree_acttitude, 8.8 )

	def test_setters (self):
		self.tch1.departament = "Ciencias Informaticas"
		self.tch1.left_cuba = True
		self.tch1.teaching_category = "Auxiliary"
		self.tch1.scientific_category = "Ninguna"
		self.assertEqual(self.tch1.departament, "Ciencias Informaticas" )
		self.assertEqual(self.tch1.left_cuba, True )
		self.assertEqual(self.tch1.teaching_category, "Auxiliary" )
		self.assertEqual(self.tch1.scientific_category, "Ninguna" )

		self.tch2.departament = "Ciencias Economicas"
		self.tch2.left_cuba = False
		self.tch2.teaching_category = "Auxiliary"
		self.tch2.scientific_category = "Master"
		self.assertEqual(self.tch2.departament, "Ciencias Economicas" )
		self.assertEqual(self.tch2.left_cuba, False )
		self.assertEqual(self.tch2.teaching_category, "Auxiliary" )
		self.assertEqual(self.tch2.scientific_category, "Master" )

		self.tch3.departament = "Ciencias Informaticas"
		self.tch3.left_cuba = True
		self.tch3.teaching_category = "Assistant"
		self.tch3.scientific_category = "Master of Science"
		self.assertEqual(self.tch3.departament, "Ciencias Informaticas" )
		self.assertEqual(self.tch3.left_cuba, True )
		self.assertEqual(self.tch3.teaching_category, "Assistant" )
		self.assertEqual(self.tch3.scientific_category, "Master of Science" )