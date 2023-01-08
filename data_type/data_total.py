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


# s = "我叫周杰伦"
#可以采用索引的方式来提取某一个字符（文字）
#
# print(s[3])#程序员都是从O开始数数
# print(s[0])
# print(s[-1])
#一表示倒数

#切片：从一个字符串中提取一部分内容
# s = "我叫周杰轮，你呢？你叫周润发吗？"
#
# print(s[3:6])#从索引3位置进行切片，切到6结束，坑：切片拿不到第二个位置的元素
# #语法：s[start:end】从start到end进行切片，但是取不到end[start,end)
# print(s[0:5])
# print(s[:5])
# #如果start是从开头进行切片，可以省略
# print(s[6:])
# #从start开始一直截取到末尾
# print(s[:])
#
# print(s[-3:-1])#目前还是只能从左往右切片
# print(s[-1:-3])#没结果，这里是坑！！！！


# s="我爱你"
#可以给切片添加步长来控制切片的方向
#print(s[::-1])#-表示从右往左
#语法：s[start:end:step]从start切到end,每step个元素出来一个元素
# s = "abcdefghiiklmnopgrst"
# # print(s[2:11:3])
# print(s[-1:-10:-3])


# 3.字符串常规操作
#字符串的操作一般不会对原字符串产生影时。一般是返回一个新的字符串
#3.1字符串大小写转换
# s = "python"
# s1 =s.capitalize()  单词首字母大写
# print(s1)

# s ="I have a dream!"
# s1=s.title()#单词的首字母大写
# print(s1)
# s ="I HAVE A DREAM"
# s1=s.lower()#变成小写字母
# print(s1)

#如何忽略大小写来进行判断
# verify_code =  "xAd1"
# user_input=input(f"请输入验证码({verify_code}):")
# if verify_code.upper() == user_input.upper():
#  print("验证码正确")
# else:
#  print("验证码不正确")

# 3.2替换和切割(*)
# strip(去掉字符串左右两端的空白符（空格，\t,\)
#
# s =input("验证前后空格问题:")
# s1 = s.strip()
# print(s1)

##replace(old,new)字符串替换
# s ="你好啊，我叫赛利亚"
# s1=s.replace("赛利亚","周杰伦")
# print(s1)
# a ="hello i am a good man!"
# al=a.replace(" ","")
# # 去掉所有的空格
# print(al)

#split(用什么切割)字符串切割，用什么切，锅会损朱掉裤：com
# a = "python java_cc#javascript"
# lst=a.split("_")#切之后的结果会放在列表当中
#print(lst)
# lst = a.split("_java_") #java就被直接切断
# print(lst)
# replace(),split(),strip()  记住

#3,4查找和判断
#查找
s = "你好啊,我叫周润发"
# ret =s.find("周润发1")#返回如果是-1就是没有该字符串出现
# print(ret)
# ret =s.index("周润发12312")#如果报错就是没有
# print(ret)

print("周润发" in s)   #in 可以做条件判断
# not in  判断是否存在
print("周润发" not in s)

# 判断
# name = input("请输入你的名字")
# # 判断你是否姓王
# if name.startswith("王"):  #判断字符串的开头   ，endsswith 判断结尾
#     print("你姓王")
# else:
#     print("你不姓王")


money = input("判断你的钱足够出去玩")

if money.isdigit():  #判断字符串是否是由整数组成
    money = int(money > 50)
    print("可以出去玩")
else:
    print("穷逼，玩不起")








# 3.5补充内容

# s = "hello"
# print("长度:",len(s))
#
# # join()
# s = "pytho_java_c_c#javascript"
# let = s.split("_")
# print(let)

let = ['赵本山','王大拿','大张伟','马大哈']
# 用_把上面的名字连起来
s = "_".join(let)
print(s)
#
# 总结：
# 1.  f"{变量}" 格式化一个字符串
# 2.索引和切片
#     索引:从0开始. []
#     切片:s[start: end: step],end 位置的数据永远拿不到
# 3.相关操作
# 字符串操作对原字符串是不发生改变的，
#   1.upper()在需要忽略大小写的时候
#   2.strip()可以去掉字符串左右两端的空白（空格，\t,\n)
#   3.replace()字符串替换
#   4.split() 对字符串进行切割
#   5.join()拼接一个列表中的内容成为新字符串
#   6,startswith()判断字符串是否以xxx开头
#   7.1en()字符串长度（内置函数）
#      字符串的循环和遍历
#         for c in s:
#             print(c) 字符串中的每一个字符




