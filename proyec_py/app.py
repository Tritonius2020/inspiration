from Flask import Flask

app = Flask (__name__ )

@app.route ('/')
def Index():
      return 'hola mundo'
@app.route ('/add_contact')
def add_contact ():
     return 'agrega contacto'

if __name__  == '__main__ ':
    app.run (port = 3000, debug = true)