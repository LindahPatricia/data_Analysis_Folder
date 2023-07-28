#EXERCISE1
# lists
#outing the second item
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Second item:", names[1])


# changing the first item with a new item
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names[0] = "Alex"
print("Updated list:", names)

#adding the sixth item in the list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.append("Frank")
print("Updated list:", names)


#adding "Bethel" as the 3rd item in the list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.insert(2, "Bethel")
print("Updated list:", names)


#removing the fourth item from the list
names = ["Alice", "Bob", "Bethel", "Charlie", "David", "Eve"]
del names[3]
print("Updated list:", names)


# using negative indexing to print the last item in the list
names = ["Alice", "Bob", "Bethel", "David", "Eve"]
print("Last item:", names[-1])


# creating a new list and print the 3rd, 4th, and 5th items using a range of indexes
items = [1, 2, 3, 4, 5, 6, 7]
print("Items:", items[2:5])

#making a copy of a list of countries
countries = ["USA", "Canada", "Australia", "Germany"]
countries_copy = countries.copy()
print("Copied list:", countries_copy)


#looping through the list of countries
countries = ["USA", "Canada", "Australia", "Germany"]
for country in countries:
    print(country)

#sorting a list of animal names in both descending and ascending order
animals = ["Lion", "Tiger", "Elephant", "Monkey", "Giraffe"]
animals.sort()
print("Ascending order:", animals)
animals.sort(reverse=True)
print("Descending order:", animals)

#outputting only animal names with the letter 'a' in them
animals = ["Lion", "Tiger", "Elephant", "Monkey", "Giraffe"]
a_animals = [animal for animal in animals if 'a' in animal.lower()]
print("Animals with 'a':", a_animals)


#joining two lists containing first names and second names
first_names = ["Alice", "Bob", "Charlie"]
second_names = ["Smith", "Johnson", "Williams"]
full_names = first_names + second_names
print("Joined names:", full_names)




#EXERCISE2
#tuples

x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[0]
print("Favorite phone brand:", favorite_brand)



x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print("Second last item:", second_last_item)

x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print("Updated tuple:", x)


x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)
print("Updated tuple:", x)

#looping through the tuple
x = ("samsung", "iphone", "tecno", "redmi")
for item in x:
    print(item)


z = x[1:]
print("Updated tuple:", x)


cities = tuple(["Kampala", "Entebbe", "Jinja"])
print("Cities in Uganda:", cities)


x = ("samsung", "iphone", "tecno", "redmi")
phone1, phone2, phone3, phone4 = x
print(phone1, phone2, phone3, phone4)


#To use a range of indexes to print the 2nd, 3rd, and 4th cities in the tuple
cities = ("Kampala", "Entebbe", "Jinja", "Mbale", "Gulu")
print(cities[1:4])


#To join two tuples containing first names and second names
first_names = ("John", "Alice", "Bob")
second_names = ("Doe", "Smith", "Johnson")
full_names = first_names + second_names
print("Full names:", full_names)


#To create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print("Multiplied colors:", multiplied_colors)


#To return the number of times 8 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears:", count_8)





#EXERCISE3
#sets
#using set() constructor to create a set of 3 of your favorite beverages
beverages = set(["coffee", "tea", "juice"])
print(beverages)

#adding 2 more items to the beverages set.
beverages.add("water")
beverages.add("soda")
print(beverages)

#Checking if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# removing “kettle” from the set above
mySet.remove("kettle")
print(mySet)

#looping through the set above.
for item in mySet:
    print(item)

#creating a set of 4 items and a list of two items
mySet = {1, 2, 3, 4}
myList = [5, 6]

#adding elements in the list to elements in the set.
for item in myList:
    mySet.add(item)
print(mySet)


#two sets, one containing your ages and the other your first names. Join the two sets.

ages = {25, 30, 35}
names = {"John", "Alice", "Bob"}

combined_set = ages.union(names)
print(combined_set)



#EXERCISE 4
#strings
integer_var = 10
string_var = "Hello"

concatenated = str(integer_var) + string_var
print(concatenated)


txt = " Hello, Uganda! "
output = txt.replace(" ", "")

print(output)

#o convert the value of ‘txt’ to uppercase.
txt = " Hello, Uganda! "
output = txt.upper()
print(output)

#replace character ‘U’ with ‘V’ in the string
txt = " Hello, Uganda! "
output = txt.replace("U", "V")
print(output)

#return a range of characters in the 2nd,3rd and 4th position.
y = "I am proudly Ugandan"
output = y[1:4]
print(output)

#o correcting the code given
x = 'All "Data Scientists" are cool!'
print(x)





#EXERCISE

#dictionaries
# Dictionary
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of the shoe size
print("Shoe size:", shoes["size"])

# Change the value "Nick" to "Adidas"
shoes["brand"] = "Adidas"
print("Updated brand:", shoes["brand"])

# Add a new key/value pair "type": "sneakers"
shoes["type"] = "sneakers"
print("Updated dictionary:", shoes)

#To return a list of all the keys in the dictionary
shoes_keys = list(shoes.keys())
print("Keys:", shoes_keys)

shoes_values = list(shoes.values())
print("Values:", shoes_values)

if "size" in shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")


shoes.pop("color")
print("Updated dictionary:", shoes)


shoes.clear()
print("Empty dictionary:", shoes)

original_dict = {"name": "John", "age": 25}
copy_dict = dict(original_dict)
print("Original Dictionary:", original_dict)
print("Copy Dictionary:", copy_dict)


countries = {
    "USA": {
        "capital": "Washington D.C.",
        "population": "331 million"
        },
    "India": {
        "capital": "New Delhi",
        "population": "1.366 billion"
    }
}

for country, details in countries.items():
    print(country)
    for key, value in details.items():
        print(key, ":", value)
    print()

