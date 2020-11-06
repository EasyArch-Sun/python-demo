
#===========模仿ContextManager===============================

class MyException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Res:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print(self.name+" enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.name+" exit")
        return False

class MyGeneratorContextManager():
    def __init__(self, gen):
        print("__init__ called")
        self.gen = gen

    def __enter__(self):
        print("__enter__ called")
        return self.gen.__next__()

    def __exit__(self, type, value, traceback):#__exit__如果return true就会结束掉异常
        # if type is None:
        #     try:
        #         next(self.gen)
        #     except StopIteration:
        #         return
        # else:
        try:
            self.gen.throw(type, value, traceback)
        except:
            return True


def MyContextManager(func):
    def tmpf(*args):
        print("func info:", func)
        return MyGeneratorContextManager(func(*args))

    return tmpf


@MyContextManager
def foo(ex):
    try:
        yield
    except ex as e:
        print("+++++",e)

i=0
with foo(MyException),Res("withtest")  as tmp:
    print("+++")
    if i == 0:
        raise MyException("错了错了错了")
    print("---")


print("end!!")

#柯理化
def decorate(name):
    def wrapper(func):
        def sub_wrapper(arg):
            print("定义一个带参数的装饰器",name)
            func(arg)
        return sub_wrapper
    return wrapper

@decorate(name="python")
def text1(arg):
    print("text1",arg)

text1("xxx")

print("="*50+"6")

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