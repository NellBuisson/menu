class ListeIngredients :
    def __init__ (self) :
        self.liste = {}

    def AjouterIngredient(self, ing, n) :
        nouv = self.liste.get(ing, -1)
        if nouv != -1 :
            self.liste[ing] = n
        else : 
            print("Cet ingrédient est déjà présent")
    
    def Ingredients(self) :
        return 

    def NbrEnVente(self, ing) :
        if self.liste.get(ing, -1) != -1 :
            return self.liste[ing] 

    def AfficherListe(self) :
        for cle, valeur in self.liste.items() :
            print(f" Ingrédient : {cle} \n Quantité par paquet : {valeur}")
    
    def RetirerIngredient(self, ing) :
        if self.liste.get(ing, -1) != -1 :
            del self.liste[ing]

    def Liste(self) :
        return self.liste


