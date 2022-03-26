
import math
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
def fibonacci(n):
    if n == 2 or n==3 :
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def sum_0f_digit(x):
  assert x >= 0 and x == int(x) , 'Number should be integer'
  if x == 0:
      return 0
  else:
      return x%10 + sum_0f_digit(int(x/10))

def power_0f_num(x,y):
   if x == 0:
       return 0
   if y == 0:
       return 1
   else:
       return x * power_0f_num(x,y-1)

num = int(input("Enter the number:"))
pow = int(input("Enter the power:"))
print(power_0f_num(num,pow))
