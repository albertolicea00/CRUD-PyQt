import psycopg2
from database.conection import conection
from model.util.structures.linked_stack import LinkedStack
from model.util.structures.single_linked_list import LinkedList
from model.util.birthdayClass import Birthday
import numpy as np

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
		try:
			with conection.cursor() as cursor:

				query = "SELECT COUNT(STUDENT.id), STUDENT.yearofcarrer, ADDRESS.province FROM STUDENT, ADDRESS WHERE STUDENT.address = ADDRESS.id " \
						"AND STUDENT.yearofcarrer={} AND ADDRESS.province='{}' GROUP BY STUDENT.yearofcarrer, ADDRESS.province".format(year, province)

				cursor.execute(query)
				students = cursor.fetchall()[0][0]  	# obtiene el count de la consulta

				return students

		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")

	def show_older_teacher_address (self, municipality):
		"""
		Operation # E

		>>> repoService.show_older_teacher_address (object_teacher.address.address_municipality)
		[ ] : return a list with the older teacher, in case two or more people exist with the same age, return all of they 
		"""
		teachers = LinkedStack()
		bigger_tch = LinkedStack()
		try:
			with conection.cursor() as cursor:

				query = "SELECT TEACHER.id, TEACHER.name, TEACHER.lastname, ADDRESS.street, ADDRESS.number, ADDRESS.province, ADDRESS.municipality " \
						"FROM TEACHER, ADDRESS WHERE TEACHER.address = ADDRESS.id " \
						"AND ADDRESS.municipality='{}'".format(municipality)

				cursor.execute(query)
				tch = cursor.fetchall()

		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")


		bigger = 99991231				# fecha de comparacion =  9999-12-31
		for i in range(len(tch)):		# recorriendo la consulta
			bth = Birthday(tch[i][0])

			datebth = int(str(bth.date_birthday.year) + str(bth.date_birthday.month) + str(bth.date_birthday.day))
			teachers.push([datebth, list(tch[i]) + [bth.age]])		# añdiendo los profesores a una pila

			# calculando el/los profesores mas viejos
			if datebth < bigger:
				bigger = datebth

		while teachers.is_empty() == False:
			tch = teachers.pop()

			if tch[0] == bigger:		# almacenando para retornar en otra pila solo los profesores que sean mas viejos (si has mas de uno los retorna todos)
				bigger_tch.push(tch[1])

		return bigger_tch

	def show_teachers_per_teaching_category (self, teaching_category):
		"""
		Operation # F

		>>> repoService.show_teachers_per_teaching_category (object_teacher.teaching_category)
		[ ] : return a list with all teachers who have that teaching_category in the repository sorted by teachers age
		"""
		teachers = []
		ages = []

		try:
			with conection.cursor() as cursor:

				query = "SELECT TEACHER.id, TEACHER.name, TEACHER.lastname FROM TEACHER, ADDRESS WHERE TEACHER.address = ADDRESS.id " \
						"AND TEACHER.teachingcategory='{}' AND TEACHER.leftcuba='false'".format(teaching_category)
				cursor.execute(query)
				tch = cursor.fetchall()

		except psycopg2.Error as e:
			raise Exception(f"Error in database: {e}")
		finally:
			with conection.cursor() as cursor:
				cursor.execute("rollback")

		# separando una lista de edades y otra con los profesores
		for i in range(len(tch)):
			bth = Birthday(tch[i][0])
			ages += [bth.age]
			teachers += [tch[i]]

		# convirtiendo las listas a arrays de numpy
		teachers = np.array(teachers)
		ages = np.array(ages)

		# ordena y retorna un modelo de indices del array de edades
		inds = np.argsort(a=ages, kind='quicksort')	 	# parametro-kind:{'quicksort'', 'mergesort', 'heapsort', 'stable', ...}
		sorted_tch = teachers[inds]	 # segun el orden de edades se ordena el array de profesores

		return sorted_tch
