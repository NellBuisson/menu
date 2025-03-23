from c_plat import *
class ListePlats :
    def __init__(self):
        self.plats = []
        self.nbrPlats = 0

    def AjouterPlat(self, nom, ingredients) :
        nouvPlat = Plat(nom, ingredients)
        if nouvPlat not in self.plats :
            self.plats.append(nouvPlat)
            self.nbrPlats += 1

    def AjouterPlatExistant(self, plat) :
        if plat not in self.plats :
            self.plats.append(plat)
            self.nbrPlats += 1

    def RetirerPlat(self, nom_plat) :
        for num_plat in range(self.nbrPlats - 1) :
            if self.plats[num_plat].Nom() == nom_plat :
                del self.plats[num_plat]

    def AjouterIngredientPlat(self, plat, ingredient, quantite) :
        for num_plat in range(self.nbrPlats - 1) :
            if self.plats[num_plat].Nom() == plat :
                self.plats[num_plat].AjouterIngredient(ingredient, quantite)

    def AfficherPlats(self) :
        for plat in self.plats :
            print(plat.Nom())

    def AfficherPlatSpecifique(self, nom_plat) :
        for plat in self.plats : 
            if plat.Nom() == nom_plat :
                print(f"{nom_plat} est composé de")
                for nom_ingredient, quantite_ingredient in plat.Ingredients() :
                    print(quantite_ingredient, nom_ingredient)
"""
    def Afficher(self) :
        for cle, valeur in self.plats.items() :
            print(f"Le plat {cle} a besoin de :")
            for nom_ingredient, quantite_ingredient in valeur.items() :
                print(quantite_ingredient, nom_ingredient)

    def IngredientPlat(self, plat) :
        if plat in self.plats.keys() :
            return self.plats.get(plat).items()
"""
     
    
liste = ListePlats()
liste.AjouterPlat("pate", {"pate" : 0.3})
liste.AjouterPlat("pate carbo", {"pate" : 0.3, "sauce" : 1})
liste.AjouterIngredientPlat("pate carbo", "lardon", 2)
liste.AfficherPlats()


