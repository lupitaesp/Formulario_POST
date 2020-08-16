import mysql.connector


class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='lnnyn4x50lgaurnl',
                password='mxjd2imd3ju02t06',
                host='etdq12exrvdjisg6.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='hd2trui8dy2v6dj2'
            )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)
    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM personass;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'matricula':row[1],
                    'nombre':row[2],
                    'apellido_pa':row[3],
                    'apellido_ma':row[4],
                    'edad':row[5],
                    'fecha_na':row[6],
                    'sexo':row[7],
                    'estado':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result
    def view(self,matricula):
        try:
            self.connect()
            query = ("SELECT * FROM personass WHERE matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                diccionario = {
                    "id_alumno":row[0],
                    "matricula":row[1],
                    "nombre":row[2],
                    "apellido_pa":row[3],
                    "apellido_ma":row[4],
                    "edad":row[5],
                    "fecha_na":row[6],
                    "sexo":row[7],
                    "estado":row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
    def insert(self, matricula, nombre, apellido_pa, apellido_ma, edad, fecha_na, sexo, estado):
        try:
            self.connect()
            query = ("INSERT INTO personass (matricula,nombre,apellido_pa,apellido_ma,edad,fecha_na,sexo,estado) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula,nombre,apellido_pa,apellido_ma,edad,fecha_na,sexo,estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    def update(self, matricula, nombre,apellido_pa, apellido_ma, edad, fecha_na,sexo,estado):
        try:
            self.connect()
            query = ("UPDATE personass SET nombre=%s,apellido_pa=%s,apellido_ma=%s,edad=%s,fecha_na=%s,sexo=%s,estado=%s WHERE matricula=%s;")
            values = (nombre,apellido_pa,apellido_ma,edad,fecha_na,sexo,estado,matricula)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    def delete(self, matricula):
        try:
            self.connect()
            query = ("DELETE FROM personass WHERE matricula= %s;")
            values = (matricula,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Personas()
objeto.connect() 
#print(objeto.delete("1718110388"))
#objeto.update("1718110388","Lupita","Espinoza","Riveros","22","2000/04/05","Femenino","Hidalgo")
for row in objeto.select():
    print(row)