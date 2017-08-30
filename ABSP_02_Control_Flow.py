# encoding: utf-8
"""
@ Author: Kunkai Su 
@ Contact: su.kk@qq.com
@ Site: www.geneureka.com
@ Project: ABSP
@ File: ABSP_02_Control_Flow.py
@ Time: 2017/8/30 14:37:27

这一行开始写关于本文件的说明与解释
"""

# IF
name = 'Alice'
age = 14
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You ar not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

# WHILE
spam = 0
while spam < 5:
    print('Hello world.')
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you.')

# BREAK
while True:
    print('Please type your name:')
    name = input()
    if name == 'your name':
        break
print("Thank you.")

# CONTINUE
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is your password? (It is a fish.)')
    passwword = input()
    if passwword == 'swordfish':
        break
print("Access granted.")

# FOR
print('My name is')
for i in range(5):
    print('Jimmy five times (' + str(i) + ')')

    # range()
for i in range(0, 10, 2):
    print(i)

# import
import random

for i in range(5):
    print(random.randint(1, 10))
