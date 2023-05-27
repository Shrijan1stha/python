# Encapsulation is the concept of making the attributes private, public or protected.

class Vechile:
    def __init__(self,color, doors, mileage):
        self.color = color  # This is a public attribute.
        self._doors = doors  # This is a protected attribute.
        self.__mileage = mileage  # This is a private attribute.

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        self.__mileage = mileage


# Public attributes are accessible from outside the class
car = Vechile('red', 4, 50)
print(car.color)  # This is getting value.
car.color = 'blue'  # This is setting value.
print(car.color)


# Protected attributes are also accessible from outside the class but not recommended.
print(car._doors)  # This is getting value.
car._doors = 2  # This is setting value. It is possible for protected members
print(car._doors)


# Private members are not accessible from outside the class.
# print(car.__mileage)
# car.__mileage = 70  # This is not possible for private members.


print(car.get_mileage())
car.set_mileage(40)
print(car.get_mileage())


print(dir(car))

print(car._Vechile__mileage)  # This is termed as Name Mangling.
