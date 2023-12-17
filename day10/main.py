from art import logo
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
print(logo)

def calculator():

  num1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)
    
  shouldContinue = True
  while shouldContinue is True:
    operationSelect = input("What's the operation to preform?: ")
    num2 = float(input("What's the second number?: "))
    answer = operations[operationSelect](num1, num2)

    print(f"{num1} {operationSelect} {num2} = {answer} ")
    if input(f"Would you like to contiunue with {answer}? Press 'y' to continue, or 'n' to not.: ") == 'y':
      num1 = answer  
    else:
      shouldContinue = False
      calculator()
  
    

calculator()