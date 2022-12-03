from unittest import TestCase
import datetime
from model.personClass import *

class Person_Test (TestCase):
	psn1 = Person ("99020742326" , ["Manuel","Lopez"] , "Male" , ["Puerto Principe", 333, "La Habana" ,"Arroyo Naranjo"] , ["Vectores2" , "This is a little description1..." , False])
	psn2 = Person ("00010957241" , ["Frank","Cespedes"] , "Male" , ["Bembeta", 666, "Holguín" ,"Gibara"] , ["Vectores3" , "This is a little description2..." , False])
	
	def test_getters (self):
		self.assertEqual(self.psn1.ID, "99020742326" )
		self.assertEqual(self.psn1.fullname.name, "Manuel" )
		self.assertEqual(self.psn1.fullname.last_name, "Lopez" )
		self.assertEqual(self.psn1.gender, "Male" )
		self.assertEqual(self.psn1.birthday, datetime.datetime(1999, 2, 7) )
		self.assertEqual(self.psn1.age, 23 )
		self.assertEqual(round(self.psn1.degree_acttitude_base),  8)
		self.assertEqual(self.psn1.degree_acttitude_base, 7.699999999999999 )

		self.assertEqual(self.psn2.ID, "00010957241" )
		self.assertEqual(self.psn2.fullname.name, "Frank" )
		self.assertEqual(self.psn2.fullname.last_name, "Cespedes" )
		self.assertEqual(self.psn2.gender, "Male" )
		self.assertEqual(self.psn2.birthday, datetime.datetime(2000, 1, 9) )
		self.assertEqual(self.psn2.age, 22 )
		self.assertEqual(self.psn2.degree_acttitude_base, 7.8 )



	def test_setters (self):
		self.psn1.ID = "01030767989"
		self.psn1.gender = "Other"
		self.psn1.fullname.name= "Ariel"
		self.psn1.fullname.last_name= "Domingues"
		self.assertEqual(self.psn1.ID, "01030767989" )
		self.assertEqual(self.psn1.fullname.name, "Ariel" )
		self.assertEqual(self.psn1.fullname.last_name, "Domingues" )
		self.assertEqual(self.psn1.gender, "Other" )
		self.assertEqual(self.psn1.birthday, datetime.datetime(2001, 3, 7) )
		self.assertEqual(self.psn1.age, 21 )
		self.assertEqual(self.psn1.degree_acttitude_base,  7.699999999999999)

		self.psn2.ID = "00010944123"
		self.psn2.gender = "Famale"
		self.psn2.fullname.name = "Susana"
		self.psn2.fullname.last_name= "Valentina"
		self.assertEqual(self.psn2.ID, "00010944123" )
		self.assertEqual(self.psn2.gender, "Famale" )
		self.assertEqual(self.psn2.fullname.name, "Susana" )
		self.assertEqual(self.psn2.fullname.last_name, "Valentina" )
		self.assertEqual(self.psn2.birthday, datetime.datetime(2000, 1, 9) )
		self.assertEqual(self.psn2.age, 22 )
		self.assertEqual(self.psn2.degree_acttitude_base,  7.8)
