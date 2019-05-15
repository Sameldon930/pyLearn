#-*-coding:utf-8-*-

from sys import exit

def gold_room():
    #这个房间里全是金子。你要带多少钱?
    print "This room is full of gold. How much do you take?"
    # 你要带走多少 请输入
    next = raw_input("How much do you take?") 
    if "0" in next or "1" in next: 
        how_much = int(next) 
    else: 
        dead("Man, learn to type a number.")
    # 如果上面的数字小于 50 就成功 并不在执行程序
    if how_much < 50: 
        print "Nice, you're not greedy, you win!" 
        exit(0) 
    # 如果大于五十 就说明你这个人很贪婪
    else: 
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."  #这里有一只熊
    print "The bear has a bunch of honey."   #熊有一串蜂蜜
    print "The fat bear is in front of another door."   #胖熊在另一扇门前。
    print "How are you going to move the bear?"  #你打算怎么移动这只熊?
    # 默认熊没有移动
    bear_moved = False
    
    while True:
        
        next = raw_input(">")
        # 如果要拿糖果 没有 死路一条
        if next == "take honey":
            # 熊看着你，然后把你的脸打了下来
            dead("The bear looks at you then slaps your face off.")
        # 如果要嘲讽熊 并且 熊在移动
        elif next == "taunt bear" and not bear_moved:
            # 熊已经离开了门。你现在可以过一遍了
            print "The bear has moved from the door. You can go through it now." 
            bear_moved = True
        # 如果要嘲讽熊 并且 熊不在移动  
        elif next == "taunt bear" and bear_moved:
            # 熊生气了，咬掉了你的腿。
            dead("The bear gets pissed off and chews your leg off.") 
        # 如果是打开门 并且熊已经移动 那就进入到黄金的屋子
        elif next == "open door" and bear_moved: 
            gold_room() 
        # 如果进到这个房间没有想法 就没办法进行下一步
        else: 
            print "I got no idea what that means."
            
def cthulhu_room(): 
    print "Here you see the great evil Cthulhu."  #这里你看到的是邪恶的克苏鲁
    print "He, it, whatever stares at you and you go insane." #他，它，无论什么盯着你看，你就会发疯。
    print "Do you flee for your life or eat your head?" #你们是逃命呢，还是吃自己的头呢?
 
    next = raw_input("> ")
    # 逃命
    if "flee" in next: 
        # 就会原来的地方进行重新选择
        start() 
        # 选择死亡
    elif "head" in next: 
        dead("Well that was tasty!") 
    else: 
        cthulhu_room()
        
def dead(why): 
    print why, "Good job!" 
    exit(0)
    
def start(): 
    print "You are in a dark room." #你在一个黑暗的房间里。
    print "There is a door to your right and left." #在你的左右两边都有一扇门。
    print "Which one do you take?" #你选哪一个?
    next = raw_input("right or left ")
    if next == "left":
        # 如果是选择左边  bear_room
        bear_room() 
    # 如果是右边  cthulhu_room
    elif next == "right": 
        cthulhu_room() 
    else: 
        dead("You stumble around the room until you starve.")
start()