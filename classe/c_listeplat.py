class Plat : 
    def __init__(self, nom, diff, ingredient):
        self.nom = nom.lower()
        self.ingredients = ingredient
        self.nbrPers = 2
        self.difficulte = diff
    
    def AjouterIngredient(self, ingredient, quant) :
        self.ingredients[ingredient] = quant
    
    def ModQuantiteIng(self, ing, quant) :
        if ing in self.ingredients.keys() :
            self.ingredients[ing] = quant
        else : 
            print("Cet ingrédient n'est pas dans la liste des ingrédients")

    def RetirerIngredient(self, ingredient) :
        if ingredient in self.ingredients.keys() :
            del self.ingredients[ingredient]

    def Nom(self) :
        return self.nom

    def CmbPers(self) :
        return self.nbrPers
    
    def Ingredients(self) :
        return self.ingredients.items()
    
    def Difficulte(self) :
        return self.difficulte
    
    def Afficher(self) :
        print(f" Nom : {self.nom} \n Pour : {self.nbrPers} personnes \n Difficulté : {self.difficulte} Ingrédients :")
        for cle, valeur in self.ingredients.items() :
            print(cle, valeur)
    


class ListePlats :
    def __init__(self):
        self.plats = []
        self.nbrPlats = 0

    def PlatPresent(self, nom_plat) :
        if self.nbrPlats != 0 :
            for plat in self.plats :
                if plat.Nom() == nom_plat :
                    return True
        return False 
    
    def AjouterPlat(self, nom, ingredients) :
        if not self.PlatPresent(nom) :
            nouvPlat = Plat(nom, ingredients)
            self.plats.append(nouvPlat)
            self.nbrPlats += 1

    def AjouterPlatExistant(self, plat) :
        if plat not in self.plats :
            self.plats.append(plat)
            self.nbrPlats += 1

    def RetirerPlat(self, nom_plat) :
        if self.PlatPresent(nom_plat) :
            for num_plat in range(self.nbrPlats - 1) :
                if self.plats[num_plat].Nom() == nom_plat :
                    del self.plats[num_plat]

    def AjouterIngredientPlat(self, nom_plat, ingredient, quantite) :
        if self.PlatPresent(nom_plat) :
            for num_plat in range(self.nbrPlats - 1) :
                if self.plats[num_plat].Nom() == nom_plat :
                    self.plats[num_plat].AjouterIngredient(ingredient, quantite)

    def RetirerIngredientPlat(self, nom_plat, ingredient) :
         if self.PlatPresent(nom_plat) :
            for num_plat in range(self.nbrPlats - 1) :
                if self.plats[num_plat].Nom() == nom_plat :
                    self.plats[num_plat].RetirerIngredient(ingredient)

    def AfficherPlats(self) :
        if self.nbrPlats != 0 :
            print("La liste contients les plats :", end='')
            for plat in self.plats :
                print(f"{plat.Nom()}, ", end='')

    def AfficherPlatCompletSpecifique(self, nom_plat) :
        if self.PlatPresent(nom_plat):
            for plat in self.plats : 
                if plat.Nom() == nom_plat :
                    print(f"{nom_plat} est composé de")
                    for nom_ingredient, quantite_ingredient in plat.Ingredients() :
                        print(quantite_ingredient, nom_ingredient, end='')

    def Afficher(self) :
        if self.nbrPlats != 0 :
            print("Voici la liste complète des plats enregistrées (nom et ingrédients) :")
            for plat in self.plats :
                print(f"{plat.Nom().capitalize()} a besoin de :")
                for nom_ingredient, quantite_ingredient in plat.Ingredients() :
                    print(quantite_ingredient, nom_ingredient)


    def IngredientsPlat(self, nom_plat) :
        if self.PlatPresent(nom_plat) :
            for num_plat in range(self.nbrPlats) :
                if self.plats[num_plat].Nom() == nom_plat :
                    return self.plats[num_plat].Ingredients()
                     


    

