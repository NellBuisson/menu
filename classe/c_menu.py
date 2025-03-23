from c_menujour import MenuJour

class Menu : 
    def __init__(self, nbr):
        self.menusJour = []
        self.nbrPlats = 0
        self.nbrTotalRepas = nbr
        
    def AjouterPlat(self, j, p) :
        nouvMenu = MenuJour(j, p)

        #On gère la semaine du nouveau plat ajouté
        if self.nbrPlats != 0 :
            for plat in self.menusJour :
                if plat.Date() == nouvMenu.Date() :
                    nouvMenu.ModifierSemaine(nouvMenu.Semaine() + 1)

        self.menusJour.append(nouvMenu)
        self.nbrTotalRepas += 1
    def AjouterPlatPers(self, j, p, nbr) :
        nouvMenu = MenuJour(j, p)

        #On gère la semaine du nouveau plat ajouté
        if self.nbrPlats != 0 :
            for plat in self.menusJour :
                if plat.Date() == nouvMenu.Date() :
                    nouvMenu.ModifierSemaine(nouvMenu.Semaine() + 1)

        #On gère le changement de nombre de personnes
        nouvMenu.ModifierNbrPersonne(nbr)


        self.menusJour.append(nouvMenu)
        self.nbrTotalRepas += 1

    def RetirerPlat(self, plat) : 
        for menu in self.menusJour : 
            if menu.Plat() == plat.lower() : 
                self.menusJour.remove(menu)

    def ListePlats(self) :
        return self.menusJour


