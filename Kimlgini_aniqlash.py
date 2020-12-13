# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:01:54 2020

@author: Hakerjon
"""

guruhlar = {404}
kursdoshlar404 = ['Mansur Abdugaffarov', 
                  'Rashid', 
                  'Nurmuhammad', 
                  'Eldor', 
                  'Otabek', 
                  'Shohrux', 
                  'Doston', 
                  'Yusuf', 
                  "Mansur Turg'unboyev",
                  'Nurali', 
                  'Mirolim',
                  'Sherzod',
                  'Begzod', 
                  'Pardaboy', 
                  'Shaxob', 
                  'Farxod', 
                  "G'olib", 
                  'Feruza', 
                  'Fotima', 
                  'Nafisa']
kursdoshlar405 = []
tarif = ["Iyaa kim bu axir, o`zimni maqtasam uyat bo'ladiye",
         "Shu bola qachondir go'shtga to`yganini eslolmayman, to'g'risida))",
         'Rashid bilan birga yurib uni 4 yil to`ydirolmagan jabrlanuvchi, ha-ya mendan 30ming qarz edi',
         'Mindee qaraseng, operativkasi yo`q bolaga o`xshaydi, lekin fikrlarida mazasi bor tuppa tuzuk bola',
         'Eng katta xatosini 4 kurs oxirida tushunib yetib o`zgargan bola, nu baribir 100 foiz o`zgarmaganmkuya',
         'Bo`yi operativkasidan katta bola shu bo`ladi',
         'Shu bola ichadiganlarga qo`shildiyu aynidi',
         'Koreyaga ketolmagan koreys bola',
         'Mansur ismlilar o`zi azaldan yaxshi bo`lganu,lekin bu Mansur hali o`rganishi kerak bo`lganlari ko`p',
         '4 ballik zil-zillani 8 ballga aylantirib beradigan bola',
         'Fotining rasmiy shirasi edi',
         'Faqat uyida yaxshi mehmon qilganini eslay olaman',
         'Ijod domla aytganidek: Odamzotning boshlanishi...',
         'Umuman so`kinmaydigan bolaku bu',
         'Yaxshi bo`lishga doim harakat qiladi-yu...',
         'Unga hech narsani farqi yo`q, meni fikrimni ham',
         'Shu bolaga diplom kerakmas edi, biznesda gullaydi',
         'Haaa, chuqur nafas olgan holda bu qizni ta`riflashdan o`tib ketamiz',
         'Bir so`z bilan aytganda pismiq edi, lekin yaxshi qiz, atrofida asalarilar ko`p bo`lgandi',
         'Mujik, gapida turadi, o`zi shunday bo`lish kerakda odam']
print("Siz bu dasturcha orqali kursdoshlaringiz haqida pozitiv yoki negativ ta'rifni bilib olishingiz mumkin")
kursdosh = input("Qaysi kursdoshingizni bilmoqchi bo'lsangiz, uni ismini kiriting: ")
if kursdosh in kursdoshlar404:
    i = kursdoshlar404.index(kursdosh)
    print(tarif[i])
if kursdosh not in kursdoshlar404:
    xato = input("Kechirasanku lekin bunday ismni topolmadim, balki xato yozgandirsan, agar ro`yxatni ko`rmoqchi bo'lsang yordam deb yoz\n>>>")
    print(xato)
    if xato == ('yordam'):
        print(kursdoshlar404)
        print("  >>>>>>Ko'rib turganingdek bu ism mavjud emas<<<<<")
# Agar 405-guruh uchun o'zing ismlar va tariflar qo'shaman desang kodlarga tegmasdan append yordamida amalga oshir, o'zingni namoyon qil
   