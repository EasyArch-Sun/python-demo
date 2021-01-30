
#================函数修饰类===================

def clsdeco(clz):
    class Test:
        def __init__(self):
            self.couse=clz()

        def getContent(self):
            return "couse: "+self.couse.getContent()

    return Test

@clsdeco
class Eng:
    def getContent(self):
        return "ENG"

s=Eng()
print(s.getContent())

# c=clsdeco(Eng)
# s=c()
# print(s.getContent())


#===============类装饰函数====================

class desc1:
    def __init__(self,func):
        print("￥￥￥￥￥")
        self.func=func
    def __call__(self, *args, **kwargs):
        print("～～～～")
        res=self.func(args[0])
        return res

@desc1
def some(arg):
    return arg+1

r=some(1)
print(r)

# s=desc1(some)
# r=s.__call__(1)
#
# print(r)

#===============类装饰类======================

class decro1:
    def __init__(self,clz):
        self.clz=clz #Eng1

    def __call__(self, *args, **kwargs):
        class prof:
            def __init__(self,couse):
                self.couse=couse     #couse存储了Eng1的对象

            def getContent1(self):
                return self.couse.getContent1()+"|ZH|MATH"
        return prof(self.clz())

@decro1
class Eng1:
    def __init__(self):
        print("00000000")
    def getContent1(self):
        return "ENG"

class Eng2:
    def getContent1(self):
        return "ENG2"

c=Eng1()
print(c.getContent1())
print("--------------------------")

d=decro1(Eng2)
c=d.__call__()
print(c.getContent1())


#=====================对象装饰方法－－－－－call被调用===============================

class Xxx():
    def __init__(self):
        pass

    def __call__(self, func):
        def _call(*args, **kw):
            return func(*args, **kw)

        return _call

class Yyy(object):
    @Xxx()                   #执行顺序是:Xxx()得到一个对象x,然后再@x相当于执行了对象x的call方法，并且将被修饰方法的类对应的方法传入了call，为了可以调用方法，因此隐含的实现了被修饰方法的类对象
    def dis(self, test, ids):
        print('yyyyyyy: '+test+" "+ids)

Xxx().__call__(Yyy().dis)("aaa","bbb")

Yyy().dis("aaa","bbb")


#=====================函数装饰方法===============================


def log(mth):
    def wrapper(self,*args,**kwargs):
        print(self,args,kwargs)
        return mth(self,*args,**kwargs)#mth(s,1,2)
    return wrapper

class Some:
    @log
    def doit(self,a,b):
        return a+b

    def doit2(self,a,b):
        return a+b

s=Some()
print(s.doit(1,2))

s=Some()
print(log(Some.doit2)(s,1,2))

print("="*50+"15")

#=====================类装饰方法－－－－－这个例子要先看discriptor后才能看懂===============================
class lazy():
    def __init__(self, func):
        print("#####")
        self.func = func

    def __get__(self, instance, cls):
        print("=====",instance,cls)
        val = self.func(instance)
        setattr(instance, self.func.__name__, val) #相当于在get中将Circle类的方法area修改位名字相同的属性，并且值是恒定的(调用原area返回的值)
        return val


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @lazy
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2


c = Circle(4)
print("+++++")
print(c.radius)
print("-----")
print(c.area)
print("111")
print(c.area)
print("222")
print(c.area)
