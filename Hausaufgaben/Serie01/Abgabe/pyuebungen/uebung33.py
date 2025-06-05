# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 14:26:38 2025

@author: engin.bilir
"""

import os

#tdatei = "temp_datei.txt"
#with open(tdatei, "w", encoding="utf-8") as temp:

    # Übung1
"""
if not os.path.exists("temp_datei.txt"):
    print("Datei existiert nicht!")
else:
    print("Datei existiert bereits!")
"""
filename = "test.tst"
objekt = open(filename, "w")
objekt.write("Das ist nur ein Test")
objekt.close()

if os.path.exists(filename):
    os.remove(filename)
    print("Datei wurde gelöscht")
else:
    print("Datei wurde nicht gelöscht!")

    # Übung2
"""
if os.path.exists ("temp_ordner") and not os.listdir ("temp_ordner"): # Prüfen ob existiert und ob leer ist
    os.rmdir ("temp_ordner")
    print("Leerer Ordner gelöscht.")
else:
    print("Ordner kann nicht gelöscht werden.")
"""

foldername = "Test Ordner"
if not os.path.exists(foldername):
    os.mkdir(foldername)
    print("Ordner wurde erstellt")
else:
    print("Der Ordner exsistiert bereits!")

if os.path.exists(foldername) and not os.listdir(foldername):
    os.rmdir(foldername)
    print("Ordner wurde gelöscht")
else:
    print("Fehler !")
    
    # Übung3
if os.path.exists ("temp_ordner") and not os.listdir ("temp_ordner"): # Prüfen ob existiert und ob leer ist
    shutil.rmtree("temp_ordner")
    print("Leerer Ordner wurde gelöscht.")
else:
    print("Ordner kann nicht gelöscht!")

    
    