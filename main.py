from art import logo

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    
    calc_continue = True
    while calc_continue:
        operation_symbol = input("Choose one of the operators: ")
        num2 = float(input("What is the next number?: "))
    
        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}. Type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            calc_continue = False
            calculator()

calculator()
