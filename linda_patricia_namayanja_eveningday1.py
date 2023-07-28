# lists, tuples,dictionaries,sets

w = 40
print(type(w))  # output is int
z = "i love python"
print(type(z))


# python lists
# Lists are ordered,changeable,allow duplicates
Afternoon = ["linda", "petre", "eve"]
print(Afternoon)

afternoon2 = ["12", "32", "424e", "12"]
print(afternoon2)

# list length

print(len(Afternoon))

# type
print(type(afternoon2))

# accessing list items
print(Afternoon[2])
print(Afternoon[1])
print(Afternoon[-2])

# add items using insert method
afternoon2.insert(0, "lyn")
print(afternoon2)

# remove items from the list
afternoon2.remove("32")
print(afternoon2)


# modifying list elements
listed_items = [1, 2, 3, 4, 5]
listed_items[2] = 10
print(listed_items)
print(listed_items[1:3])
print(listed_items[1:5])
print(listed_items[:5])

# output 1,2,10,4,5


# appending items
my_list = ["eve", "lin", "ivan", "den"]
my_list.append("patty")


# tuples are used to store items in a
# single variable
# tuples are ordered and unchangeable

phones = ("samsung", "iphone", "techno")
print(phones)

# length of the tuple
print(len(phones))

# tuple with elements of different datatypes
my_tuple = ("Hello", 42, 3.14, True)
print(my_tuple)
print(len(my_tuple))

tuple1 = ("matooke", "rice", "cassava")
tuple2 = (100, 233, 455, 200)
print(type(tuple1))

# accessing tuple items using index
my_tuple = ("Hello", 42, 3.14, True)
my_first = my_tuple[0]
print(my_first)
my_second = my_tuple[2]
print(my_second)
my_third = my_tuple[1]
print(my_third)

# adding items to the tuple
# steps
# first convert the tuple into a list
# add items by using append method
# change iot to a tuple
phones = ("nokia", "samsung", "iphone")
z = list(phones)
z.append("techno")
phones = tuple(z)


# sets are unordered collection of unique
# elements with
# enclosing a comma-separated sequence of elements
# inside curly braces {}
my_set = {1, 2, 3, 4, 5}
print(my_set)

# duplicates are not allowed
# Accessing items in a set
my_set1 = {1, 2, 3, 4, 5, 6, 6, 6}
print(my_set1)
for x in my_set:
    print(x)

# add an item in a set
my_set.add(6)
print(my_set)
# remove an item in a set
my_set.remove(4)
print(my_set)
# looping in sets
for x in my_set1:
    print(x)
