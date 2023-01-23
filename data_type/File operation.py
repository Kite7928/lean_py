# 1.找到这个文件，双击打开它
# open(文件路径,mode="",encoding="")
# 1,绝对路径  d:/test/xxxx.txt
# 2,相对路径 相对于当前你的程序所在的文件夹
#
# ../上一层文件夹

# mode:
# r:read读取
# w:write写
# a:append追加写入
# b:读写的是非文本文件
# with:上下文，不需要手动去关闭一个文件
import os  #导入操作系统的相关类库
import time #和时间相关的类库
# 想当于一条管子，需要就读取
# f = open("夜晚数据.txt", mode="r", encoding="utf-8")
# content = f.read() #全部读取
# print(content)
#
# line = f.readline().strip() #去掉字符串左右两端的空白，空格，换行，制表符
# print(line)
#
# line1 = f.readlines()
# print(line1)


#最重要的一种文本读取方式（必须掌握）     #从f中读取到每一行数据
# for line in f:
#     line4 =line.strip()
#
#     print(line4)

# 写入文件
#     在w模式下,如果文件不存在,自动的创建一个文件
    # w模式下，每一次open会清空文件中的内容
    # k = open("奇幻.txt", mode="w",encoding="utf-8")
    # k.write("流量王")
    # k.close() #每次操作过后记得关闭
    #准备一个列表，要求把列表中的每一项内容写入到文件中
# lst = ['赵子龙','黄忠','张飞','关羽','刘邦']
#
# v = open("三国志.txt", mode="w",encoding="utf-8")
# #大多数情况要吧open写在循环外面,  千万不要选错自动模板，不然更改后无效
# for item in lst:
#     v.write(item)
#     v.write("\n")
#
# v.close()

#追加数据
# s = open("三国志.txt", mode="a",encoding="utf-8")
# s.write("黎明")

#with 自动关闭，不用close
# with open("三国志.txt", mode="r", encoding="utf-8") as f:
#     for  line in f:
#         print(line.strip())

# 想要读取图片
#在读写非文本文件的时候要加上b
# with open("小狗狗.png", mode="rb") as f:
#     for line in f:
#         print(line) #读取出来为字节码

# 文件的复制
# 从源文件读取内容，写入到新路径去
# with open("小狗狗.png", mode="rb") as f1,\
#     open("../len/大狗狗.png", mode="wb") as f2:
#     for line in f1:
#         f2.write(line)

#把文件中的周->张
with open("人名单.txt", mode="r",encoding="utf-8") as f1, \
    open("人名单_副本.txt", mode="w",encoding="utf-8" ) as f2:
    for line in f1:
        line = line.strip() #去掉换行
        if line.startswith("张"):
            line = line.replace("张","肖")  #修改
            f2.write(line)
            f2.write("\n")

time.sleep(3) #让程序休眠3秒钟
#删除源文件
os.remove("人名单.txt")

time.sleep(3) #让程序休眠3秒钟
#把副本文件从命名成源文件
os.rename("人名单_副本.txt","人名单.txt")




