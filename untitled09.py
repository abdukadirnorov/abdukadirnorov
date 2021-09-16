# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 00:06:14 2021

@author: USER
"""

# for sikli (for takrorlash operatori)  Dasturlashda bu tsikl (loop) deb ataladi. 
# mehmonlar=['ali', 'vali', 'hasan', 'husan', 'olim']
# for mehmon in mehmonlar: #  Tsikl boshlanishi ikki nuqta (:)
#     # print(mehmon) # "For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.
#     print(f"Hurmatli {mehmon} sizni sizni 10- sentyabr kuni  nahorgi oshga taklif etamiz")
#     print("Hurmat bilan Bahodir akalar oilasi ") #Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi. 
    
    # for bilan sonli ro'yxat ishlash 
# sonlar=list(range(12))
# sonning_kvdrt=[]
# for son in sonlar:
#    sonning_kvdrt.append(son**2)    
   
# print(sonlar) 
# print(sonning_kvdrt)

# # for va input funkstiyasi orqali ro'yxatni to'ldirish 
# dostlar=[]
# print("beshta eng yaqin do'stingizni kiriting:")
# for n in range(5):
#     dostlar.append(input(f"{n+1c}-do'stingizni kiriting: "))  
# print(dostlar) 

# names=["Hasan", "Sobir", "Javohir", "Jasur","Dadaxon"]
# for name in names:
#     # print(f"salom {name} bugun ko'rishamizmi?")#
#0     print("salom", name , "bugun ko'rishamizmi?")
# toq_sonlar=list(range(1,100,2))
# for son in toq_sonlar:
#     print(son**3)
# toq_sonlar=list(range(1,100,2))
# sonning_kubi=[]
# for son in toq_sonlar:
#     sonning_kubi.append(son**3)
# print(toq_sonlar)
# print(sonning_kubi)    
# print("5 ta eng sevimli kinoyingizni kiritng.")    
# kinolar=[]    
# for n in range(5):
#     print(kinolar.append(input(f"{n+1 }- eng yaxshi ko'rgan kinoyingiz: ")))
# print(kinolar)
     
n_odam=int(input("bugun nechta inson bilan suhbat qildingiz :"))
ismlar=[]
for n in range(n_odam):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi? "))
print(ismlar)    