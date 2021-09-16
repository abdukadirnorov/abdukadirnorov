# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 00:09:02 2021

@author: USER
"""
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars=cars[0:4]
# print(my_cars)

# print(cars[1:3]) # 1 va 2 ni oladi 3 esa qoladi 
# print(cars[3:5]) # be yerda esa 3 va 4 ni oladi 
# print(cars[:3]) # be yerda 0 dan 2 gachani olishi mumkin 
# print(cars[2:]) # bu yerda 2 dan boshlab oxirigacha olishi mumkin
# sonlar=[1,2,3,4,5]
# sonlar2=sonlar
# sonlar2.append(8)
# sonlar2.append(10)
# print(sonlar2)# bu yerda ikkila elementning qiymatlari bir xil o'zgaradi

# sonlar2=sonlar[:] # nusxalash ajoyib
# sonlar2.append(1112)
# sonlar2.append(450)
# print(sonlar2)
# print(sonlar) # bu nusxalash deyiladi, 
#  # TUPLE FUNKTSIYASI (O'ZGARMAS DEYILADI)
# tomonlar=(12, 15, 16.5)
# print(tomonlar) 
# toys=('bus', 'car', 'dino', 'snake', 'lizard')
# print(toys[2:])
# print(toys[0:3]) # bu holatda list kabi ish berdi 
# toys[2]='dracon' # TypeError: 'tuple' object does not support item assignment
# print(toys) # bu yerda o'zgartirib bo'lmaydi qavs ichidagi qiymatlarni 
# o'zgartirish mumkin qachonki biz tuple dan listga o'tsak
# toys=list(toys)
# print(type(toys)) 
# toys.append('dracon')
# toys.remove('bus')
# toys[1]='mcqueen'
# print(toys)
countries=['russia','usa','japan', 'korea', 'indonesia', 'UK']
# print(countries)
# print(sorted(countries))
# print(sorted(countries, reverse=True))
# print(sorted(countries, reverse=False))
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)
numbers=list(range(120,1200,2))
# print(numbers)
# numbers=sum(numbers)
# print(sum(numbers))

# # son=max(numbers)-min(numbers)

# print(len(numbers))
# print(numbers[:20])
print(numbers[-20:])
taomlar=['somsa', 'manti', 'osh', 'lagman','qovurdoq']
nonushta=taomlar[:]
nonushta.remove('somsa') 
nonushta.remove('manti')
nonushta.remove('osh')
nonushta.remove('lagman')
nonushta.remove('qovurdoq')
nonushta.append('mastava')
nonushta.append('goja')
nonushta.append('osh')
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)
# print(type(nonushta))
nonushta[0]="qaymoq va issiq non"