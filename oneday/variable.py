# -*- coding:utf-8 -*-
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpppl_capacity =  cars_driven * space_in_a_car
average_passengers_per_car =  passengers / cars_driven

# print cars
# print drivers
# print cars_not_driven
# print carpppl_capacity
# print passengers
# print "We need to put about", average_passengers_per_car,"in each car."
# print "hey %s there." % "you"


my_name = 'Zed A.shaw'
my_age = 35 
my_height = 74
my_weight = 180
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

# print "Let's talk about %r." % my_name  
# #Let's talk about Zed A.shaw
# print "He's %d inches tall." % my_height
# #He's 74 inches tall 
# print "He's %d pounds heavy." % my_weight
# # He's 180 pounds heavy
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# # He's got blue eyes and brown hair
# print "His teeth are usually %s depending on the coffee." % my_teeth
# # His teeth are usually white depending on the coffee 
# print "If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight)
# # If I add 35, 74, and 180 I get 289.

zzs = "sameldon930"
# print "你好 我叫 %s." % zzs

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# print x
# print y

# print  "I said: %r." % x

hilarious = False

jokeevaluation = "Isn't that joke so funny?! %r"
# print jokeevaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# +号让字符串组合成新的字符串
# print w+e

# print "Mary had a little lamb."
# print "Its fleece was white as %s." % 'snow'
# print "And everywhere that Mary went."
# print "." * 10 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# 含逗号是连接符（等于空格）  所以输出的结果是  Cheese Burger
# print end1 + end2 + end3 + end4 + end5 + end6,
# print end7 + end8 + end9 + end10 + end11 + end12

#不含逗号 相当于输出两句
# Cheese
# Burger
# print end1 + end2 + end3 + end4 + end5 + end6
# print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"

# print formatter % (1,2,3,4)
# print formatter % ("one","two","three","four")
# print formatter % (True, False, False, True)
# print formatter % (
#     "I had this thing.", 
#     "That you could type up right.", 
#     "But it didn't sing.", 
#     "So I said goodnight."
# )

days = "Mon Tue Wed Thu Fri Sat Sun"
# \n 换行的意思
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# print "here are the days:",days
# print "Here are the months: ", months 
# 一对 三个双引号或者三个单引号 包起来 相当于换行段落  引号之间不能有空格
# print """
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """

# \符号 可以进行转义
# print "my name is  \"zzs \" "


# \t 缩进一格 两个缩进两格 以此类推
tabby_cat = "\t\t\tI'm tabbed in."
# \n 表示换行
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# \n后面还有其他内容 会导致换行失效
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
'''

fat_cat2 = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
"""
# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat
# print fat_cat2

# print "how old are you",
# age = raw_input()
# print "how tall are you",
# height = raw_input()
# print "how weight are you",
# weight = raw_input()
# print "So, you're %r old, %r tall and %r heavy." % ( 
# age, height, weight
# )
# # Name? 可以用来提示用户
# y =  raw_input("Name? ")

# age = raw_input("how old are you ")
# height = raw_input("how tall are you")
# weight = raw_input("how weight are you")

# print "So, you're %r old, %r tall and %r heavy." % ( 
# age,height,weight)


