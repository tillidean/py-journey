# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 13:42:54 2025

@author: engin.bilir
"""
# Übung 1
"""
schreibe = ("Das ist Zeile 1\n", "Das ist Zeile 2\n", "Das ist Zeile 3\n")
with open("meine_notizen.txt", "w", encoding="utf-8") as textWrite:
    textWrite.writelines(schreibe)
"""
filename = "meine_notizen.txt"
filename2 = "einkaufsliste.txt"
"""
with open(filename, "w", encoding="UTF-8") as file:
    for i in range(0, 3):
        item = input(f"gib dein Notiz {i} ein: ")
        file.write(item + "\n")
        
with open(filename, "r", encoding="UTF-8") as file:
    print(file.read())    

# Übung 2
zeilenschreiben = ("Tomaten", "Gurken", "Salat", "Eier")
with open(filename2, "a") as textWrite:
    textWrite.writelines(zeilenschreiben)
    
with open(filename2, "r") as textWrite:
    lesetext = textWrite.readlines()
    print(lesetext)
"""    
filename = "einkaufsliste.txt"
zeilenschreiben = ("Tomaten", "Gurken", "Salat", "Eier")

with open(filename, "a") as file:
    for item in zeilenschreiben:
        file.write(item + "\n")
        
    
# Übung 3
zeilenschreiben_New = ("Das ist die 3. Übungsaufgabe!")
filename3 = "log.txt"
try:
    with open("filename3", "x", encoding="UTF-8") as textWrite_New:
        textWrite_New.write(zeilenschreiben_New)
        
except FileExistsError as e:
    print(f"Die Datei {filename3} exsistiert bereits. - {e} ")