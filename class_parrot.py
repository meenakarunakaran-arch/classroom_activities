class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
species = parrot("Krish", 5)
print("Name:", species.name, species)
print("Age:", species.age)