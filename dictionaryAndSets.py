fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for makinf cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet. fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "mango": "the tastiest fruit",
         "broccoli": "this isn't a fruit",
         "pineapple": "Spongebob's house",
         "cucumber": "cats think these are snakes"}
choice = input("Choose a fruit: ")
print(fruit)
print(fruit[choice])
print(fruit["lemon"])
fruit["pear"] = "an odd shaped apple"
print(fruit)
print(fruit["pear"])
