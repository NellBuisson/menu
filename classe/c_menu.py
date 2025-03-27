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
        self.listeRepas = []
        self.nbrRepas = 0
        self.nbrTotalRepas = nbr
        
    def AjouterRepas(self, j, p) :

        if self.nbrRepas != self.nbrTotalRepas :
            nouvMenu = MenuJour(j, p)

            #On gère la semaine du nouveau repas ajouté
            if self.nbrRepas != 0 :
                for repas in self.listeRepas :
                    if repas.Date() == nouvMenu.Date() :
                        nouvMenu.ModifierSemaine(nouvMenu.Semaine() + 1)

            #on ajoute le nouveau menu au Menu
            self.listeRepas.append(nouvMenu)
            self.nbrRepas += 1

    def AjouterRepasPers(self, j, p, nbr) :
        if self.nbrRepas != self.nbrTotalRepas :
            nouvMenu = MenuJour(j, p)

            #On gère la semaine du nouveau repas ajouté
            if self.nbrRepas != 0 :
                for repas in self.listeRepas :
                    if repas.Date() == nouvMenu.Date() :
                        nouvMenu.ModifierSemaine(nouvMenu.Semaine() + 1)

            #On gère le changement de nombre de personnes
            nouvMenu.ModifierNbrPersonne(nbr)

            #on ajoute le nouveau menu au Menu
            self.listeRepas.append(nouvMenu)
            self.nbrRepas += 1

    def RetirerRepas(self, repas) : 
        for menu in self.listeRepas : 
            if menu.Plat() == repas : 
                self.listeRepas.remove(menu)   
                self.nbrRepas -= 1        

    def ListeRepas(self) :
        return self.listeRepas

    def RepasManquant(self) :
        return self.nbrTotalRepas - self.nbrRepas
    
    def NbrRepas (self) :
        return self.nbrRepas
    
    def ModifierNbrRepas(self, nbr) :
        if self.nbrRepas <= nbr :
            self.nbrTotalRepas = nbr 
    
    def Afficher(self) :
        print(f"Menu pour {self.nbrTotalRepas} repas, possède actuellement {self.nbrRepas} :")

        for repas in self.listeRepas :
            repas.Afficher()


