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


def Protocol(protocol):
    def temp(func):
        def sub_temp(arg):
            print("用http协议",protocol)
            func(arg)
        return sub_temp
    return temp

@Protocol(protocol="http协议")
def user(arg):
    print("user",arg)

user("xxx")

print("="*50+"11")
#=================四层==================
def decorate1(func):
    def wrapper():
        func
    return wrapper

def decorate2(name):
    def wrapper(func):
        print("second",name)
        func()
    return wrapper

def decorate3(func):
    def wrapper():
        func
    return wrapper

def decorate4(name4):
    def wrapper(func):
        print("forth",name4)
        func()
    return wrapper

@decorate1
@decorate2(name="java")
@decorate3
@decorate4(name4="python")
def test1():
    print("lllll")

test1()


print("="*50+"21")

def decorate11(func):
    def wrapper():
        func
    return wrapper

def decorate22(name2):
    def wrapper(func):
        print("second",name2)
        func
    return wrapper

def decorate33(func):
    def wrapper():
        func
    return wrapper

def decorate44(name4):
    def wrapper(func):
        print("forth",name4)
        func
    return wrapper

def test12():
    print("222222")

decorate11(decorate22(name2="java")(decorate33(decorate44(name4="python")(test12()))))
print("="*50+"22")
#==================================
def decorate(func):
    def wrapper():
        func()
    return wrapper

def decoratex(func):
    def wrapper():
        func()
    return wrapper

@decorate
@decoratex
def test11():
    print("lllll")

test11()



def decorate(func):
    def wrapper():
        func()
    return wrapper

def decoratex(func):
    def wrapper():
        func()
    return wrapper

def test11():
    print("lllll")

decorate(decoratex(test11))()

print("="*50+"3")

#==============================
def decorate(protocol,port):
    def servlet(func):
        def service(arg):
            print("协议:"+protocol+"端口:"+port)
            func(arg)
        return service
    return servlet

@decorate(protocol="http1.1",port="30000")
def test(arg):
    print("服务是",arg)

test("tcp服务")

decorate(protocol="http2.0",port="30001")(test(arg="udp服务"))

print("="*50+"4")
#===================================
