#-*-coding:utf-8-*-
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copy from %s to %s."%(from_file,to_file)
# 打开要复制的文件
in_file = open(from_file)
# 读取文件的内容
indata  = in_file.read()

# 计算出该文件有多少字节
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."

# # 确认是否进行下一步
# raw_input("continue or abort ?")
# 以写模式打开目标文件
out_file = open(to_file,'w')
# 将刚才读取的文件内容 写入目标文件
out_file.write(indata)

print "Alright, all done."
# 文件关闭
out_file.close()
in_file.close()