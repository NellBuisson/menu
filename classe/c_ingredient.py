class Ingredient :
    def __init__ (self, nom, nbr) :
        self.nom = nom
        self.nbrVente = nbr
        
    def NbrEnVente(self, n) :
        self.nbrVente = n

    def Afficher(self) :
        print(f" Nom : {self.nom} \n Quantité en Vente : {self.nbrVente}")
    
    def Nom(self) :
        return self.nom
    
    def QuelleVente(self) :
        return self.nbrVente

