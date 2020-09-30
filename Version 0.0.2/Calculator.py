#!/usr/bin/python

# This program is the first version of a calculator I intend to have working with a full functional GUI on different languages

# Program: Calculator
# Version: 0.0.2
# Author: José Pedro Castro Ferreira

# This second version is intended to be working with a functional GUI made with tkinter

import tkinter

# Global variable that will be showed to the user on the calculator's screen
expression = ""

def input_number(number, equation):
    # accesses the global variable
    global expression

    # concatenation of the string
    expression = expression + str(number)
    equation.set(expression)

def clear_input(equation):
    # accesses the global variable and set it to the default empty state
    global expression
    expression = ""

    # setting empty string in input field
    equation.set("Enter the expression")

def evaluate(equation):
    # acesses the global variable
    global expression

    # trying to evaluate the expression
    try:
        result = str(eval(expression))
        equation.set(result)
        # expression = "" wouldn't allow user to operate on the result of the previous expression
    except:
        equation.set("Enter a valid expression")
        expression = ""

def main():
    # creates the window
    window = tkinter.Tk()

    # sets the name of the window
    window.title("Calculator")

    # sets window's size
    window.geometry("225x215")

    # variable class instatiation
    equation = tkinter.StringVar()

    # input field for expression
    input_field = tkinter.Entry(window, textvariable = equation)
    input_field.place(height=100)

    # using grid position to arrange widgets
    input_field.grid(columnspan = 4, ipadx = 50, ipady = 20)

    # settin the placeholder message for users
    equation.set("Enter the expression")

    # creating buttons and placing them at respective positions
    _1 = tkinter.Button(window, text='1', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(1, equation), height=2, width=7)
    _1.grid(row = 4, column = 0)
    _2 = tkinter.Button(window, text='2', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(2, equation), height=2, width=7)
    _2.grid(row = 4, column = 1)
    _3 = tkinter.Button(window, text='3', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(3, equation), height=2, width=7)
    _3.grid(row = 4, column = 2)
    _4 = tkinter.Button(window, text='4', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(4, equation), height=2, width=7)
    _4.grid(row = 3, column = 0)
    _5 = tkinter.Button(window, text='5', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(5, equation), height=2, width=7)
    _5.grid(row = 3, column = 1)
    _6 = tkinter.Button(window, text='6', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(6, equation), height=2, width=7)
    _6.grid(row = 3, column = 2)
    _7 = tkinter.Button(window, text='7', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(7, equation), height=2, width=7)
    _7.grid(row = 2, column = 0)
    _8 = tkinter.Button(window, text='8', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(8, equation), height=2, width=7)
    _8.grid(row = 2, column = 1)
    _9 = tkinter.Button(window, text='9', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(9, equation), height=2, width=7)
    _9.grid(row = 2, column = 2)
    _0 = tkinter.Button(window, text='0', fg='white', bg='#15284A', activebackground='#162F5C', bd=1, command=lambda: input_number(0, equation), height=2, width=7)
    _0.grid(row = 5, column = 0)

    plus = tkinter.Button(window, text='+', fg='white', bg='black', activebackground='#162F5C', bd=1, command=lambda: input_number('+', equation), height=2, width=7)
    plus.grid(row=2, column=3)
    minus = tkinter.Button(window, text='-', fg='white', bg='black', activebackground='#162F5C', bd=1, command=lambda: input_number('-', equation), height=2, width=7)
    minus.grid(row=3, column=3)
    multiply = tkinter.Button(window, text='*', fg='white', bg='black', activebackground='#162F5C', bd=1, command=lambda:  input_number('*', equation), height=2, width=7)
    multiply.grid(row=4, column=3)
    divide = tkinter.Button(window, text='/', fg='white', bg='black', activebackground='#162F5C', bd=1, command=lambda: input_number('/', equation), height=2, width=7)
    divide.grid(row=5, column=3)
    equal = tkinter.Button(window, text='=', fg='white', bg='black', activebackground='#162F5C', bd=1, command=lambda: evaluate(equation), height=2, width=7)
    equal.grid(row=5, column=2)
    clear = tkinter.Button(window, text='Clear', fg='white', bg='black', activebackground='#162F5C', bd=1, command=lambda: clear_input(equation), height=2, width=7)
    clear.grid(row=5, column=1)

    # actually showing GUI
    window.mainloop()

# start of the program
if __name__ == '__main__':
    main()