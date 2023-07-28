# Matching and searching
# regex re.match re.search() re.findall()

# Example 1
# demonstrating regular explanations
# merge first word, merge group word, merge all numbers

import re
text = "Hello, My name is linda. Iam a programmer with 2 year experience"

# merge first word

match = re.search(r"^\b\w+\b", text)

if match:
    print("Matches:", match.group())
matches = re.findall(r"\d+", text)
print("Matches:", matches)

# Example 2
# validate email format or email address


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


email = 'linda1925@gmail.com'
email1 = "Kisakye34789"

print(validate_email(email))
print(validate_email(email1))


# my_example3

text = "hello,my name is linda,iam a full stack developer"

# match first word
match = re.search(r"\b\w+\b", text)
if match:
    print("match:", match.group())


# example4

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
text = "Email me at linda@example.com or daisy@example.co.uk"

matches = re.findall(pattern, text)
print(matches)  # Output: ['linda@example.com', 'daisy@example.co.uk']


# generators and iterators
# 'yield' generator
# iterator __iter__ __next__ iterator

def factorial(n):
    if n == 0:
        yield 1
    else:
        yield n * next(factorial(n-1))


# Print the factorial of a number from 1 to 10
for i in range(1, 11):
    print(i, ":", next(factorial(i)))


#sample in my understanding generators
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Using the generator
fib_gen = fibonacci_generator()
for _ in range(6):
    print(next(fib_gen))



# using a iterator sample
class my_iterator:
    def __init__(self, count):
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count:
            self.index += 1
            return self.index
        else:
            raise StopIteration


# creating the instance
my_iterator1 = my_iterator(4)
for num in range(4):
    print(num)


# Example 2
# Generate function that yields the square of numbers from 1 to 1

# decorators
def my_decorator(func):
    def inner():
        print("this is my decorator")
        func()
    return inner


@my_decorator
def outer_decorator():
    print("this is outer function")


outer_decorator()
