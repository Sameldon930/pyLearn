#-*- coding:utf-8-*-

ten_things =  "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

# 将字符串 根据空格进行切割
stuff = ten_things.split(' ')

# 输出字符串处理后的结果  处理之后变成列表
# ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
print stuff

print "\n"

more_stuff = [
    "Day", 
    "Night", 
    "Song", 
    "Frisbee", 
    "Corn", 
    "Banana", 
    "Girl", 
    "Boy"
]

while len(stuff) != 10:
    # 删除more_stuff列表中的key  返回被删除key对应的value  从尾部开始删
    next_one = more_stuff.pop()
    print next_one
    # 将上面返回的value 放到 stuff 这个列表
    stuff.append(next_one)
    print len(stuff)
    
# ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
print stuff

print "Let's do some things with stuff."
print "\n"


# 下标为1 也就是第二个  Oranges
print stuff[1]
# 下标为-1 也就是最后一个 Corn
print stuff[-1] 
# pop从尾部开始删除  也就是默认先删掉最后一个  corn
print stuff.pop()
# 输出stuff列表 拼接上空格 变成数组 
# join方法 将序列中的元素以指定的字符连接生成一个新的字符串  str.join(列表)
print ' '.join(stuff) 
# 用#拼接stuff[3:5]中的下标为3 和 下标为5-1的 原理同range()  Telephone#Light
print '#'.join(stuff[3:5]) 

