#Alumno: Maximiliano Martinez
#matricula: 2530071
#Grupo: A-105

#3. CONVENCIONES (NAMING Y OUTPUT EN INGLÉS)
TAX_RATE = 0.15

hours_worked_input = input("Enter hours worked: ").strip()
hourly_rate_input = input("Enter hourly rate: ").strip()

if hours_worked_input == "" or hourly_rate_input == "":
    print("Error: invalid input")
else:
    try:
        hours_worked = float(hours_worked_input)
        hourly_rate = float(hourly_rate_input)

        if hours_worked < 0 or hourly_rate < 0:
            print("Error: invalid input")
        else:
            gross_salary = hours_worked * hourly_rate
            tax_amount = gross_salary * TAX_RATE
            net_salary = gross_salary - tax_amount

            print(f"Total hours: {hours_worked}")
            print(f"Gross salary: {gross_salary}")
            print(f"Tax amount: {tax_amount}")
            print(f"Net salary: {net_salary}")

    except ValueError:
        print("Error: invalid input")

 
"4. RESUMEN EJECUTIVO (COMENTARIOS EN EL .py)"


# Los tipos int y float representan números enteros y números con decimales; 
# se diferencian en que los float permiten valores reales.

# Un booleano (True/False) indica si una condición es verdadera o falsa
# y normalmente se obtiene mediante comparaciones como >, <, == o >=.

# Validar rangos es importante para evitar errores lógicos, valores imposibles
# y cálculos incorrectos.

# Evitar la división entre cero es esencial porque genera un error que detiene el programa.

# El documento cubrirá: descripción de cada problema, sus entradas y salidas, 
# las validaciones aplicadas y el uso de int, float y bool.

# También mostrará cómo estos tipos permiten realizar cálculos, tomar decisiones lógicas
# y manejar condiciones de forma segura.

"5. PRINCIPIOS Y BUENAS PRÁCTICAS (COMENTARIOS)"

# Usar el tipo int es ideal para contadores o cantidades enteras, mientras que float se utiliza cuando se necesitan valores con decimales.
# Para evitar repetir expresiones complejas, es mejor guardar los resultados en variables intermedias y así mantener el código claro.
# Siempre se debe validar que los datos numéricos sean correctos antes de operar, como verificar que horas y salarios no sean negativos.
# Los nombres de variables deben ser descriptivos y los mensajes de salida claros para que el usuario entienda los resultados.
# También es importante documentar cómo se interpretan los valores booleanos, indicando qué representa true y qué representa false en cada caso.


#6. PLANTILLA POR PROBLEMA (PARA COMENTARIOS)


# Problem X: <short title>
# Description:
# - <line 1 explaining the purpose of the program>
# - <line 2 explaining what it calculates or determines>
# - <optional line 3–4 for extra detail>

# Inputs:
# - <input_name>: <type and meaning>
# - <input_name>: <type and meaning>

# Outputs:
# - <description of output 1>
# - <description of output 2>

# Validations:
# - <validation rule 1>
# - <validation rule 2>
# - <validation rule 3>

# Test cases:
# 1) Normal: <a valid and typical case>
# 2) Border: <a limit case, e.g., minimal acceptable value>
# 3) Error: <invalid input that should trigger error handling>

#7. PROBLEMAS

#7.1 Problem 1: Temperature converter and range flag

temperature_c = input ("seet your temperature in celsius:").strip()

if temperature_c == "":
    print("Error: invalid input")
else:
    try:
        temp_c = float(temperature_c)
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15

        if temp_k < 0.0:
            print("Error: invalid input")
        else:
            is_high_temperature = (temp_c >= 30.0)
     
            print(f"Fahrenheit: {temp_f}")
            print(f"Kelvin: {temp_k}")
            print(f"High temperature: {str(is_high_temperature).lower()}")

    except ValueError:
        print("Error: invalid input")

