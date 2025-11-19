cars=["audi","bmw","chevrolet","corvette","tesla"]
for car in cars:
    if car=="bmw" or car  =="tesla" or car == "audi" :
        print(car.upper())
    else:
        print(car)

#condicionales : el condicional es el corazon de un if 
#condicional true
car="bmw"
print(car=="bmw")

car_2="Audi"
print(car_2=="audi") # salida= false

#condicion false
car_2="audi"
print(car_2.lower()=="audi") #salida = true

#comparaciones numericas 
age=18 # = int
print(age==18)# = true

answer=17
if answer !=42:
    print("esa no es la respuesta corectoa. intenta otra vez")

age =19
print(age<21) #true
print(age<=21) #true
print(age>21) # false
print(age>=21) #false

#multiples condiciones
age_0=22
age_1=18
print("multiples condiciones ")
print(age_0>=21 and age_1>=21) # false
print(age_0>=21 or age_1>=18) # true

#¿como preguntar si esta en una lista 
print("\n como preguntar si esta en una lista ")
requested_toppings=["mushrooms","onions","pineapple"]
print("mushrooms" in requested_toppings) # true
print("pepperoni" in requested_toppings) # false

#¿como preguntar si no esta en una lista
banned_users=["andres","carla","juan"]
user="pedro" 
print(user not in banned_users) # true
user="andres"
print(user not in banned_users) # false

#tipos de datos booleanos
game_active=True # los boleanos solo son true y false
can_edit=False


"""
 if stratement 
  if condicion
      do something

   if condicion:
        do something(true)
    else:
         do something(false)

"""

#preguntar la edad del usuario y decirle si tiene la edad suficiente para votar 
#input()
age=int(input("ingresa tu edad: "))#convertir a entero

if age>=18:
    print("tienes la edad suficiente para votar")
else:
    print("no tienes la edad suficiente para votar")

#
#try:
    #age= int(input("escribe tu edad: "))
   
#except:
    age = -1
    #print("error caracter no valido")
#<>
if age >= 100:
    print("tienes mas de un siglo")
elif age >= 18 and age < 100:
    print("eres mayor de edad: ")
elif age >=0 and age < 18:
    print("eres menor de edad ")
else:
    print("eres menor de edad: ")


try :
   age= int(input("escribe tu edad: "))
except :
 print("error, ingresas un caracter no valido")


if age <= 4:
    print("tienes entrada gratuita")
elif age <18 and age >4 :
    print("su entrada es de $200")
elif age >=18:
    print("la entrada cuesta 400")

#multipe if

guisos =["desebrada", "asado", "salsa verde", "pozole"]
if "salsaverde" in guisos:
    print("si hay guisi")
if "asado" in guisos:
    print("si hay guisos")
if "desebrada " in guisos:
    print("si hay guisos")
if "pozole" in guisos:
    print("si hay guisos")
if "tamales" in guisos:
    print("no hay tamales ")

#utilizando varias listas
guisos_disponibles =["desebrada"," mole", "salsa verde"]
guisos_a_ordenar = ["desebrada","mole"]
print("¿que guiso desea ordena?")
for guiso in guisos_a_ordenar:
    print(f"deseo{guiso}")
    if guiso in guisos_disponibles:
        print(f"si tenemos{guiso}")
    else:
        print("no tenemos de ese guiso")
print("realizando pedido...")

