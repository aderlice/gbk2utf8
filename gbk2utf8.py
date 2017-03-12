# #encoding: utf-8
# s = "《" # 整个文件是UTF-8编码，所以这里的字符串也是UTF-8
# u = bytes(s, "utf-8") # 将utf-8的str转换为unicode
# g = s.encode('GBK') # 将unicode转换为str，编码为GBK
# print(type(s), "len=", len(s))
# # 输出： len= 6，utf-8每个汉字占3字节
# print(type(u), "len=", len(u))
# # 输出： len= 6，unicode统计的是字数
# print(type(g), "len=", len(g))
# # 输出：g = u.encode('GBK')，GBK每个汉字占2字节
# print(s) 
# # 在GBK/ANSI环境下（如Windows），输出乱码，
# #因为此时屏幕输出会被强制理解为GBK；Linux下显示正常
# print(g)
# print(u) 
# # 在Windows下输出“你好”，
# #Linux(UTF-8环境)下报错，原因同上。

f0 = open('test.txt', 'rb')
f1 = open('test1.txt', 'wb')
count = 0
while True :
    # count = count + 1
    # print(count)
    text = ""
    text = f0.read(1)
    if not text:
        break
    if(text < b'\x80') :
        f1.write(text)
        # test = b'\x80'
        # test = test + text.decode('ascii')
        # print(test)
        continue
    # if(count > 20) :
    #     break
    text = text + f0.read(1)
    try :
        text1 = text.decode('gbk')
        # print(text1)
        text2 = text1.encode('utf8')
    # print(text2)
        f1.write(text2)
    except Exception as e:
        continue
f0.close()
f1.close()