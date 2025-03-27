from classe.c_listecourse import *
from classe.c_menu import *
from classe.c_listeplat import *


def RemplirCourseAvecMenu(menu, liste_de_course, liste_plat) :
    for plat in menu.Plats() :
        for ingredient_et_quantite in liste_plat.IngredientsPlat(plat) :
            for ingredient, quantite in ingredient_et_quantite :
                liste_de_course.AjouterElement(ingredient, quantite)

    liste_de_course.Afficher()

menu_semaine = Menu(4)
menu_semaine.AjouterPlat("Dimanche", "pate carbo")
menu_semaine.AjouterPlat("Samedi", "poulet")
menu_semaine.AjouterPlat("Lundi", "Riz au thon")

liste_plat = ListePlats()
liste_plat.AjouterPlat("pate carbo", {"pate" : 0.3, "sauce" : 1, "lardon" : 1})
liste_plat.AjouterPlat("pate carbo", {"poulet" : 1, "sauce" : 1})

liste_de_course = ListeCourse("auj")

RemplirCourseAvecMenu(menu_semaine, liste_de_course, liste_plat)

