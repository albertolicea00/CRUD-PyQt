from view.Search__average_teachers_per_province_and_departament import *

class Search__average_teachers_per_province_and_departamentController ():
	def __init__ (self, repo, repoService):
		self.__repository = repo
		self.__repositoryService = repoService

	def run (self):
		try:
			self.__view = Search__average_teachers_per_province_and_departament(self)
			self.assigOption1()
			self.__validateOpen()
			self.__view.show()
		except Exception as e:
			self.__view.showError(e.args[0])

	def search (self):
		try:
			departament = self.__view.value_departament
			province = self.__view.value_province
			found = self.__repositoryService.average_teachers_per_province_departament(departament, province)
			msg= None
			if departament != "": #and province !="" :
				if found==0:
					raise Exception("Please insert a teacher before make any operation")
				else:
					msg = f"Within the teachers in the repository, the average age {round(found)} years old\n"
			else:
				raise Exception("Please insert a teacher before make any operation")
			
			self.__view.showResult(msg)
		except Exception as e:
			self.__view.showError(e.args[0])
# ------------------------------------------------------   
#			Load Options
# ------------------------------------------------------
	def assigOption1 (self):
		if self.__view.box_province.count() != 0:
			self.__view.box_province.clear()

		for i in self.__repository.getTeacher(att="address"):
			province_tch = self.__repository.getAddress(addid=str(i[0]), att="province")[0][0]
			province_box = []
			for j in range(self.__view.box_province.count() + 1):
				province_box.append(self.__view.box_province.itemText(j))

			if province_tch not in province_box:
				self.__view.box_province.addItem(str(province_tch))	


	def assigOption2 (self, opt):
		if self.__view.box_departament.count() != 0:
			self.__view.box_departament.clear()

		for i in self.__repository.getTeacher(att="address, departament"):
			province = self.__repository.getAddress(addid=str(i[0]), att="province")[0][0]

			if province == opt:
				departament_tch = i[1]
				departament_box = []
				
				for j in range(self.__view.box_departament.count() + 1):
					departament_box.append(self.__view.box_departament.itemText(j))

				if departament_tch not in departament_box:
					self.__view.box_departament.addItem(str(departament_tch))
# ------------------------------------------------------
#			VALIDATIONS 
# ------------------------------------------------------
	def __validateOpen (self):
		if self.__view.box_province.count() == 0:
			raise Exception("You must input at least one Teacher before make any search") 
