from art import logo
print(logo)
def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}
def calculator():
  num1 = float(input("Enter first number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("Enter second number: "))
    calculation_function = operations[operation_symbol]
    ans = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {ans}")
  
    if input(f"Continue (y/n) with previous answer {ans}: ") == 'y':
      num1 = ans
    else:
      should_continue = 'False'
      calculator()

calculator()