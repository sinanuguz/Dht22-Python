# -*- coding: utf-8 -*-

#############################################################################

isim = 'Ali'

def fonk():
    
    # global isim
    isim += ' ÇELİK'
    return isim

print(fonk())


# Python herhangi bir nesneye göndermede bulunduğumuzda, yani o nesnenin 
# değerini talep ettiğimizde aradığımız nesneyi ilk önce mevcut isim alanı 
# içinde arar. Eğer aranan nesneyi mevcut isim alanı içinde bulamazsa 
# yukarıya doğru bütün isim alanlarını tek tek kontrol eder.


x = 0

def fonk():
    # x = 10
    print("Fonksiyon içindeki(local) x değeri :", x)
    
fonk()
print("Fonksiyon dışındaki(global) x değeri :", x)


