# 3 types of methods in Python OOP
# 1. Instance Method -> needs object to be called
# 2. Class Method -> needs class to be called
# 3. Static Method -> doesn't need object or class to be called

class Kist:
    def __init__(self, building, classes):
        self.building = building
        self.classes = classes

        def details(self,a,b):
            print(a+b,self.building)
            