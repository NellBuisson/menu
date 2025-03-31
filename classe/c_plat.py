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
    