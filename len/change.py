# # 默认是字符串输出
# a = input("请输入第一个数字")
# b = input("请输入第2个数字")
#
# a = int(a)
# b = int(b)
# print("计算结果为:", a + b )

# break让当前这个循环立即停止
# continue:停止当前本次循环，继续执行下一次循环
# while 循环 break continue
# while  True:
#     content = input("请输入你要喷的内容(q结束):")
#     if content == "q":
#         break
#         print("发送给下路的:",content)

# 从1-10
# i = 1
# while i <= 10:
#     if i == 4:
#         i = i + 1
#         continue  # 终止本次继续执行下一次循环
#     print(i)
#     i = i + 1
"测试git正常使用"



#字符串是可迭代的
# for循环:
#
#     for 变量 in 可迭代的东西:
#         代码
#     把可迭代的东西中的每一项内容拿出来. 挨个的赋值给变量. 每一次赋值都要执行一次循环体(代码)
#
#
# for循环想要计数. 必须借助于range
#
# range(n): 从0数到n. 不包含n
# range(m, n): 从m数到n, 不包含n
# range(m, n, s): 从m数到n, 不包含n, 每次的间隔是s
#
# 平时用的多的是for循环, while循环用的多的是死循环

# s = "你好，朋友"
# for c in s:
#     print("打招呼:",c)

# for i in range(3,10,2):
#         print(i)


# pass 占位符
# a = 10
# if a > 10:
#     pass

