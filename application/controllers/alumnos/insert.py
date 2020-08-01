import web 
import app 
import application.models.model as personas

model_personas = personas.Personas()
render=web.template.render('application/views/alumnos')

class Insert():

    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self):
        try:
            form = web.input()
            matricula = form.matricula
            name = form.name
            primero = form.primero
            segundo = form.segundo
            edad = form.edad
            fecha = form.fecha
            sexo = form.sexo
            estado = form.estado
            model_personas.insert(matricula,name,primero,segundo,edad,fecha,sexo,estado)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return render.insert()