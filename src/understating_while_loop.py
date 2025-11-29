##while infinito
"""
 si el usuario escribe un numero entre 25 y 50 entonces esta dentro del rango
 y salir de while 

"""
while True:
    try:
        number = int(input("ingrese un numero: "))

        if 10 <= number <=20 :
            print("estas dentro del rango")
            break
        else:
            print("estas fuera de rango")
    except ValueError:
        print("se ha introducido una variable ")
    except KeyboardInterrupt:
        print("programa terminandopor el usuario ")
        break
print("saliste de while yupii")