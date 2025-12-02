# Student: Martinez Zurita, Maximiliano Antonio
# Matricula: 2530071
# Group: A-105
#
# --------------------------------------------------
# Resumen ejecutivo
# --------------------------------------------------
# This file contains six small programming problems to practice Python functions:
# - Problem 1: area and perimeter of a rectangle
# - Problem 2: grade classifier
# - Problem 3: list statistics (min, max, average)
# - Problem 4: apply discount to a list (pure function)
# - Problem 5: greeting function with default parameter
# - Problem 6: factorial (iterative)
#
# Each problem includes: Description, Inputs, Outputs, Validations and 3 test cases
# (normal, border, error). The code defines functions (with parameters and return values),
# performs input validations, prints "Error: invalid input" when appropriate and demonstrates
# the functions with example test cases from the "main" routine.
#
# --------------------------------------------------
# Good practices and principles
# --------------------------------------------------
# - Prefer small functions with single responsibility.
# - Avoid repeating code: extract common validations into helper functions if needed.
# - Try to make functions pure (same input -> same output) when possible.
# - Document each function briefly and use descriptive names (lower_snake_case).
# - Validate inputs early and return/print clear error messages.
#
# --------------------------------------------------
# NOTES:
# - All messages and identifiers are in English.
# - Outputs use the English labels requested by the assignment.
# --------------------------------------------------


# --------------------------
# Problem 1: Rectangle area and perimeter
# Description:
#   Two functions calculate area and perimeter of a rectangle.
#
# Inputs:
#   width (float), height (float)
#
# Outputs:
#   "Area:" <area_value>
#   "Perimeter:" <perimeter_value>
#
# Validations:
#   width > 0 and height > 0
#   if invalid -> print "Error: invalid input"
#
# Test cases:
# 1) Normal: width=5, height=3 -> area=15, perimeter=16
# 2) Border: width=0.1, height=0.1 -> area=0.01, perimeter=0.4
# 3) Error: width=-2, height=3 -> Error: invalid input
# --------------------------
def calculate_area(width, height):
    """Return area of rectangle (width * height)."""
    return width * height


def calculate_perimeter(width, height):
    """Return perimeter of rectangle (2*(width+height))."""
    return 2 * (width + height)


def run_problem_1_tests():
    print("\n--- Problem 1 tests ---")
    tests = [
        {"width": 5.0, "height": 3.0, "label": "normal"},
        {"width": 0.1, "height": 0.1, "label": "border"},
        {"width": -2.0, "height": 3.0, "label": "error"},
    ]
    for t in tests:
        w = t["width"]
        h = t["height"]
        print(f"\nTest ({t['label']}): width={w}, height={h}")
        if w <= 0 or h <= 0:
            print("Error: invalid input")
            continue
        area = calculate_area(w, h)
        perimeter = calculate_perimeter(w, h)
        print("Area:", area)
        print("Perimeter:", perimeter)


