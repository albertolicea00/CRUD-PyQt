
class Place_to_location ():
	def __init__(self, place):

		"""
		*This class its just a useful class*
			... for a better doumentation see the fullname method of Person class


		>>> plc = Place_to_location(["CDP" , "This is a little description..." , True])
		None		
		"""
		self.__place = place
		self.__validate("input")

		self.__place_name : str = place[0]
		self.__place_description : str = place[1]
		self.__place_in_university : bool = place[2]

		self.__validate("output")

	def __str__(self):
		return "name: {} \ndescription: {} \ninCollege: {}".format(self.__place_name ,self.__place_description , self.__place_in_university ) 

	@property
	def place(self):
		"""
		This is for the person class to call all Place_to_location method easily
		"""
		return self.__place

	# -------------------------------
	#				GETTERS 
	# -------------------------------
	@property
	def place_name (self):
		"""
		>>> print(plc.place_name)
		'CDP'
		"""
		return self.__place_name 

	@property
	def place_description (self):
		"""
		>>> print(plc.place_description)
		'This is a little description...'
		"""
		return self.__place_description 

	@property
	def place_in_university (self):
		"""
		>>> print(plc.place_in_university)
		True
		"""
		return self.__place_in_university 
	# -------------------------------
	#				SETTERS
	# -------------------------------
	@place_name.setter
	def place_name (self, value):
		"""
		>>> plc.place_name = "Guantanamo-34"
		"""
		self.__place_name = value

	@place_description.setter
	def place_description (self, value):
		"""
		>>> plc.place_description = "I dont know"
		"""
		self.__place_description = value

	@place_in_university.setter
	def place_in_university (self, value):
		"""
		>>> plc.place_in_university = False
		"""
		self.__place_in_university = value

	# -------------------------------
	#			VALIDATIONS 
	# -------------------------------
	def __validate (self, Type):
		"""
		There is an entry validation and an output validation:
		- The entry validation: Type="input" is for the first instance, the data types for, the model
		- The output validation: Type="output is for the instance, the possible inputs from the user, for the view (GUI)
		"""
		if Type == "input":
			if type(self.__place) != list:
				raise Exception("The place_to_ubication format must be a list")
		if Type == "output":
		 	if type(self.__place_name) != str :
		 		raise Exception("The name of 'Place to ubication' format must be a string")
		 	if type(self.__place_description) != str :
		 		raise Exception("The description of 'Place to ubication' format must be a string")
		 	if type(self.__place_in_university) != bool :
		 		raise Exception("The 'ubication in or out the university' of 'Place to ubication' format must be a boolean")
