from string import *
cood = {'lattitude' : '102.9SW', 'longitude' : '76.4NE'}
print("Coordinates: {lattitude}, {longitude}".format(**cood))

"""Printing out the result of the value in each corresponding format"""
print("int = {0:c}; hex = {1:#x}; bin = {0:#b}; oct = {1:#o}".format(65,24))

"""Using mapping to format a dictionary and get the required result"""
players = {'left_footer' : 'Lionel Messi', 'right_footer' : 'Cristiano Ronaldo'}
print("Favourite_foot: left footer({left_footer}), right footer({right_footer})".format(**players))

"""Using comma to separate thousand in a digit""" 
s = 1927344889
print("{:,}".format(s))

"""Print in percentage"""
price  = 19
total = 22
print("{:.2%}\n".format(price/total))

"""This is how to align text"""
print("{:*<100}\n".format("to_the_left"))

print("{:*^100}\n".format("to_the_center"))

print("{:*>100}\n".format("to_the_right"))

s = (str.split("if i was made from a broken mould"))
for i in s:
    d = str.capitalize(s)
    print(d)