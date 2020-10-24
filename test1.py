# coding=utf-8

import json

# 数据类型 数字，字符,tuple 不可变类型
# site，map，list  可变类型
# Rooney串，不支持转义字符，所见即所得
# b后面的字符串是二进制数据
a='xx\nx'
a1="xxxx"
a2='''xxxxx'''
a3="""xxxxxx"""
a4=R'xxx\nxxx'
# xxx.getByte()
a5=b"123"
a6=u"我"
print(a,a1,a2,a3,a4)
print(a5,a6)


# 默认  索引  k-v
print("aaa:{},bbb:{}".format(1,2))
print("aaa:{0},bbb:{1}".format(1,2))
print("aaa:{a},bbb:{b}".format(a=1,b=2))


# json
b={"aaa":1,"yyy":2}
print(type(b))
c=json.dumps(b)
print(type(c),c)
d=json.loads(c)
print(type(d),d)


# 控制语句
e=1
if e==1:
    print("1111")
else:
    print("2222")

g=[1,2,3,4,5]
for f in g:
    print(f)

#迭代器--py特殊数据类型 协程重要元素 生成器yeild
r=range(1,10)
print(r)
print(type(r))
for i in range(1,10):  #for i=1;i<10;i++
    print(i)

#循环生成数组
l1=[i for i in range(10)]
print(type(l1))
str1=","
l2=[str(i) for i in range(10)]
print(l2)
str2=str1.join(l2)  #join 把集合中元素和符号拼成字符串
print(str2)

h=0
while True:
    print(h)
    h+=1
    if h>9:
        break

#99乘法表

i2=0
while i2<10:
    print(i2)
    i2+=1
else:
    print("aaa",i2)

for i3 in range(10):
    print(i3)
    i3+=1
else:
    print("xxx",i3)


#函数 不可重载 赋初值可重载
def xxx(a,b,c):
    print("a={},b={},c={}".format(a,b,c))
    return
#def xxx(a,b):
#    print("a={},b={}".format(a,b))
def xxx(a,b=1,c=1):
    print("a={},b={},c={}".format(a,b,c))
#xxx(1,2,3)
#xxx(c=1,b=2,a=3)
xxx(b=13,a=12)

print("*"*100)

#可变参数 ,可变参后一半不加不变参
def xxx1(a1,*b1):
    print(a1)
    print(type(b1))
    for i in b1:
        print(i)
xxx1(1,2,3,4)

def xxx11(a2,**b2):
    print(a2)
    for i in b2:
        print(i,"==",b2[i])
xxx11(1,b=2,c=3,d=4)

print("*"*100)

def xxx111(a2,*c2,**b2):
    print(a2)
    for i in c2:
        print(i)
    print("-" * 100)
    for i in b2:
        print(i,"==",b2[i])
#xxx111(1,2,3,5,b=2,c=3,d=4)

l2=[3,5,8,9]
m2={"b2":2,"c2":3}
xxx111(1,*l2,**m2)

#    nonlocal   就近找
#    global   全局找
def xxx2():
    num=1
    def yyy2():
#        num=2
        nonlocal num
        num=22
        print("inner",num)
    yyy2();
    print("outer",num)
xxx2()


def zzz():
    pass
print(type(zzz))

#加减
def myadd(a,b):
    return a+b

def mysub(a,b):
    return a-b

def ops(f,a,b):
    return f(a,b)

print(ops(myadd,1,2))
print(ops(mysub,3,2))

print("闭包")

#闭包
def incr():
    a=0
    def xxx():
        nonlocal a
#        global a
        a+=1
        return a
    return xxx

i=incr();
i2=incr();
print(i())
print(i2())
print(i())
print(i2())
print(i())
print(i2())

print("*"*100)

#lambda表达式 匿名函数 左函数右体
yyy=lambda a,b,c:a+b+c
print(yyy(1,2,3))

def ops1(f,a,b):
    return f(a,b)

print(ops1(lambda a,b:a+b,1,2))
print(ops1(lambda a,b:a-b,7,2))


# 生成器  断点函数 generator
def yyy():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

y=yyy()   #定义生成器  1、y=function()  2、y()
print(y)    #<generator object yyy at 0x7fe94b6bdba0>
#协程
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

#print(next(y))  #StopIteration
print("*"*100)

def yyy():
    yield 1

    yield 2
    yield 3
    yield 4
    yield 5

y=yyy()   #定义生成器
print(next(y))
print(y.send("aaa"))


# for i in yyy();
#     print(i)


l3=[1,2,3,4]
i6=iter(l3) #l3通过这一部成了生成器
for i5 in i6:
    print(i5)

class T():
    pass

print(T)    #<class '__main__.T'>
t=T()
print(t)    #<__main__.T object at 0x7f18d4433400>

def zzz():
    print("zzz")
    z=yield 2
    print(z)
    z = yield 3
    print(z)
    z = yield 4
    print(z)


z=zzz()
print(next(z))
print(next(z))
