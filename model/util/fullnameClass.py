
class Full_Name ():
	def __init__(self, fullname):
		"""
		*This class its just a useful class*
			... for a better doumentation see the fullname method of Person class
		
		>>> fn = Full_Name("John","Deep")
		None
		"""
		self.__fullname = fullname
		self.__name = fullname[0].strip().capitalize()
		self.__last_name = fullname[1].strip().capitalize()
		self.__validate()
		
	def __str__(self):
		return f"{self.__name} {self.__last_name}"

	# -------------------------------
	#				GETTERS 
	# -------------------------------
	@property
	def name (self):
		"""
		>>> print(fn.name)
		'John'
		"""
		return self.__name

	@property
	def last_name (self):
		"""
		>>> print(fn.last_name)
		'Deep'
		"""
		return self.__last_name
	# -------------------------------
	#				SETTERS 
	# -------------------------------
	@name.setter
	def name (self, value):
		"""
		>>> fn.name = "Jhonny"
		"""
		self.__name = value
		self.__validate()

	@last_name.setter
	def last_name (self, value):
		"""
		>>> fn.last_name = "Sims"
		"""
		self.__last_name = value
		self.__validate()
	# -------------------------------
	#			VALIDATIONS 
	# -------------------------------
	def __validate (self):
		"""
		There is only an output validation:
		- The output validation: Type="output is for the instance, the possible inputs from the user, for the view (GUI)
		"""
		if type(self.__fullname) is not list :
		 	raise Exception("The name format must be a list")
	
		if len(self.__name) < 3 or len(self.__name) > 13 :
			raise Exception(f"The name must have between 3 and 13 characters, not {len(self.__name)} characters ")
		if len(self.__last_name) < 3 or len(self.__last_name) > 13:
			raise Exception(f"The name last must have between 3 and 13 characters, not {len(self.__last_name)} characters")


		# esto hay que corregirlo y validar cuando me entren numeros como un nombre (la vista al ser un input lo saca como string == "123" )
		if not self.__name.isalpha():  
			raise Exception("Please input just one name without : spaces, numbers or any strange character")
		if not self.__last_name.isalpha():
			raise Exception("Please input just one last name without : spaces, numbers or any strange character")