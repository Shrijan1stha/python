# # Create a class Department with parameters name and number_of_students. Create a method total students,
# which takes object as a parameter and return the total number of students form all departments.

class Department:

    def __init__(self, name, no_of_students):
        self.name = name
        self.no_of_students = no_of_students

    def total_students(self, *args):
        # print(args)  # (d2, d3, d4)
        students_lists = []
        for obj in args:
            students_lists.append(obj.no_of_students)
        students = sum(students_lists)
        return self.no_of_students + students


d1 = Department("CS", 20)
print(d1.no_of_students)

d2 = Department("Maths", 10)
print(d2.no_of_students)
d3 = Department("Civil", 30)
d4 = Department("Physic", 5)

print(d1.total_students(d2, d3, d4))
