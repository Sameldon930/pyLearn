#-*- coding:utf-8-*-
from sys import argv
#解包
script,filename =  argv
# 打开文件
txt = open(filename)
# 获取到文件的名字
print "Here's your file %r:" % txt
print "\n"
# 读取文件内容
print txt.read()
print "Type the filename again:"
# 输入文件的名字
file_again = raw_input(">")
# 打开上面输入的文件的名字
txt_again = open(file_again)
print txt_again.read()

