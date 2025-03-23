#creating a simple calculator in python
#Accepting user inputs

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#try to enter an operand like '+','-','*','/'

operand = input("Enter an operand(+-/*): ")

#operations to perform calculations.

if operand == '+':
    print(num1 + num2)

elif operand == '-':

    print(num1 - num2)

elif operand == '*':

    print(num1 * num2)

else:

    print(num1 / num2)

