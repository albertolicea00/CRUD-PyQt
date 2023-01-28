import psycopg2
from database.conection import conection

class Repository ():
    def __init__(self):
        """
        This is the principal Repository class of the 'The University'
        where all students, teachers and places to location are inserted, deleted, updated and showed, & can search a id of each object

        >>> repo = Repository()
        None
        """
        pass

    @staticmethod
    def maxIndexAddress():
        #  retorna el id maximo en la tabla de direcciones

        try:
            with conection.cursor() as cursor:

                cursor.execute("SELECT MAX(id) FROM ADDRESS")    # retorna el id maximo en la tabla de direcciones
                addid = cursor.fetchall()[0][0] 				 # obtiene el id de la direccion agregada

                return addid
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")

    @staticmethod
    def getAll(table):
        try:
            with conection.cursor() as cursor:

                query = "SELECT * FROM {}, ADDRESS WHERE {}.address = ADDRESS.id".format(table, table)

                cursor.execute(query)
                return cursor.fetchall()

        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
    # ----------------------------------------------------------
    #		    QUERY			QUERY			QUERY
    # ----------------------------------------------------------

    def getPlace(self, plcid="ID", plcname="name", att="*"):
        # retorna las columnas(att) de un lugar de ubicacion segun el nombre pasado por parametro
        # att:str => 'name, inuniversity'

        try:
            with conection.cursor() as cursor:

                query = "SELECT " + att + " FROM PLACETOLOCATION WHERE ID=" + plcid
                if plcname != "name":
                    query += " and name='" + plcname + "'"

                cursor.execute(query)
                values = cursor.fetchall()

                # if len(values) == 0:
                # 	raise()

                return values
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")

    def getAddress(self, addid="ID", att="*"):
        #  retorna las columnas(att) de un lugar de ubicacion segun el nombre pasado por parametro
        # att:str => 'name, inuniversity'

        try:
            with conection.cursor() as cursor:
                query = "SELECT " + att + " FROM ADDRESS WHERE ID=" + addid
                cursor.execute(query)
                values = cursor.fetchall()

                # if len(values) == 0:
                # 	raise()

                return values
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")


    def getStudent(self, stdid="ID", att="*"):
        try:
            with conection.cursor() as cursor:

                query = "SELECT " + att + " FROM STUDENT WHERE ID=" + stdid
                cursor.execute(query)
                values = cursor.fetchall()
                return values

        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        # finally:
        # 	conection.close()
        # return self.__possible_students


    def getTeacher(self, tchid="ID", att="*"):
        try:
            with conection.cursor() as cursor:

                query = "SELECT " + att + " FROM TEACHER WHERE ID=" + tchid
                cursor.execute(query)
                values = cursor.fetchall()
                return values

        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")

    # ----------------------------------------------------------
    #			 SHOW			 SHOW			 SHOW
    # ----------------------------------------------------------

    @property
    def Students (self):
        """
        >>> repo.Students
        [object_student1, object_student2, object_student3 ...]
        """
        try:
            with conection.cursor() as cursor:

                query = "SELECT * FROM STUDENT"
                cursor.execute(query)
                std = cursor.fetchall()
                return std

        except psycopg2.Error as e:
            raise Exception("Error in database: ", e)
        # finally:
        # 	conection.close()
        # return self.__possible_students

    @property
    def Teachers (self):
        """
        >>> repo.Teachers
        [object_student1, object_teacher2, object_teacher3 ...]
        """
        return self.__possible_teachers

    @property
    def Places (self):
        """
        >>> repo.Places
        [object_student1, object_place, 2object_place ...3]
        """
        try:
            with conection.cursor() as cursor:

                query = "SELECT * FROM PLACETOLOCATION"
                cursor.execute(query)
                plcs = cursor.fetchall()
                return plcs

        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        # finally:
        # 	conection.close()

    # ----------------------------------------------------------
    #			INSERT			INSERT			INSERT
    # ----------------------------------------------------------

    def __insertAddress (self, address):
        """
        >>> repo.__insertAddress ( addresslist )
        id
        """
        try:
            with conection.cursor() as cursor:

                query = "INSERT INTO ADDRESS (street, number, province, municipality) " \
                        "VALUES('{}','{}','{}','{}')".format(address.address_street, address.address_number, address.address_province, address.address_municipality)
                cursor.execute(query)

                conection.commit()
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")

    def insertStudent (self, std):
        """
        >>> repo.insertStudent (object_student)
        None
        """
        # try:
        # obtiene el id de la direccion agregada
        self.__insertAddress(std.address)
        addid = Repository.maxIndexAddress()
        # except:

        # obtiene el id del lugar de ubicacion escogido
        plcid = self.getPlace(plcname=std.place_to_location.place_name, att='id')[0][0]


        try:
            with conection.cursor() as cursor:

                query = "INSERT INTO STUDENT VALUES('{}','{}','{}','{}','{}','{}', {},'{}','{}', {})".format( std.ID,
                    std.fullname.name, std.fullname.last_name, std.gender, addid, plcid, std.degree_acttitude, std.carrer, std.year_of_carrer, std.average )

                cursor.execute(query)
                conection.commit()

        # excepts de validacion a otros problemas a validar ....
        except psycopg2.errors.UniqueViolation:
            raise Exception(f"The student already exist in the repository")
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
            # validar si ocurre algun problema elimine el address insertado (crear un metodo para eliminar addrsss en privado)
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")




    def insertTeacher (self, tch):
        """
        >>> repo.insertStudent (object_teacher)
        None
        """
        # obtiene el id de la direccion agregada
        self.__insertAddress(tch.address)
        addid = Repository.maxIndexAddress()
        # except:

        # obtiene el id del lugar de ubicacion escogido
        plcid = self.getPlace(plcname=tch.place_to_location.place_name, att='id')[0][0]

        try:
            with conection.cursor() as cursor:

                query = "INSERT INTO TEACHER VALUES('{}','{}','{}','{}','{}','{}', {},'{}','{}', '{}', '{}')".format( tch.ID,
                    tch.fullname.name, tch.fullname.last_name, tch.gender, addid, plcid, tch.degree_acttitude, tch.departament, tch.left_cuba, tch.teaching_category,
                    tch.scientific_category)

                cursor.execute(query)
                conection.commit()

        # ecepts de validacion a otros problemas a validar ...
        except psycopg2.errors.UniqueViolation:
            raise Exception(f"The teacher already exist in the repository")
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
            # validar si ocurre algun problema elimine el address insertado
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")




    def insertPlace (self ,plc):
        """
        >>> repo.insertPlace (object_place)
        None
        """

        try:
            with conection.cursor() as cursor:
                query = "INSERT INTO PLACETOLOCATION (name, description, inuniversity) VALUES('{}','{}','{}')".format(plc.place_name, plc.place_description, plc.place_in_university)
                
                cursor.execute(query)
                conection.commit()
                
        except psycopg2.errors.UniqueViolation:
            raise Exception	(f"The place already exist in the repository")
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")

    # ----------------------------------------------------------
    #			UPDATE			UPDATE			UPDATE
    # ----------------------------------------------------------

    def updateStudent (self, old_std_ID , new_std ):
        """
        >>> repo.updateStudent (object_place.id , object_place)
        None
        """

        # actualiza la direccion
        oldstdid= "'" + old_std_ID + "'"
        oldidadd = self.getStudent(stdid=oldstdid, att="address")[0][0]
        self.__updateAddress(oldidadd, new_std.address)

        # obtiene el id del lugar de ubicacion escogido
        plcid = self.getPlace(plcname=new_std.place_to_location.place_name, att='id')[0][0]

        try:
            with conection.cursor() as cursor:
                query = "UPDATE STUDENT SET id = '{}', name = '{}', lastname = '{}', gender = '{}', placetolocation = {}, degreeacttitude = {}, carrer = '{}', yearofcarrer = {}, average = {}" \
                        "WHERE id = '{}'".format(new_std.ID, new_std.fullname.name, new_std.fullname.last_name, new_std.gender, plcid, new_std.degree_acttitude, new_std.carrer, new_std.year_of_carrer, new_std.average, old_std_ID)

                cursor.execute(query)
                conection.commit()

        except psycopg2.errors.UniqueViolation:
            raise Exception	(f"The student already exist in the repository")
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")
    # ----------------------------------------------------------


    def __updateAddress (self, oldid, newadd):
        try:
            with conection.cursor() as cursor:

                query = "UPDATE ADDRESS SET street='{}', number='{}', province='{}', municipality='{}' WHERE id={}".format(newadd.address_street, newadd.address_number, newadd.address_province, newadd.address_municipality, oldid)
                cursor.execute(query)

                conection.commit()
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")


    def updateTeacher (self, old_tch_ID , new_tch ):
        """
        >>> repo.updateTeacher (object_place.id , object_place)
        None
        """
        #actualiza la direccion
        oldtchid = "'" + old_tch_ID + "'"
        oldidadd = self.getTeacher(tchid=oldtchid, att="address")[0][0]
        self.__updateAddress(oldidadd, new_tch.address)

        #obtiene el id del lugar de ubicacion escogido
        plcid = self.getPlace(plcname=new_tch.place_to_location.place_name, att='id')[0][0]

        try:
            with conection.cursor() as cursor:
                query = "UPDATE TEACHER SET id = '{}', name = '{}', lastname = '{}', gender = '{}', placetolocation = {}, degreeacttitude = {}, departament = '{}', teachingcategory = '{}', scientificcategory = '{}' " \
                        "WHERE id = '{}'".format(new_tch.ID, new_tch.fullname.name, new_tch.fullname.last_name, new_tch.gender, plcid, new_tch.degree_acttitude, new_tch.departament, new_tch.teaching_category, new_tch.scientific_category, old_tch_ID)
                cursor.execute(query)
                conection.commit()

        except psycopg2.errors.UniqueViolation:
            raise Exception( f"The student already exist in the repository" )
        except psycopg2.Error as e:
            raise Exception( f"Error in database: {e}" )
        finally:
            with conection.cursor() as cursor:
                cursor.execute( "rollback" )

    def updatePlace (self, old_plc_id , new_plc ):
        """
        >>> repo.updatePlace (object_place.name , object_place)
        None
        """

        try:
            with conection.cursor() as cursor:
                query = "UPDATE PLACETOLOCATION SET name = '{}', description = '{}', inuniversity = {} " \
                        "WHERE name = '{}'".format(new_plc.place_name, new_plc.place_description, new_plc.place_in_university, old_plc_id)

                cursor.execute(query)
                conection.commit()

        except psycopg2.errors.UniqueViolation:
            raise Exception(f"The place already exist in the repository")
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")

    # ----------------------------------------------------------
    #			DELETE			DELETE			DELETE
    # ----------------------------------------------------------
    def __removeAddress (self, add_ID):
        try:
            with conection.cursor() as cursor:
                cursor.execute("DELETE FROM ADDRESS WHERE id = {}".format(add_ID))
                conection.commit()

        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")




    def removeStudent (self, std_ID):		#quisas aqui le pase solo el CI(ID)

        std_ID = "'" + std_ID + "'"
        add_ID = self.getStudent(stdid=std_ID, att="address")[0][0]

        try:
            with conection.cursor() as cursor:

                query = "DELETE FROM STUDENT WHERE id = {}".format(std_ID)
                cursor.execute(query)
                conection.commit()

        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")

        # elimina la direccion asociada a este estudiante => funciona como un 2 factor de verificacion ya que la direccion elimina en cascada
        # (en la vida real el que elimina en casacada deberia ser el estudiante) pero por problemas de compatibilidad entre la bbdd y el proyecto
        # viejo no se pudo (se complicaria demaciado empezar a cambiar cosas a esta altura)
        self.__removeAddress(add_ID)



    def removeTeacher (self, tch_ID):
        """
        >>> repo.removeTeacher (object_place)
        None
        """
        tch_ID = "'" + tch_ID + "'"
        add_ID = self.getTeacher( tchid=tch_ID, att="address" )[0][0]

        try:
            with conection.cursor() as cursor:

                query = "DELETE FROM TEACHER WHERE id = {}".format( tch_ID )
                cursor.execute( query )
                conection.commit()

        except psycopg2.Error as e:
            raise Exception( f"Error in database: {e}" )
        finally:
            with conection.cursor() as cursor:
                cursor.execute( "rollback" )

        self.__removeAddress( add_ID )


    def removePlace (self, plc_name):
        """
        >>> repo.removePlace (object_place)
        None
        """
        try:
            with conection.cursor() as cursor:
                query = "DELETE FROM PLACETOLOCATION WHERE name = '{}'".format(plc_name)

                cursor.execute(query)
                conection.commit()
        except psycopg2.errors.ForeignKeyViolation as e:
            raise Exception(f"You can't remove this places becouse is assigned in a PERSON \nto continueremove the place: update it from student/teacher CRUD")
        except psycopg2.Error as e:
            raise Exception(f"Error in database: {e}")
        finally:
            with conection.cursor() as cursor:
                cursor.execute("rollback")