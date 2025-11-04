#lists
"""

las listas nos ayudan a guardar informacion en algun lugar , 
la cantidad que tengas ya sean pocos elementos o millones de elementos .

se recomienda nombrar una variable de tipo lista en plural.
en python los corchetes[] define una lista,suselementos van separadas por comas 
ejemplo:
"""
bicycles=["trek","canondale","redline","specialized","giant"]
print(bicycles) 

print(bicycles[0].title())

#Los indices comienzan en 0
print(bicycles[4].title())

#accediendo al ultimo elemento
print(bicycles[-1].title())
print(bicycles[-2].title())
print(bicycles[-5].title())

#utilizando valores de la lista
message= "mi primera bicicleta fue una mercury " + bicycles[4].title()+"."
print(message)

message_f = f"mi primera bicicleta fue una ,{bicycles[4].title()}"
print(message_f)

#agreagar elementos de una lista
print("ahgregar elementos a una lista ")
print(bicycles)
print("\n")

print("metodo de listas para agregar elementos: lista_name .append(element)")
bicycles.append("ducatti")
print(bicycles)