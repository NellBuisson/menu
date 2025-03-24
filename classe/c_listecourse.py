from c_menu import *

class ListeCourse : 
    def __init__(self, nom):
        self.nom = nom
        self.liste = {}

    def Possede(self, element) :
        return element in self.liste.keys()

    def AjouterElement(self, element, quantite) :
        if self.Possede(element) :
            self.liste[element] += quantite
        else : 
            self.liste[element] = quantite
    
    def ModQuantite(self, element, quantite) :
        if self.Possede(element) :
            self.liste[element] = quantite

    def RetirerElement(self, element) :
        if self.Possede(element) :
            del self.liste[element]

    def Nom(self) :
        return self.nom
    
    def Afficher(self) :
        print(f"La liste {self.nom} contient :")
        for element, quantite in self.liste.keys() :
            print(quantite, element)

    def DonneListe(self) :
        return self.liste.items()
        