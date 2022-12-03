from unittest import TestCase
from model.util.placetolocationClass import *

class Placetolocation_Test (TestCase):
	plc1 = Place_to_location(["CDP-34" , "This is a little description1..." , True])
	plc2 = Place_to_location(["RJK-98" , "This is a little description2..." , True])
	plc3 = Place_to_location(["Vector-2" , "This is a little description3..." , False])
	
	def test_getters (self):
		self.assertEqual(self.plc1.place_name, "CDP-34" )
		self.assertEqual(self.plc1.place_description, "This is a little description1..." )
		self.assertEqual(self.plc1.place_in_university, True )

		self.assertEqual(self.plc2.place_name, "RJK-98" )
		self.assertEqual(self.plc2.place_description, "This is a little description2..." )
		self.assertEqual(self.plc2.place_in_university, True )

		self.assertEqual(self.plc3.place_name, "Vector-2" )
		self.assertEqual(self.plc3.place_description, "This is a little description3..." )
		self.assertEqual(self.plc3.place_in_university, False )

	def test_setters (self):
		self.plc1.place_name = "A-59124"
		self.plc1.place_description = "Bla bla bla"
		self.plc1.place_in_university = False
		self.assertEqual(self.plc1.place_name, "A-59124" )
		self.assertEqual(self.plc1.place_description, "Bla bla bla" )
		self.assertEqual(self.plc1.place_in_university, False )

		self.plc2.place_name = "Civica-5090"
		self.plc2.place_description = "blablabla"
		self.plc2.place_in_university = False
		self.assertEqual(self.plc2.place_name, "Civica-5090" )
		self.assertEqual(self.plc2.place_description, "blablabla" )
		self.assertEqual(self.plc2.place_in_university, False )

		self.plc3.place_name = "Hospital-5A"
		self.plc3.place_description = "BLABLABLABLA"
		self.plc3.place_in_university = False
		self.assertEqual(self.plc3.place_name, "Hospital-5A" )
		self.assertEqual(self.plc3.place_description, "BLABLABLABLA" )
		self.assertEqual(self.plc3.place_in_university, False )