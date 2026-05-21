# Single level inheritance

class A:

    def showA(self):
        print("I'm in class A")


class B(A):

    def showB(self):
        print("I'm in class B")


if __name__ == "__main__":

    obj = B()

    obj.showA()
    obj.showB()


#########################################################################

# Multi level inheritance

class A:

    def showA(self):
        print("I'm in class A")


class B(A):

    def showB(self):
        print("I'm in class B")


class C(B):

    def showC(self):
        print("I'm in class C")


if __name__ == "__main__":

    obj = C()

    obj.showA()
    obj.showB()
    obj.showC()


#########################################################################

# Multiple inheritance

class A:

    def showA(self):
        print("I'm in class A")


class B:

    def showB(self):
        print("I'm in class B")


class C(A, B):

    def showC(self):
        print("I'm in class C")


if __name__ == "__main__":

    obj = C()

    obj.showA()
    obj.showB()
    obj.showC()


#########################################################################

# Hybrid inheritance

class A:

    def showA(self):
        print("I'm in class A")


class B(A):

    def showB(self):
        print("I'm in class B")


class C(A):

    def showC(self):
        print("I'm in class C")


class D(B, C):

    def showD(self):
        print("I'm in class D")


if __name__ == "__main__":

    obj = D()

    obj.showA()
    obj.showB()
    obj.showC()
    obj.showD()

#########################################################################

# Hierarchical inheritance

class A:

    def showA(self):
        print("I'm in class A")


class B(A):

    def showB(self):
        print("I'm in class B")


class C(A):

    def showC(self):
        print("I'm in class C")


class D(A):

    def showD(self):
        print("I'm in class D")


if __name__ == "__main__":

    obj1 = B()
    obj2 = C()
    obj3 = D()

    obj1.showA()
    obj1.showB()

    obj2.showA()
    obj2.showC()

    obj3.showA()
    obj3.showD()
