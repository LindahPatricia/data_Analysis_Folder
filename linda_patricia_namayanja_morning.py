
# control flow statements using for loop
cars = ['ford', 'jeep', 'wish', 'benz']
for car in cars:
    print(car)


fruits = ['tomato', 'apple', 'oranges', 'pie']
for fruit in fruits:
    print(fruit)

# using a while loop
# executes a block of code when the condition is fulfilled

fruits = ['oranges', 'mangoes', 'banana', 'pies']
fruit_count = 0
while fruit_count < len(fruits):
    print(fruits[fruit_count])
    fruit_count += 1

# using break and continue statements
z = 0
while z < 5:
    print(z)
    z += 1
 # example1
for x in range(10, 20):
    if (x == 15):
        break
    print(x)

 # example2
for number in range(1, 10):
    if number == 5:
        continue
    print(number)
    if number == 8:
        break



emotion = {
    'happy': "'am glad ur happy'",
    'angry': "'she is not angry'"
    'joy'"'she is joyous not fearful'",
    'peased': "'she is free'",
}
# prompt the user to enter her emotions
# python is case sensitive
user_emotion = input("how are you feeling today?")

if user_emotion in emotion:
    print(emotion[user_emotion])

else:
    print("am sorry i dont understand that")



"""
exception is an error which
 happens at the time of e
 xecution of a program. However, while
 running a program

 try catch exception
 try:

except:

 finally
"""

numlist = ['is', 'are', 'out']
try:
    print(numlist[1])
except IndexError:
    print('error: indexerror')
finally:
    print('this is always executed')


# exercise of students emotions
#prompting on a scale of 1-10
emotions = {
    1: "Angry",
    2: "Happy",
    3: "Sad",
    4: "Excited",
    5: "Bored",
    6: "Anxious",
    7: "Relaxed",
    8: "Confused",
    9: "Proud",
    10: "Grateful"
}

# Prompt the user to select an emotion
while True:
    try:
        rating = int(input("On a scale of 1-10, how do you feel? "))
        if 1 <= rating <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Please enter a valid number.")

# Display the selected emotion
selected_emotion = emotions[rating]
print("You selected:", selected_emotion)

