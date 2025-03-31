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


class Menu : 
    def __init__(self, nbr):
        self.liste_repas = []
        self.nbr_repas = 0
        self.nbr_total_repas = nbr
        
    def ajouter_repas(self, j, p) :

        if self.nbr_repas != self.nbr_total_repas :
            nouv_menu = MenuJour(j, p)

            #On gère la semaine du nouveau repas ajouté
            if self.nbr_repas != 0 :
                for repas in self.liste_repas :
                    if repas.donner_date() == nouv_menu.donner_date() :
                        nouv_menu.modifier_semaine(nouv_menu.donner_semaine() + 1)

            #on ajoute le nouveau menu au Menu
            self.liste_repas.append(nouv_menu)
            self.nbr_repas += 1

    def ajouter_repas_avec_pers(self, j, p, nbr) :
        if self.nbr_repas != self.nbr_total_repas :
            nouv_menu = MenuJour(j, p)

            #On gère la semaine du nouveau repas ajouté
            if self.nbr_repas != 0 :
                for repas in self.liste_repas :
                    if repas.donner_date() == nouv_menu.donner_date() :
                        nouv_menu.modifier_semaine(nouv_menu.donner_semaine() + 1)

            #On gère le changement de nombre de personnes
            nouv_menu.modifier_nbr_personnes(nbr)

            #on ajoute le nouveau menu au Menu
            self.liste_repas.append(nouv_menu)
            self.nbr_repas += 1

    def retirer_repas(self, repas) : 
        for menu in self.liste_repas : 
            if menu.donner_plat() == repas : 
                self.liste_repas.remove(menu)   
                self.nbr_repas -= 1        

    def donner_liste_repas(self) :
        return self.liste_repas

    def donner_nbr_repas_manquant(self) :
        return self.nbr_total_repas - self.nbr_repas
    
    def nbr_repas_menu (self) :
        return self.nbr_repas
    
    def modifier_nbr_repas(self, nbr) :
        if self.nbr_repas <= nbr :
            self.nbr_total_repas = nbr 
    
    def afficher(self) :
        print(f"Menu pour {self.nbr_total_repas} repas, possède actuellement {self.nbr_repas} :")

        for repas in self.liste_repas :
            repas.afficher()


