"""
las listas tambien
 se puede almacenear numero y de echo so ideales para esto
 python ofrece una gran cantidad de herramientas que ayudan a trbajar eficientemente con listas 

 """
print("numeros del 0 al 9 ")
for value in range(10): # 10 numeros del 0 al 9
 print(value)

print("numeros del 1 al 9 ")
for value in range(1,10): # 10 numeros del 1 al 9
 print(value)

print("numeros inpares del 1 al 9 ")
for value in range(1,10,2): # 10 numeros del 1 al 9 de 2 en 2
 print(value)

print("numeros pares del 0 al 8 ")
for value in range(0,10,2): # 10 numeros del 0 al 9 de 2 en 2
 print(value)

print("creando una lista de numeros del 0 al 9 ")
numbers = list(range(10)) # crea una lista de numeros del 0 al 9
print(numbers)
numbers_list=list(numbers)

print("creando una lista de numeros dela tabla del 9 ")
for value in range(0,91,9): 
 print(value)

#cuadrados de los primeros 10 numeros 

squares= []
for numero in range(1,11):
    square = numero**2
    squares.append(square)
print(squares)

#metodo min()
digits=[1,2,3,4,5,6,7,8,9,0]

