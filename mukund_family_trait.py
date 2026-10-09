class FamilyMember:
    def __init__(self, eye_color, height):
        self.eye_color = eye_color
        self.height = height

    def show_traits(self):
        print("Eye Colour:", self.eye_color)
        print("Height in cm:", self.height)


class Kid(FamilyMember):

    def __init__(self, name, age, eye_color, height):
        self.name = name
        self.age = age
        super().__init__(eye_color, height)

    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def favorite_hobby(self):
        self.hobby = input("What is your favourite hobby? ")
        print(f"The favourite hobby of {self.name} is {self.hobby}.")

        
child = Kid("Mukund", 15, "Black", 160)
child.show_traits()
child.favorite_hobby()
result = issubclass(Kid, FamilyMember)
print("Is Kid in Family Member?", result)