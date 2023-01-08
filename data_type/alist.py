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
t = ('张无忌','赵敏','呵呵哒')
print(t)

print(t[1:3])
t[0]='樵夫' #tuple'oblect does not support item assignment
print(t)


