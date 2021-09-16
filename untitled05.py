# 5-dars string(matn)lar bilan ishlash!!!
# ism="Ahad"
# familiya="Qayum"
# print("mening ismim " + ism )
# print("Familiyam esa "+familiya)
# print(ism + ' '+ familiya)
# ikki va undan ortiq matnlar bilan ishlash uchun esa f stringdan foydalaniladi
ism="Alisher"
familiya="Akbarov"
ism_familiya=f"{ism} {familiya}"
print(ism_familiya.upper())
# ism="James"
# familiya="Bond"
# print(f"mening ismim {ism}, familyam esa {familiya}, {ism} {familiya}")
# print("hello \tworld")
# print("hello \nworld")
# print(ism_familiya.title()) 

# input metodi
# ism=input("Ismingiz nima oka :")
# print("salom "+ ism)

#homework
kocha=input("Ko'changizning nomi :")
k=kocha.upper()
mahalla=input("Mahallangiz nomi:")
m=mahalla.capitalize()
tuman=input("qaysi tuman:")
t=tuman.capitalize()
viloyat=input("Qaysi viloyat")
v=viloyat.capitalize()

print(f"{kocha}. ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyatida \
yashayman      ") # bunisi osonroq ekan 
print(" men " + kocha+ " ko'chasi " + mahalla + " mahallasida turaman"  )
