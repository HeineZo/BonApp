from urllib.request import urlretrieve
import csv

urlretrieve('http://www.lycee-marcellinberthelot-questembert.ac-rennes.fr/sites/lycee-marcellinberthelot-questembert.ac-rennes.fr/IMG/csv/menus_semaine.csv', 'menu_semaine_en_cours.csv')

menu = []
with open('menu_semaine_en_cours.csv', newline = '') as fichier_csv:
    fichier_lu = csv.DictReader(fichier_csv, delimiter = ';')
    for ligne in fichier_lu:
        menu.append(dict(ligne))
      
def clean_menu(menu):
    """Suppression des cases vides""" #Développé par Elouann
    for i in range (len(menu)) :
        del menu[i]['']
    return menu

clean_menu(menu)
categorie = list(menu[0].keys())#Catégories correspondants a la première ligne du CSV

def liste_mets_categorie(menu, categorie, num_jour):
    """Retourne tous les mets d'une catégorie""" #Développé par Elouann
    categorie_menu = []
    mets_max = 9 # 9 = Nombre de mets maximum par categorie le midi
    mets_max_soir = 4 # 4 = Nombre de mets maximum par categorie le soir
    ligne_lundi_soir = 45
    ligne_mardi_soir = ligne_lundi_soir + 4
    ligne_mercredi_soir = ligne_mardi_soir + 4
    if len(menu) < 59 :
        ligne_jeudi_soir =  ligne_mercredi_soir + 1
    else :
        ligne_jeudi_soir =  ligne_mercredi_soir + 2
    for i in range(mets_max):
        if num_jour <= 4 :
            categorie_menu.append(menu[i + num_jour * 9][categorie])
    for j in range(mets_max_soir):
        if num_jour == 5 :
            categorie_menu.append(menu[j + ligne_lundi_soir][categorie])
        elif num_jour == 6 :
            categorie_menu.append(menu[j + ligne_mardi_soir][categorie])
        elif num_jour == 7 :
            categorie_menu.append(menu[j + ligne_mercredi_soir][categorie])
        elif num_jour == 8 :
            categorie_menu.append(menu[j + ligne_jeudi_soir][categorie])
    return categorie_menu

def liste_mets_jour(menu,  categorie, num_jour):
    """Retourne tous les mets d'un jour""" #Développé par Elouann
    mets_menu = []
    for i in range(4):#Nombre de categories de mets (entrée, plat, produit laitier, dessert)
        mets_menu.append(liste_mets_categorie(menu, categorie[i], num_jour))
    return mets_menu

def plat_jour(menu, debut_categorie, fin_categorie, num_jour):
    """Renvoie les mets d'une categorie d'un jour""" #Développé par Elouann
    mets_categorie_menu= []
    for i in range(debut_categorie, fin_categorie): #Selection de la catégorie, Entrées : 0 à 1, Plat : 1 à 2, etc...
        mets_categorie_menu.append(liste_mets_jour(menu, categorie, num_jour)[i])
    mets_categorie_menu = [j for j in mets_categorie_menu[0] if j] #Supression du texte vide
    return mets_categorie_menu