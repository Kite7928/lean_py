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
i = 1
while i <= 10:
    if i == 4:
        i = i + 1
        continue  # 终止本次继续执行下一次循环
    print(i)
    i = i + 1
"测试git正常使用"