class Plat : 
    def __init__(self, nom):
        self.nom = nom
        self.ingredients = {}
        self.nbrPers = 2
    
    def AjouterIngredient(self, ingredient, quant) :
        self.ingredients[ingredient] = quant
    
    def ModQuantiteIng(self, ing, quant) :
        mod = self.ingredients.get(ing, -1)
        if mod != -1 :
            self.ingredients[ing] = quant
        else : 
            print("Cet ingrédient n'est pas dans la liste des ingrédients")

    def RetirerIngredient(self, ingredient) :
        del self.ingredients[ingredient]

    def ModifPers(self, p) :
        self.nbrPers = p
    
    def Nom(self) :
        return self.nom

    def CmbPers(self) :
        return self.nbrPers
    
    def Ingredients(self) :
        return self.ingredients.items()
    
    def Afficher(self) :
        print(f" Nom : {self.nom} \n Pour : {self.nbrPers} personnes \n Ingrédients :")
        for cle, valeur in self.ingredients.items() :
            print(cle, valeur)
    
