# 1) Create a class `India` with three methods:
#    a) `capital()` to print the capital of India.
#    b) `language()` to print the main language spoken in India.
#    c) `type()` to print the type of country India is.

# 2) Create another class `USA` with the same method names:
#    a) `capital()` to print the capital of USA.
#    b) `language()` to print the primary language of USA.
#    c) `type()` to print the type of country USA is.

# 3) Create objects for both classes:
#    a) `obj_ind = India()`
#    b) `obj_usa = USA()`

# 4) Use a common interface (polymorphism) to call the same method names
#    on different objects:
#    a) Use a `for` loop to iterate through `(obj_ind, obj_usa)`.
#    b) For each object `country`, call:
#       - `country.capital()`
#       - `country.language()`
#       - `country.type()`
#    (Each object runs its own class implementation of these methods.)

class India:
    def capital(self):
        print("Dehli")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing country")
class USA:
    def capital(self):
        print("Washington DC")
    def language(self):
        print("English")
    def type(self):
        print("Developing country")
obj_ind = India()
obj_usa = USA()
for i in (obj_ind, obj_usa):
    i.capital()
    i.language()
    i.type()