from model.personClass import Person

class Teacher ( Person ):
	def __init__(self ,ID , full_name , gender , address, place_to_location,        departament , left_cuba , teaching_category , scientific_category):
		super().__init__(ID , full_name , gender , address, place_to_location)
		"""
		*This class its one of the principal in the program*
			- Implemets all the attributes and method of his paren class: Person
			- Teachers own attributes: [	departament : string
											left_cuba : boolean 
											teaching_category  : string
											scientific_category : string
										]

		>>> tch = Teacher ("70010957241" , ["Jessica" ,"Alba"] , "Famale" , ["San Clemente",326, "Florida" , "Camagüey" ] , ["Guantanamo-672" , "This is a little description..." , False], "Ciencias Informaticas" , False , "Auxiliar" , "Master")
		None
		"""
		self.__departament =str(departament)
		self.__left_cuba = bool(left_cuba)							
		self.__teaching_category = str(teaching_category)			
		self.__scientific_category = str(scientific_category)		
 		
		self.__validate()
	# --------------------------------------------
	#				GETTERS 
	# --------------------------------------------
	@property	
	def degree_acttitude (self):
		"""
		The degree_acttitude of the teacher is calculated automatic using one degree_acttitude_base and a general formula
		"""
		if self.left_cuba:		#Es lo mismo  ->->->->    if self.left_cuba == True :
			self.__degree_acttitude = 4 + self.degree_acttitude_base
		else:
			self.__degree_acttitude = self.degree_acttitude_base
		return self.__degree_acttitude
	@property
	def departament (self):
		"""
		>>> print(tch.departament)
		'Ciencias Informaticas'
		"""
		return self.__departament
	
	@property
	def left_cuba (self):
		"""
		>>> print(tch.left_cuba)
		False
		"""
		return self.__left_cuba

	@property
	def teaching_category (self):
		"""
		>>> print(tch.teaching_category)
		'Auxiliar'
		"""
		return self.__teaching_category
	
	@property
	def scientific_category (self):
		"""
		>>> print(tch.scientific_category)
		'Master'
		"""
		return self.__scientific_category
	# --------------------------------------------
	#				SETTERS
	# --------------------------------------------
	@departament.setter
	def departament (self , value):
		"""
		>>> tch.departament = "Ciencias Sociales"
		"""
		self.__departament = value
		# self.__validate()

	@left_cuba.setter
	def left_cuba (self , value):
		"""
		>>> tch.left_cuba = True
		"""
		self.__left_cuba = value
		# self.__validate()

	@teaching_category.setter
	def teaching_category (self , value):
		"""
		>>> tch.teaching_category = "Instructor"
		"""
		self.__teaching_category = value
		self.__validate()

	@scientific_category.setter
	def scientific_category (self , value):
		"""
		>>> tch.scientific_category = "Doctor"
		"""
		self.__scientific_category = value
		self.__validate()
	# -------------------------------------------
	#		INTERNALS OPERATION 
	# -------------------------------------------
	#...
	# -------------------------------------------
	#			VALIDATIONS 
	# -------------------------------------------
	def __validate(self):
		spanish__teaching_category = ["Titular", "Auxiliar", "Asistente" , "Instructor"] + ["Titular Docente", "Auxiliar Docente", "Asistente Docente" , "Instructor Docente"]
		english__teaching_category = ["Auxiliary", "Auxiliary", "Assistant" , "Instructor"] + ["Head Teacher" , "Teaching Assistant" , "Teaching Auxiliar" , "Teaching AIstructor"]
		spanish__scientific_category = ["Doctor", "Master", "Ninguna"] +  ["Doctor en Ciencias", "Master en Ciencias"]
		english__scientific_category = ["Doctor", "Master", "None" ] + ["Doctor of Science", "Master of Science" ]

		if self.__teaching_category not in spanish__teaching_category + english__teaching_category:
			raise Exception("Please input a truly teaching category")
	
		if self.__scientific_category not in spanish__scientific_category + english__scientific_category:
			raise Exception("Please input a truly scientific category")