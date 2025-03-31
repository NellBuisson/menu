class Plat : 
    def __init__(self, nom, diff, ingredient):
        self.nom = nom
        self.ingredients = ingredient
        self.nbr_pers = 2
        self.difficulte = diff
    
    def ajouter_ingredient(self, ingredient, quant) :
        self.ingredients[ingredient] = quant
    
    def modifier_quantite_ingredient(self, ing, quant) :
        if ing in self.ingredients.keys() :
            self.ingredients[ing] = quant
        else : 
            print("Cet ingrédient n'est pas dans la liste des ingrédients")

    def retirer_ingredient(self, ingredient) :
        if ingredient in self.ingredients.keys() :
            del self.ingredients[ingredient]

    def donner_nom(self) :
        return self.nom

    def combien_de_pers(self) :
        return self.nbr_pers
    
    def donner_ingredients(self) :
        return self.ingredients.items()
    
    def donner_difficulte(self) :
        return self.difficulte
    
    def afficher(self) :
        print(f" Nom : {self.nom} \n Pour : {self.nbr_pers} personnes \n Difficulté : {self.difficulte} Ingrédients :")
        for cle, valeur in self.ingredients.items() :
            print(cle, valeur)
    


class ListePlats :
    def __init__(self):
        self.plats = []
        self.nbr_plats = 0

    def plat_present(self, nom_plat) :
        if self.nbr_plats != 0 :
            for plat in self.plats :
                if plat.donner_nom() == nom_plat :
                    return True
        return False 
    
    def ajouter_plat(self, nom, ingredients) :
        if not self.plat_present(nom) :
            nouvPlat = Plat(nom, ingredients)
            self.plats.append(nouvPlat)
            self.nbr_plats += 1

    def ajouter_plat_existant(self, plat) :
        if plat not in self.plats :
            self.plats.append(plat)
            self.nbr_plats += 1

    def retirer_plat(self, nom_plat) :
        if self.plat_present(nom_plat) :
            for num_plat in range(self.nbr_plats - 1) :
                if self.plats[num_plat].donner_nom() == nom_plat :
                    del self.plats[num_plat]

    def ajouter_ingredient_plat(self, nom_plat, ingredient, quantite) :
        if self.plat_present(nom_plat) :
            for num_plat in range(self.nbr_plats - 1) :
                if self.plats[num_plat].donner_nom() == nom_plat :
                    self.plats[num_plat].ajouter_ingredient(ingredient, quantite)

    def retirer_ingredient_plat(self, nom_plat, ingredient) :
         if self.plat_present(nom_plat) :
            for num_plat in range(self.nbr_plats - 1) :
                if self.plats[num_plat].donner_nom() == nom_plat :
                    self.plats[num_plat].retirer_ingredient(ingredient)

    def afficher_plats(self) :
        if self.nbr_plats != 0 :
            print("La liste contients les plats :", end='')
            for plat in self.plats :
                print(f"{plat.donner_nom()}, ", end='')

    def afficher_plat_complet(self, nom_plat) :
        if self.plat_present(nom_plat):
            for plat in self.plats : 
                if plat.donner_nom() == nom_plat :
                    print(f"{nom_plat} est composé de")
                    for nom_ingredient, quantite_ingredient in plat.donner_ingredients() :
                        print(quantite_ingredient, nom_ingredient, end='')

    def afficher(self) :
        if self.nbr_plats != 0 :
            print("Voici la liste complète des plats enregistrées (nom et ingrédients) :")
            for plat in self.plats :
                print(f"{plat.donner_nom().capitalize()} a besoin de :")
                for nom_ingredient, quantite_ingredient in plat.donner_ingredients() :
                    print(quantite_ingredient, nom_ingredient)


    def donner_ingredients_plat(self, nom_plat) :
        if self.plat_present(nom_plat) :
            for num_plat in range(self.nbr_plats) :
                if self.plats[num_plat].donner_nom() == nom_plat :
                    return self.plats[num_plat].donner_ingredients()
                     


    

