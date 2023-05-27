# Create a class person with attribute name and age. Create a method get_details in this class
# to print name and age.
# Create another class Employee with attributes salary and designation and inherits the Person class.
# Create a method get_details in this class to print name, age, salary and designation of the employee.


class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def get_details(self):  # This is a instance method.
        return f"Person's name is {self.name} and age is {self.age}"

class Employee(Person):

    def __init__(self,name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation
    
    def get_details(self):  # This is a instance method.
        print(super().get_details())
        return f"Salary is {self.salary}. Designation is {self.designation}"


e1 = Employee("Jon", 45, 30000, "Accountant")
print(e1.get_details())
