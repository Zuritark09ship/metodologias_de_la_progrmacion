#Alumno: Maximiliano Martinez
#matricula: 2530071
#Grupo: A-105

"CONVENCIONES (NAMING Y OUTPUT EN INGLÉS)"
from shlex import split
from turtle import title


MIN_NAME_LENGTH = 2
REQUIRED_EMAIL_CHAR = "@"
 
user_name = input("seet your email :").strip()
print(user_name) 

if user_name == "":
    print("error")
elif (REQUIRED_EMAIL_CHAR not in user_name):
    print("invalid your email must contain @")
elif(len(user_name) < MIN_NAME_LENGTH):
    print("your email is too short")
elif user_name :
    print("Result:")
    print(f"Name: {user_name.title()}")
    print(f"Name length: {len(user_name)}")
    print(f"Email: {user_name.lower()}")
    print(f"Email length: {len(user_name)}")

"RESUMEN EJECUTIVO (COMENTARIOS EN EL .py)"

#1. ¿Qué es un string en Python (tipo de dato, inmutabilidad)?

#Un string es un tipo de dato que representa texto en Python. Está formado por una secuencia de caracteres
#y es inmutable, lo que significa que no puede modificarse directamente una vez creado; cualquier cambio genera un nuevo string.

#2. ¿Qué operaciones básicas se pueden realizar: concatenar, obtener longitud,
#extraer sub-cadenas, buscar patrones, reemplazar texto?

#con los strings se pueden hacer operaciones como concatenar texto, obtener la longitud con len(), 
#extraer subcadenas usando slicing, buscar patrones mediante in o find(), y reemplazar texto con métodos como replace().

#3. ¿Por qué es importante validar y normalizar texto de entrada (por ejemplo, correos, nombres, contraseñas)?

#Validar y normalizar entradas garantiza que los datos sean correctos, seguros y consistentes; evita errores futuros, 
#previene formatos inválidos y ayuda a procesar información como correos, nombres o contraseñas de manera confiable.

#4. ¿Qué cubrirá tu documento?

#El documento incluirá la descripción de cada problema, el diseño de las entradas y salidas, las validaciones aplicadas 
#y el uso de métodos de string, además de casos de prueba completos acompañados del código correspondiente.



"5. PRINCIPIOS Y BUENAS PRÁCTICAS"

# Los strings son inmutables: cualquier modificación genera una nueva cadena en lugar de cambiar la original.
# Es buena práctica normalizar la entrada usando strip() y lower() antes de compararla.
# Evita los "números mágicos" en índices; documenta siempre qué está extrayendo cada slice.
# Usa los métodos de string en lugar de reescribir lógica básica manualmente.
# Las validaciones deben ser claras y ordenadas: primero verificar si la entrada está vacía y luego revisar el formato.
# Escribe código legible: utiliza nombres de variables descriptivos y mensajes de error que se entiendan fácilmente.


"6. PLANTILLA POR PROBLEMA (PARA COMENTARIOS)"

# --------------------------------------------------
# Problem X: validate name 
# Description:This program asks the user for a name, removes extra spaces,
# validates that it is not empty and meets the minimum length, 
# and finally prints the formatted name and its length.
#
# Inputs:
#   -user_name (string)
# Outputs:
#   - result
#   - formatted name
#   - name length
# Validations:
#   - input not valid if empty
#   - input must meet minimum length
#   - input must be cleaned with strip()
# Test cases:
#   1) Normal: "maria"
#   2) Border: "MA" (minimum length)
#   3) Error: ""


#7. PROBLEMAS

#7.1 Problem 1: Full name formatter (name + initials)
#Descripción:
#Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
#1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
#2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

full_name= input("Seet your full name :")
clean_name = full_name.strip()

if len(clean_name) == 0:
    print("error")
else:
    name_parts = clean_name.split()

if len(name_parts) < 2:
        print("Error: invalid input (two words required)")
else: formatted_name = clean_name.title()
initials = ""
for word in name_parts:
    initials += word[0].upper() + "."
print(f"Formatted name: {formatted_name}")
print(f"Initials: {initials}")

#7.2 Problem 2: Simple email validator (structure + domain)

#Descripción:
#Valida si una dirección de correo tiene un formato básico correcto:
#- Contiene exactamente un '@'.
#- Después del '@' debe haber al menos un '.'.
#- No contiene espacios en blanco.
#Si el correo es válido, también muestra el dominio (la parte después de '@').

email_text = input("Enter email: ".strip())

if len(email_text) == 0:
    print("Valid email: false")
elif " " in email_text:
    print("Valid email: false")
elif email_text.count("@") != 1:
    print("Valid email: ")
