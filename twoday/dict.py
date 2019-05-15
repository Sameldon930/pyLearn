#-*-coding:utf-8-*-
# things = ['a','b','c','d']
# print things[1]  # 'b'

# things[1] = 'e'
# print things[1] # 'e'

# # 此时things这个列表的第二个元素已经从 b 变成 e
# print things

# # 对象
# stuff = {'name':'zed','age':36,'height':6*12+2}
# print stuff['name']

# print stuff['age']

# print stuff['height']

# stuff['city'] = 'zzs'

# print stuff['city'] 

states = {
    'Oregon'  :'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}
cities = {
    'CA':'San Francisco',
    'MI': 'Detroit', 
    'FL': 'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10

print cities['NY']
print cities['OR']

print '-' * 10
print states['Michigan']
print states['Florida']

print '-' * 10
print cities[states['Michigan']]
print cities[states['Florida']]

print '-' * 10
# items() 方法以列表返回可遍历的(键, 值) 元组数组。
for state, abbrev in states.items(): 
    print "%s is abbreviated %s" % (state, abbrev)
    
print '-' * 10
# items() 方法以列表返回可遍历的(键, 值) 元组数组。
for abbrev, city in cities.items(): 
    print "%s has the city %s" % (abbrev, city)
    
print '-' * 10
# items() 方法以列表返回可遍历的(键, 值) 元组数组。
for state, abbrev in states.items(): 
    print "%s state is abbreviated %s and has city %s" % ( state, abbrev, cities[abbrev])

print '-' * 10

state = states.get('Texas', None)

if not state: 
    print "Sorry, no Texas."
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
