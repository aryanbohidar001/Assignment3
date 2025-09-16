# Assignment3
Task 1: Calculate Factorial Using a Function  AND  Task 2: Using the Math Module for Calculations


This repository contains two Python programming tasks:

## Task 1: Calculate Factorial Using a Function

**Problem Statement:**  
Write a Python program that:
1. Defines a function named `factorial` that takes a number as an argument and calculates its factorial using a loop or recursion.
2. Returns the calculated factorial.
3. Calls the function with a sample number and prints the output.

**Example:**
```python
#factorial
n=int(input('Enter a number:'))
def factorial(n):
    if n<0:
        return "undefine for negative numbers"
    elif n<2 :
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(n)
print('Factorial of',n,'is:',result)

# Output:
 Enter a number: 5
 Factorial of 5 is 120
```

## Task 2: Using the Math Module for Calculations

**Problem Statement:**  
Write a Python program that:
1. Asks the user for a number as input.
2. Uses the `math` module to calculate the:
   - Square root of the number
   - Natural logarithm (log base e) of the number
   - Sine of the number (in radians)

**Example:**
```python
from math import *
a=int(input('Enter a number:'))
print('Square roort:', sqrt(a))
print('Logarithm:', log(a))
print('sine:', sin(a))

#output:
Enter a number: 25
Square roort: 5.0
Logarithm: 3.2188758248682006
sine: -0.13235175009777303
```

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/aryanbohidar001/Assignment3.git
   cd Assignment3
   ```
2. Run the scripts for each task:
   ```bash
   python task1.py
   python task2.py
   ```

## Author

- Aryan Bohidar

---

Feel free to use and modify these programs for learning and practice!
