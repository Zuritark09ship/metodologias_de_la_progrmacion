"""
string variables

un string e de manera sencilla una serie de caracteres .
en python todo lo que se encuentre dentro de comillas simples o dobles 
sera considerado un string.

ejemplos 
"esto es un string"
`esto tambien es un string`

`le dije a un amigo "python es mi lenguaje favorito"`
" el lenguaje `python` lleva el nombre por Mony python , no por la
serpiente"



"""
name= "clase de programacion"
print(name) 
# title 
print(name.title())
print(name)
"""
un metodo es una accion que python puede realizar en un fragmento de datos
o sobre una variable
El punto despues de un variable seguido de el metodo python dice que se tiene que ejecutar el metodo 
python de la variable name.
  todos los metodos van seguidos por parentesis porque en ocasiones necesitan informacion adicional 
  la cual la infromacion irira dentro de los parentsis 
  En esta ocasion el metodo .title() no requiere infromacion para ejecutarse 

"""
print("metodo upper:", name.upper())
print("metodo lower:",name.lower())

# concatenacion de STRINGS
first_name= "max"
last_name = "zurita"
full_name = first_name +" "+ last_name
print(full_name)
print(full_name.title())

#whitespaces
"""
 un whittespaces se refiere a cualquier caracter que no se imprime , es decir , un espacio,
 tabuladores y finales de linea . los whitespaces se utilizan comunmente para organizar las salidas 
 de tal manera que sea mas amigable de leer o ver para el usuario 

   ejemplo : 
   - tabulador :\t
  - salto de linea :\n
"""
print("whitespace tabulador")
print("python")
print("\t python")
print("\t\tpython")

print("ehitspace salato de linea:")
print("lenguages :\n\tpython\nC\n\tjavascript")

#eliminacion de espacios en blanco 
programming_languages = "python"
print(programming_languages)
print(programming_languages.rstrip()) 
print(programming_languages.lstrip())
print(programming_languages.strip()) 

#sintax error con string
message= "una fortaleza de python es su comunidad"
print(message)

#f-strings
famous_person = "tailor swift "
message ="{famous_person} una vz dijo me voy al oxxo en avion "
print(f"{famous_person.upper()}una vez dijo me viy al oxxo en avion")

#actividad 
"""
elige el nombre de una persona famosa .
eligue una cita famosa de esa persona
iguala ambos strings a una variable

1)realiza la concatenacion utilizando el signo de suma
2)realiza la concatenacion utiliza f-strings
"""
famous_person= "Luis Humberto Navejas"
print(famous_person)
message= "{una vez dijo `mi cuerpo se aleja del lugar que me hizo etraño mas ese lugar no me deja pues soy hijo del proaño`"
print(f"{famous_person}una vez dijo `mi cuerpo se aleja del lugar que me hizo etraño mas ese lugar no me deja pues soy hijo del proaño`")
print(famous_person + message)

#number 
"""
enteros 
 los podemos ,sumar(+), resta(-)
 multiplicae (*)y dividir (/).

"""
number_1= 24
number_2= 2
suma = number_1 + number_2
resta= number_1- number_2
division = number_1/number_2
multiplicacion= number_1*number_2
potencia = number_1**2
modulo = number_1%number_2
print("suma: ", suma, type(suma))
print("resta: ", resta, type(resta))
print("division : ", division , type (division) )
print("multiplicacion : ", multiplicacion,type(multiplicacion))
print("potencia: ",modulo,type(potencia))
print("modulo",modulo,type(modulo))

"""
jerarquia de operaciones 
2+3*4 =14
(2+3)*4=20
"""

"""
floats
 python llama floats a cualquier numero con un punto decimal

los podemos ,sumar(+), resta(-)
 multiplicae (*)y dividir (/)
 les podemos aplicar potencias (**2,**3,**4,...),
 """
print(0.1+0.1)
print(0.2-0.2)
print(0.1*0.1)
print(0.2/0.2)

#imprimir edad de alguien
age=18
message = "max tiene :"+ str(age) + "años"
print(message)
"""
type error : esto significa que python no puede reconocer el tipo de 
informacion que se esta utilizando 
"""

"""
buil-in
methods =print(),str()type()
stringhs 
y investigar que es  zen de python
"""

