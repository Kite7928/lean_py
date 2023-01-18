#定义:能装东西的东西
#在python 中用[]来表示是一个 列表，列表中的元素通过,隔开
a=["张三丰","张无忌","张绍刚",[1,23,True]]

# 特性:
# 1.也可以像字符串一样做索引和切片
# 2.如果索引超过范围报错
# 3.可以用for循环进行遍历
# 4.可以用len拿到列表的长度
#
# lst = ["标题","分类","大小"]
#
# print(lst[0])
# print(lst[1:3])
# print(lst[::-1])
# print(lst[3306])  #list index out of range

# for item in lst:
#     print(item)
#     print(len(lst))

# 4.2列表的增删改查
lst = []
# 向列表中添加内容
# append()追加*
# lst.append("袁灏")
# lst.append("王阳明")
# lst.append("知行合一")
# insert() 插入，前叉慢
# lst.insert(0,"心学")
# extend()  合并列表
# lst.extend(["算法","数据结构","程序"])
# 删除

# ret= lst.pop(-1) #给出被删除的索引，返回被删除的元素
# print(ret)
# lst.remove("心学")#删除某个元素*

# 修改
# lst[0] = "狗子" #直接用索引就可以进修改操作

#查询
# print(lst[2])  #直接用索引进行查询

#小练习：
# 把所有的姓张的人修改成姓李
# lst=['赵敏','张绍刚','张无忌','武则天','赢政','马超']

# for item in lst: #此时，看不到元素的索引位置
# for i in range(len(lst)): # len(lst) 列表的长度 -> 可以直接拿到列表索引的for 循环
#     item = lst[i] #item 依然是列表中的每一项
#     if item.startswith("张"):
#         new_name = "李"+item[1:]
        # print(new_name)
    # 把新名字丢回列表(需要索引?)
    #     lst[i] = new_name #修改

# print(lst)

# 4.3==========================
# 列表的其他操作，补充
#排序
# lst=[1,2,3,"麻花藤","武大郎"]#列表会按照你存放的顺序来保存
# print(lst)
# lst=[222,444,123,43,123.43243,111]
# lst.sort()
#对列表进行升序排序
# lst.sort(reverse = True) #reverse:翻转
# print(lst)

#列表的嵌套
# lst = ["abc","def",["呵呵哒","妈妈呀","苦苦脊瓦",["可乐","scrapy",123]],'aed',"qpr"]
# print(lst[2][3][1].upper())

# 列表的循环删除
# lst = ['赵敏‘，张绍刚','张无忌','武则天','赢政行行马']
# temp = [] #准备一个临时列表，负责存储删除的内容
#
# for itme in lst:
#     if itme.startswith("赵"):
#         temp.append(itme) #把要删除的内容记录下来
#         # lst.remove[itme] #不可用 跨值
# for itme in temp:
#     lst.remove(itme)
#     print(lst)

    # 安全稳妥的循环删除方式：
    # 将要删除的内容保存在一个新列表中，循环新列表，删除老列表


# tuple  元组 ，特点:不可变的列表
# t = ('张无忌','赵敏','呵呵哒')
# print(t)
#
# print(t[1:3])
# t[0]='樵夫' #tuple'oblect does not support item assignment
# print(t)

#你固定了某些数据，不允许外界修改
#元组如果只有1个元素(*)，  需要在元素的末尾添加一个逗号
#t=(“哈哈，)  #()默认是优先级
##print((1+3)*6)
# print(t)
# print(type(t))
#关于元组的不可变（坑）   代指的是内存地址不可变
# t=(1,2,3,["呵呵哒","么么哒"])
# t[3].append("哒哒哒")
# print(t)

# set 集合   set集合是无序的，
# s = {1,"呵呵哒",2,3}
# print(type(s))
# print(s)

#不可哈希:python 中set 集合进行数据存储的时候，需要对数据进行哈希计算，根据计算出来的哈希值进行存储
    # set 集合要求存储的数据必须进行哈希计算
    # 可变的数据类型，list ,dict, set
#可哈希：不可变的数据类型，int ,str ,tuple,bool
# s = {1,"呵呵哒",2,3,[]}  #unhashable type: 'list'
# print(s)

# s = set() #创建空集合
# s.add("sw")
# s.add("wzl")
# s.add("李小龙")

# s.pop()  #由于集合无序，测试没法验证
#
# s.remove("李小龙")
# 逍遥修改，先删除，在新增

