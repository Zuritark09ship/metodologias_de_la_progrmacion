"""
vamos a realizar un programa 

el usuario va a tener un maximo de intentos para coloca bienn el pin 
si usuarionsobrepasa este mazimo de intentos se le va a bloquear la ceunta y el acceso

"""
CORRECT_PIN = "12345"
MAX_ATTEMPTS= 3
attemps=0


while attemps < MAX_ATTEMPTS:
    
    user_input= input(f"ingresa tu pin: ")
 
    if user_input == CORRECT_PIN:
       print("acceso consebido ")
       break
    else:
        attemps+=1
        reamining_attemps = MAX_ATTEMPTS - attemps
        if reamining_attemps >0:
            print("ingresaste un pin valido ")
            print(f"te quedan {reamining_attemps}intenos")
        else:
            print("cuenta blqueada por puto ")