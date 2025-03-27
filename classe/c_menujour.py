class MenuJour :
    def __init__ (self, j, p) :
        self.jour = j
        self.semaine = 1
        self.plat = p
        self.nbrPersonne = 2

    def ModifiierJour(self, jour) :
        self.jour = jour
    
    def ModifierPlat(self, plat) :
        self.plat = plat

    def ModifierNbrPersonne(self, nbr) :
        self.nbrPersonne = nbr

    def ModifierSemaine(self, s) :
        self.semaine = s
    
    def Afficher(self) :
        print(f"{self.jour} de la semaine {self.semaine} : {self.plat} pour {self.nbrPersonne} personne.s.")

    def Contenu(self) :
        return (self.jour, self.semaine, self.plat, self.nbrPersonne)
    
    def Date(self) :
        return (self.jour, self.semaine)
    
    def Jour(self) :
        return self.jour
    
    def Semaine(self) :
        return self.semaine
    
    def Repas(self) :
        return (self.plat, self.nbrPersonne)
    
    def Plat(self) :
        return self.plat

