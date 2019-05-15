#-*-coding:utf-8-*-
# 引入包
from sys import argv
# 拆包
script,input_file = argv

# 定义读取文件方法 传入文件名字
def print_all(f):
    print f.read()
# 定义文件读取指针的指定位置的方法
def rewind(f):
    f.seek(0)
# 读书文件的每一行的内容 以及行数
def print_a_line(line_count,f):
    print line_count,f.readline()
    
# 打卡一个文件存入变量
current_file = open(input_file)

print "First let's print the whole file:\n"
# 读取打开的文件内容
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# seek()移动文件读取指针到指定位置
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line +=  1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

# f.seek(0) 你就回到了文件的开始
# f.readline() 则会读取文件的一行
