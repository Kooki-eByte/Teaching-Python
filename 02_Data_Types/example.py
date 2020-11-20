# # Data Types

# # Int
# i = 1

# # Float
# f = 5.5

# # Boolean
# b = True
# b2 = False

# # String
# s = "Hello, \"World\""

# # List - [...,...,...]
# l = [1, 5, 6, 2]
# l2 = [1, "Blue"]

# # Set - {...,...,...}
# # You cannot access items in a set by referring to an index or a key. They are unordered and unindexed.
# # But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# st = {"apple", "grapes", "banana"}

# for x in st: 
#     print(x)

# # Tuples - (...,...,...)
# # The items inside of a tuple are indexed
# # Tuples are collection of items that are ordered and unchangeable.
# t = ("apple", "banana", "grapes")

# Dictionary
# key:value

car = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2018,
    "isRunning": False
}

# print(car["model"])
car2 = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2018,
    "isRunning": True
}

# # something new to python 3.9
# print(d | d2) # this is the same thin but the new way of merging the dictionaries together
# print({**car, **car2})

# car.update(car2)
# print(d)

