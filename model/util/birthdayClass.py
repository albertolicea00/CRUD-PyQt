import datetime
from datetime import date

class Birthday ():
	"""
	Does not have settes becouse is dependent on the ID of the person created person
	*You cant use this class without a idClass and personClass , this class its just a useful*
		... **for a better doumentation see the birthday method of Person class
	
	"""
	def __init__ (self, ID):
		self.__ID = ID 
		self.__today = date.today()
		self.__id_year = self.__ID [0:2] 
		self.__id_month = self.__ID [2:4] 
		self.__id_day = self.__ID [4:6] 
		self.__date_birthday = self.__id_year  + self.__id_month + self.__id_day
		self.validate_birthday("input")

		self.__date_birthday = datetime.datetime.strptime(self.__date_birthday, "%y%m%d")
		self.__age = self.__calculate_age()

		self.validate_birthday("output")
	
	def __str__ (self):
		return f"{self.__id_day}-{self.__id_month}-{self.__date_birthday.year}"

	# -------------------------------
	#				GETTERS 
	# -------------------------------
	@property
	def date_birthday(self):
		"""
		This is for the person class to call all Birthday method easily
		"""
		return self.__date_birthday
		self.validate_birthday()

	@property
	def age(self):
		return self.__age
	# -------------------------------
	#		INTERNALS OPERATION 
	# -------------------------------
	def __calculate_age (self):
		if self.__date_birthday.day == 29 and self.__date_birthday.month == 2 : 
			return self.__today.year - self.__date_birthday.year - ((self.__today.month , self.__today.day) < (self.__date_birthday.month , self.__date_birthday.day-1))	
		else:	
			return self.__today.year - self.__date_birthday.year - ((self.__today.month , self.__today.day) < (self.__date_birthday.month , self.__date_birthday.day)) 
	
	def __month_comprobation(self):
		def leap_year():
			return int(self.__id_year) % 4 == 0  and  (int(self.__id_year) % 100 != 0 or int(self.__id_year) % 400 ==0)  

		if int(self.__id_month) in [4,6,9,11]:
			return 30
		elif int(self.__id_month) == 2:
			if leap_year():		# biciesto
				return 29
			else:
				return 28
		else:
			return 31
	# -------------------------------
	#			VALIDATIONS 
	# -------------------------------
	def validate_birthday (self, Type):
		"""
		There is an entry validation and an output validation:
		- The entry validation: Type="input" is for the first instance, the data range, for the model
		- The output validation: Type="output is for the instance, the possible inputs from the user, for the view (GUI)
		"""

		if Type == "input":
			if int(self.__id_month) < 1 or int(self.__id_month) > 12:
				raise Exception("The id entered is wrong, it does not match an existing month")
			if int(self.__id_day) < 1 or int(self.__id_day) > self.__month_comprobation():
				raise Exception("The id entered is wrong, it does not match an existing day")
		if Type == "output":
			if self.__age < 0 :
				raise Exception("The id entered is wrong, it does not match a valid year of birth")
			if self.__age < 18 :
				raise Exception("Too young to enter the university defence")
			if self.__age > 80 : 
				raise Exception("Too old to enter the university defence")

