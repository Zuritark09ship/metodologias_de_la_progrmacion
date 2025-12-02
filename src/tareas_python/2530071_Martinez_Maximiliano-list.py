# Alumno: Maximiliano Martinez
# Matrícula: 2530071
# Grupo: A-105

"""
------------------------------------------------------------
RESUMEN EJECUTIVO
------------------------------------------------------------
Este documento presenta seis problemas diseñados para practicar colecciones 
de Python: listas, tuplas y diccionarios. Una lista es una colección ordenada 
y mutable, útil cuando es necesario agregar, eliminar o modificar elementos. 
Una tupla es ordenada pero inmutable, lo que la hace ideal para registros fijos 
como coordenadas o conjuntos de datos constantes. Un diccionario almacena pares 
clave-valor, lo que permite búsquedas rápidas mediante una clave descriptiva. 
Cada problema incluye diseño de entrada y salida, reglas de validación y casos 
de prueba que demuestran aplicaciones prácticas como listas de la compra, 
catálogos de productos, gestión de calificaciones, frecuencias de palabras y 
una agenda de contactos sencilla. El documento destaca cómo las colecciones 
permiten organizar, procesar y recuperar datos de forma eficiente en programas reales.
"""

"""
------------------------------------------------------------
GOOD PRACTICES AND PRINCIPLES (STRINGS)
------------------------------------------------------------
- Strings are immutable: any modification creates a new string.
- Always normalize input with strip() and lower() before comparing it.
- Avoid magic numbers when slicing; document each slice clearly.
- Prefer built-in string methods instead of rewriting basic logic.
- Validation order matters: first check empty input, then structure.
- Write clean code with descriptive variable names and clear messages.
"""

"""
------------------------------------------------------------
Problem 1
------------------------------------------------------------
Description:
This program works with a shopping list created from an input string.
It creates an initial list, adds a new item, counts the total items,
and checks if a specific product is in the list.
"""

initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter new item to add: ").strip()
search_item = input("Enter item to search: ").strip()

if initial_items_text == "" or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list = [item.strip() for item in initial_items_text.split(",")]
    items_list.append(new_item)

    total_items = len(items_list)
    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", total_items)
    print("Found item:", str(is_in_list).lower())

"""
------------------------------------------------------------
Problem 2
------------------------------------------------------------
This program reads the coordinates of two points in 2D space,
creates two tuples, calculates the Euclidean distance, 
and computes the midpoint between both points.
"""

x1_text = input("Enter x1: ")
y1_text = input("Enter y1: ")
x2_text = input("Enter x2: ")
y2_text = input("Enter y2: ")

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
except:
    print("Error: invalid input")
else:
    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

"""
------------------------------------------------------------
Problem 3
------------------------------------------------------------
This program manages a small product catalog with a dictionary.
It reads a product name and quantity, checks if the product exists,
and calculates the total price.
"""

product_prices = {
    "apple": 10.0,
    "milk": 15.5,
    "bread": 12.0
}

product_name = input("Enter product name: ").strip()
quantity_text = input("Enter quantity: ")

if product_name == "":
    print("Error: invalid input")
else:
    try:
        quantity = int(quantity_text)
        if quantity <= 0:
            print("Error: invalid input")
        else:
            if product_name in product_prices:
                unit_price = product_prices[product_name]
                total_price = unit_price * quantity

                print("Unit price:", unit_price)
                print("Quantity:", quantity)
                print("Total:", total_price)
            else:
                print("Error: product not found")
    except:
        print("Error: invalid input")

"""
------------------------------------------------------------
Problem 4
------------------------------------------------------------
This program manages student grades using a dictionary.
It calculates the average grade and determines if the student passed.
"""

students_grades = {
    "Alice": [90, 85, 88],
    "Bob": [60, 72, 68],
    "Mark": [70]
}

student_name = input("Enter student name: ").strip()

if student_name == "":
    print("Error: invalid input")
else:
    if student_name in students_grades:
        grades_list = students_grades[student_name]

        if len(grades_list) == 0:
            print("Error: student not found")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= 70.0

            print("Grades:", grades_list)
            print("Average:", round(average, 2))
            print("Passed:", str(is_passed).lower())
    else:
        print("Error: student not found")

"""
------------------------------------------------------------
Problem 5
------------------------------------------------------------
This program reads a sentence, splits it into words, counts the frequency
of each word, and identifies the most common one.
"""

sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    for p in ",.!?;:":
        sentence = sentence.replace(p, "")

    words_list = sentence.lower().split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}
        for word in words_list:
            freq_dict[word] = freq_dict.get(word, 0) + 1

        most_common = max(freq_dict, key=freq_dict.get)

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common)

"""
------------------------------------------------------------
Problem 6
------------------------------------------------------------
Simple contact book using a dictionary.
Supports actions: ADD, SEARCH, DELETE.
"""

contacts = {
    "Alice": "1234567890",
    "Bob": "5551112222",
    "Carlos": "9876543210"
}

action_text = input("Action (ADD / SEARCH / DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    name = input("Name: ").strip()

    if not name:
        print("Error: name cannot be empty")
    else:

        if action_text == "ADD":
            phone = input("Phone: ").strip()

            if not phone:
                print("Error: phone cannot be empty")
            else:
                contacts[name] = phone
                print("Contact saved:", name + ",", phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")

"""
------------------------------------------------------------
CONCLUSIÓN
------------------------------------------------------------
Las listas, las tuplas y los diccionarios tienen diferentes propósitos en Python.
Las listas permiten agregar, eliminar y modificar datos; son ideales cuando la 
información cambia con frecuencia. Las tuplas sirven para almacenar datos fijos 
que no deben modificarse, como coordenadas. Los diccionarios destacan por su 
velocidad en búsquedas, ya que cada valor está asociado a una clave única. 
Combinarlos permite construir estructuras más completas, como catálogos, 
registros de estudiantes y agendas de contactos.
"""

"""
------------------------------------------------------------
REFERENCIAS
------------------------------------------------------------
https://ellibrodepython.com/tuplas-python
https://elpythonista.com/tuplas-en-python-tuple
https://ellibrodepython.com/listas-en-python
https://ebac.mx/blog/listas-en-python
https://ellibrodepython.com/diccionarios-en-python
"""
