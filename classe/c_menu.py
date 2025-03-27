class MenuJour :
    def __init__ (self, j, p) :
        self.jour = j.lower()
        self.semaine = 1
        self.plat = p.lower()
        self.nbrPersonne = 2

    def ModifiierJour(self, jour) :
        self.jour = jour.lower()
    
    def ModifierPlat(self, plat) :
        self.plat = plat.lower()

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


class Menu : 
    def __init__(self, nbr):
        self.listePlats = []
        self.nbrPlats = 0
        self.nbrTotalRepas = nbr
        
    def AjouterPlat(self, j, p) :

        if self.nbrPlats != self.nbrTotalRepas :
            nouvMenu = MenuJour(j, p)

            #On gère la semaine du nouveau plat ajouté
            if self.nbrPlats != 0 :
                for plat in self.listePlats :
                    if plat.Date() == nouvMenu.Date() :
                        nouvMenu.ModifierSemaine(nouvMenu.Semaine() + 1)

            #on ajoute le nouveau menu au Menu
            self.listePlats.append(nouvMenu)
            self.nbrPlats += 1

    def AjouterPlatPers(self, j, p, nbr) :
        if self.nbrPlats != self.nbrTotalRepas :
            nouvMenu = MenuJour(j, p)

            #On gère la semaine du nouveau plat ajouté
            if self.nbrPlats != 0 :
                for plat in self.listePlats :
                    if plat.Date() == nouvMenu.Date() :
                        nouvMenu.ModifierSemaine(nouvMenu.Semaine() + 1)

            #On gère le changement de nombre de personnes
            nouvMenu.ModifierNbrPersonne(nbr)

            #on ajoute le nouveau menu au Menu
            self.listePlats.append(nouvMenu)
            self.nbrPlats += 1

    def RetirerPlat(self, plat) : 
        for menu in self.listePlats : 
            if menu.Plat() == plat.lower() : 
                self.listePlats.remove(menu)   
                self.nbrPlats -= 1        

    def Plats(self) :
        return self.listePlats

    def PlatManquant(self) :
        return self.nbrTotalRepas - self.nbrPlats
    
    def NbrPlats (self) :
        return self.nbrPlats
    
    def ModifierNbrRepas(self, nbr) :
        if self.NbrPlats() <= nbr :
            self.nbrTotalRepas = nbr 
    
    def Afficher(self) :
        print(f"Menu pour {self.nbrTotalRepas} repas, possède actuellement {self.nbrPlats} :")

        for plat in self.listePlats :
            plat.Afficher()


