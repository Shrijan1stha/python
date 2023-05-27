## Multiple inheritance

class A:
    a = 1


class B:
    a = 2


class C(A, B):
    pass

obj = C()
print(obj.a)


## Hooerarchical Inheritance

class A:
    a = 1


class B(A):
    a = 2


class C(A):
    a = 3

obj = C()
print(obj.a)


## Multilevel Inheritance

class A:
    a = 1

class B(A):
    a = 2

class C(B):
    a = 3


class D(C):
    pass

obj = D()
print(obj.a)


## Hybrid Inheritance

class A:
    a = 1

class B:
    a = 2

class C(A, B):
    a = 3

class D(C):
    a = 4

class E(C):
    pass

print(E.mro())  # Method Resolution Order(tells the order of inheritance)


