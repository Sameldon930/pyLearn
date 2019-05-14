#-*- coding:utf-8-*-
from sys import argv
script,user_name,age = argv
prompt = '>>>>>>'
# prompt存放符号
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
like = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print "are you %s years old ?" % age
sure = raw_input(prompt)
print """ 
Alright, so you said %r about liking me.
ang you are %r years old.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. """ % (
    like, age,lives, computer)