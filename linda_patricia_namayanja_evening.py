# dictionaries
# dictionaries is used with {}
phones = {
    1: "iphone",
    2: "samsung",
    3: "nokia",
    4: "techno"
}
# length pf the dictionary
print(len(phones))
# datatype
print(type(phones))

# accessing items in the dict
z = phones[3]
print(z)

# change an item or updating an item
phones[2] = "galaxy"
print(phones)

# adding items in the dict
phones[5] = "iphone16"
print(phones)


#exercise
# removing an item in the dictionary
phones.pop(1)
print(phones)

# copying items in the dict
mydict = phones.copy()
print(mydict)


#exercise
# nesting dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)


# using a key()
w = phones.keys()
print(w)

# using value() method
s = phones.values()
print(s)

# Check if a key exists in the dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

key = "age"
if key in student:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")

# looping through the dict
for x in phones:
    print(x)


# numbers
a = 10
b = 10j
w = 5.5
x = 12.097609887

# datatype
print(type(a))
print(type(b))
print(type(w))
print(type(x))

# type conversion
# converting int to float
s = float(a)
print(s)

# converting int to complex
r = complex(a)
print(r)

# casting works mostly when you
# want to specify a
# a variable type
a = int(19)
h = int(3.34)
f = int(700000)
print(a)
print(h)
print(f)
print(type(a))

# dealing with floats
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x)
print(y)
print(z)
print(w)
print(type(w))


# dealing with strings
print("Hello world")
print('Hello linda')

# assigning a variable to a string
message = "Hello my linda"
print(message)

# dealing with multi strings
emotional_message = """l like you,
i love you so much,
i hate you"""
print(emotional_message)

# strings as arrays
# each letter is put into account
main = "god is good"
print(main[0])
print(main[1])
print(main[2])
print(main[3])
print(main[4])
print(main[5])
print(main[6])
print(main[7])

#formatting strings
#capitalizing the string
a = "Hello, World!"
print(a.upper())


#in lowercase
print(a.lower())

# formatting a string

d = " hello {} "
print(d.format("linda"))



#concatenating the strings
x = "Hello"
y = "World"
z = x + " " + y
print(z)



# exercise1
# using len() method to find the length
# white space is counted
print(len(main))
print(len(emotional_message))
print(len(message))

#exercise2
# using a for loop in a string
for x in message:
    print(x)

for x in emotional_message:
    print(x)

for x in main:
    print(x)


#exercise3
 # example of slicing in the string
txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
# slice from the start
print(b[:5])
# slice from the end
print(b[2:])
# slice in a range of characters
print(b[1:5])
print(b[3:5])


# boolean
# evaluate to a true or false
print(20 > 10)
print(30 == 40)
print(30 > 10)

# use a condition to show how to use booleans
# Boolean variables

is_raining = True
is_sunny = False

# Using conditionals with booleans
if is_raining:
    print("Remember to take an umbrella.")

if is_sunny:
    print("Don't forget to wear sunscreen.")
