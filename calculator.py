# CREATE A SIMPLE CALCULATOR
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

def avg(num1,num2):
    return (num1+num2)

def per(num1,num2):
    return (num1/num2)*100

print("please select a operation:\n" \
      "1. Additiom\n" \
      "2. Substractiom\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Aveage\n"
      "6. Percentage\n")

select= int(input("Select a operation from 1,2,3,4,5,6: "))

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2,"=", add(num1,num2))
elif select == 2:
    print(num1, "-", num2, "=", sub(num1,num2))
elif select == 3:
    print(num1, "*", num2, "=", mul(num1,num2))
elif select == 4:
    print(num1, "/", num2,"=", div(num1,num2))
elif select == 5:
    print("(",num1, "+", num2, ")", "/", "2", "=", avg(num1,num2))
elif select == 6:
    print(num1, "/", num2, "*", "100", "=", per(num1,num2))
else:
    print("Invalid option! Please select again!")





