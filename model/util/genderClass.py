#from util.Genders.main import spanishGenders
#from util.Genders.main import englishGenders

class Gender :
	def __init__ (self, gender):
		"""
		*This class its just a useful class*
		
		>>> gr = Gender("Male")
		None
		"""
		self.__gender = gender
		self.__validate()

	def __str__ (self):
		return f"{self.__gender}"
	# -------------------------------
	#				GETTERS 
	# -------------------------------
	@property
	def gender (self):
		"""
		>>> print(gr.gender)
		'Male'
		"""
		return self.__gender
	# -------------------------------
	#				SETTERS
	# -------------------------------
	@gender.setter
	def gender (self, value):
		"""
		>>> gr.gender = "Other"
		"""
		self.__gender = value
	# -------------------------------
	#			VALIDATIONS 
	# -------------------------------
	# Aqui faltaria incrementar mas generos o hacerlo un poquito mas personalozable, con un parametro extra para agregar uno a la lista/bbdd de la validacion
	def __validate (self):		
		if self.__gender not in ["Male" , "Famale" , "Other"]:# + englishGender + spanishGeder:
		 	raise Exception("The gender entered does not exist in our database")

