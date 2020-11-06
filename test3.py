class Z:
    def __init__(self,a):
        self.__a=a

z=Z("yyy")
print(vars(z))
print(z.__dict__)
#print(z._Z__a)


class Z1:
    def __init__(self,a1,b1):
        self.a=a1
        self.b=b1

z1=Z1("xxxx","ttt")
#print(z1.a1)


#菱形继承
class A:
    pass
class B:
    pass

class C(B,A):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class C1(A,B):
    def __init__(self, a, b):
        self.a = a
        self.b = b

#继承关系,mro只读，bases可改
print(C.__mro__)
print(C.__base__)

print(C1.__mro__)
print(C1.__base__)


class A1:
    def xxx(self):
        pass

class B1:
    pass
