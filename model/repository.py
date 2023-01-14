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


	@staticmethod
	def maxIndexAddress():
		#  retorna el id maximo en la tabla de direcciones

		try:
			with conection.cursor() as cursor:

				cursor.execute("SELECT MAX(id) FROM ADDRESS")    # retorna el id maximo en la tabla de direcciones
				addid = cursor.fetchall()[0][0] 				 # obtiene el id de la direccion agregada

				return addid
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")



# *****************************************************************
#							CRUD
# *****************************************************************
	# ----------------------------------------------------------
	#			 SHOW			 SHOW			 SHOW 			
	# ----------------------------------------------------------
	def getPlace(self, plcid="id", plcname="name", att="*"):
		# retorna las columnas(att) de un lugar de ubicacion segun el nombre pasado por parametro
		# att:str => 'name, inuniversity'

		try:
			with conection.cursor() as cursor:

				query = "SELECT " + att + " FROM PLACETOLOCATION WHERE id=" + plcid
				if plcname != "name":
					query += " and name='" + plcname + "'"

				cursor.execute(query)
				values = cursor.fetchall()

				# if len(values) == 0:
				# 	raise()

				return values
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")

	def getAddress(self, addid="id", att="*"):
		#  retorna las columnas(att) de un lugar de ubicacion segun el nombre pasado por parametro
		# att:str => 'name, inuniversity'

		try:
			with conection.cursor() as cursor:
				query = "SELECT " + att + " FROM ADDRESS WHERE id=" + addid
				cursor.execute(query)
				values = cursor.fetchall()

				# if len(values) == 0:
				# 	raise()

				return values
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")


	def getStudent(self, stdid="id", att="*"):
		try:
			with conection.cursor() as cursor:

				query = "SELECT " + att + " FROM STUDENT WHERE id=" + stdid
				cursor.execute(query)
				values = cursor.fetchall()
				return values

		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		# finally:
		# 	conection.close()
		# return self.__possible_students






	@property	
	def Students (self):
		"""
		>>> repo.Students
		[object_student1, object_student2, object_student3 ...]
		"""
		try:
			with conection.cursor() as cursor:

				query = "SELECT * FROM STUDENT"
				cursor.execute(query)
				std = cursor.fetchall()
				return std

		except psycopg2.Error as e:
			raise Exception("Error in database: ", e)
		# finally:
		# 	conection.close()
		# return self.__possible_students

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
			raise Exception(f"Error in database: {e}")
		# finally:
		# 	conection.close()

	# ----------------------------------------------------------
	#			INSERT			INSERT			INSERT			 
	# ----------------------------------------------------------

	def __insertAddress (self, address):
		"""
		>>> repo.__insertAddress ( addresslist )
		id
		"""
		try:
			with conection.cursor() as cursor:

				query = "INSERT INTO ADDRESS (street, number, province, municipality) " \
						"VALUES('{}','{}','{}','{}')".format(address.address_street, address.address_number, address.address_province, address.address_municipality)
				cursor.execute(query)

				conection.commit()
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")

	def insertStudent (self, std):
		"""
		>>> repo.insertStudent (object_student)
		None
		"""
		# try:
		# obtiene el id de la direccion agregada
		self.__insertAddress(std.address)
		addid = Repository.maxIndexAddress()
		# except:

		# obtiene el id del lugar de ubicacion escogido
		plcid = self.getPlace(plcname=std.place_to_location.place_name, att='id')[0][0]


		try:
			with conection.cursor() as cursor:

				query = "INSERT INTO STUDENT VALUES('{}','{}','{}','{}','{}','{}', {},'{}','{}', {})".format( std.ID,
					std.fullname.name, std.fullname.last_name, std.gender, addid, plcid, std.degree_acttitude, std.carrer, std.year_of_carrer, std.average )

				cursor.execute(query)
				conection.commit()

		# excepts de validacion a otros problemas a validar ....
		except psycopg2.errors.UniqueViolation:
			raise Exception(f"The student already exist in the repository")
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
			# validar si ocurre algun problema elimine el address insertado (crear un metodo para eliminar addrsss en privado)
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")



			
	def insertTeacher (self ,tch):
		"""
		>>> repo.insertStudent (object_teacher)
		None
		"""
		if self.indexTeacher(tch.ID) != None :
			raise Exception("The teacher already exist in the repository")
		self.Teachers.append(tch)

		# try:
		# 	with conection.cursor() as cursor:
		# 		query = "INSERT INTO TEACHER (ID, name, lastname, gender, address, placetolocation, degreeacttitude, departament, leftcuba, teachingcategory, scientificcategory) " \
		# 				"VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}''{}','{}')".format(tch.ID, tch.fullname.name, tch.fullname.lastname, tch.gender, 1, 1, tch.degree_acttitude, tch.departament, tch.left_cuba, tch.teaching_category, tch.scientific_category)
		# 		cursor.execute(query)
		# 		conection.commit()
		# except psycopg2.Error as e:
		# 	print("Error in database: ", e)
		# # finally:
		# # 	conection.close()

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
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")

	# ----------------------------------------------------------
	#			UPDATE			UPDATE			UPDATE			
	def updateStudent (self, old_std_ID , new_std ):
		"""
		>>> repo.updateStudent (object_place.id , object_place)
		None
		"""

		# actualiza la direccion
		oldstdid= "'" + old_std_ID + "'"
		oldidadd = self.getStudent(stdid=oldstdid, att="address")[0][0]
		self.__updateAddress(oldidadd, new_std.address)

		# obtiene el id del lugar de ubicacion escogido
		plcid = self.getPlace(plcname=new_std.place_to_location.place_name, att='id')[0][0]

		try:
			with conection.cursor() as cursor:
				query = "UPDATE STUDENT SET id = '{}', name = '{}', lastname = '{}', gender = '{}', placetolocation = {}, degreeacttitude = {}, carrer = '{}', yearofcarrer = {}, average = {}" \
						"WHERE id = '{}'".format(new_std.ID, new_std.fullname.name, new_std.fullname.last_name, new_std.gender, plcid, new_std.degree_acttitude, new_std.carrer, new_std.year_of_carrer, new_std.average, old_std_ID)

				cursor.execute(query)
				conection.commit()

		except psycopg2.errors.UniqueViolation:
			raise Exception	(f"The student already exist in the repository")
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")
	# ----------------------------------------------------------


	def __updateAddress (self, oldid, newadd):
		try:
			with conection.cursor() as cursor:

				query = "UPDATE ADDRESS SET street='{}', number='{}', province='{}', municipality='{}' WHERE id={}".format(newadd.address_street, newadd.address_number, newadd.address_province, newadd.address_municipality, oldid)
				cursor.execute(query)

				conection.commit()
		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")


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
		# revisa esto

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