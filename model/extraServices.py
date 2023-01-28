from model.repository import *
import requests


import psycopg2
from database.conection import conection

class extraService ():
    def __init__(self):
        """
        This is the extras Services class of the 'APP' (backups, conection web, ...)

        >>> repo = extraServices()
        None
        """
        self.facebookAL = 'http://'
        self.instagramAL = 'http://'
        self.whastappAL = 'http://'
        self.telegramAL = 'http://'
        self.linkedlnAL = 'http://'

        self.github = 'http://'

    @staticmethod
    def save(path, table):
        filename = path
        result = Repository.getAll('STUDENT')

        with open(file=filename, mode='w+') as file:
            for i in range(len(result)):
                for j in range(len(result[1])):
                    reg = str(result[i][j]) + ' , '

                    file.write(reg)
                file.write("\r")



