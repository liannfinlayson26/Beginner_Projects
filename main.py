from art import logo

#Calculator
#Add
def add(n1, n2):
  return n1 + n2

#Substract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#Divide
def divide(n1,n2):
  return n1 / n2


operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide}

#function = operations["*"]
#function(2,3)

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  #Flag
  keep_going = True

#Recurssion of the function that could call itself

  while keep_going:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      keep_going = False
      calculator()

calculator()


#Another way of doing if with while condition and exit
# for symbol in operations:
#   if symbol == operation_symbol:
#       calculation_function = operations[symbol]
#       first_answer = calculation_function(num1,num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# while True:
#     continue_operations = input("Type 'y' to continue calculating with {answer} or type 'n' to start new calculation.: ")
#     if continue_operations == 'n':
#         break
#     operation_symbol = input("Pick an operation: ")
#     num3 = int(input("What is the next number?: "))
#     for symbol in operations:
#         if symbol == operation_symbol:
#             calculation_function2 = operations[symbol]
#             next_answer = calculation_function2(first_answer, num3)
#     print(f"{first_answer} {operation_symbol} {num3} = {next_answer}")
#     first_answer = next_answer


  