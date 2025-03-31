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
    
