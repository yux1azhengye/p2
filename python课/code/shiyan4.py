# #写入
# with open('留言.txt','a') as fw:
#     fw.write(input("你想给小明的留言:"))
# #读取
# with open('留言.txt','r') as fr:
#     message = fr.read()
# print("小明收到的留言:",message)

#二进制存储图片
# with open ('头像.jpg','rb') as f:
#     with open('存放头像二进制.dat','wb') as f2:
#         for line in f.readlines():
#             f2.write(line)
#
# dat转jpg
# with open('存放头像二进制.dat','rb') as f:
#     with open('取出的头像.jpg','wb') as f2:
#         for line in f.readlines():
#             f2.write(line)


#
# import shutil
# import os
#
# if not os.path.exists('留言板'):
#     os.mkdir('留言板')
# if not os.path.exists('留言板备份'):
#     os.mkdir('留言板备份')
# path1 = '留言板/'
# path2 = '留言板备份/'
# filename = input("留言条标题:")+".txt"
# text     = input("留言条内容:")
# srcfile = path1 + filename
# bakfile = path2 + filename
# with open( srcfile , 'w+') as f1:
#     f1.write(text)
# # 这一句不能放在with里面 因为with需要完整走完整个with后才会将文件执行完成,具体原理不知道,不过这是调试的结果
# shutil.copy(srcfile,bakfile)
# with open('留言.txt','a') as fw:
#     fw.write(input("你想给小明的留言:"))
# #读取
# with open('留言.txt','r') as fr:
#     message = fr.read()
# print("小明收到的留言:",message)

import os.path
import os

total = 0

def cont_txt(path):
    global total
    for file in os.listdir(path):
        file = os.path.join(path,file)
        if os.path.isdir(file):
            cont_txt(file)
        elif file.endswith(".txt"):
            for line in open(file,'r').readlines():
                total += len(line.strip('\n'))
cont_txt("留言板")
print("截止目前留言板的总字数:",total)
