import web 
import app 
import application.models.model as personas

model_personas = personas.Personas()


render=web.template.render('application/views/alumnos')

class List():

    def GET(self):
      try:
        result = model_personas.select()
        return render.list(result)
      except Exception as e:
        return "Error" + str(e.args)