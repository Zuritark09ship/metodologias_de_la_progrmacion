### FUNCIONES
#Las funciones son bloques de codigo para realizar 
# una tarea en especifico 

# cuando quereos realizae ña tarea que se ha definido en la funcion
#tenemos que llamar el nombre de la 
#funcion que realiaza la accion 
"""
sinraxis de una funcion 
   def nombre_funcion()
   acciones 
           
        ejemplo : vamos a definir una funcion que de un saludo a christopher    
"""
def gretting_crhistophe():
    for i in range (0,10):
     print("hello crhistopher")

gretting_crhistophe()

#ejemplo de una funcion que genere el nombre completo 
# de una persona y lo regrese


#parametros posicionales 
def create_full_name(first_name, last_name, middle_name =""):
   full_name = f"{first_name.strip()} {middle_name.strip()} {last_name.strip()}".title()
   return full_name 

first_name = input("seet your first name :")
middle_name = input("seet yout middle name :")
last_name = input("seet yout las name : ")

generated_full_name = create_full_name(
         first_name.lower(),
        middle_name.lower(),
        last_name.lower())
print(generated_full_name)

#argumentos llave 
generates_fullname2 = create_full_name(
   middle_name = user_middle_name,
   first_name = User_first_name,
   last_name = user_last_name
)
