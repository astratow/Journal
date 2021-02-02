# calculator


#adding

def add(n1, n2):
  return n1 + n2

#substracting

def substract(n1, n2):
  return n1 - n2

#multiply

def multiply(n1, n2):
  return n1 * n2

#divide

def divide(n1, n2):
  return n1 / n2

operation = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide,
}
def calculator():
  num1 = float(input("Please enter first number:\n"))
  for operation_symbol in operation:
    print(operation_symbol)
  should_continue = True

  while should_continue:    
    num2 = float(input("Please enter second number:\n"))
    operation_symbol = (input("Please select:\n +  -  *  / \n"))
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    menu = (input(f"Type 'c' to continue calculating with {answer},  'n' to start new calculation or any other key to stop:\n"))
    if menu == "c":
      answer = num1
    elif menu == "n":
      should_continue = False
      calculator()
    else:
      should_continue = False
      print("Thank you for using my calculator! Have a great day!")
calculator()