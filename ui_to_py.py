# -*- coding: utf-8 -*-

def ui_to_py():
    
    from PyQt5 import uic
    
    uiname = "C:/Users/Kelebek/Desktop/DHT22/Arduino_anapen.ui"
    pyname = "C:/Users/Kelebek/Desktop/DHT22/Arduino_anapen.py"
    
    with open(pyname, 'w', encoding="utf-8") as fout:
       uic.compileUi(uiname, fout)

ui_to_py()    