# --------------------------
# Problem 2: Grade classifier
# Description:
#   classify_grade(score) returns letter grade A-F based on score 0-100.
#
# Inputs:
#   score (float or int)
#
# Outputs:
#   "Score:" <score>
#   "Category:" <grade_letter>
#
# Validations:
#   0 <= score <= 100
#   invalid -> print "Error: invalid input"
#
# Test cases:
# 1) Normal: score=92 -> Category A
# 2) Border: score=70 -> Category C
# 3) Error: score=150 -> Error: invalid input
# --------------------------
def classify_grade(score):
    """Return grade letter for numeric score in [0,100]."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def run_problem_2_tests():
    print("\n--- Problem 2 tests ---")
    tests = [
        {"score": 92.0, "label": "normal"},
        {"score": 70.0, "label": "border"},
        {"score": 150.0, "label": "error"},
    ]
    for t in tests:
        s = t["score"]
        print(f"\nTest ({t['label']}): score={s}")
        if not (0 <= s <= 100):
            print("Error: invalid input")
            continue
        category = classify_grade(s)
        print("Score:", s)
        print("Category:", category)


# --------------------------
# Problem 3: List statistics (min, max, average)
# Description:
#   summarize_numbers(numbers_list) returns dict with keys "min","max","average"
#
# Inputs:
#   numbers_text: comma-separated numbers -> converted to list of float
#
# Outputs:
#   "Min:", "Max:", "Average:"
#
# Validations:
#   - numbers_text not empty after strip
#   - all elements convertible to float
#   - list not empty
#   - if invalid -> print "Error: invalid input"
#
# Test cases (demonstrated programmatically):
# 1) Normal: "10,20,30" -> min=10, max=30, avg=20
# 2) Border: "5" -> min=max=avg=5
# 3) Error: "" (empty) -> Error: invalid input
# --------------------------
def summarize_numbers(numbers_list):
    """Return dictionary {'min':..., 'max':..., 'average':...} for a non-empty list."""
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {"min": min_value, "max": max_value, "average": average_value}


def run_problem_3_tests():
    print("\n--- Problem 3 tests ---")
    tests = [
        {"text": "10,20,30", "label": "normal"},
        {"text": "5", "label": "border"},
        {"text": "", "label": "error"},
    ]
    for t in tests:
        txt = t["text"]
        print(f"\nTest ({t['label']}): input='{txt}'")
        if txt.strip() == "":
            print("Error: invalid input")
            continue
        try:
            nums = [float(x.strip()) for x in txt.split(",") if x.strip() != ""]
        except ValueError:
            print("Error: invalid input")
            continue
        if len(nums) == 0:
            print("Error: invalid input")
            continue
        stats = summarize_numbers(nums)
        print("Min:", stats["min"])
        print("Max:", stats["max"])
        print("Average:", stats["average"])


# --------------------------
# Problem 4: Apply discount list (pure function)
# Description:
#   apply_discount(prices_list, discount_rate) returns new list with discounted prices.
#
# Inputs:
#   prices_text: comma-separated prices -> list of float
#   discount_rate: float 0..1
#
# Outputs:
#   "Original prices:", "Discounted prices:"
#
# Validations:
#   - prices_text not empty
#   - each price > 0
#   - 0 <= discount_rate <= 1
#   - invalid -> print "Error: invalid input"
#
# Test cases:
# 1) Normal: prices "100,200", rate 0.1 -> [90,180]
# 2) Border: prices "0.01", rate 0 -> [0.01]
# 3) Error: negative price or rate >1 -> Error: invalid input
# --------------------------
def apply_discount(prices_list, discount_rate):
    """Return new list with discounted prices; pure function (does not modify input)."""
    return [price * (1 - discount_rate) for price in prices_list]


def run_problem_4_tests():
    print("\n--- Problem 4 tests ---")
    tests = [
        {"prices_text": "100,200", "rate": 0.1, "label": "normal"},
        {"prices_text": "0.01", "rate": 0.0, "label": "border"},
        {"prices_text": "50,-10", "rate": 0.2, "label": "error"},
    ]
    for t in tests:
        pt = t["prices_text"]
        rate = t["rate"]
        print(f"\nTest ({t['label']}): prices='{pt}', rate={rate}")
        if pt.strip() == "" or not (0 <= rate <= 1):
            print("Error: invalid input")
            continue
        try:
            prices = [float(x.strip()) for x in pt.split(",") if x.strip() != ""]
        except ValueError:
            print("Error: invalid input")
            continue
        if len(prices) == 0 or any(p < 0 for p in prices):
            print("Error: invalid input")
            continue
        discounted = apply_discount(prices, rate)
        print("Original prices:", prices)
        print("Discounted prices:", discounted)


# --------------------------
# Problem 5: Greeting function with default parameters
# Description:
#   greet(name, title="") returns "Hello, <title name>!"
#
# Inputs:
#   name (string), title (string optional)
#
# Outputs:
#   "Greeting:" <greeting_message>
#
# Validations:
#   - name not empty after strip
#
# Test cases:
# 1) Normal: ("Alice","") -> "Hello, Alice!"
# 2) Border: (" Bob ","Dr.") -> "Hello, Dr. Bob!"
# 3) Error: ("", "Dr.") -> Error: invalid input
# --------------------------
def greet(name, title=""):
    """Return greeting string with optional title."""
    n = name.strip()
    t = title.strip()
    if n == "":
        # We choose to return None for invalid input; caller prints appropriate error.
        return None
    if t:
        full_name = f"{t} {n}"
    else:
        full_name = n
    return f"Hello, {full_name}!"


def run_problem_5_tests():
    print("\n--- Problem 5 tests ---")
    tests = [
        {"name": "Alice", "title": "", "label": "normal"},
        {"name": " Bob ", "title": "Dr.", "label": "border"},
        {"name": "", "title": "Dr.", "label": "error"},
    ]
    for t in tests:
        name = t["name"]
        title = t["title"]
        print(f"\nTest ({t['label']}): name='{name}', title='{title}'")
        greeting = greet(name, title)
        if greeting is None:
            print("Error: invalid input")
        else:
            print("Greeting:", greeting)


# --------------------------
# Problem 6: Factorial function (iterative)
# Description:
#   factorial(n) returns n! implemented iteratively to avoid recursion limits.
#
# Inputs:
#   n (int)
#
# Outputs:
#   "n:" <n>
#   "Factorial:" <value>
#
# Validations:
#   - n int, n >=0, n <= 20 (limit to avoid extremely large numbers)
#   - invalid -> print "Error: invalid input"
#
# Test cases:
# 1) Normal: n=5 -> 120
# 2) Border: n=0 -> 1
# 3) Error: n=-1 or n=21 -> Error: invalid input
# --------------------------
def factorial(n):
    """Iterative factorial implementation. Assumes n is a non-negative integer."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def run_problem_6_tests():
    print("\n--- Problem 6 tests ---")
    tests = [
        {"n": 5, "label": "normal"},
        {"n": 0, "label": "border"},
        {"n": -1, "label": "error"},
    ]
    for t in tests:
        n = t["n"]
        print(f"\nTest ({t['label']}): n={n}")
        if not isinstance(n, int) or n < 0 or n > 20:
            print("Error: invalid input")
            continue
        print("n:", n)
        print("Factorial:", factorial(n))



