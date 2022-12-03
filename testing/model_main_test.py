import unittest
from testing.model_test_address import *
from testing.model_test_placetolocation import *
from testing.model_test_person import *
from testing.model_test_teacher import *
from testing.model_test_student import *
from testing.model_test_repository import *
from testing.model_test_repository_service import *


class Testing :
	"""
	>>> test = Testing()
	>>> test.start()
	OK
	"""
	def start (self):
		unittest.main()