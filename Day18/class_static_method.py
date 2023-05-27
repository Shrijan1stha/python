class Person:
    __department = "CS"  # Class attribute

    def __init__(self,name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    @classmethod
    def set_department(cls, department):
        cls.__department = department

    @classmethod
    def get_department(cls):
        return cls.__department


# print(Person.department)  # Cant access form outside the class because it is a private class attribute.

print(Person.get_department())  # Result => CS

Person.set_department("Mathematics")
print(Person.get_department())  # Result => Mathematics
