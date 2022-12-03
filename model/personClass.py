from model.util.idClass import Id
from model.util.genderClass import Gender
from model.util.fullnameClass import Full_Name
from model.util.birthdayClass import Birthday
from model.util.addressClass import Address
from model.util.placetolocationClass import Place_to_location

class Person ():
	def __init__(self, ID , full_name , gender , address, place_to_location):
		"""
		*This class its one of the principal in the program*
	
		>>> psn = Person ("00010957241" , ["Alberto","Licea"] , "Male" , ["Bembeta",333, "Camagüey" , "Camagüey" ] , ["Guantanamo-672" , "This is a little description..." , False])
		None
		
		The birthday and age of the person is calculated using the ID, in their respective usefull classes
		
		** each property are implemented in its respective usefull Class ,
			this help to the next development to [Delete - Modify - Fix - Add] a functionality 
			keeped the organization and privacy ...
		"""
		self.__ID = Id(ID)
		self.__birthday = Birthday(self.__ID.ID) 
		self.__fullname = Full_Name(full_name)
		self.__gender = Gender(gender)
		self.__address = Address(address)
		self.__place_to_location = Place_to_location(place_to_location)	

		self.__degree_acttitude_base = 10 - (self.age * 0.1 )				
	
	# --------------------------------------------
	#				GETTERS 
	# --------------------------------------------
	@property
	def ID (self):
		return self.__ID.ID

	@property
	def birthday (self):
		"""
		Syntasis: object.birthday.[year , month , day ]
			>>> print(object.birthday.year)
			2000
			>>> print(object.birthday.month)
			1
		"""
		return self.__birthday.date_birthday

	@property
	def age (self):
		return self.__birthday.age

	@property
	def gender (self):
		return self.__gender.gender
		
	@property	
	def degree_acttitude_base (self):
		return self.__degree_acttitude_base
	
	# --------------------------------------------
	# 			SETTERS
	# --------------------------------------------
	@ID.setter
	def ID (self, value):
		self.__ID.ID = value
		self.__birthday.__init__(value)

	@gender.setter
	def gender (self, value):
		self.__gender.gender = value

	# --------------------------------------------
	#		GETTERS Y SETTERS
	# --------------------------------------------
	@property
	def fullname (self):
		"""
		Syntasis: object.fullname.[name , lastname ]
		
			GET:	>>> print(object.fullname)
					[Alberto Licea]
					>>> print(object.fullname.name)
					'Alberto'
				
			SET:	>>> object.fullname = ["nombre" , "apellidos"]
					ERROR!
					>>> object.fullname.name = "nombre"
					>>> object.fullname.lastname = "apellido"
		"""
		return self.__fullname

	@property
	def address (self):
		"""
		Syntasis: object.address.[address_street , address_number , address_municipality , address_province ]

			GET:	>>> print(object.address.address_province)
					Camagüey
				
			SET:	>>> object.address.address_street = "San Isidro"
		"""
		return self.__address
		
	@property
	def place_to_location (self):
		"""
		Syntasis: object.place_to_location.[place_name , place_description , place_in_university]
		
			GET:	>>> print(object.place_to_location.place_in_university)
					False
				
			SET:	>>> object.place_to_location.place_in_university = True
		"""
		return self.__place_to_location