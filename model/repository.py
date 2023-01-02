from model.studentClass import Student 
from model.teacherClass import Teacher
import psycopg2
from database.conection import conection

class Repository ():
	def __init__(self):
		"""
		This is the principal Repository class of the 'The University' 
		where all students, teachers and places to location are inserted, deleted, updated and showed, & can search a id of each object 
		
		>>> repo = Repository()
		None
		"""

		self.__possible_students = [] 	# esto se borrara mas adelante
		self.__possible_teachers = [] 	# esto se borrara mas adelante
		self.__possible_places = [] 	# esto se borrara mas adelante

	# -------------------------------
	#		INTERNALS OPERATION 
	# -------------------------------
	def indexStudent(self , ID):
		for i in range(len(self.Students)):
			if self.Students[i].ID == ID:
				return i
	def indexTeacher(self , ID):
		for i in range(len(self.Teachers)):
			if self.Teachers[i].ID == ID:
				return i

	def indexPlace(self , place_name):
		for i in range(len(self.Places)):
			if self.Places[i].place_name == place_name:
				return i
	
# *****************************************************************
#							CRUD
# *****************************************************************
	# ----------------------------------------------------------
	#			 SHOW			 SHOW			 SHOW 			
	# ----------------------------------------------------------
	@property	
	def Students (self):
		"""
		>>> repo.Students
		[object_student1, object_student2, object_student3 ...]
		"""
		return self.__possible_students
	@property
	def Teachers (self):
		"""
		>>> repo.Teachers
		[object_student1, object_teacher2, object_teacher3 ...]
		"""
		return self.__possible_teachers
	@property
	def Places (self):
		"""
		>>> repo.Places
		[object_student1, object_place, 2object_place ...3]
		"""
		try:
			with conection.cursor() as cursor:

				query = "SELECT * FROM PLACETOLOCATION"
				cursor.execute(query)
				plcs = cursor.fetchall()
				return plcs

		except psycopg2.Error as e:
			raise Exception("Error in database: ", e)
		# finally:
		# 	conection.close()


		return self.__possible_places
	# ----------------------------------------------------------
	#			INSERT			INSERT			INSERT			 
	# ----------------------------------------------------------
	def insertStudent (self, std ):
		"""
		>>> repo.insertStudent (object_student)
		None
		"""
		if self.indexStudent(std.ID) != None :
			raise Exception("The student already exist in the repository")
		self.Students.append(std)
			
	def insertTeacher (self ,tch):
		"""
		>>> repo.insertStudent (object_teacher)
		None
		"""
		if self.indexTeacher(tch.ID) != None :
			raise Exception("The teacher already exist in the repository")
		self.Teachers.append(tch)


	def insertPlace (self ,plc):
		"""
		>>> repo.insertStudent (object_place)
		None
		"""

		try:
			with conection.cursor() as cursor:
				query = "INSERT INTO PLACETOLOCATION (name, description, inuniversity) VALUES('{}','{}','{}')".format(plc.place_name, plc.place_description, plc.place_in_university)
				cursor.execute(query)
				conection.commit()
		except psycopg2.errors.UniqueViolation:
			raise Exception	(f"The place already exist in the repository")
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		# finally:
		# 	conection.close()

	# ----------------------------------------------------------
	#			UPDATE			UPDATE			UPDATE			
	# ----------------------------------------------------------
	def updateStudent (self, old_std_ID , new_std ):
		"""
		>>> repo.updateStudent (object_place.id , object_place)
		None
		"""
		old_index = self.indexStudent(old_std_ID)
		new_index = self.indexStudent(new_std.ID)

		if old_index == None:
			raise Exception("The student do not exist in the repository")
		if new_index != None and new_index != old_index:
			raise Exception("The teacher already exist in the repository")
		self.Students[old_index] = new_std

	def updateTeacher (self, old_tch_ID , new_tch ):
		"""
		>>> repo.updateTeacher (object_place.id , object_place)
		None
		"""
		old_index = self.indexTeacher(old_tch_ID)
		new_index = self.indexTeacher(new_tch.ID)

		if old_index == None:
			raise Exception('The teacher do not exist in the repository')
		if new_index != None and new_index != old_index:
			raise Exception("The teacher already exist in the repository")
		self.Teachers[old_index] = new_tch

	def updatePlace (self, old_plc_name , new_plc ):
		"""
		>>> repo.updatePlace (object_place.name , object_place)
		None
		"""
		old_index = self.indexPlace(old_plc_name)
		new_index = self.indexPlace(new_plc.place_name)

		if old_index == None:
			raise Exception('The place do not exist in the repository')
		if new_index != None and new_index != old_index:
			raise Exception("The place already exist in the repository")
		self.Places[old_index] = new_plc

	# ----------------------------------------------------------
	#			DELETE			DELETE			DELETE 			
	# ----------------------------------------------------------
	def removeStudent (self, std_ID):		#quisas aqui le pase solo el CI(ID)
		"""
		>>> repo.removeStudent (object_place)
		None
		"""
		index = self.indexStudent(std_ID)
		if index == None:
			raise Exception("The student do not exist in the repository")
		self.Students.remove(self.Students[index])

	def removeTeacher (self, tch_ID):
		"""
		>>> repo.removeTeacher (object_place)
		None
		"""
		index = self.indexTeacher(tch_ID)
		if index == None:
			raise Exception("The teacher do not exist in the repository")
		self.Teachers.remove(self.Teachers[index])

	def removePlace (self, plc_name):
		"""
		>>> repo.removePlace (object_place)
		None
		"""
		index = self.indexPlace(plc_name)
		if index == None:
			raise Exception("The place do not exist in the repository")
		self.Places.remove(self.Places[index])