import sys
import os
from dotenv import load_dotenv
import psycopg2



class Conection():

    load_dotenv()

    def __init__(self):
        self.__host = os.getenv('DB_HOST')
        self.__port = os.getenv('DB_PORT')
        self.__database = os.getenv('DB_DATABASE')
        self.__user = os.getenv('DB_USERNAME')
        self.__password = os.getenv('DB_PASSWORD')

        self.__conection = None
        self.__cursor = None

        self.__conect()

    def __conect(self):
        try:
            self.__conection = psycopg2.connect(
                host=self.__host,
                port=self.__port,
                database=self.__database,
                user=self.__user,
                password=self.__password
            )
            self.__cursor = self.__conection.cursor()

            print('Database is Connected!')


        except psycopg2.Error as e:
            print("Error while connecting to database: ", e)
            self.__conection = None
            self.__cursor = None


        # finally:
        #     self.__conection.close()
        #     self.__cursor.close()


    def conection(self):
        return self.__conection

    def cursor(self):
        return self.__cursor

