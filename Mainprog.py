# -*- coding: utf-8 -*-

##############################################################################

import serial                   # PySerial Kütüphanesi, seri portu kulllanabilmek için
import serial.tools.list_ports  # Bağlı portların tespiti için
from time import *              # Zamanla ilgili kütüphane
import sys                      # Sistem komutlarının çalıştırılabilmesi için

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem                # Tasarladığımız arayüzün kullanılabilmesi için

from Arduino_anapen import *



















## ARAYÜZ TANIMLANIP EKRANA GETİRİLİYOR 

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Ui_anapencere() # class ismi

ui.setupUi(MainWindow)
MainWindow.show()


















## CSS İLE FORMAT VE BİÇİM TANIMLAMALARI YAPILIYOR 

sicak = """
QProgressBar {
     border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);	
 }

 QProgressBar::chunk {
     background-color: rgb(255, 0, 0);  
 }
"""

soguk = """
QProgressBar {
     border: 2px solid;
	 border-color: gray;
     border-radius: 5px;
     background-color: rgb(255, 255, 255);	
 }

 QProgressBar::chunk {
     background-color: rgb(0, 0, 255);   
 }
"""

## FONKSİYONLAR TANIMLANIYOR 

## ZAMANLAYICILAR OLUŞTURULUYOR 

def zaman_yaz():
    
    global zaman
    zaman = ctime() # Mon Dec 10 00:25:14 2018
    ui.label_7.setText(zaman[10:19])


timer0 = QtCore.QTimer()
timer0.start(1000)
timer0.timeout.connect(zaman_yaz)


















## PORT AÇILIYOR

def port_ac():
    
    port = str(ui.port.currentText())
    
    baud = str(ui.baudrate.currentText())
    
    global ser
    
    try:
        
        ser = serial.Serial(port, baudrate=baud, timeout=0)
        
        if ser.is_open:
            ui.statusbar.showMessage(" "*1 + " Port açıldı...", 1500)
        
            global timer1    
            timer1 = QtCore.QTimer()
            timer1.start(1000)
            timer1.timeout.connect(sensoroku)

    except:
        
        ui.statusbar.showMessage(" "*1 + " Port açılamadı !!! Lütfen sensörün bağlı olduğu portu seçiniz !!!", 1500)
    









      
def port_kapat():
    
    try:
        
        global ser
        
        # port = str(ui.port.currentText())
        # baud = str(ui.baudrate.currentText())
        # ser = serial.Serial(port, baudrate=baud, timeout=0)
        
        timer1.stop()
        
        if ser.is_open:
           
            ser.close()
            
            print("Port kapatıldı...")
            
            ui.label_5.setText("")
            ui.label_6.setText("")
            
            ui.progressBar_1.setValue(10)
            ui.progressBar_2.setValue(10)
            
            # ui.statusbar.showMessage(" "*1 + " Port kapatıldı...", 1500)
    

    except:
        
        ui.statusbar.showMessage(" "*1 + "Açık port bulunamadı...", 1500)
        




    
def sensoroku():
    
    global ser
    
    print ("Bekleyen byte sayısı :", ser.in_waiting)
    
    data = ser.read(14)   # Seri Porttan 14 bytelık veri okunuyor
    
    print(data)
    print("\n")
    
    veri = str(data)
    
    if len(veri) > 3: # b'' değilse...
        print(zaman[11:19], " Isı: ", veri[10:15]," Nem: ", veri[2:7])
        
        derece = float(veri[10:15])
#        derece = -35.00
        nem = float(veri[2:7])
         
        ui.label_5.setText(veri[10:15])
#        ui.label_5.setText(str(derece))
        ui.label_6.setText(veri[2:7])
        
        global sicak, soguk
        
        if derece > 0:
            ui.progressBar_1.setStyleSheet(sicak)
        
        else:
            ui.progressBar_1.setStyleSheet(soguk)
    
        ui.progressBar_1.setValue(abs(derece))
        ui.progressBar_2.setValue(nem)




        
def cikis():
    
    port_kapat()
    
    sys.exit(app.exec_())
    





















ui.portac.clicked.connect(port_ac)
ui.portkapat.clicked.connect(port_kapat)
# ui.pb_cikis.clicked.connect(cikis)


# İŞLETİM SİSTEMİNE ÇIKIŞ
sys.exit(app.exec_())





















