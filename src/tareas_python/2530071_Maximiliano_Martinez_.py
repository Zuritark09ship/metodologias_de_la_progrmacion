#Alumno: Maximiliano Martinez
#matricula: 2530071
#Grupo: A-105

#3. CONVENCIONES (NAMING Y OUTPUT EN INGLÉS)
from curses import ALL_MOUSE_EVENTS


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
temp_c_input = input("Enter temperature in Celsius: ").strip()

if temp_c_input == "":
    print("Error: invalid input")
else:
    try:
        temp_c = float(temp_c_input)

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


"7.2 Problem 2: Work hours and overtime payment"
hours_worked_text = input("Enter your hours worked: ").strip()
hourly_rate_text = input("Enter your hourly rate: ").strip()

if hours_worked_text == "" or hourly_rate_text == "":
    print("ERROR")
else:
    try:
        hours_worked = float(hours_worked_text)
        hourly_rate = float(hourly_rate_text)

        if hours_worked < 0 or hourly_rate < 0:
            print("ERROR")
        else:
            regular_hours = min(hours_worked, 40)
            time_extra = max(hours_worked - 40, 0)
            regular_pay = regular_hours * hourly_rate
            time_extra_pay = time_extra * (hourly_rate * 1.5)
            total_pay = regular_pay + time_extra_pay
            has_overtime = hours_worked > 40

            print(f"regular_pay: {regular_pay}")
            print(f"time_extra_pay: {time_extra_pay}")
            print(f"total_pay: {total_pay}")
            print(f"has_overtime: {str(has_overtime).lower()}")
    except ValueError:
        print("ERROR")

"7.3 Problem 3: Discount eligibility with booleans  "

purchase_total_text = input("Enter purchase total: ")
is_student_text = input("Is student? (YES/NO): ")
is_senior_text = input("Is senior? (YES/NO): ")

# Validation: purchase_total must be float and >= 0.0
try:
    purchase_total = float(purchase_total_text)
except:
    print("Error: invalid input")
    exit()

if purchase_total < 0.0:
    print("Error: invalid input")
    exit()


is_student_text = is_student_text.strip().upper()
is_senior_text = is_senior_text.strip().upper()


if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
    print("Error: invalid input")
    exit()

is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "YES")

discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)


if discount_eligible:
    final_total = purchase_total * 0.9
else:
    final_total = purchase_total


print(f"Discount eligible: {str(discount_eligible).lower()}")
print(f"Final total: {final_total}")



"7.4 Problem 4: Basic statistics of three integers"

N1= input("seet your number A: ")
N2= input("seet your number B:")
N3= input("seet ypur number C :")

if N1 and N2 and N2 == "" :
    print("ERROR")
else:
    try:
        sum= (N1+N2+N3)
        print(sum)
        average_value = sum / 3
        print(average_value)
        max_valuable = max(N1,N2,N3)
        print(max_valuable)
        min_valuable = min(N1,N2,N3)
        print(min_valuable)
        if  all_eve(N1%2 =0)and (N2%2 =0) and (N3%2 =0)
    except:
       print(all_even)
    

