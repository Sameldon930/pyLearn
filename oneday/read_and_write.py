#-*- coding:utf-8-*-
from sys import argv

script,filename = argv
print "We're going to erase %r." % filename
#我们将擦去这个文件 如果不愿意 就退出 愿意就回车继续
print "If you don't want that, hit CTRL-C (^C). "
print "If you do want that, hit RETURN."

raw_input(">>")
#正在打开文件
print "Opening the file..."
# 打开文件 写的状态
target = open(filename,'w')
print "Truncating the file. Goodbye!"
# 清空文件的内容
target.truncate()

print "Now I'm going to ask you for three lines."
# 清空之后 开始写入新的内容
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#执行写入
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "And finally, we close it."
# 文件关闭
target.close()

