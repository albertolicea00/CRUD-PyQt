from model.util.CubaProvinces.base.main import *


class CubaProvinces_BoxGroup ():
	def __init__(self, provinceBox = None , municipalyBox = None , parent = None, allignment="row"):
		self.__repository = Provinces_Municipaly ()
		
		self.__provinceBox = provinceBox
		self.__municipalyBox = municipalyBox
		
		self.allignment = allignment.lower()
		self.parent = parent

		self.__validateParent (parent)


	def exec (self):
		self.exec_()
	def exec_ (self):
		if self.__provinceBox is not None and self.__municipalyBox is not None: 
			self.__provinceBox.addItems(self.__repository.provinces)
			self.__municipalyBox.addItems(self.__repository.IsladelaJuventud)
			self.__provinceBox.currentIndexChanged.connect(self.__linkTogether)
			
		elif self.__provinceBox is not None and self.__municipalyBox is None:
			self.__provinceBox.addItems(self.__repository.provinces)
			
		elif self.__municipalyBox is not None and self.__provinceBox is None:
			self.__municipalyBox.addItems(self.__repository.municipaly)




	def __validateParent (self, parent):
		if parent is not None:
			self.__buildComboBox(parent)

	def __buildComboBox (self, parent):
		#meterlo posiblemente en un layout o un grupBox
		self.__provinceBox = QComboBox(parent)
		self.__municipalyBox = QComboBox(parent)
		
		
		if self.allignment == "row":
			self.__provinceBox.setGeometry(0,0,200,30)
			self.__municipalyBox.setGeometry(0,32,200,30)
		elif self.allignment == "column":
			self.__provinceBox.setGeometry(0,0,200,30)
			self.__municipalyBox.setGeometry(202,0,200,30)

		


	def __linkTogether (self , province_opt):
		if self.__municipalyBox.count() != 0:
			self.__municipalyBox.clear()
		

		if province_opt == 0:
			self.__municipalyBox.addItems(self.__repository.IsladelaJuventud)

		elif province_opt == 1:
			self.__municipalyBox.addItems(self.__repository.PinardelRio)

		elif province_opt == 2:
			self.__municipalyBox.addItems(self.__repository.Artemisa)

		elif province_opt == 3:
			self.__municipalyBox.addItems(self.__repository.LaHabana)

		elif province_opt == 4:
			self.__municipalyBox.addItems(self.__repository.Mayabeque)

		elif province_opt == 5:
			self.__municipalyBox.addItems(self.__repository.Matanzas)

		elif province_opt == 6:
			self.__municipalyBox.addItems(self.__repository.Cienfuegos)

		elif province_opt == 7:
			self.__municipalyBox.addItems(self.__repository.VillaClara)

		elif province_opt == 8:
			self.__municipalyBox.addItems(self.__repository.SanctiSpiritus)

		elif province_opt == 9:
			self.__municipalyBox.addItems(self.__repository.CiegodeAvila)

		elif province_opt == 10:
			self.__municipalyBox.addItems(self.__repository.Camaguey)

		elif province_opt == 11:
			self.__municipalyBox.addItems(self.__repository.LasTunas)

		elif province_opt == 12:
			self.__municipalyBox.addItems(self.__repository.Granma)

		elif province_opt == 13:
			self.__municipalyBox.addItems(self.__repository.Holguin)

		elif province_opt == 14:
			self.__municipalyBox.addItems(self.__repository.SantiagodeCuba)

		elif province_opt == 15:
			self.__municipalyBox.addItems(self.__repository.Guantanamo)


	@property
	def return_province(self):

		#aqui ya no se que hacer

		if province_opt == 0:
			return None

		elif province_opt == 1:
			return None

		elif province_opt == 2:
			return None

		elif province_opt == 3:
			return None

		elif province_opt == 4:
			return None

		elif province_opt == 5:
			return None

		elif province_opt == 6:
			return None

		elif province_opt == 7:
			return None

		elif province_opt == 8:
			return None

		elif province_opt == 9:
			return None

		elif province_opt == 10:
			return None

		elif province_opt == 11:
			return None

		elif province_opt == 12:
			return None

		elif province_opt == 13:
			return None

		elif province_opt == 14:
			return None

		elif province_opt == 15:
			return None

	# @property
	# def municipaly(self):
	# 	return












