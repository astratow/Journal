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
  ":" : divide,
}
for operation_symbol in operation:
  print(operation_symbol)
num1 = int(input("Please enter first number:\n"))
num2 = int(input("Please enter second number:\n"))
operation_symbol = (input("Please select:\n +  -  *  / \n"))
calculation_function = operation[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation:\n + - * /\n")
num3 = int(input("What is your next number?\n"))
calculation_function = operation[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")