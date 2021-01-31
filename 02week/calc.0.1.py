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
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")