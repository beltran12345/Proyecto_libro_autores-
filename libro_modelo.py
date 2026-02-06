class libro_modelo:
   def __init__(self,fecha,genero,cantidad_hojas,tematica):
       
    self.fecha = fecha
    self.cantidad_hojas = cantidad_hojas
    self.tematica =tematica
    self.genero = genero
       
    def get_cantidas_hojas(self):
        return self.cantidad_hojas

#hacer responsabilidad dela clase

    def registro_cantidad_hojas(self):
        mensaje = " se registra la base de datos"
        return mensaje


    def registrar_fecha_libro(self):
        mensaje = " las fechas se rejistratros de la b d"
        return mensaje
    
    def mostrar_cantidada_hojas(self):
        mensaje = "el libro tiene la siguiente cantidad:"
        mensaje = mensaje + self.get_cantidad_hojas()
        return mensaje


    def registrar_tematica(sefl):
    # sql
        mensaje = "tematica registrada"
        return mensaje

    def mostrar_tematica(self):
     mensaje = self.get_tematica()
     return mensaje

    def info_autor(self, obj_autor):
     obj_autor.ver_info()