# 查询
# for item in s:
#     print(item)

    # 交集，并集，差集
# s1 = {"刘能","赵四","皮长山"}
# s2 = {"刘科长","冯乡长","皮长山"}
#
# print(s1 & s2)  # 交集
# print(s1.intersection(s2))
# print(s1 | s2)  # 并集
# print(s1.union(s2))
# print(s1 - s2)  # 差集
# print(s1.difference(s2))

# 重要的作用：可以去除重复
# s1 = {"周杰伦","哈利","菜大师","李小康"}
# print(s1)
# s1.add("周杰伦")
# print(s1)

# lst=["周杰伦","昆凌","蔡依林","侯佩岑","周杰伦","昆凌","蔡依林","侯佩岑","周杰伦","昆凌","蔡休"]
# print(lst)
# print(list(set(lst))) #去除重复之后的数据是无序的，



#首先，字典是以键值对的形式进行数据存储的
# 字典的表示方式:{key:value,key1:value1}
# dict = {"jay":"杰伦","金毛狮王":"谢逊"}
# val = dict["金毛狮王"] #用起来就是把索引换成了key
# print(val)
#
# # 字典的key 必须是可哈希的数据类型
# # val可以是任何的数据类型
# dic = {[]:123}
# print(dic)

# 4.2字段的增删改查
#
# dic = dict()
# dic['jay'] = "李小龙"
# dic[1] = 123
#
# print(dic)
#
# dic.setdefault("jay","牛杂汤")   #设置默认值.如果以前已经有了tom了，setdefault就不起作用了
# print
#
# # 删除
# dic.pop("jay")  #根据key删除

#查询
# print(dic['jay10010'])  #如果key 不存在,程序报错，当你确定key是没问题的时候使用
# print(dic.get('jay10086'))  #如果key不存在,程序返回None，不确定用

# #None
# a = None   #单纯是空，没有意思
# print(type(a))_

# dic = {
#     "王子龙":"特牛逼",
#     "李云龙":"开大炮",
#     "李小龙":"武功好",
#     "成龙":"一刀999",
#
# }
#
# name = input("请输入你要查找的龙")
#
# val = dic.get(name)
# if val is None:
#     print("没找到这个龙")
# else:
#     print(val)
#

# 字典的循环与嵌套

#1.可以用for循环，直接拿到key
# dic = {
#     "王子龙":"特牛逼",
#     "李云龙":"开大炮",
#     "李小龙":"武功好",
#     "成龙":"一刀999",
#
# }
# for key in dic:
#     print(key,dic[key])

#2,希望把所有的key全都保存在一个列表中
# print(list(dic.keys()))#拿到所有的key了

#3,希望吧所有的value都放在一个列表中
# print(list(dic.values()))
#
#4,直接拿到字典中的key和value
# print(list(dic.items()))
# for key,value in dic.items():  #可以直接拿到字典的所有key,value
#     # key = item[0]
#     # value = item[1]
#     print(key,value)

# a, b = (1, 2)  # 元组或者列表都可以执行该操作，该操作被称为解构（解包）
# print(a)
# print(b)

# k，v直接提取字典值
# for k,v in dic.items():
#     print(k,v)

# 字典的嵌套
# wangfeng ={
#     "name":"汪峰",
#     "age":18,
#     "wife":{
#         "name":"章子怡",
#         "hobby":"演戏",
#         "assistant":{
#             "name":"樵夫",
#             "age":"19",
#             "hobby":"打游戏",
#         }
#     },
#     "children":[
#         {"name":"孩儿1","age": 13},
#         {"name": "孩儿2", "age": 10},
#         {"name": "孩儿3", "age": 5},
#     ]
# }
#
# #汪峰妻子的助手的名字
# name = wangfeng['wife']['assistant']['name']
# print(name)
# #给汪峰的第二个孩子加1岁
# wangfeng['children'][1]['age'] = wangfeng['children'][1]['age']+1
# print(wangfeng)

#7.4 关于字典的循环删除
#
# dic = {
#     "王子龙":"特牛逼",
#     "李云龙":"开大炮",
#     "李小龙":"武功好",
#     "成龙":"一刀999",
#
# }
#
# temp = [] #存放即将要删除的key
# for k in dic:
#     if k.startswith("王"):
#         temp.append(k)
#         # dic.pop(k) #dictionary changed size during iteration
# for t in temp:
#     dic.pop(t)
#
# print(dic)




