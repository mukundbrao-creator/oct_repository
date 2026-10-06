class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print("This method runs automatically, when the object is created.")

modelX = Vehicle(240, 18)
cclss = Vehicle(300, 20)
bmw = Vehicle(180, 20)
print("Model Max Speed", modelX.max_speed)
print("Model Mileage",modelX.mileage)