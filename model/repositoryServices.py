import psycopg2
from database.conection import conection
from model.util.structures.linked_stack import LinkedStack
from model.util.birthdayClass import Birthday

class RepositoryService ():
	def __init__(self, repo):
		"""
		This is the principal RepositoryService class of the 'The University' 
		where all secundary operations are maked
		
		*first you need to create University Repository to work with this Service 
			url:[...model/repository.py(class Repository)] ; {print( help(Repository) )}

		>>> repoService = RepositoryService(repo)
		None
		"""
		self.__repository = repo

	def average_teachers_per_province_departament (self, departament, province):
		"""
		Operation # C

		repoService.average_teachers_per_province_departament ()
		float : return the average of teachers who have a given a departament and a province 
		"""

		age_stack = LinkedStack()
		age_counter = 0
		num_counter = 0

		try:
			with conection.cursor() as cursor:

				query = "SELECT TEACHER.id FROM TEACHER, ADDRESS WHERE TEACHER.address = ADDRESS.id " \
						"AND TEACHER.departament='{}' AND ADDRESS.province='{}'".format(departament, province)

				cursor.execute(query)
				tchid = cursor.fetchall()  	# obtiene el id de los profesores con dicha condicion

		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")

		# aqui hay un bucle de mas pero hay que usar estructura de datos
		for i in range(len(tchid)):
			tch_age = Birthday(tchid[i][0])
			age_stack.push(tch_age)

		while age_stack.is_empty() == False:
			tch_age = age_stack.pop()
			age_counter += tch_age.age
			num_counter += 1

		try:
			return age_counter / num_counter
		except ZeroDivisionError:
			return 0.0


	def count_students_per_province_year (self ,year, province):
		"""
		Operation # D

		>>> repoService.average_teachers_per_province_departament (object_student.year_of_carrer , object_student.address.address_province)
		int : return the number of students who have a given province and a year of carrer 
		"""
		students = 0 
		for i in range(len(self.__repository.Students)):
			std = self.__repository.Students[i]
			if std.year_of_carrer == int(year) and std.address.address_province == province:
				students+=1
		return students

	def show_older_teacher_address (self, municipality):
		"""
		Operation # E

		>>> repoService.show_older_teacher_address (object_student.address.address_municipality)
		[ ] : return a list with the older teacher, in case two or more people exist with the same age, return all of they 
		"""
		teachers = []			# aqui irira una lista enlazada pa meter a cojones
		for i in range(len(self.__repository.Teachers)):
			tch = self.__repository.Teachers[i]
			if tch.address.address_municipality == municipality:
				teachers.append(tch)
		if len(teachers) != 0:
			older = [teachers[0]]
			for i in range(len(teachers)):
				tch = teachers[i]
				for j in range(len(older)):
					if tch.birthday.year < older[0].birthday.year :
						if len(older) == 1:
							older[0] = tch
						else:
							older = [tch]
					elif tch.birthday.year == older[0].birthday.year :
						if tch.birthday.month < older[0].birthday.month :
							if len(older) == 1:
								older[0] = tch
							else:
								older = [tch]
						elif tch.birthday.month == older[0].birthday.month :
							if tch.birthday.day < older[0].birthday.day :
								if len(older) == 1:
									older[0] = tch
								else:
									older = [tch]
							elif tch.birthday.day == older[0].birthday.day and tch not in older:
								older.append(tch)
		else:
			older = []

		return older
		

	def show_teachers_per_teaching_category (self, teaching_category):
		"""
		Operation # F

		>>> repoService.show_teachers_per_teaching_category (object_teacher.teaching_category)
		[ ] : return a list with all teachers who have that teaching_category in the repository sorted by teachers age
		"""
		teachers = []
		for i in range(len(self.__repository.Teachers)):
			tch = self.__repository.Teachers[i]
			if tch.teaching_category == teaching_category and tch.left_cuba:
				teachers.append(tch)
		return sorted(teachers, key=lambda tch: tch.birthday)