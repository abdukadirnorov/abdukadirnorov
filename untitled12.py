# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:07:59 2021

@author: USER
"""

# XATOLAR BILAN ISHLASH 

# print("hello world) # SyntaxError: EOL while scanning string literal
      # bu yerda qator yakunida xatolik bor degani,  
  
#print "Hello World"      
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World")?
# qavs tushib qoldi degani (parentheses).

# print("Hello world"
# SyntaxError: unexpected EOF while parsing- funksiya oxirida xatolik mavjud degani       

 # print("Hello world")

    # ^
# IndentationError: unexpected indent # bu yerda esa bosh joy mavjud degan ma'noni beradi

# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1)
# IndentationError: expected an indented block- bu yerda ham huddi teskarisi bo'sh joy tashlash zarur'

#RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK!!!
 # run time error ni turlari ko'p ulardan ba'zilari
# Type Error:
# son = input("Istalgan son kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng")
# bu yerda son ichida string holatida bo'ladi biz intejerga olib o'tishimiz zarur

#NameError:
# prit("Hello world")    
#NameError: name 'prit' is not defined- bu yerda prit degan nom topilmadi.

# ValueError:
# son = int(input("Istalgan son kiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")    
# ValueError: invalid literal for int() with base 10: '46.5' integer faqat butun
#  sonlar bilan ishlaydi, float esa o'nlik sonlar bilan ishlaydi ex: (45.2), (14.8)

# IndexError
# mevalar = ['olma','anor','uzum']
# print(mevalar[3])
# bu yerda indeks xato berilganligi sababli funktsiya bajarilmaydi o dan boshlanadi sanoq pythonda

#ZeroDivisionError:
# Dastur jarayonida 0 ga bo'lish yuzaga kelgandagi xatolik
# x, y = 50, 50
# z = 250/(x-y) 
# bu yerda (x-y)- o ga teng bo'lganligi sababli xato kelib chiqadi
  
# MANTIQIY XATOLAR:
# radius = 5
# pi = 4.14   
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)
# bu yerda funksiya bajariladi ammo natija xato chiqadi shuning uchun qitmat berishda diqqatni qaratish zarur!!!

# yana bir misol ko'raylik 
# son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2
# print(f"{son} ning ildizi {ildiz} ga teng")
# istalgan son kiriting: 9
# Natija:4.5 sabab bu yerda son birinchi birinchi darajaga ko'taradi keyin esa ikkiga bo'ladi 
# biz buning uchun qavs ichiga olishimiz zarur ex: (1/2) yoki 0.5 dep yozishimiz zarur:
    
#Noo'rin bo'sh joy qoldirish (yoki qoldirmaslik) ham mantiqiy xatoga olib 
#kelishi mumkin:   
# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi") - #bu yerda dastur tugadi for siklga qo'shilib qoladi va
    # qaytarilaveradi biz buning uchun joy qoldirmasdan surib qo'yishimiz zarur.
    
    

    