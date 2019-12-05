# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))


# parrotList = ["non pinin'", "no more", "a stiff", "bereft of life"]
# parrotList.append("A Norwegian Blue")
# for state in parrotList:
#     print("This parrot is {}".format(state))


# number = int(input("Please enter a number: "))
# even = [0, 2, 4, 6, 8]
# if number in even:
#     print("This number is even!")
# else:
#     print("The number is odd!")


# even = [0, 2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# numbers.sort()
# print(numbers)
# even = [0, 2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# numbersInOrder = sorted(numbers)
# print(numbersInOrder)
# if numbers == numbersInOrder:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
# if numbers.sort() == numbersInOrder:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
# if sorted(numbers) == numbersInOrder:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")


# list1 = []
# list2 = list()
# print("List 1: {}".format(list1))
# print("List 2: {}".format(list2))
# if list1 == list2:
#     print("The lists are equal")
#
#
# print(list("The quick brown fox"))
# numberTest = str(123456789)
# print(list(numberTest))


# even = []
# number = 1
# while number <= 20:
#     if (number % 2 == 0) and (number % 10 != 0):
#         print(number)
#         even.append(number)
#         number += 1
#     elif number % 10 == 0:
#         print(even)
#         number += 1
#     else:
#         number += 1


# #Here it is important to note that in python if you make two lists equal to each other, they technically point
# # to the same place. This means if you change one list variable, you also change the other list variable. The example
# # code below shows this.
# even = [2, 4, 6, 8]
# anotherEven = even
# anotherEven.sort(reverse=True)
# print(even)
# #The method copies the list over to a new variable however, the two variables are completely unattached. This means
# #changes to one variable wont have any affect on the other variable.
# even = [2, 4, 6, 8]
# anotherEven = list(even)
# anotherEven.sort(reverse=True)
# print(even)


# even = [2, 4, 6, 8, 0]
# odd = [1, 3, 5, 7, 9]
# numbers = [even, odd]
# print = numbers
# for number_set in numbers:
#     print(number_set)
#     for value in number_set:
#         print(value)


welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
metallica = "Ride the Lighting", "Metallica", 1984
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# imelda = imelda[0], "Imelda May", imelda[2]
#
# metallica2 = ["Ride the Lighting", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)
print(imelda)
title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)

