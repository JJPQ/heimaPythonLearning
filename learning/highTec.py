import random
import threading
import time
import socket


# 闭包
# def bank(initial_account=0):
#     def atm(num, deposit=True):
#         nonlocal initial_account
#         if deposit:
#             initial_account += num
#         else:
#             initial_account -= num
#         print(f"现在余额为{initial_account}")
#
#     return atm
#
#
# account1 = bank()
# account2 = bank(100)
# balance1 = account1(10, True)
# balance2 = account2(10, False)


# 装饰器
# def outer(func):
#     def inner():
#         print("开始睡觉")
#         func()
#         print("睡觉结束")
#
#     return inner
#
# @outer
# def sleep():
#     num = random.randint(1, 5)
#     print(f"我要睡觉了，睡{num}秒")
#     time.sleep((num))
#
#
# sleep()


# 单例模式
# class single:
#     pass
#
#
# single = single()
# s1 = single
# s2 = single
# print(s1, s2)


# 工厂模式
# class Person:
#     pass
# class Worker(Person):
#     pass
# class Student(Person):
#     pass
# class Farmer(Person):
#     pass
#
# class PersonFactory:
#     def get_person(self,str):
#         if str=='w':
#             return Worker()
#         elif str=='s':
#             return Student()
#         elif str=='f':
#             return Farmer()
#
# worker=PersonFactory().get_person('w')
# student=PersonFactory().get_person('s')
# print(type(worker))


# 多线程编程
# def sing(msg):
#     while 1:
#         print(f"我在唱歌，{msg}")
#         time.sleep(1)
# def dance(msg):
#     while 1:
#         print(f"我在跳舞，{msg}")
#         time.sleep(1)
# sing_thread=threading.Thread(target=sing,args=("啦啦啦",))
# dance_thread=threading.Thread(target=dance,kwargs={"msg":"嘿嘿嘿"})
# sing_thread.start()
# dance_thread.start()


# socket服务端开发
