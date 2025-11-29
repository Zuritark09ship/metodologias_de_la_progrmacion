"""
Docstring for understating_whilr_loop_centinel
  un programa que:
  - cuente cuantos numeros ha ingresado el usuario
  - realice la suma de estos numeros
  -me diga cual es el minimo de los numeros ingresados 
  - me diga cual es el maximo de los numeros
""" 
counter =0
smn_numbers =0.0
minimum= None
maximum = None

while True:
    print("escribe exit para salir :"),
    user_input=input("ingrese una cantidad (MXN): ").strip()
    
    if user_input==  "exit":
        break
    try:
        Value = float(user_input)
    except ValueError :
       print("caracter invalido porfavor ingrese un numero ")
    except KeyboardInterrupt:
        print("salida manual")
        break

        counter + 1 =1 #counter = counter + 1 (contador)
    sum_quantities += Value 

    if minimum is None or Value < minimum:
        minimum =Value
    
    if maximum is None or Value < maximum
       maximum = Value

print("cantidad de numeros ingresados :", counter)
print("suma de cantidades :", sum_quantities)
print("maximo de cantidades: ", maximum)
print("minimo de cantidades ", minimum)
     