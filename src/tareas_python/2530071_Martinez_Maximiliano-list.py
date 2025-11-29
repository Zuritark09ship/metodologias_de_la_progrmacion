#Alumno: Maximiliano Martinez
#matricula: 2530071
#Grupo: A-105

#RESUMEN EJECUTIVO
"""
¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
- ¿Qué significa que una lista sea mutable y una tupla inmutable?
- ¿Cómo se usan los diccionarios para asociar claves con valores?
- ¿Qué cubrirá tu documento?: descripción de cada problema, diseño de entradas y 
salidas, validaciones aplicadas y uso de listas, tuplas y diccionarios en contextos 
prácticos (por ejemplo, catálogos, registros, estadísticas).
"""
# PRINCIPIOS Y BUENAS PRÁCTICAS
# - Usar listas cuando se necesite agregar, eliminar o modificar elementos con frecuencia.
# - Usar tuplas para datos que no cambian, como coordenadas, fechas o configuraciones fijas.
# - Usar diccionarios cuando se requiere asociar claves con valores, permitiendo búsquedas rápidas
#   mediante identificadores como "name", "age", "id" o "price".
# - Evitar modificar una lista mientras se recorre con un for, a menos que se controle cuidadosamente el proceso.
# - Usar nombres de claves descriptivos en los diccionarios para mejorar la claridad del código.
# - Mantener el código legible, ordenado y con mensajes claros para el usuario.

#7.1 Problem 1: Shopping list basics (list operations)

#Description:
# Este programa trabaja con una lista de productos creada a partir
# de una cadena de texto separada por comas. Permite agregar un
# nuevo producto al final y verificar si un producto específico
# existe dentro de la lista.

initial_items=input("seet your item :").strip()

if initial_items == "":
    print("ERROR")
else:
    items_list= [item.strip() for item in initial_items.slip(",") if item.strip() != ""]

    new_item = input("seet yout new item ").strip()
    search_item = input("seet your product :").strip()

    if new_item =="" or search_item == "":
        print("ERROR")
    else:
     initial_items.append(new_item)
     len_list= len(items_list)

     is_in_list = ( search_itemin  initial_items)

print("items list :",initial_items)
print("total items :", len_list)
print("found item :",str(is_in_list).lower())

#7.2 Problem 2: Points and distances with tuples

#Descripción:
#Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
# Crear dos tuplas point_a y point_b a partir de entradas numéricas.
# Calcular la distancia euclidiana entre ambos puntos.
# Crear una nueva tupla midpoint con el punto medio entre ellos.

try:
   x1=float (input("seet your number x1 : ").strip())
   y1=float (input("seet your number y1 :").strip())
   x2=float (input("seet your number x2 :").strip())
   y2=float (input("seet your number y2 :").strip())

   point_a=(x1 , x2)
   point_b=(y1,y2)

   distance =((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
   midpoint= ((x1 + x2) / 2, (y1 + y2) / 2),
   print("Point A:", point_a)
   print("Point B:", point_b)
   print("Distance:", distance)
   print("Midpoint:", midpoint)

except ValueError:
    print("Error: invalid input")