import web 
import app 

render=web.template.render('application/views/alumnos')

class Formulario():

    def GET(self):
      try:
        return render.formulario()
      except Exception as e:
        return "Error" + str(e.args)