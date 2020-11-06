
#面向对象
#继承关系：类-->object-->type-->built
#
class T:
    print("xxx")

print(type(T))  #类

t=T()
print(type(t))  #对象


class T1(object):
    print("zzz")

t1=type("TTT",(object,),{})
print(type(t1))

TT=type("TTT",(object,),{})
t2=TT()
print(type(t2))


class P:
    pass

p=P()
p.name="xxx"
p.age=12
print(p)

#类   type("TTT",(object,),{})
#类中定义函数  type("TTT",(object,),{“__init__”,__init__})
class T2(object):
    print("xxx")
    def __init__(self):
        pass

t=T2()
print(type(t))

t1=type("TTT",(object,),{})
print(type(t1))


#引用计数器释放   ，：挥拳引用：用weak_ptr释放
#python也有这问题__weakref__
#__dict__:可动态往里塞东西 相当于一个接口
class T3:
    x=1
    def xx(self):
        pass
print(vars(T3))
print(T3.__dict__)

#写实复制
t=T3()
print(t.x)
print(vars(t))

#不可重载 会报错
class T4:
    def xxx(self):
        print("xxx")
#    def xxx(self,xxx):
#        print("yyy",x)

#t=T4()
#t.xxx()


#装饰器 =java注释器
def fun(f):
    f()
@fun   # fun(ff)
def ff():
    print("xxx")


def fun1(f):
    def xxx():
        print("----")
        f()
        print("++++")
@fun1   # fun1(ff)
def ff():
    print("xxx")


def fun2(f):
    def xxx():
        print("----")
        f()
        print("++++")
    return xxx
@fun2   # fun2(ff)
def ff():
    print("xxx")

fun2(ff)

