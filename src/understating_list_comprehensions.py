"""
squares=[]
for value in range(0,11)
    square=value**2
    squares.append(square)
print(suquares)
"""
"""
una list comprenhrtion combina el ciclo for y la creacion
de nuevos elementos en una sola linea y automaticamente agregar cada nuevo elemento a la lista , es decir,
sinutilizar el metodo append
"""
squares= [value**2 for value in range(0,11)]

# para los numerps pares entre el 0 y el 100
evens_range= [value for value in range(0,101,2)]

evens_if= [value for value in range(0,101) if value%2==0]
print(evens_if)
