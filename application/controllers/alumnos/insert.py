import web 
import app 

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
            print(form)
            print(form.matricula)
            print(form.name)
            print(form.primero)
            print(form.segundo)
            print(form.edad)
            print(form.fecha)
            print(form.sexo)
            print(form.estado)
            return render.insert()
        except Exception as e:
            return "Algo salio mal en la inserción!"