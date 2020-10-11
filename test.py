# coding=utf-8
import myorg
from myorg import a

print(1+1)
print("xxx".__add__(str(1)))

print(__name__)

a=1
b=2
print(dir(myorg.a))
print(__builtins__)
#print(dir())
#print(__package__)
#print(__path__)
#print(__file__)

# 类型和地址
c=2
d=2
print(type(c))
print(id(c),id(d))

# 交换
e=1
f=2
e,f=f,e
print(e,f)



#  元组 tuple
f=(1,"xxx",44)
(id,name,age)=f
print(id,name,age)
print(type(f))

#  数组
g=[1,2,3,4]
g[3]=2   #修改下标为3的值
print(g)
print(g[0:2])

#  map
h={"name":"xxx","age":12}
print(type(h))
print(h)
print(name)

# set 不能改，只能加  Set无序
#j={}默认为map，若想为Set，则j=Set{}
j={1,2,3,4}
j.add(8)
print(j)

# 去重
h=[1,3,5,3,2]
print(set(h))