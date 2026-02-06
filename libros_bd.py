class libros_bd:
    def  __init__(self):
         self.base_datos_libro =[]

    def guardar_libro(self,obj_libro):
         self.base_datos_libro.append(obj_libro)
      
    def extender_libros(self,nueva_lista):
         self.base_datos(nueva_lista)

    def insertar_libros(self,obj_libros, pos_index):
         self.base_datos_libro.insert(pos_index,obj_libros)

    def remover_libro(self, obj_libros):self.base_datos_libros.remove(obj_libros)    

    def eliminar_libros(self, pos_index):
         self.base_datos_libros. pop(pos_index)

    def buscar_libros(self, nombre_obj):
         self .base_datos_libros.index(nombre_obj)

    def contar_libros(self, valor):
         self.base_datos_libro.count(valor)


    def  ordenar_libros(self):
         self.base_datos_libro.sort()

    def invertir_libros(self):
         self.base_datos_libro.converse()

    def   mostrar_info(self):
          
          
          for in  range(len(self, base_datos_libros)) # type: ignore
              tematica=self, base_datos_libros[i] get_tematica() # type: ignore
              fecha=self.base_datos_libro[i] get_fecha() # type: ignore
              print(f"tematica libro:{tematica } - fecha libro:{fecha} ,")    
       
        
                            

         