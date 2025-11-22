"""
   Las tuples son listas de ekementos que no
   cambian de tamaño. Las tuples son inmutables.

   Se utilizan los () para definir una tupla
"""
rectangle_measurements = (200, 50) #El primer elemento es indice 0, el segundo elemento es indice 1
#(largo, ancho)
print(rectangle_measurements[0])
print(rectangle_measurements[1])

for measure in rectangle_measurements:
    print(measure)

#print(dir(rectangle_measurements)) #built-in-dir

# Regresandp a las listas
cars = ["bwm", "porche", "masda"]
print(cars)
cars[0] ='bmw'
cars[1] ='porsche'
cars[2] ='mazda'
print(cars)

rectangle_measurements = (200, 50)
# rectangle_measumerents[0]=300 #No se puede
# rectangle_measumerents[1]=100 #No se puede
rectangle_measumerents = (300, 100)