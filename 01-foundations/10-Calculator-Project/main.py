logo = r"""
 _____________________
|  _________________  |
| | Pythoncalc   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2, memory):
    if memory != 0:
        return memory + n2
    else:
        return n1 + n2

def subtract(n1,n2, memory):
    if memory != 0:
        return memory - n2
    else:
        return n1 - n2

def multiply(n1, n2, memory):
    if memory != 0:
        return memory * n2
    else:
        return n1 * n2

def divide (n1 , n2, memory):
    if memory != 0:
        return memory / n2
    else:
     return n1 / n2


print(logo)
in_game = True
memory = 0

while in_game:

    resultado = 0
    if memory == 0:
        n1 = int(input("Whats the first number?: "))

    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    n2 = int(input("Whats the second number?: "))

    if operation == "+":
        resultado = add(n1, n2, memory)
        print(n1, "+", n2, "=", resultado)
        memory = resultado

    elif operation == "-":
        resultado = subtract(n1, n2, memory)
        print(n1, "-", n2, "=", resultado)
        memory = resultado

    elif operation == "*":
        resultado = multiply(n1, n2, memory)
        print(n1, "*", n2, "=", resultado)
        memory = resultado

    elif operation == "/":
        resultado = divide(n1, n2, memory)
        print(n1, "/", n2, "=", resultado)
        memory = resultado

    else:
        print("Invalid operation. Please try again.")
        break

    decision = input(f"Type 'y' to continue operating with {resultado} or 'n' to start a new calculation: ")

    if decision == "y":
        memory = resultado

    else:
        memory = 0