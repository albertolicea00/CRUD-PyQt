from unittest import TestCase
from model.studentClass import *
from model.teacherClass import *
from model.util.placetolocationClass import *
from model.repositoryServices import *
from model.repository import *

class Repository_Test (TestCase):
	repo = Repository()

	std1 =  Student ("98010742326" , ["Walter" , "Mendives"] , "Male" , ["Cristo",409, "Camagüey" , "Jimaguayú"] , ["Guantanamo-672" , "This is a little description1..." , False] ,"Informatica" , 1 , 90.90)
	std2 =  Student ("97021744529" , ["Daniella" , "Gimenez"] , "Famale" , ["Cielo","15a", "Camagüey" , "Minas"] , ["Guantanamo-672" , "This is a little description2..." , False] ,"Informatica" , 3 , 95.88)
	std3 =  Student ("00010947739" , ["Jorge" , "Placeres"] , "Male" , ["Avenida",2499, "Camagüey" , "Camagüey"] , ["Guantanamo-672" , "This is a little description3..." , False] ,"Informatica" , 1 , 56.01)		
	tch1 =  Teacher ("81090912312" , ["Roberto","Lopez"] , "Male"   , ["Hospital", "5A", "Camagüey", "Camagüey"] , ["RTA56", "This is a little description3..." , True] , "Veterinaria", False , "Auxiliar"  , "Master of Science")
	tch2 =  Teacher ("97010465789" , ["Sonia" ,"Dias"]   , "Famale" , ["San Clemente", 326 , "Camagüey" , "Camagüey"] , ["UID-72" , "This is a little description2..." , False] ,"Ciencias Aplicadas" , True , "Instructor" , "Doctor")
	tch3 =  Teacher ("70010957241" , ["Jessica" ,"Alba"] , "Famale" , ["San Patricio", 76 , "Camagüey" , "Florida"] , ["Guantanamo-672" , "This is a little description3..." , False] ,"Veterinaria" , False , "Auxiliar" , "None")
	tch4 =  Teacher ("90030955547" , ["Roberto" ,"Jonathan"] , "Male" , ["Timbalito", 76 , "Camagüey" , "Najasa"] , ["Part2w" , "This is a little description4..." , False] ,"Economia" , False , "Titular Docente" , "Master of Science")
	plc1 =  Place_to_location(  ["CDP-34" , "This is a little description1..." , True]) 
	plc2 =  Place_to_location( ["RJK-98" , "This is a little description2..." , True])
	plc3 =  Place_to_location(["Vector-2" , "This is a little description3..." , False])
	
	# repo.insertTeacher(tch1)
	repo.insertTeacher(tch2)
	repo.insertTeacher(tch3)
	# repo.insertTeacher(tch4)
	# repo.insertStudent(std1)
	repo.insertStudent(std2)
	repo.insertStudent(std3)
	# repo.insertStudent(std4)
	# repo.insertPlace(plc1)
	repo.insertPlace(plc2)
	repo.insertPlace(plc3)
	# repo.insertPlace(plc4)

		
	def test_indexStudent (self):
		operation = self.repo.indexStudent(self.std3.ID)
		self.assertEqual(operation , 1)

	def test_indexTeacher (self):
		operation = self.repo.indexTeacher(self.std3.ID)
		self.assertIsNone(operation)
		
	def test_indexPlace (self):
		operation = self.repo.indexPlace("RJK-98")
		self.assertEqual(operation , 0)



	def test_show_Students (self):
		operation = self.repo.Students
		self.assertEqual(operation , [self.std2 , self.std3] )

	def test_show_Teachers (self):
		operation = self.repo.Teachers
		self.assertEqual(len(operation) , 2)

	def test_show_Places (self):
		operation = self.repo.Places
		self.assertEqual(type(operation) , list)



	def test_insertStudent (self):
		operation = self.repo.insertStudent(self.std1)
		self.assertIsNone(operation)

	def test_insertTeacher (self):
		operation = self.repo.insertTeacher(self.tch1)
		self.assertIsNone(operation)

	def test_insertPlace (self):
		operation = self.repo.insertPlace(self.plc1)
		self.assertIsNone(operation)



	def test_updateStudent (self):
		operation = self.repo.updateStudent(self.std2.ID, self.std2)
		self.assertIsNone(operation)

	def test_updateTeacher (self):
		operation = self.repo.updateTeacher("97010465789", self.tch4)
		self.assertIsNone(operation)

	def test_updatePlace (self):
		operation = self.repo.updatePlace("RJK-98", self.plc2)
		self.assertEqual(operation, None)



	def test_removeStudent (self):
		operation = self.repo.removeStudent("98010742326")
		self.assertIsNone(operation)

	def test_removeTeacher (self):
		operation = self.repo.removeTeacher("81090912312")
		self.assertIs(operation, None)

	def test_removePlace (self):
		operation = self.repo.removePlace("CDP-34")
		self.assertIsNone(operation)