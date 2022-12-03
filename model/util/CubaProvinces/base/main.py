from model.util.CubaProvinces.base.municipaly_Artemisa import *
from model.util.CubaProvinces.base.municipaly_Camaguey import *
from model.util.CubaProvinces.base.municipaly_CiegodeAvila import *
from model.util.CubaProvinces.base.municipaly_Cienfuegos import *
from model.util.CubaProvinces.base.municipaly_Granma import *
from model.util.CubaProvinces.base.municipaly_Guantanamo import *
from model.util.CubaProvinces.base.municipaly_Holguin import *
from model.util.CubaProvinces.base.municipaly_IsladelaJuventud import *
from model.util.CubaProvinces.base.municipaly_LaHabana import *
from model.util.CubaProvinces.base.municipaly_LasTunas import *
from model.util.CubaProvinces.base.municipaly_Matanzas import *
from model.util.CubaProvinces.base.municipaly_Mayabeque import *
from model.util.CubaProvinces.base.municipaly_PinardelRio import *
from model.util.CubaProvinces.base.municipaly_SanctiSpiritus import *
from model.util.CubaProvinces.base.municipaly_SantiagodeCuba import *
from model.util.CubaProvinces.base.municipaly_VillaClara import *


class Provinces_Municipaly ():
	def __init__ (self):
		self.__provinces = {

			"Isla de la Juventud**" : municipaly_IsladelaJuventud ,
			"Pinar del Rio" : municipaly_PinardelRio ,
			"Artemisa" : municipaly_Artemisa  ,
			"La Habana" : municipaly_LaHabana ,
			"Mayabeque" : municipaly_Mayabeque ,
			"Matanzas" : municipaly_Matanzas ,
			"Cienfuegos" : municipaly_Cienfuegos  ,
			"Villa Clara" : municipaly_VillaClara ,
			"Sancti Spíritus" : municipaly_SanctiSpiritus ,
			"Ciego de Ávila" : municipaly_CiegodeAvila  ,
			"Camagüey" : municipaly_Camaguey  ,
			"Las Tunas" : municipaly_LasTunas ,
			"Granma" : municipaly_Granma  ,
			"Holguín" : municipaly_Holguin ,
			"Santiago de Cuba" : municipaly_SantiagodeCuba ,
			"Guantánamo" : municipaly_Guantanamo 

		}
		# i comment it to save memory and becouse i will not use it 
		#				i think ther is a better way to do it
		"""
		self.__provinces_West = {
			"Isla de la Juventud" : municipaly_IsladelaJuventud ,
			"Pinar del Rio" : municipaly_PinardelRio ,
			"Artemisa" : municipaly_Artemisa  ,
			"La Habana" : municipaly_LaHabana ,
			"Mayabeque" : municipaly_Mayabeque ,
			"Matanzas" : municipaly_Matanzas ,
		}
		self.__provinces_Center = {
			"Cienfuegos" : municipaly_Cienfuegos  ,
			"Villa Clara" : municipaly_VillaClara ,
			"Sancti Spíritus" : municipaly_SanctiSpiritus ,
			"Ciego de Ávila" : municipaly_CiegodeAvila  ,
		}
		self.__provinces_East = {
			"Camagüey" : municipaly_Camaguey ,
			"Las Tunas" : municipaly_LasTunas ,
			"Granma" : municipaly_Granma ,
			"Holguín" : municipaly_Holguin ,
			"Santiago de Cuba" : municipaly_SantiagodeCuba ,
			"Guantánamo" : municipaly_Guantanamo ,
		}
		"""

	@ property
	def provinces (self):
		return list(self.__provinces)

	@ property
	def municipaly (self):
		return	  self.__provinces["Isla de la Juventud**"] \
				+ self.__provinces["Pinar del Rio"] 		\
		 		+ self.__provinces["Artemisa"] 				\
				+ self.__provinces["La Habana"]	 			\
				+ self.__provinces["Mayabeque"] 			\
				+ self.__provinces["Matanzas"] 				\
				+ self.__provinces["Cienfuegos"]	 		\
				+ self.__provinces["Villa Clara"] 			\
				+ self.__provinces["Sancti Spíritus"]	 	\
				+ self.__provinces["Ciego de Ávila"]	 	\
				+ self.__provinces["Las Tunas"] 			\
				+ self.__provinces["Camagüey"] 				\
				+ self.__provinces["Granma"]				\
				+ self.__provinces["Holguín"]				\
				+ self.__provinces["Santiago de Cuba"] 		\
				+ self.__provinces["Guantánamo"]			





#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#							 SETERS PER PROVINCES 
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------



	@ property
	def IsladelaJuventud  (self):
		return self.__provinces["Isla de la Juventud**"]
	




	@ property
	def PinardelRio (self):
		return self.__provinces["Pinar del Rio"]
	
	@ property
	def Artemisa (self):
		return self.__provinces["Artemisa"]
	
	@ property
	def LaHabana (self):
		return self.__provinces["La Habana"]
	

	@ property
	def Mayabeque (self):
		return self.__provinces["Mayabeque"]
	
	@ property
	def Matanzas (self):
		return self.__provinces["Matanzas"]








	@ property
	def Cienfuegos (self):
		return self.__provinces["Cienfuegos"]
	

	@ property
	def VillaClara (self):
		return self.__provinces["Villa Clara"]
	

	@ property
	def SanctiSpiritus (self):
		return self.__provinces["Sancti Spíritus"]
	

	@ property
	def CiegodeAvila (self):
		return self.__provinces["Ciego de Ávila"]
	






	@ property
	def Camaguey (self):
		return self.__provinces["Camagüey"]
	
	@ property
	def LasTunas (self):
		return self.__provinces["Las Tunas"]
	
	@ property
	def Granma (self):
		return self.__provinces["Granma"]
	
	@ property
	def Holguin (self):
		return self.__provinces["Holguín"]
	
	@ property
	def SantiagodeCuba (self):
		return self.__provinces["Santiago de Cuba"]
	
	@ property
	def Guantanamo (self):
		return self.__provinces["Guantánamo"]
	



	def check (self, province , municipaly):
		if municipaly in self.__provinces[ province ]:
			return True 
		else:
			return False

