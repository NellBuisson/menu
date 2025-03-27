from classe.c_listecourse import *
from classe.c_menu import *
from classe.c_listeplat import *


def RemplirCourseAvecMenu(menu, liste_de_course, liste_plat) :   
    for repas in menu.ListeRepas() :
        plat, nbr_pers = repas.Repas()
        
        for ingredient_et_quantite in liste_plat.IngredientsPlat(plat) :
            
            print(ingredient_et_quantite)
            
            for ingredient, quantite in ingredient_et_quantite :
                if nbr_pers != 2 :
                    quantite = nbr_pers*quantite/2
                liste_de_course.AjouterElement(ingredient, quantite)

    liste_de_course.Afficher()

menu_semaine = Menu(4)
menu_semaine.AjouterRepas("Dimanche", "pate carbo")
menu_semaine.AjouterRepas("Samedi", "poulet")

liste_plat = ListePlats()
liste_plat.AjouterPlat("pate carbo", {"pate" : 0.3, "sauce" : 1, "lardon" : 1})
liste_plat.AjouterPlat("poulet", {"poulet" : 1, "sauce" : 1})
liste_plat.AjouterPlat("Riz au thon", {"thon" : 1, "tomate" : 1})
liste_de_course = ListeCourse("auj")


RemplirCourseAvecMenu(menu_semaine, liste_de_course, liste_plat)