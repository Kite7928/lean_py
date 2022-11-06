# int 整数，加减乘除，大小比较
#  a = 10
# float:小数，浮点数
# a=10.5
# print(a)
# print(10/3)
#小数：数据范围是无限的。整数：在某一个特定的区间内是可以表示的很清楚的，
#1-100000000
#0 - 1
#计算机是一个二进制的产品：0,1
# 表示小数会有误差

# bool:用来做条件判断的
# 取值范围：True,False
# #基础数据类型之间的转化
# a="10" #字符串
# print(type(a))
# b=int(a)#把字符串转化成int()
# print(type(b))

#a=0
#在python中，所有的非零的数字都是True,零是False
# b = bool(a)
# while 1:#死循环，恒为真
#  print("还我钱")



#综上，在python的基本数据类型中，表示空的东西都是False,
# 不空的东西都是true
# lst = []
# print(bool(lst))


# //演示
# while 1:
#     content = input("请输入你要讲的话:")
#     if content:
#         print("开始你的表演:",content)
#     else:
#         break


# #1,字符串的格式化问题
# #我叫XXx,我住在XXXX,
# 我今年Xx岁，我喜欢做KXXXX
# name=input("请输入你的名字：")
# address=input("请输入你的住址：")
# age=int(input("请输入你的年龄："))
# hobby=input("请输入你的爱好：")
# #%S字符串占位
# #%d占位整数
# s="我叫%s,我住在%s,我今年%d岁，我喜欢%s"%(name,address,age,hobby)
# s1="我叫{}，我住在{}，我今年{}岁，我喜欢{)".format(name,address,age,hobby)
# print(s1)



# 字符串赋值最优方案
# s2 = f"我叫{name},地址{address},年龄{age},爱好{hobby}"
# print(s2)

