from view.Search__show_older_teacher_address import *

class Search__show_older_teacher_addressController ():
	def __init__ (self, repo, repoService):
		self.__repository = repo
		self.__repositoryService = repoService

	def run (self):
		try:
			self.__view = Search__show_older_teacher_address(self)
			self.assigOption1()
			self.__validateOpen()
			self.__view.show()
		except Exception as e:
			self.__view.showError(e.args[0])

	def search (self):
		try:
			municipality = self.__view.value_municipality
			msg= None
			if municipality != "":
				found = self.__repositoryService.show_older_teacher_address(municipality)

				if len(found) == 1:
					msg = f"This is the older teacher in the repository\n"
				elif len(found) > 1:
					msg = f"They are the olders teachers in the repository\n"
			else:
				raise Exception("Please insert a teacher before make this Operation")

			while not found.is_empty():
				tch = found.pop()
				tch_msg = f"\n   - {tch[7]} years old : {tch[0]}, {tch[1]} {tch[2]}:\n                  address: {tch[3]}, {tch[4]}, {tch[5]} - {tch[6]}\n"
				msg += tch_msg

			self.__view.showResult(msg)
		except Exception as e:
			self.__view.showError(e.args[0])
# ------------------------------------------------------
#			Load Options
# ------------------------------------------------------
	def assigOption1 (self):
		for i in range(len(self.__repository.Teachers)):
			province = self.__repository.Teachers[i].address.address_province
			municipality = self.__repository.Teachers[i].address.address_municipality

			self.__view.box_province.addItem(str(province))
			self.__view.box_municipaly.addItem(str(municipality))


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
		if self.__view.box_municipality.count() != 0:
			self.__view.box_municipality.clear()

		for i in self.__repository.getTeacher(att="address"):
			for j in self.__repository.getAddress(addid=str(i[0]), att="province, municipality"):
				province = j[0]

			if province == opt:
				municipality_tch = j[1]
				municipality_box = []

				for j in range(self.__view.box_municipality.count() + 1):
					municipality_box.append(self.__view.box_municipality.itemText(j))

				if municipality_tch not in municipality_box:
					self.__view.box_municipality.addItem(str(municipality_tch))
# ------------------------------------------------------
#			VALIDATIONS
# ------------------------------------------------------
	def __validateOpen (self):
		if self.__view.box_province.count() == 0:
			raise Exception("You must input at least one Teacher before make any search") 

