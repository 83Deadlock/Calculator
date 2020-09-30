# This program is the first version of a calculator I intend to have working with a full functional GUI on different languages

# Program: Calculator
# Version: 0.0.1
# Author: José Pedro Castro Ferreira

# This first version is intended to be working as a text IO interface

# Function adds two numbers
def add (x, y):
    return x + y

# Function subtracts two numbers
def subtract (x, y):
    return x - y

# Function multiplies two numbers
def multiply (x, y):
    return x * y

# Function divides two numbers
def divide (x, y):
    return x / y

def percentage (x,y):
    return (x / y) * 100




while True:
    #Printing menu untill user shuts it down
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Percentage")
    print("6.Exit")
    print("\n")

    #Takes user's input
    choice = input("Select operation: ")

    #Just to create some space between the input and output
    print("\n")

    #Checks if the user's choice is any of the available
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first factor: "))
        num2 = float(input("Enter second factor: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "in", num2, "represents", percentage(num1, num2),"% of total amount")

        elif choice == '6':
            print("Exiting")
            break

        # Just to create some space between the input and output
        print("\n")

    else:
        print("Invalid Input")