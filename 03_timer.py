# -*- coding: utf-8 -*-

##########################################################################

# Timer (Zamanlayıcı) Nesneleri sadece belirli bir zaman geçtikten sonra 
# çalıştırılan bir eylemi, -bir zamanlayıcıyı- temsil eder. 
# Zamanlayıcılar, start() yöntemi çağrılarak başlatılır, 
#                 stop() yöntemi ile durdurulur. 

##########################################################################

import sys
from time import *

from PyQt5 import QtCore # timer için

app = QtCore.QCoreApplication(sys.argv)

timer1 = QtCore.QTimer()
timer2 = QtCore.QTimer()
timer3 = QtCore.QTimer()
timer4 = QtCore.QTimer()


def tick():
    zaman = ctime() # Mon Dec 10 00:25:14 2018
    print (zaman[11:19], 'tick')
    


def tok():
    zaman = ctime() # Mon Dec 10 00:25:14 2018
    print (zaman[11:19], "     tock")
    # print('\n')


def birkere():
    zaman = ctime() # Mon Dec 10 00:25:14 2018
    print(zaman[11:19], "Bu bir kere....")
    print('\n')
    
def son():
    timer1.stop()
    timer2.stop()
    timer3.stop()
    timer4.stop()
    app.exit()
    
zaman = ctime() # Mon Dec 10 00:25:14 2018
print(zaman[11:19], "Başlangıç Zamanı")


timer1.start(1000)    
timer1.timeout.connect(tick)

timer2.timeout.connect(tok)
timer2.start(3000)

timer3.singleShot(5000, birkere)

timer4.singleShot(10000, son)



sys.exit(app.exec_())