def main():
    print("Assignment: Functions practice - Problems 1 to 6")
    print("Student: Martinez Zurita, Maximiliano Antonio - Matricula 2530071")
    # Run test suites for each problem
    run_problem_1_tests()
    run_problem_2_tests()
    run_problem_3_tests()
    run_problem_4_tests()
    run_problem_5_tests()
    run_problem_6_tests()
    print("\nAll tests executed. Verify outputs against expected test cases.")


if __name__ == "__main__":
    main()


# Conclusions 
# Functions in Python allow dividing logic into reusable units that improve readability
# and testability. Parameters (in the function definition) describe expected inputs,
# while arguments are the concrete values passed at the call site. Returning values
# instead of printing inside the function makes the function more versatile (we can
# reuse results, chain computations, or test outputs). Default parameters simplify
# function calls when some values are often the same. Separating main logic from
# helper functions helps maintain clean, testable code.


# References:
# 1) Python documentation - Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) Python docs - Built-in Functions: https://docs.python.org/3/library/functions.html
# 3) Real Python - Functions in Python: https://realpython.com/defining-your-own-python-function/
# 4) Automate the Boring Stuff with Python - Functions chapter
# 5) "Effective Python" by Brett Slatkin - items about functions and naming

# Checklist:
# - File name suggestion: 2530071_MartinezZuritaMaximilianoAntonio.py
# - Portada, Resumen ejecutivo, Problems 1-6, Conclusions and References included.
# - Each problem has Description, Inputs, Outputs, Validations and 3 test cases.
# - Names and messages are in English.
# - Each problem defines and calls functions with return values.

