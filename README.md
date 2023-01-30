# UniDef, Proyecto fin curso 1-2 año, Universidad, Camagüey

Título: Sistema de control de la defensa para la Universidad de Camagüey.
Proyecto número 8

Problematica:

  Se desea realizar un sistema en la Universidad de Camagüey para almacenar la información de todas las personas que estudian o trabajan en la universidad para organizarlas para la defensa con su posible ubicación. 
  De los estudiantes se conoce su carné de identidad, nombre completo, sexo, fecha de nacimiento, carrera, año que cursa, promedio docente, dirección y ubicación para la defensa. 
  De los profesores se conoce su carné de identidad, nombre completo, sexo, fecha de nacimiento, departamento, si ha salido al extranjero, categoría docente (Titular, Auxiliar, Asistente o Instructor), categoría científica (Doctor en Ciencias, Master en Ciencias o Ninguna), dirección y ubicación para la defensa. 
  Por otro lado, de las direcciones se registra la calle, el número, el municipio y la provincia. 
  De las posibles ubicaciones para la defensa se registra el nombre, una breve descripción y si es fuera de la universidad. 
  Se conoce que en la universidad hay un listado de personas posibles a movilizar en función de la defensa y una lista de posibles ubicaciones.

Este proyecto permite funciones para: 
  - insertar, actualizar, eliminar y listar los datos de profesores, estudiantes y lugares de ubicación, de forma independiente,
  - obtener el el grado de aptitud para la defensa de cada persona. 
  - determinar el promedio de edad de los profesores de un departamento dado que son de otra provincia y que no han salido al extranjero. 
  - determinar la cantidad de estudiantes de un año dado que son de una provincia dada. 
  - obtener la dirección del profesor más viejo que no vive en el municipio. 
  - obtener un listado con los datos de los profesores de una categoría docente dada que hayan salido al extranjero 

Las herramientas y tecnologías utilizadas para el desarrollo del proyecto fueron: 
  - patrón de diseño de software MVC (Modelo-Vista-Controlador) 
  - PyQT5
  - QTDesigner
  - Python 3.9
  - PostgreSQL
  - modulos para conecciones a la BBDD (dotenv, psycopg2, sys, os, ..)
  - módulos extras de python para optimización y funcionalidades del mismo  (unittest , doctest, datatime, re, numpy, webbrowser, …)
