# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:24:13 2022

@author: perda
"""

liste_areal = []
liste_befolkning = []
liste_tetthet = []
liste_land = []

class Land:
    def __init__(self, navn, areal, befolkning, tekst):
        self.navn = navn
        self.areal = areal
        self.befolkning = befolkning
        self.tekst = tekst
    
    def __str__(self):
        resultat = "Oversikt over: " + self.tekst + "\n"
        for i in liste_land:
            resultat += "{}: {}".format(i, liste_land[i]) + "\n"
        return resultat
   
with open("C:/Users/perda/OneDrive/Documents/UiS/1. Semester/DAT120/Øving 8 filer/areal_tabell_csv.txt", encoding="UTF8") as fil1:
    x = [line.strip() for line in fil1]
    for i in x:
        x = i.split(";")
        liste_areal.append(x)
   
        
with open("C:/Users/perda/OneDrive/Documents/UiS/1. Semester/DAT120/Øving 8 filer/befolkning_tabell_csv.txt", encoding="UTF8") as fil2:
   x = [line.strip() for line in fil2]
   for i in x:
       x = i.split(";")
       liste_befolkning.append(x)
       
liste_tetthet = dict(liste_tetthet)
liste_areal = dict(liste_areal)
liste_befolkning = dict(liste_befolkning)
liste_land = {}

for key in (liste_areal.keys() | liste_befolkning.keys()):
    if key in liste_areal: liste_land.setdefault(key, []).append(liste_areal[key])
    if key in liste_befolkning: liste_land.setdefault(key, []).append(liste_befolkning[key])
    
if __name__ == "__main__":
    navn = liste_land[key]
    areal = liste_land.values()
    befolkning = liste_land.values()
    tekst = "Land, Areak, Befolkning"
    print(Land(navn, areal, befolkning, tekst))
    
        
   
    
   
