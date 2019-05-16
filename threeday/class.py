#-*-coding:utf-8-*-
# 定义一个类
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
        # 遍历所传参数
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
# 实例类成为对象 传入参数
happy_bday = Song([
    "Happy birthday to you", 
    "I don't want to get sued", 
    "So I'll stop right there"
])
# 实例类成为对象 传入参数
bulls_on_garade = Song([
    "They rally around the family", 
    "With pockets full of shells"
])

zzs = Song(['1231312','12321312','35456575'])

# 上面的对象调用方法
happy_bday.sing_me_a_song()
bulls_on_garade.sing_me_a_song()
zzs.sing_me_a_song()

# class : 告诉 Python 创建新类型的东
# object : 两个意思：最基本类型的东西，或者某个东西的实例。
# instance : 这是当你让Python创建一个 class 的时候，你得到的东西。
# def : 这是在类里边定义函数的方法。
# self : class 里边的函数会用到这个参数，self 指代被访问的 object 或者 instance 的一个变量。
# inheritance : 指一个 class 可以继承另一个类的特性，和父子关系类似。
# composition : 指一个 class 可以将别的类作为它的部件构建起来，有点像车子和车轮的关系。
# attribute : class 的一个属性，它来自于 composition，而且通常是一个变量。
# is-a : 用来描述继承关系，例如 Salmon is-a Fish.
# has-a : 用来描述某个东西是另外一些东西组成的，或者某个东西有某个特征，例如Salmon has-a mouth.