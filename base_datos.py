#from peewee import *
from peewee import SqliteDatabase, Model, CharField, DateTimeField,TextField, BooleanField
from datetime import datetime as dt

db = SqliteDatabase('nivel_avanzado.db')

class BaseModel(Model):
    class Meta:
        database = db

class Noticia(BaseModel):
    titulo = CharField(unique = True)
    fecha = DateTimeField(default = dt.now)
    descripcion = TextField()
    estado_de_publicacion = BooleanField(default = True)
    
    def __str__(self,):
        return "El título es: " + str(self.titulo)
         
db.connect()
db.create_tables([Noticia])
db.close()
