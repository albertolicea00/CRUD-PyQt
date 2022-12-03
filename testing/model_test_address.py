from unittest import TestCase
from model.util.addressClass import *


class Address_Test (TestCase):
	adr1 = Address(["2nd Avenue", 23 , "Holguín", "Gibara" ])
	adr2 = Address(["20 de Mayo", 56 , "Camagüey" , "Camagüey" ])
	adr3 = Address(["San Patricio", 192 , "Villa Clara" , "Caibarién"])

	def test_getters (self):
		self.assertEqual(self.adr1.address_street, "2nd Avenue" )
		self.assertEqual(self.adr1.address_number, '23' )
		self.assertEqual(self.adr1.address_province, "Holguín")
		self.assertEqual(self.adr1.address_municipality, "Gibara" )

		self.assertEqual(self.adr2.address_street, "20 de Mayo" )
		self.assertEqual(self.adr2.address_number, '56' )
		self.assertEqual(self.adr2.address_province, "Camagüey" )
		self.assertEqual(self.adr2.address_municipality, "Camagüey" )

		self.assertEqual(self.adr3.address_street, "San Patricio" )
		self.assertEqual(self.adr3.address_number, '192' )
		self.assertEqual(self.adr3.address_province, "Villa Clara" )
		self.assertEqual(self.adr3.address_municipality, "Caibarién" )

	def test_setters (self):
		self.adr1.address_street = "Maximo Gomez"
		self.adr1.address_number = 14
		self.adr1.address_province = "Cienfuegos"
		self.adr1.address_municipality = "Abreus"
		self.assertEqual(self.adr1.address_street, "Maximo Gomez" )
		self.assertEqual(self.adr1.address_number, 14 )
		self.assertEqual(self.adr1.address_province, "Cienfuegos")
		self.assertEqual(self.adr1.address_municipality, "Abreus" )

		self.adr2.address_street = "20 de Mayo"
		self.adr2.address_number = 56
		self.adr2.address_province = "Camagüey"
		self.adr2.address_municipality = "Esmeralda"
		self.assertEqual(self.adr2.address_street, "20 de Mayo" )
		self.assertEqual(self.adr2.address_number, 56 )
		self.assertEqual(self.adr2.address_province, "Camagüey" )
		self.assertEqual(self.adr2.address_municipality, "Esmeralda" )

		self.adr3.address_street = "San Ramon"
		self.adr3.address_number = 43
		self.adr3.address_province = "Las Tunas"
		self.adr3.address_municipality = "Amancio"
		self.assertEqual(self.adr3.address_street, "San Ramon" )
		self.assertEqual(self.adr3.address_number, 43 )
		self.assertEqual(self.adr3.address_province, "Las Tunas" )
		self.assertEqual(self.adr3.address_municipality, "Amancio" )