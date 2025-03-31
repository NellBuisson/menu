class ListeCourse : 
    def __init__(self, nom):
        self.nom = nom
        self.liste = {}

    def posseder(self, element) :
        return element in self.liste.keys()

    def ajouter_element(self, element, quantite) :
        if self.posseder(element) :
            self.liste[element] += quantite
        else : 
            self.liste[element] = quantite
    
    def modifier_quantite(self, element, quantite) :
        if self.posseder(element) :
            self.liste[element] = quantite

    def retirer_element(self, element) :
        if self.posseder(element) :
            del self.liste[element]

    def donner_nom(self) :
        return self.nom
    
    def afficher(self) :
        print(f"La liste {self.nom} contient :")

        for element, quantite in self.liste.items() :
            print(quantite, element)

    def donne_liste(self) :
        return self.liste.items()
        
