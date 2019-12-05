__author__ = 'karam'

# name = input("Please enter your name: ")
# age = int(input("Now please enter you age: "))
#
# if (age >= 18) and (age <= 30):
#     print("Welcome to the holiday {}.".format(name))
# else:
#     print("Not eligible for holiday")

# ip = input("Please enter an IP address: ")
# segmentSize = 0
# segmentNum = 1
# for char in ip:
#     if char in '.':
#         print("Segment number {1} has a length of {0} ".format(segmentSize, segmentNum))
#         segmentSize = 0
#         segmentNum += 1
#     elif char in '0123456789':
#         segmentSize += 1
#     elif char not in '.0123456789':
#         print("No other symbols allowed in IP addresses. Error in segment {}".format(segmentNum))
#         break
# else:
#     print("Segment number {1} has a length of {0} ".format(segmentSize, segmentNum))
#     print("Total number of segments = {}".format(segmentNum))
#     segmentNum += 1


# menu = []
# menu.append(["egg", "spam", "bacon"])
# menu.append(["egg", "sausage", "bacon"])
# menu.append(["egg", "spam"])
# menu.append(["egg", "bacon", "spam"])
# menu.append(["egg", "bacon", "sausage", "spam"])
# menu.append(["spam", "bacon", "sausage", "spam"])
# menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# menu.append(["spam", "egg", "sausage", "spam"])
#
# print(menu)
#
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#         for ingredient in meal:
#             print(ingredient)


# string = "1234567890"

# myIterator = iter(string)
# print(myIterator)
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)


# names = ["James", "Jack", "Juliet", "Mike", "Franzo"]
# numOfNames = len(names)
# print(numOfNames)
# myIterator = iter(names)
# for myIterator in names:
#     print(myIterator)


# myList = list(range(10))
# print(myList)
#
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
# print(even)
# print(odd)


# myString = "abcdefghijklmnopqrstuvwxyz"
# print(myString.index('k'))
# print(myString[14])
#
# sevens = range(7, 1000, 7)
# x = int(input("Please enter a positive number which is less than 1000: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
# else:
#     print("{} is NOT divisible by seven".format(x))
#
#
# decimals = range(0, 100)
# print(decimals)
# myRange = decimals[3:40:3]
# print(myRange)
# for i in myRange:
#     print(i)
# print('=' * 40)
# for i in range[3:40:3]:
#     print(i)
# print(myRange == range[3:40:3])

# r = range(0, 100)
# print(r)
# for i in r[::-1]:
#     print(i)
#
# print('=' * 40)
# for i in range[100, 0, -1]:
#     print(i)
#
# backString = "egaugnal lufrewop yrev a si nohtyP"
# print(backString[::-1])

# o = range(0, 100, 4)
# print(o)
# p = o[::5]
# print(p)
# for i in p:
#     print(i)


# t = "a", "b", "c"
# print(t)
# print("a", "b", "c")
# print(("a", "b", "c"))

imelda = "More Mayhem", "Imilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), \
         (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number: {}, Track name: {}".format(track, title))








