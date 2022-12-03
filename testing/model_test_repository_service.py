from unittest import TestCase
from model.studentClass import *
from model.teacherClass import *
from model.util.placetolocationClass import *
from model.repository import *
from model.repositoryServices import *

class RepositoryService_Test (TestCase):
	repo = Repository()
	tch1 =  Teacher ("81090912312" , ["Roberto","Lopez"] , "Male"   , ["Hospital", "5A", "Camagüey", "Camagüey"] , ["RTA56", "This is a little description3..." , True] , "Veterinaria", False , "Auxiliar"  , "Master of Science")
	tch2 =  Teacher ("97010465789" , ["Sonia" ,"Dias"]   , "Famale" , ["San Clemente", 326 , "Camagüey" , "Camagüey"] , ["UID-72" , "This is a little description2..." , False] ,"Ciencias Aplicadas" , True , "Instructor" , "Doctor")
	tch3 =  Teacher ("70010957241" , ["Jessica" ,"Alba"] , "Famale" , ["San Patricio", 76 , "Camagüey" , "Florida"] , ["Guantanamo-672" , "This is a little description3..." , False] ,"Veterinaria" , False , "Auxiliar" , "None")
	std1 =  Student ("98010742326" , ["Walter" , "Mendives"] , "Male" , ["Cristo",409, "Camagüey" , "Jimaguayú"] , ["Guantanamo-672" , "This is a little description1..." , False] ,"Informatica" , 1 , 90.90)
	std2 =  Student ("97021744529" , ["Daniella" , "Gimenez"] , "Famale" , ["Cielo","15a", "Camagüey" , "Minas"] , ["Guantanamo-672" , "This is a little description2..." , False] ,"Informatica" , 3 , 95.88)
	std3 =  Student ("00010947739" , ["Jorge" , "Placeres"] , "Male" , ["Avenida",2499, "Camagüey" , "Camagüey"] , ["Guantanamo-672" , "This is a little description3..." , False] ,"Informatica" , 1 , 56.01)		
	plc1 =  Place_to_location(  ["CDP-34" , "This is a little description1..." , True]) 
	plc2 =  Place_to_location( ["RJK-98" , "This is a little description2..." , True])
	plc3 =  Place_to_location(["Vector-2" , "This is a little description3..." , False])
	
	repo.insertTeacher(tch1)
	repo.insertTeacher(tch2)
	repo.insertTeacher(tch3)
	repo.insertStudent(std1)
	repo.insertStudent(std2)
	repo.insertStudent(std3)
	repo.insertPlace(plc1)
	repo.insertPlace(plc2)
	repo.insertPlace(plc3)
	
	def setUp(self):
		self.repoService = RepositoryService(self.repo)	


	def test_1_average_teachers_per_province_departament (self):
		operation = self.repoService.average_teachers_per_province_departament("Veterinaria" , "Camagüey")
		self.assertEqual(operation , 46.0)
	
	def test_2_average_teachers_per_province_departament (self):
		operation = self.repoService.average_teachers_per_province_departament("Economia" , "Camagüey")
		self.assertEqual(operation , 0.0)


	
	def test_1_count_students_per_province_year (self):
		operation = self.repoService.count_students_per_province_year(1,"Camagüey")
		self.assertEqual(operation , 2)
	
	def test_2_count_students_per_province_year (self):
		operation = self.repoService.count_students_per_province_year(1,"La Habana")
		self.assertEqual(operation , 0)



	def test_1_show_older_teacher_address (self):
		operation = self.repoService.show_older_teacher_address("Florida")
		self.assertEqual(operation , [self.tch3])
	
	def test_2_show_older_teacher_address (self):
		operation = self.repoService.show_older_teacher_address("Arrollo Naranjo")
		self.assertEqual(operation , [])



	def test_1_show_teachers_per_teaching_category (self):
		operation = self.repoService.show_teachers_per_teaching_category("Instructor")
		self.assertEqual(operation , [self.tch2] )

	def test_2_show_teachers_per_teaching_category (self):
		operation = self.repoService.show_teachers_per_teaching_category("Titular")
		self.assertEqual(operation , [])
