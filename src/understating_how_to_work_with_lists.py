#trabajando con listas

"""
 recorrer una lista sin importar la cantidad
 de elemetnos que tenga
"""
magicians = ["ron","hermione","harry"]

print(magicians[0],magicians[1],magicians[2])

for magician in magicians :
   print(magician)
   print(magician.upper())
   print(f"{magician.title()} eso fue un gran hechizo")
   print(f"\t {magician.lower()} no podemos esperar a ver el siguiente hechizo")

print("Gracias a todos por participar en el show")
"""
python utiliza la indentacion para definir bloques de codigo
 en lugar de llaves {} o palabras clave como begin end
"""
#no olvidemos identar
magicians = ["ron","hermione","harry"] 
for magician in magicians :
    print(magician)
   
    print(f"i can't wait to see the next trick , {magician.title()}")

#identacion inecesaria 
message = "Hello Python "
print(message)

