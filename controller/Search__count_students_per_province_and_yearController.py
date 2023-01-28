from view.Search__count_students_per_province_and_year import *

class Search__count_students_per_province_and_yearController ():
	def __init__ (self, repo, repoService):
		self.__repository = repo
		self.__repositoryService = repoService

	def run (self):
		try:
			self.__view = Search__count_students_per_province_and_year(self)
			self.assigOption1()
			self.__validateOpen()
			self.__view.show()
		except Exception as e :
			self.__view.showError(e.args[0])

	def search (self):
		try:
			year = self.__view.value_year
			province = self.__view.value_province
			found = self.__repositoryService.count_students_per_province_year(year, province)
			if year == "1":
				year = "first"
			elif year == "2":
				year = "second"
			elif year == "3":
				year = "thrid"
			elif year == "4":
				year = "fourth"
			elif year == "5":
				year = "fifth"

			msg= None
			if year != "" and province != "":
				if found == 0:
					msg = f"Dont exist any student from {province} in {year} year of school in the repository"
				elif found==1:
					msg = f"There are {found} student from {province} in {year} year of school in the repository\n"
				else:
					msg = f"There are {found} students from {province} in {year} year of school in the repository\n"
			else:
				raise Exception("Please insert a teacher before make any Operation")

			self.__view.showResult(msg)
		except Exception as e:
			self.__view.showError(e.args[0])
# ------------------------------------------------------   
#			Load Options
# ------------------------------------------------------
	def assigOption1 (self):
		if self.__view.box_year.count() != 0:
			self.__view.box_year.clear()

		for i in self.__repository.getStudent(att="yearofcarrer"):
			year_std = str(i[0])
			year_box = []

			for j in range(self.__view.box_year.count() + 1):
				year_box.append(self.__view.box_year.itemText(j))

			if year_std not in year_box:
				self.__view.box_year.addItem(str(year_std))
			
	def assigOption2 (self, opt):
		if self.__view.box_province.count() != 0:
			self.__view.box_province.clear()

		for i in self.__repository.getStudent(att="yearofcarrer, address"):
			year = str(i[0])

			if year == opt:
				province_std = self.__repository.getAddress(addid=str(i[1]), att="province")[0][0]
				province_box = []

				for j in range(self.__view.box_province.count() + 1):
					province_box.append(self.__view.box_province.itemText(j))

				if province_std not in province_box:
					self.__view.box_province.addItem(str(province_std))
# ------------------------------------------------------
#			VALIDATIONS 
# ------------------------------------------------------
	def __validateOpen (self):
		if self.__view.box_year.count() == 0:
			raise Exception("You must input at least one Student before make any search") 
