# 1.字符集和编码
# 01=>1010101010=>二进制转化成十进制=>8
# 电脑如何进行存储文字信息
# 2.bytes
# ascii=>编排了128个文字符号.只需要7个0和1就可以表示了，01111111=>1byte=>8bit
# ANSI=>一套标准，每个字符16bit,2byte
# 0000000001111111
# 到了中国，gb2312编码
# 到了台湾，big5编码
# 到了日本，JIS编码


# 总结：
# 1.ascii:8bit,lbyte
# 2.gbk:16bit,2byte
# windows默认
# 3.unicode:32bit,4byte(没法用，只是一个标准)
# 4.utf-8:
# mac默认
# 英文：8bit,1byte
# 欧洲：16bit,2byte
# 中文：24bit,3byte
#
# gbk和utf-8能直接就进行转化.
# 我军密码本->文字->敌军密码本

s = "王子龙"
bs1 = s.encode('gbk')
bs2 = s.encode('utf-8')
print(bs1)
print(bs2)

# 怎么把一个gbk的字节转换成utf-8的字节
bs = b'\xcd\xf5\xd7\xd3\xc1\xfa'
#先变成文字符号(字符串)
s = bs.decode('gbk')
print(s)

#1,str.encode("编码")进行编码
#2,bytes,decode("编码")进行解码



