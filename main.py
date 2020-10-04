def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2

print(""" Select any one of the operations:

1. Addition
2. Subtraction
3. multiplication
4. Division
5. Powers
6. Remainders""")

choose = int(input('Which operation do you want to perform?1/2/3/4/5/6: '))

num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))

if choose == 1:
  print(num1, '+', num2, '=', add(num1, num2))
elif choose == 2:
  print(num1, '-', num2, '=', subtract(num1, num2))
elif choose == 3:
  print(num1, 'x', num2, '=', multiply(num1, num2))
elif choose == 4:
  print(num1, '/', num2, '=' , divide(num1, num2))
elif choose == 5:
  print(num1, '^', num2, '=', num1**num2)
elif choose == 6:
  print(num1, 'R', num2, '=',  num1 % num2)
else:
  print("Invalid input!")
