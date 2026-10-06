class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot("Blu", 10)
woo = Parrot ("Wu", 15)
print("Blue is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is {} years old".format(blu.name, blu.age))

print("{} is {} years old".format(woo.name, woo.age))