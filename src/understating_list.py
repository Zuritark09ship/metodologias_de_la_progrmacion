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

"""
agregar elemet¡ntos a una lista
 -apepend (): agregar elementos al final de la lista 
"""

print("\n--- Agregar elementos  a lista metodo append()---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki', 'ducati'] 

"""
agregar elementos a una lista en una posicion especifica
 -insert(): agregar elementos en una posicion especifica
"""
print("\n--- Agregar elementos  a lista metodo insert()---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles) #salida: ['ducati', 'honda', 'yamaha', 'suzuki']
"""
elimar elementos de una lista
 -del : elimina un elemento en una posicion especifica

"""
print("\n--- Eliminar elementos  a lista metodo del ---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) #salida: ['yamaha', 'suzuki']

"""
 -pop(): elimina el ultimo elemento de la lista y lo devuelve   

 """
print("\n--- Eliminar elementos  a lista metodo pop() ---") 
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) #salida: ['honda', 'yamaha']
print(f"la motocicleta eliminada es: {popped_motorcycle}") #salida: suzuki

"""
 -pop(i): elimina un elemento en una posicion especifica y lo devuelve  
 """
print("\n--- Eliminar elementos  a lista metodo pop(i) ---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki']
first_motorcycle = motorcycles.pop(0)
print(motorcycles) #salida: ['yamaha', 'suzuki']
print(f"la primera motocicleta eliminada es: {first_motorcycle}") #salida

"""
 -remove(): elimina un elemento por su valor  
 """
print("\n--- Eliminar elementos  a lista metodo remove() ---")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("ducati")
print(motorcycles) #salida: ['honda', 'yamaha', 'suzuki']
print("\n")

"""
sort- ordenar una lista permanentemente
"""
print("\n--- ordenar una lista metodo sort() ---")  
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) #salida: ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #salida: ['audi', 'bmw', 'subaru', 'toyota']
print("\n--- ordenar una lista metodo sort(reverse=True) ---")
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) #salida: ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) #salida: ['toyota', 'subaru', 'bmw', 'audi']

"""
sorted-ordenar una lista temporalmente
"""
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) #salida: ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars)) #salida: ['audi', 'bmw', 'subaru', 'toyota']
print(cars) #salida: ['bmw', 'audi', 'toyota', 'subaru']


print("\n--- ordenar una lista temporalmente metodo sorted(reverse=True) ---")
cars = ["bmw", "audi", "toyota", "subaru"]
print(sorted(cars, reverse=True)) #salida: ['toyota', 'subaru', 'bmw', 'audi']
print(cars) #salida: ['bmw', 'audi', 'toyota', 'subaru']

""""
ejemplo
"""
Students=["ana","juan","pedro","maria","luis"]
print(Students)
desired_student=input("que estudiante deseas borrar ")
Students.remove(desired_student.strip().lower())
print(Students)
print("tu has eliminado :",desired_student)
Students.reverse()
print(Students)

print(len(Students))

