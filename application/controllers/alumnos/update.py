import web 
import app 

import application.models.model as personas

model_personas = personas.Personas()

render=web.template.render('application/views/alumnos')

class Update():

    def GET(self, matricula):
      try:
        result = model_personas.view(matricula)[0]
        #print(result)
        return render.update(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, matricula):
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
            result = model_personas.update(matricula,name,primero,segundo,edad,fecha,sexo,estado)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"
