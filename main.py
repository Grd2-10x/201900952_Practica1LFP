import json
import re
import webbrowser


def __init__(self, Promedio, Nombre, Edad, Activo ):
    self.Promedio = Promedio
    self.Nombre = Nombre
    self.Edad = Edad
    self.Activo = Activo

def inicio():
  razon=True
  while(razon):
      ingreso = input("ingrese comando: ")
      entrada = ingreso.split(maxsplit=1)
      instruccion = entrada [0].lower()

if instruccion == "CARGAR":
      charge(entrada[1])
elif instruccion == "SELECCIONAR":
  print("No hay archivos cargados ")
  inicio()
  elif instruccion == "CUENTA":
  print("No hay archivos cargados ")
  inicio()
  elif instruccion == "MAXIMO":
  print("No hay archivos cargados ")
  inicio()
  elif instruccion == "MINIMO":
  print("No hay archivos cargados ")
  inicio()
  elif instruccion == "REPORTAR":
  print("No hay archivos cargados ")
  inicio()
 elif instruccion == "SALIR":
    razon=False
    print("Saliste del Menu de comandos")
    else:
     print("Comando equivocado")

  Array=[]

class Dato:
    Nombre=''
    Edad=0
    Activo=True
    Promedio=0.0

    def Cargando(direcc):
        with open(direcc) as content:
            arch = json.load(content)
            for archs in arch:
                x = Dato(archs.get('nombre'), archs.get('edad'), archs.get('activo'), archs.get('promedio'))
                Array.append(x)

    def charge(routes):
        chain = routes.split(', ')
        for direcc in chain:
            Cargando(direcc)
        print("Carga exitosa")
        menu()


def menu():
    razon = True
    while (razon):
        ingreso = input("ingrese comando: ")
        entrada = ingreso.split(maxsplit=1)
        instruccion=entrada[0].upper()
  if instruccion == "CARGAR":
     charge(entrada[1])
    elif instruccion == "SELECCIONAR":
         select(entrada[1])
  elif instruccion == "CUENTA":
      print('la cuenta de registros es:'+ str(len(Array)))
    elif instruccion == "MAXIMO":
            maxs(entrada[1])
    elif instruccion == "MINIMO":
            mins(entrada[1])
    elif instruccion == "REPORTAR":
            reportweb(int(entrada[1]))
   elif instruccion == "SUMA":
      adicion(entrada[1])
    elif instruccion == "SALIR":
    razon = False
    print("Saliste del Menu de comandos")
  else:
       print("Comando equivocado")

    def select(cadena):
        Promed = False
        Name = False
        Age = False
        state = False
        elegir = cadena.split('')
        opcion = elegir[0].replace(' ', '')
        if opcion == '*':
            Promed = True
            Name = True
            Age = True
            state = True
        else:
            atrib = opcion.split(',')
            for x in atrib:
                if x == 'promedio':
                    Promed = True
                elif x == 'nombre':
                    Name = True
                elif x == 'edad':
                    Age = True
                elif x == 'activo':
                    state = True

                else:
                    print('Opcion desconocida ' + x)
            res = ''
            for x in Array:
                if Promed == True:
                    a = str(x.Promedio)
                    res = res + " Promedio: " + a
                if Name == True:
                    res = res + " Nombre: " + x.Nombre
                if Age == True:
                    ed = str(a.Edad)
                    res = res + " Edad: " + ed
                if state == True:
                    if a.Activo == True:
                        res = res + " Activo"
                    elif a.Activo == False:
                        res = res + " Inactivo"

                print(res)
                res = ""
  def adicion(valor):
      if valor == 'Promedio':
          sumprom = 0.0
          for x in Array:
              sumprom = sumprom + x.Promedio
          print('La suma es: ' + str(sumprom))
          
      elif valor == 'Edad':
        sumval=0
        for a in Array:
            sumval = sumval+a.Edad
        print('La suma es: '+str(sumval))





def mins(valor):
    if valor == 'Edad':
        data = Array[0].Edad
        for x in Array:
            if data < x.Edad:
                data = x.Edad
        print('El minimo es: ' + str(data))
    elif valor == 'Promedio':
        numero = Array[0].Promedio
        for x in Array:
            if data < x.Promedio:
                data = x.Promedio
        print('El minimo es: ' + str(data))

 def maxs(valor):
            if valor == 'Edad':
                data = Array[0].Edad
                for x in Array:
                    if data > x.Edad:
                        data = x.Edad
                print('El maximo es: ' + str(data))
            elif valor == 'Promedio':
                numero = Array[0].Promedio
                for x in Array:
                    if data > x.Promedio:
                        data = x.Promedio
                print('El maximo es: ' + str(data))

 def reportweb(ammo):
                GG = open("reporte.html", "w")

                fase = """<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>Reporte de Archivos</h2>
  
  <table class="table">
    <thead class="thead-dark">
      <tr>
        <th>Numero</th>
        <th>Promedio</th>
        <th>Nombre</th>
        <th>Edad</th>
        <th>Activo</th>
      </tr>
    </thead> """
                GG.write(fase)

            count = 0
            for a in Array:
                GG.write("<tbody>")
                if count==ammo:
                    break
                else:
                    if a.Activo==False:
  GG.write("<tr> <td>"+str(a.Promedio)+"</td> <td>"+str(a.Nombre)+"</td> <td>"+str(a.Edad)+"</td> <td>False</td> </tr>\n")
                    elif a.Activo == True:
GG.write("<tr> <td>" + str(a.Promedio) + "</td> <td>" + str(a.Nombre) + "</td> <td>" + str(a.Edad) + "</td> <td>True</td> </tr>\n")
              ammo=ammo+1
                GG.write("</tbody>")
                GG.write("</table>")
                GG.write("</body>")
                GG.write("</html>")
                GG.close()
                webbrowser.open_new_tab("reporte.html")

   
