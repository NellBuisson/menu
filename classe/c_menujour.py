class MenuJour :
    def __init__ (self, j, p) :
        self.jour = j
        self.semaine = 1
        self.plat = p
        self.nbr_pers = 2

    def modifier_jour(self, jour) :
        self.jour = jour
    
    def modifier_plat(self, plat) :
        self.plat = plat

    def modifier_nbr_personnes(self, nbr) :
        self.nbr_pers = nbr

    def modifier_semaine(self, s) :
        self.semaine = s
    
    def afficher(self) :
        print(f"{self.jour} de la semaine {self.semaine} : {self.plat} pour {self.nbr_pers} personne.s.")

    def donner_menu(self) :
        return (self.jour, self.semaine, self.plat, self.nbr_pers)
    
    def donner_date(self) :
        return (self.jour, self.semaine)
    
    def donner_jour(self) :
        return self.jour
    
    def donner_semaine(self) :
        return self.semaine
    
    def donner_repas(self) :
        return (self.plat, self.nbr_pers)
    
    def donner_plat(self) :
        return self.plat
