from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class menu_contact(QDialog):
	def __init__(self, controler):
		self.__do = controler
		QDialog.__init__(self)
		uic.loadUi("view/ui/Help__contact.ui",self)

		self.instagramAL = 'https://www.instagram.com/alberto.licea00'
		self.telegramAL = 'http:/t.me/albertolicea00/'
		self.linkedlnAL = 'http://www.linkedin.com/in/albertolicea00'
		self.githubAl = 'https://github.com/albertolicea00'

		self.telegramRafa = 'https:/t.me/showmakerlol/'
		self.githubRafa = 'https://github.com/showhack'

# ------------------------------------------------------
#			BUTTONS ACTIONS
# ------------------------------------------------------
		self.btn_githubRafa.clicked.connect(lambda: self.__do.connect_web(self.githubRafa))
		self.btn_telegramRafa.clicked.connect(lambda: self.__do.connect_web(self.telegramRafa))

		self.btn_githubAl.clicked.connect(lambda: self.__do.connect_web(self.githubAl))
		self.btn_linkedlnAl.clicked.connect(lambda: self.__do.connect_web(self.linkedlnAL))
		self.btn_instagramAl.clicked.connect(lambda: self.__do.connect_web(self.instagramAL))
		self.btn_telegramAl.clicked.connect(lambda: self.__do.connect_web(self.telegramAL))
