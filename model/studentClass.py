from model.personClass import Person

class Student ( Person ):
	def __init__(self, ID , full_name , gender , address, place_to_location ,      carrer, year_of_carrer, average):
		super().__init__(ID , full_name , gender , address, place_to_location)
		"""
		*This class its one of the principal in the program*
			- Implemets all the attributes and method of his paren class: Person
			- Students own attributes: [	carrer : string
											year_of_carrer : int (bewteen 1 - 5) 
											average  : flost (bewteen 0.00 - 100.00) 
										]

		>>> std = Student ("98020747729" , ["Jorge" ,  "Placeres"] , "Male" , ["Cielo",124, "Minas" , "Camagüey" ] , ["Guantanamo-672" , "This is a little description..." , False] , "Informatica" , 1 , 92.98)
		None
		"""
		self.__carrer = str(carrer)
		self.__year_of_carrer = int(year_of_carrer)
		self.__average = float(average)
		
		self.__validate()
	# --------------------------------------------
	#				GETTERS 
	# --------------------------------------------
	@property	
	def degree_acttitude (self):
		"""
		The degree_acttitude of the student is calculated automatic using one degree_acttitude_base and a general formula
		"""
		self.__degree_acttitude = self.degree_acttitude_base + (1 - (self.year_of_carrer*0.15)+(self.average*0.03) )
		return self.__degree_acttitude

	@property
	def carrer (self):
		"""
		>>> print(std.carrer)
		'Informatica'
		"""
		return self.__carrer
	
	@property
	def year_of_carrer (self):
		"""
		>>> print(std.year_of_carrer)
		1
		"""
		return self.__year_of_carrer
	
	@property
	def average (self):
		"""
		>>> print(std.average)
		92.98
		"""
		return round(self.__average , 2)
	# --------------------------------------------
	#				SETTERS
	# --------------------------------------------
	@carrer.setter
	def carrer (self , value):
		"""
		>>> std.carrer = "Economia"
		"""
		self.__carrer = value
		# self.__validate()

	@year_of_carrer.setter
	def year_of_carrer (self , value):
		"""
		>>> std.year_of_carrer = 2
		"""
		self.__year_of_carrer = value
		self.__validate()

	@average.setter
	def average (self , value):
		"""
		>>> std.average = 80.00
		"""
		self.__average = value
		self.__validate()
	# -------------------------------------------
	#		INTERNALS OPERATION 
	# -------------------------------------------
	#...
	# -------------------------------------------
	#			VALIDATIONS 
	# -------------------------------------------
	def __validate(self):
		if self.__year_of_carrer not in [1,2,3,4,5]:
			raise Exception("The year of carrer must be truely")
	
		if self.__average < 0 or self.__average > 100 :
		 	raise Exception("The average must be between 0 and 100")