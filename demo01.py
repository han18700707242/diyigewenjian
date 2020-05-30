"""
print("hello world!",end="|")   # 字符串
print(23333)   # 整数
print(2.33)   # 小数
print(True)   # 布尔值
print(False)   # 布尔值
print(None)   # 空
print(())   # 元组
print([])   # 数组
print({})   # 字典
print("haha","xixi","heihei")
print("哈哈哈"+"嘻嘻嘻")
print(1+1)
print(((1+3*2)/2)*4)
print(3%2)
print(10%3)
"""
"""
a = input("请输入：") 
b = input("请输入：")
print(int(a)+int(b))
a = input("请输入：")
b = input("请输入：")
print(len(a)+len(b))
"""
"""
xx = (1,2,3,"哈哈哈","小","小小")
print(xx[4])
"""
"""
xx = (1,2,3,"哈哈哈","小小","小")
print(xx.count("小"))
cc = (1,2,3,"哈哈哈","小小","大大","大大")
print(cc.index("大大"))
yy =(4,5,6,cc)
print(yy[3][3])
"""
"""
zz = [2,6,8,520,"哈哈","我爱你"]
zz.append("append")  #  往数组中，追加数据
print(zz)
"""
"""
zz = [2,6,8,520,"哈哈","我爱你"]
zz.insert(3,"我不爱你")
print(zz)
"""
"""
zz = [2,6,8,520,"哈哈","我爱你","哈哈"]
zz.remove("哈哈")
print(zz)
"""
"""
zz = [2,6,8,520,"哈哈","我爱你","哈哈"]
zz.pop(5)
print(zz)
"""
"""
zz = [2,6,8,520,"哈哈","我爱你","哈哈"]
zz[0] = 524
print(zz)
"""
"""
 #  通过input分别输入多段字符串，获取他们的长度，把长度的值分别存放到数组中，并从少到大的排序。
a=len(input("请输入："))
b=len(input("请输入："))
c=len(input("请输入："))
d=len(input("请输入："))
xx = []
xx.insert(0,a)
xx.insert(1,b)
xx.insert(2,c)
xx.insert(3,d)
xx.sort()
print(xx)
"""
# 字典 键值对 key:value
# a = {"name":"张三","age":22,"sex":"男"}
# print(a["name"])
"""
a = 2
if a > 2:
    print("a大于2")
else:
    print("a小于等于2")
"""
"""
old = int(input("请输入你今年的年龄:"))
if old > 60:
    print("该退休了！")
elif old > 30:
    print("该生孩子了！")
elif old > 25:
    print("该结婚了！")
elif old > 18:
    print("该上大学了！")
elif old == 18:
    print("成年了！")
else:
    print("好好玩耍吧！")
"""
# a=input("请输入密码：")
# b=input("请输入密码：")
# ss={"username":"a","password":"b"}
# if len(a)
"""
a = 1
while a < 5:
    print("我爱你",a)
    a = a + 1
"""