else:
    email_2 = email_text.find("@")
    email_2 = email_text[email_2 + 1:]
    if "." not in email_2:
        print("Valid email: false")
    else:
        print("Valid email: true")
        print(f"Domain: {email_2}")


#7.3 Problem 3: Palindrome checker (ignoring spaces and case)
#Descripción:
#Determina si una frase es un palíndromo, es decir, se lee 
#igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

phrase = input (" seet your phrase: ")
phrase_clean = phrase.strip()

if len(phrase_clean)== 0:
   print("error")
else:
    normalized=phrase_clean.replace(" ","").lower()
if len(normalized) < 3:
    print("palindrome : false")
else:
     reversed_phrase = normalized[::-1]
     if normalized == reversed_phrase:
         print("palindrome : true")
     else:
         print("palindrome : false")

#7.4 Problem 4: Sentence word stats (lengths and first/last word)
#Descripción:
#Dada una oración, el programa debe:
#1) Normalizar espacios (quitar espacios al principio y al final).
#2) Separar las palabras por espacios.
#3) Mostrar:
# - Número total de palabras.
#- Primera palabra.
#- Última palabra.
#- Palabra más corta y más larga (por longitud).

sentences = input("Seet your sentence: ")
clear_sentence = sentences.strip()

if len(clear_sentence) == 0:
    print("error")
else:
    words = clear_sentence.split()
if len(words) == 0:
    print("error")
else:
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    short = words[0]
    long = words[0]
    for word in words:
        if len(word) < len(short):
            short = word
        if len(word) > len(long):
            long = word
print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Shortest word: {short}")
print(f"Longest word: {long}")

#7.5 Problem 5: Password strength classifier
#Descripción:
#Clasifica una contraseña como "weak", "medium" o "strong" 
#según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

pasword = input("seet your pasword:".strip())
if len(pasword) == 0:
    print("error")  
else: 
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

for ch in pasword:
   if ch.isupper():
       has_upper = True
   elif ch.islower() :
        has_lower = True
   elif ch.isdigit():
       has_digit = True
else:
    if not ch.isalnum():
        has_symbol = True

length_ok = len(pasword) >= 8
if length_ok and has_upper and has_lower and has_digit and has_symbol:
    print(" Password strength: strong")
else:
    categories = sum([has_upper, has_lower, has_digit , has_symbol])
    if length_ok and categories >= 2:
        print(" pasword strength: medium")
    else:
        print("pasword strength: weak")

#7.6 Problem 6: Product label formatter (fixed-width text)
#Descripción:
#Dado el nombre de un producto y su precio, genera una etiqueta en una sola 
# línea con el siguiente formato:

product_name = input("seet your product name: ").strip()
price_value = input("ingrese el precio :").strip()

if len(product_name) == 0:
    print("Error: el nombre del producto no puede estar vacío.")
else:
    try:
        price_num = float(price_value)
        if price_num <= 0:
            print("Error: el precio debe ser positivo.")
        else:
            price_str = str(price_num)
            label = f"Product: {product_name} | Price: ${price_str}"

            if len(label) > 30:
                label = label[:30]
            elif len(label) < 30:
                label = label + (" " * (30 - len(label)))
            print(f"Label: \"{label}\"")
    except ValueError:
        print("Error: el precio debe ser un número.")

#8. CONCLUSIONES (COMENTARIOS AL FINAL)

# Las cadenas son esenciales porque casi toda la entrada del usuario llega como texto y debemos procesarla correctamente.
# Funciones como lower(), strip() y split() permiten limpiar, uniformar y separar información para analizarla sin errores.
# Normalizar texto antes de compararlo es clave para evitar diferencias por mayúsculas, espacios o formatos inconsistentes.
# Las validaciones ayudan a detectar datos incompletos o incorrectos y evitan que el programa falle o produzca resultados basura.
# Aprendí que los strings son inmutables, por lo que cada modificación genera una nueva cadena y por eso usamos slices para obtener partes específicas.
# También comprendí que join() es útil para volver a unir palabras y que los slicing facilitan extraer fragmentos sin alterar el original.
# Todo esto permite crear programas más robustos y confiables al procesar datos textuales.


#9. REFERENCIAS (MÍNIMO 5) – EN COMENTARIOS

# References:
# 1) Python documentation – Built-in Types: Text Sequence Type — str
# 2) Python Official Docs – String Methods
# 3) W3Schools – Python Strings Tutorial
# 4) "Automate the Boring Stuff with Python" – Capítulos sobre manejo de texto
# 5) Real Python – Articles on String Manipulation and Validation
# 6) Programiz – Python String Examples and Explanations
