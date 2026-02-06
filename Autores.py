from datetime import date


class autor_modelo:
   def __init__(self,dato_nombre,dato_fecha):
      self.nombre = dato_nombre
      self.edad = dato_fecha



   def registrar_dato(self):
      mensaje ="se registran los datos"
      return mensaje
   
   def buscar_autor(self,dato_buscar):
      mensaje =" autor existe en la base de dato" + dato_buscar
      return mensaje
   
   def dar_baja_autor(self):
      mensaje =" el autor esta inactivo" + date
      return mensaje
   

   def ver_info(self):
      print(f"nonbre:{self.nombre:} - fecha:{self.fecha}")
      

      