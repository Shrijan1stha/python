# create a class Circle with an attribute radius. Create two objects of circle c1 and c2. Add the
# radius of the circle and point the result.
# Do the above task using a method and then a magic method.


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def total_radius(self, obj):
        return self.radius + obj.radius

    def is_greater(self, obj):
        # if self.radius > obj.radius:
        #     return True
        # return False

          ## OR

        return self.radius > obj.radius

    def __gt__(self, obj):  # dunder method or the magic method.
        return self.radius > obj.radius

    def __add__(self, other):
        return self.radius + other.radius



c1 = Circle(15)
c2 = Circle(20)

print(c1.radius + c2.radius)
print(c1.total_radius(c2))

if c1.radius > c2.radius:
    print("C1 is greater")
else:
    print("C2 is greater")

print(c1.is_greater(c2))
print(c2.is_greater(c1))

print(c1.__gt__(c2))
print(c1 > c2)
print(c1 + c2)
