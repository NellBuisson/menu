from c_menujour import MenuJour

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


