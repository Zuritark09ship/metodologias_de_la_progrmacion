#Alumno: Maximiliano Martinez
#matricula: 2530071
#Grupo: A-105

#3. CONVENCIONES (NAMING Y OUTPUT EN INGLÉS)
# Algorithm: weekly_pay_calculation

hours_text = input("Enter hours worked: ")
rate_text = input("Enter hourly rate: ")

# Validate numeric conversion
try:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)
except:
    print("Error: invalid input")
    exit()

# Validate ranges
if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input")
    exit()

# Separate regular and overtime hours
regular_hours = min(hours_worked, 40)
overtime_hours = max(hours_worked - 40, 0)

# Calculations
regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * hourly_rate * 1.5
total_pay = regular_pay + overtime_pay

# Boolean
has_overtime = hours_worked > 40

# Output
print(f"Regular pay: {regular_pay}")
print(f"Overtime pay: {overtime_pay}")
print(f"Total pay: {total_pay}")
print(f"Has overtime: {has_overtime}")


 
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
n1_text = input("Enter first number: ").strip()
n2_text = input("Enter second number: ").strip()
n3_text = input("Enter third number: ").strip()

if not n1_text.isdigit() and not (n1_text.startswith("-") and n1_text[1:].isdigit()):
    print("Error: invalid input")
elif not n2_text.isdigit() and not (n2_text.startswith("-") and n2_text[1:].isdigit()):
    print("Error: invalid input")
elif not n3_text.isdigit() and not (n3_text.startswith("-") and n3_text[1:].isdigit()):
    print("Error: invalid input")
else:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

#7.5 Problem 5: Loan eligibility
monthly_income_text = input("Monthly income: ")
monthly_debt_text = input("Monthly debt: ")
credit_score_text = input("Credit score: ")

try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)
except:
    print("Error: invalid input")
    exit()

if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: invalid input")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

    print("Debt ratio:", debt_ratio)
    print("Eligible:", str(eligible).lower())
 
#7.6 Problem 6: Body Mass Index (BMI) and category flag

weing_k= input("seet your weing : ").strip()
heingt_m= input("seet your heingt :").strip()

if weing_k == "" or heingt_m == "":
    print("ERROR ")
else:
    weing_k= float(weing_k)
    heingt_m= float(heingt_m)

    if weing_k <= 0 or heingt_m <= 0 :
        print("ERROR")
    else:
        bmi = weing_k / (heingt_m * heingt_m)
        is_underweight= (bmi < 18.5) 
        is_normal=(18.5 <= bmi < 25.0)
        is_overweight=(bmi >= 25.0)


print("BMI :", bmi),
print("underweigth",is_underweight)
print("normal :", is_normal)
print("overweight", is_overweight)


#8. CONCLUSIONES 
"En este documento se demostró cómo los tipos numéricos int"
" y float permiten realizar cálculos reales, desde operaciones "
"básicas hasta conversiones y fórmulas más complejas. También se "
"utilizó el tipo bool, generado a través de comparaciones y operadores"
" lógicos, para tomar decisiones dentro del programa de manera clara y "
"estructurada. Se evidenció la importancia de validar los datos de entrada,"
" especialmente rangos mínimos y evitar divisiones entre cero, ya que estas "
"verificaciones previenen errores y resultados inconsistentes. "
"Además, se aplicaron condiciones combinadas usando and, or y not, mostrando "
"cómo estos patrones permiten crear reglas lógicas precisas que se repiten en"
" problemas reales como nómina, descuentos, préstamos y evaluaciones de salud."
" En general, el trabajo reforzó el uso correcto de variables "

#9 referencias 
"""
Python Documentation – Built-in Types: Numeric Types (int, float)
    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

 Python Documentation – Boolean Type (bool) and Truth Value Testing
    https://docs.python.org/3/library/stdtypes.html#truth-value-testing
Python Documentation – Expressions, Operators (Arithmetic, Comparison, Logical)
    https://docs.python.org/3/reference/expressions.html

 “Automate the Boring Stuff with Python” – Basic Programming Concepts (Variables, Input Validation)
    https://automatetheboringstuff.com
 
   Apuntes de Programación 
  
"""