#day3
# Basic operators
"""
#Arithmetic operator

+ - * / // % **
--Comparison operators
< <= > >= == !=
--logical operators
Logical AND: and
Logical OR: or
Logical NOT: not

--Assignment operators
Assign value : =
Add value : +
Add and assign value : +=
Subtract and assign value : -=
multiply and assign value : *=
divide and assign value : /=
 and assign value : //=
modulo and assign value : %=
power and assign value : **=

--member operators
Member operators : in checks if a value  is a member of a sequence
Member operators : not in checks if a value is not a member of a sequence

--identity operators
Identity operators : is checks if a two values are identical
Identity operators : is not checks if two values are not identical
"""
# example
# + addition
x = 20 + 90
print(x)

# -subtraction
y = 50-40
print(y)
# * multiplication

z = 50*2
print(z)

# / division
w = 50/25
print(w)

# % modulus
r = 50 % 3
print(r)
# exponentiation

d = 2**4
print(d)



# Comparison operators
# greaterThan
# comparison operators
x = 5
y = 2
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

if x < y:
    print('x is less than y')
if x >= y:
    print("x is greater than y")
if x <= y:
    print("x is  greater or equal to y")

x = 20

print(x > 20 and x < 30)

a = 58
b = 20
if a > b:
    print(a > b)
    print("a is greater than b")

# lessThan
if a < b:
    print(a < b)
    print("a is less than b")

# greaterThanEqual
if a >= b:
    print(a >= b)
    print("a is greater than or equal to b")

# lessThanEqual
if a <= b:
    print("a is less than or equal to b")
    print(a <= b)

# Identity operators
#they return a boolean

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)#it considers
#is it with the same object,memory addresses
print(x is y)
print(x == y)


# logical AND
print(x and y)

# logical OR
print(x or y)

# logical NOT
print(not x)
print(not y)

# Assignment operators
k = 8
# Add and assign
k += 5
print(k)
# Subtract and assign
k -= 5
print(k)
# multiply and assign
k *= 5
print(k)
# divide and assign
# k/= 5
print(k)

# modulus and assignment
k%= 5
print(k)

# power and assignment
k **= 5
print(k)



# Membership operators
lakes = ["Victoria", "Kyoga", "Albert", "katwe", "George"]
if "Kyoga" in lakes:
    print("Kyoga is a lake")


# not in
lakes = ["Victoria", "Kyoga", "Albert", "Edward", "George"]
if "Kyoga" not in lakes:
    print("Kyoga is not a lake")

# Identity operators
x = True
y = False
print(x is y)
print(x is not y)
print(x == y)
print(x != y)


# bitwise operators
"""
Bitwise operators are used to perform operations on individual bits in of binary numbers.
Bitwise AND (&): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR (1): Performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR (^): Performs a bitwise XOR operation
Bitwise NOT (-): Performs a bitwise NOT operation between the corresponding
Bitwise left shift ('<<): Performs a bitwise left shift operation
Bitwise right shift (>>): Performs a bitwise right shift operation
"""



#bitwise operators in detail
n1=28
n2=19

print(bin(n1))
print(bin(n2))
#to remove the ob start from position 2
print(bin(n1)[2:])
print(bin(n2)[2:])

#AND bitwise operator a single & is used
n3 = n1 & n2
print(bin(n3)[2:])
#example2
a = 10
b = 20
# Bitwise AND
print(a & b)


#OR
n4 = n1 | n2
print(bin(n4)[2:])

#XOR
n5 = n1 ^ n2
print(bin(n5)[2:])




 #exercise for a simple calculator with the graphical user interface
from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("simpleCalculator_linda_patricia")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, bg="yellow",
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

window.mainloop()






