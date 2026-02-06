
from libro_modelo import libro_modelo 
from Autor_modelo import autor_modelo
from libros_bd import base_datos_libros 
from Api_datos_autores import  api_lista_autores 

obj_Api_datos_autores = api_lista_autores()




obj_Api = api_lista_autores()
obj_autor = autor_modelo("abel","25/05/1991")
obj_autor2 = autor_modelo("jesus","25/05/1991")
obj_autor3 =  autor_modelo("beltran","25/05/1991")

obj_Api.agregar_autores(obj_autor) 
obj_Api.agregar_autores(obj_autor2)
obj_Api.agregar_autores(obj_autor3)

obj_Api.mostrar_lista_autores()