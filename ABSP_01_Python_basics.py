# encoding: utf-8
"""
@ Author: Kunkai Su 
@ Contact: su.kk@qq.com
@ Site: www.geneureka.com
@ Project: ABSP
@ File: ABSP_01_Python_basics.py
@ Time: 2017/8/24 22:08:24

这一行开始写关于本文件的说明与解释
"""


def run():
    pass


if __name__ == '__main__':
    run()

# This program says hello and asks for my name.

print('Hello world')
print('What is your name?')  # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')  # aks for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
