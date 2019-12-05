__author__ = 'karam'
import random

# for i in range(1,12):
#     print("No, {} squared is {} and cubed is {:4}".format(i, i**2, i**4))
#     print("Calculate complete")


# name = input("Please enter your name: ")
# if ("shataj" in name):
#     print("You must be 53 at least. If I wasn't wearing my glasses I would of confused you for a bike grandma!!")
#
# age = int(input("How old are you, {}? ".format(name)))
#
# if age <= 20:
#     print("Must be nice to be so young {}".format(name))
# else:
#     print("Blimey, you're a f*cking dinosaur ain't ya. How are the bones? I can't imagine being that old!!")


# guess = int(input("Please guess a number between 1 and 10: "))
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input("Please guess a number between 1 and 10: "))
#     if guess == 5:
#         print("Correct")
#     else:
#         print("Incorrect, no more guesses")
# else:
#     print("Correct!! First time")


# tree1 = 'Tim'
# tree2 = 'Tim'
#
# # add the code to compare the trees
# if tree1 != tree2:
#     print("The trees are different")
# else:
#     print("The trees are the same")


# age = int(input("How old are you? "))
# if (age >= 16) and (age <=65):
#     print("Have a good day.")
# elif age < 16:
#     print("Have a good day at school")
# else:
#     print("Happy retirement")


# age = int(input("How old are you? "))
# if (age < 15) or (age > 65):
#     print("Time to relax")
# else:
#     print("Time to work")


# x = input("Please enter some text")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not write anything")


# print(not False)
# print(not True)
#
# if not True != False:
#     print("True does not equal false")
# else:
#     print("When did true equals false?!")


# parrot = "Norweigan Blue"
#
# letter = input("Enter a character: ")
# if letter in parrot:
#     print("Give me an {}, Bob".format(letter))
# else:
#     print("I don't need that letter")

# for i in range (1,20):
#     print("i is now {}".format(i))
#
#
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])


# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("The new number is {}".format(newNumber))


# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
# for char in number:
#     if char in '0123456789'
#         cleanedNumber = cleanedNumber + char
# newNumber = int(cleanedNumber)
# print("The new number is {}".format(newNumber))

# for colour in ["red", "blue", "black"]:
#     print("The rabbit is "+colour)
#
# for i in range(0,100,5):
#     print("i is {}".format(i))
#
#
# for i in range(1,13):
#     for j in range(1,13):
#         print("{1} X {0} = {2}".format(i, j, i*j))


# shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shoppingList:
#     if item == "spam":
#         print("Using continue means you go to the next loop without completing this loop. "
#               "As you can see we have skipped spam")
#         continue
#     print("Buy " + item)
#
#
# shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shoppingList:
#     if item == "spam":
#         print("Using break takes us out of the FOR loop completely. As a result we have not bought any item"
#               " after we reached spam.")
#         break
#     print("Buy " + item)


# meal = ["eggs", "bacon", "tomato", "beans", "sausages"]
# nasty_food_item = ''
# for item in meal:
#     if item == "spam":
#         nasty_food_item = item
#         break
# else:
#     print("I'll have a plate of that then please")
#
# if nasty_food_item == "spam":
#     print("Can't I have anything without spam in it")


# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
#
#
# for i in range(0,21):
#     if (i % 3 == 0) or (i % 5 == 0):
#         continue
#     else:
#         print(i)


# number = "9,223,372,036,854,775,807"
# cleanedNumber=''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(cleanedNumber))
#
# x = 23
# x += 1
# print(x)
#
# x -= 4
# print(x)
#
# x *= 5
# print(x)
#
# x /= 4
# print(x)
#
# x **= 2
# print(x)
#
# x %= 4
# print(x)
#
# greeting = "Good "
# greeting += "moring. "
# print(greeting)
#
# greeting *= 5
# print(greeting)


# i = 1
# while i <= 10:
#     print("i is now {}".format(i))
#     i += 1


# availableExits = ["East", "South", "North",]
# chosenExit = ""
# while chosenExit not in availableExits:
#     chosenExit = input("Please choose a direction: ")
#     if chosenExit == "quit":
#         print("GAME OVER")
#         break
# else:
#     print("aren't you glad you got out of there!")


# highest = int(input("Please enter the maximum value: "))
# answer = random.randint(1,highest)
# print("Please guess a number between 1 and {}".format(highest))
# guess = int(input())
# while guess != answer:
#     if guess > answer:
#         guess = int(input("Wrong! Guess lower: "))
#     else:
#         guess = int(input("Wrong! Guess higher: "))
# else:
#     print("You have guessed correctly")


for value in range(11):
    value = value * 2
    print(value)

