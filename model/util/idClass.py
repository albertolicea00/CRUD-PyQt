
class Id ():
	def __init__ (self, Id):
		"""
		*This class its just a useful class*
		
		>>>id = Id("99010678912")
		None
		"""
		self.__id = Id
		self.__validate()

	def __str__ (self):
		return f"{self.__id}"			
	# -------------------------------
	#				GETERS 
	# -------------------------------
	@property
	def ID (self):
		"""	
		>>>print(id.ID)
		'99010678912'
		"""
		return self.__id
	# -------------------------------
	#				SETTERS
	# -------------------------------
	@ID.setter
	def ID (self, value):
		"""
		>>>id.ID = 00010678912
		"""
		self.__id = value
		self.__validate()		
	# -------------------------------
	#			VALIDATIONS 
	# -------------------------------
	def __validate (self):
		"""
		There is an entry validation and an output validation:
		- The entry validation: Type="input" is for the first instance, the data types, for the model
		- The output validation: Type="output is for the instance, the possible inputs from the user, for the view (GUI)
		"""	
		if type(self.__id) != str:
			raise Exception("The id format must be a list")

		if len(self.__id) != 11 :
			raise Exception("The id length must have 11 characters")
		if not self.__id.isdigit():  
			raise Exception("The id must be a string of digists")