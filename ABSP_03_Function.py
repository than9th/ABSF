# encoding: utf-8
"""
@ Author: Kunkai Su 
@ Contact: su.kk@qq.com
@ Site: www.geneureka.com
@ Project: ABSP
@ File: ABSP_03_Function.py.py
@ Time: 2017/8/30 16:04:19

这一行开始写关于本文件的说明与解释
"""


# Function
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')


hello()
hello()
hello()


# Test parameter
def hello(name):
    print('Hello ' + name)


hello('Alice')
hello('Bob')

# Guess number
import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
print(getAnswer(random.randint(1, 9)))
