from art import logo as logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
calculator = True
n1 = None

while calculator == True:
    if n1 == None:
        n1 = float(input("What's the first number?: "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
    else:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

    result = operations[operation](n1, n2)

    print(f"{n1} {operation} {n2} = {result}")

    new_calculation = input(f"Type 'y' to continue calculation with {result}, type 'n' to start a new calculation: ")

    if new_calculation == "y":
        n1 = result
        n2 = None
    else:
        n1 = None
        n2 = None
