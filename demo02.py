"""
print(type("a")) #字符串的类型 str
print(type(520)) #整数的类型 int
print(type(1.23)) #小数的类型 float
print(type(True)) #布尔值的类型 bool
print(type(False)) #布尔值的类型 bool
print(type(None)) #空的类型 NoneType
print(type(())) #元组的类型 tuple
print(type([])) #数组(列表)的类型 list
print(type({})) #字典的类型 dict
"""
# 通过input分别输入两段字符串，然后获取他们的长度，并相加输出结果。
"""
a = input("请输入：")
b = input("请输入：")
a = len(a)
b = len(b)
print(a+b)
"""
# 元组tuple
"""
a = (1,2,3,"我爱你",True,False,"芳芳","我爱你")
print(a.count("我爱你")) # count 找寻元组中有几个一样的数据
print(a.index("我爱你")) # index 获取元组中某一个数据的下标
"""
# 请在二维元组b里，打印出“芳芳”
"""
a = (1,2,3,"我爱你",True,False,"芳芳","我爱你")
b = ("傻瓜","你个猪",520,a)
print(b[3][6])
"""
"""
a = (1,2,3,"我爱你",True,False,"芳芳","我爱你")
b = ("傻瓜","你个猪",520,a)
print(len(b))
"""
# 列表(数组)list
"""
a = [520,"爱你哟","我是谁","毛血旺",412]
print(a)
print(a.count(520)) # count是将某一个值的个数进行数字统计
print(a.index("爱你哟")) # index是将某一个值的下标打印出来
"""
# 元组与列表的区别：元组不可修改，列表可以修改。
"""
a = [520,"爱你哟","我是谁","毛血旺",412]
a.append("兰儿") # append往数组中，追加数据
print(a)
a = [520,"爱你哟","我是谁","毛血旺",412]
a.insert(2,"韩贱贱") # 给数组中指定下标位置插入数据
print(a)
a = [520,"爱你哟","我是谁","毛血旺",412]
a.remove("我是谁") # 删除数组中指定的数据（数据如有重复，只删除第一个）
print(a)
a = [520,"爱你哟","我是谁","毛血旺",412]
b = ["小韩韩","爱吃"]
c = a.pop(3) # 移动指定下标的数据（此数据只是被移动，移动的数据可以用作其它地方）
b.append(c)
print(b)
a = [520,"爱你哟","我是谁","毛血旺",412]
a[2] = "韩贱贱" #将指定下标的数据进行替换
print(a)
a = [520,"爱你哟","我是谁","毛血旺",412]
a.reverse()
print(a)
a = [18,3,69,100]
a.sort() # 将整数（字符串）数组按从小到大的顺序进行排序
print(a)
a = ["k","u","c","y"]
a.sort(reverse=True)# 将整数（字符串）数组按从大到小的顺序进行排序
print(a)
a = [520,"爱你哟","我是谁","毛血旺",412]
a.extend(["傻逼","小小"]) #将数组合并追加到另一组数组的尾巴上
print(a)
a = [520,"爱你哟","我是谁","毛血旺",412]
a.clear()
print(a)
"""
# 通过input分别输入多段字符串，然后获取他们的长度，
#  并且把长度的值分别存放到数组中，并且从小到大的排序
"""
a = len(input("请输入:"))
b = len(input("请输入:"))
c = len(input("请输入:"))
ss = [a,b,c]
ss.sort()
print(ss)
"""
"""
a = {"wife":"兰儿","husband":"老公","love":"爱"}
print(a["love"]) # 提取字典中的数据
a = {"wife":"兰儿","husband":"老公","love":"爱"}
a.update(love="喜欢") # 修改字典中的数据
print(a)
a.update(kiss="吻") # 给字典新增数据
print(a)
a = {"wife":"兰儿","husband":"老公","love":"爱"}
a["husband"]="韩贱贱" # 修改字典中的数据
print(a)
a["kiss"]="吻" # 给字典新增数据
print(a)
"""
"""
a = {"wife":"兰儿","husband":"老公","love":"爱"}
a.get("love") # 无效的取值，打印原结果某个数据还在
print(a)
print(a.get("love")) # 有效的取值 get取走字典中某个数据
a = {"wife":"兰儿","husband":"老公","love":"爱"}
a.pop("love") # pop取走字典中某个数据，打印原结果某个数据消失
print(a)
a = {"wife":"兰儿","husband":"老公","love":"爱"}
print(a.pop("love")) # pop取走字典中某个数据
a = {"wife":"兰儿","husband":"老公","love":"爱"}
print(a.keys()) # 将字典中所以的key值取出来
print(list(a.keys())) # 将终端的值转换成数组的格式
a = {"wife":"兰儿","husband":"老公","love":"爱"}
print(a.values()) # 将字典中所以的value值取出来
print(list(a.values())) # 将终端的值转换成数组的格式
"""
# get取值与无函数取值的区别
a = {"wife":"兰儿","husband":"老公","love":"爱"}
print(a.get("kiss")) # 如果key不存在,终端输出为空（None）
print(a["kiss"]) # 如果key不存在,终端输出报错
