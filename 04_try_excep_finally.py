# -*- coding: utf-8 -*-
############################################################################


# try:
#   ...bir takım işler...

# except birHata:
#   ...hata alınınca yapılacak işlemler...

# finally:
#   ...hata olsa da olmasa da yapılması gerekenler...

# finally.. blogunun en önemli özelligi, programın çalısması sırasında 
# herhangi bir hata gerçeklesse de gerçeklesmese de isletilecek olmasıdır. 
# Eger yazdıgınız programda mutlaka ama mutlaka isletilmesi gereken bir 
# kısım varsa, o kısmı finally... blogu içine yazabilirsiniz.


ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)

except ZeroDivisionError:
    
    print("Bir sayıyı 0'a bölemezsiniz!")

except ValueError:
    
    print("Lütfen sadece sayı girin!")
    
finally:
    
    print('Görüşmek üzere...')
    
# Bir program yazarken, en iyi yaklasım, yukarıda yaptıgımız gibi, 
# her hata türü için kullanıcıya ayrı bir uyarı mesajı göstermektir.

