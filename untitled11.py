# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:39:52 2021

@author: Abduqodir
"""
# if- elif-else:::
    #  elif-agar, aks holda, deb tarjima qilinadi 
#Diqqat!if-elif-else ketma-ketlikda biror shart 
#bajarilishi bilan, Python qolgan shartlarni tekshirmaydi.    
 
# yosh=int(input("yoshingizni kiriting: "))
# if yosh<=4:
#     print("sizga kirish bepul! ")   
# elif yosh<=12:
#     print("sizga kirish 5000 so'm") 
# else:
#     print("sizga kirish 10000 so'm")

# yosh=int(input("yoshingizni kiriting: ")) 
# if yosh<=4:
#     price=0
# elif yosh<=12:
#     price=5000
# else:
#     price=10000
# print(f"Sizga kirish {price} so'm ")
                
# yosh=int(input("yoshiingiz nechchida ? "))
# if yosh<=4:
#     price=0
# elif yosh<=12:
#     price=5000
# elif yosh>=65: # yoshi kattalar uchun chegirma
#     price=8000
# print(f"sizga kirish {price} so'm!!!")   

# if-elif-else zanjirida shartlarning biri bajarilishi bilan, 
# Python qolgan shartlarni tekshirmaydi, shart bajarilishi uchun or va and operatoridan foydalanamiz

# or ingliz tilida 'yoki' deb tarjima qilinadi 

# kun=input("bugun nima kun? ") 
# if kun.lower()=="shanba" or kun.lower()=="yakshanba" :
#     print("bugun dam olish kuni.")
# else:
#     print("bugun ish kuni.")    
 
# kun=input("bugun nima kun? ")
# harorat=float(input("ob-havo necha gradus? ")) 
# if kun.lower()=='yakshanba ' and harorat>=30:
#     print("qani ketdik cho'milgani.")
# elif kun.lower()=='yakshanba' and harorat<=30:
#     print("uyda dam olamiz!!!")  
    
# kun=input("bugun kuniga nima ? ")
# harorat=float(input("bugun havo harorati nechchi ?  "))
# if (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat>=30:
#     print("bugun havo harorati issiq, qani kettik cho'milgani!!!")
# elif ( kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat<=30:
#     print("bugun havo salqin uyda qolamiz!!!")

# BOOLEAN MA'LUMOTLAR TURI   boolean(mantiqiy) qiymat deb ataladi 

# narh=15000 # bu ovqat   uchun olgan.
# salat=1
# choy=1
# if choy and salat:
#     narh=narh+10000 # bu yerda choy ham salat ham olgan bo'lsa ikkovini ham olamiz
# if choy or salat:
#     narh=narh+5000 
        
# print(f"Jami {narh} so'm bo'ldi. ")    
# True/False o'rniga 1 yoki 0 ni ishlatishimiz mumkin.
# if-elif-else zanjirining kamchiligidan biri, shartlardan biri bajarilishi bilan,
 # qolgan shartlar tekshirilmaydi
 
# narh=15000 # oqat uchun 
# choy=True
# non=True
# salat=0
# kompot=0
# achchu=True
# if choy: # choy olsa
#     narh=narh+3000
#     print("Mijoz choy oldi ")
# if non: #olgan bo'lsa  
#     narh=narh+2000
#     print("Mijoz non oldi ")
# if salat: # agar salat olgan bo'lsa
#     narh=narh+5000
#     print("Mijoz salat oldi")
# if kompot: # agar kompot olgan bo'lsa 
#     narh=narh+2000
#     print("Mijoz kompot oldi ")
# if achchu: # achchu yegan bo'lsa    
#     narh=narh+1000
#     print("Mijoz achchu oldi")
# print(f"Jami {narh} so'm bo'ldi.")    
#  Ajoyib boolean mantiqiy ma'lumotlar turi 
# bu yerda har bir if alohida tekshiradi

#     in  operatorini teshshirish 

# menu=["osh", "shashlik", "shurva","katlet", "lagman", "somsa", "bifshteks"]
# ovqat=input("qanday ovqat yeysiz ? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Kechirasiz, menuda bunday ovqat yo'q")    
# menu=["trimol", "kyupen", "lorotal", "mezim", "baliq_yog'i", "nospa"] 
# remedy=input("qanday dori sizga kerak ? ") 
# if remedy.lower() not in menu:
#     print("Kechirasiz bizda bunday dori yo'q")
    
# else:
#     print("Buyurtmangiz qabul qilindi ")   

# menu=["osh", "shashlik", "shurva","katlet", "lagman", "somsa", "bifshteks"]
# buyurtma=["free", "tort", "shurva", "katlet"] 
# for taom in buyurtma:
#     if taom in menu:
#         print(f"menuda {taom} bor")
#     else:
#      print(f"Kechrasiz, {taom} yo'q") 
       
# menu=["osh", "norin", "shashlik", "qazi", "shurva", "qatlama"]
# buyurtmalar=[]
# if buyurtmalar: 
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"menuda {taom} bor")
#         else: 
#             print(f"Kechirasiz, menuda {taom} yo'q ")
# else: 
#     print("savatingiz bo'sh ")
 # tushunilmagan yaxshi  ko'rib chiqish !!!!!           
# Amaliyot 
# son=int(input("juft son kiriting: ")) 
# juft_sonlar=list(range(2,100,2))
# if son%2:
#     print(f"bu son {son} juft  emas")
# else:
#     print(f"bu son juft {son} ")   
#     print("Rahmat!")
    
# yosh=int(input("yoshingizni kiriting: "))
# if yosh<=4 or yosh>=60:
#      narh=0
# elif yosh<=18:
#      narh=10000
# elif yosh>=18:
#     narh=20000
# print(f"sizga kirish {narh} so'm")    

# son_1=float(input("birinchi sonni kiriting: "))
# son_2=float(input("Ikkinchi sonni kiriting: "))
# if son_1>son_2:
#     print(f"{son_1}>{son_2}")
# elif son_1<son_2:
#     print(f"{son_1}<{son_2}") 

# mahsulotlar=["choy", "makaron", "qoshiq", "qand", "un", "yog'", "sabzi","piyoz", "kartoshka", "limonad"]
# savat=[]    
# for n in range(5):
#     savat.append(input(f"savatga {n+1} mahsulot qo'shing :"))


# for mahsulot in savat :
#     if mahsulot in mahsulotlar:
#         print(f"do'konimizda {mahsulot} bor")
#     if mahsulot not in mahsulotlar:
#         print(f"do'konimizda {mahsulot} yo'q")


# mahsulotlar=["mayanez", "piyoz", "pomidor", "katlet", "gugurt", "sabzi", "rumolcha", "daftar", "ruchka"] 
# savat=[]
# for n  in range(5):
#     savat.append(input(f"savatga {n+1} mahsulot kiriting. ")) 


# for mahsulot  in savat:
#      if mahsulot not in mahsulotlar:
#          print(f"Do'konda {mahsulot} yo'q")
# foydanuvchilar=["tolib", "vali", "bobir", "ali", "botir"]
# login =input("yangi login kiriting: ") 
# if login.lower() in foydanuvchilar:
#     print("bu login bant boshqa login kiriting!!!") 
# else:
#     print("Xush kelibsiz!!!")       

# son=int(input("istalgan butun son kiriting: "))
# for n in range(2,11):
#     if not (son%n) :
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")