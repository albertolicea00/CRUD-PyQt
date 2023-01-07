from model.util.CubaProvinces.base.main import Provinces_Municipaly
import re 

class Address ():
	def __init__(self, address):
		"""
		*This class its just a useful class*
		
		>>> adr=Address(["2nd Avenue", 23 , "Gibara" , "Holguín" ])
		None

		
		**for a better doumentation see the birthday method of Person class
		"""
		self.__pm = Provinces_Municipaly()
		self.__address = address
		self.__validate("input")
		
		self.__address_street = str( address[0] ) 
		self.__address_number = str( address[1] )
		self.__address_province : str = address[2]
		self.__address_municipality : str = address[3]
		
		self.__validate("output")

		
	# def __str__(self):
	# 	return "{} #{} , {} , {}".format(self.address_street ,self.address_number , self.address_municipality , self.address_province)
	
	
	@property
	def address (self):
		"""
		This is for the person class to call all Place_to_location method easily
		"""
		return [self.address_street ,self.address_number , self.address_municipality , self.address_province] 
	# -------------------------------
	#				GETTERS 
	# -------------------------------
	@property
	def address_street (self):
		"""
		>>> print(adr.address_street)
		'2nd Avenue'
		"""
		return self.__address_street 

	@property
	def address_number (self):
		"""
		>>> print(adr.address_number)
		23
		"""
		return self.__address_number 

	@property
	def address_municipality (self):
		"""
		>>> print(adr.address_province)
		'Holguín'
		"""
		return self.__address_municipality 

	@property
	def address_province (self):
		"""
		>>> print(adr.address_municipality)
		"Gibara"
		"""
		return self.__address_province 	
	# -------------------------------
	#				SETTERS
	# -------------------------------

	@address_street.setter
	def address_street (self, value):
		"""
		>>> adr.address_street = "Florat"
		"""
		self.__address_street = value

	@address_number.setter
	def address_number (self, value):
		"""
		>>> adr.address_number = 45
		"""
		self.__address_number = value

	@address_municipality.setter
	def address_municipality (self, value):
		"""
		>>> adr.address_province = "Camagüey"
		"""
		self.__address_municipality = value

	@address_province.setter
	def address_province (self, value):
		"""
		>>> adr.address_municipality = "Camagüey"
		"""
		self.__address_province = value
		
	# -------------------------------
	#			VALIDATIONS 
	# -------------------------------
	def __validate (self, Type):
		"""
		There is an entry validation and an output validation:
		- The entry validation: Type="input" is for the first instance, the data types, for the model
		- The output validation: Type="output is for the instance, the possible inputs from the user, for the view (GUI)
		"""
		if Type == "input":
			if type(self.__address) != list:
				raise Exception("The address format must be a list")

		if Type == "output":
			try :
				int(self.__address_number)
				if int(self.__address_number) < 0 or int(self.__address_number) > 5000:
					raise Exception("The house number is wrong")
			except ValueError:
				split = re.search("[A-z]", self.__address_number).start()
				address_number_number = self.__address_number [ : split]
				address_number_letter = self.__address_number [split : ]
				
				if address_number_number.isdigit() == False:
					raise Exception("The house number must be started be a number")
				if len(address_number_number)==0 or int(address_number_number) < 0 or int(address_number_number) > 5000:
					raise Exception("The house number is wrong")
				if len(address_number_letter) > 1: 
						raise Exception("The house number letter is wrong, must be between A to Z, cant be 2 letters or any number before that")


			if self.__address_municipality not in self.__pm.municipaly:
				raise Exception("The municipaly entered does not exist")
			if self.__address_province not in self.__pm.provinces:
				raise Exception("The province entered does not exist")

			if not self.__pm.check(self.__address_province , self.__address_municipality):
				raise Exception("The municipaly entered does not correspond to any existing province")