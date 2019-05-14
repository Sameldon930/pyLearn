#-*-coding:utf-8-*-
# def 定义函数的关键字

# 形参有若干个 在函数体中进行定义几个
def print_two(*args):
    arg1,arg2 = args
    print "arg1:%r,arg2:%r"%(arg1,arg2)
# 两个形参
def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r"%(arg1,arg2)
# 一个形参
def print_one(arg1):
    print "arg1:%r"%arg1
# 没有参数
def print_none():
    print "i got nothin"

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("zzs")
print_none()