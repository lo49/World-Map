#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package deco
##  \brief Gestion de la décoration
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet
import drapeau
import option

def chargement_deco_menu():
    """! \brief Fonction du menu permettant de charger les image et de leur donnée des coordonné de base
    \enum liste_drapeau : Liste contenant tuplets du style (image,x_image,y_image)
    \enum image -> Sprite
    \enum x_image -> entier
    \enum y_image -> entier
    \return liste_general -> Liste
    """
    largeur,hauteur = option.window()
    ## Tout d'abord on liste les drapeaux aléatoirement grâce a la fonction crer_liste_aleatorie_drapeau de drapeau
    liste_drapeau = drapeau.creer_liste_aleatoire_drapeau(0,192)
    i= 0 ## Variable pour les coordonées
    liste_general = []
    ## boucle pour charger les image et calculé les coordonnées
    for nbr_drapeau in liste_drapeau:
        liste_pour_drapeau = []
        ## charge le drapeau :
        image_drapeau = drapeau.image_drapeau(nbr_drapeau)
        x = 2 * largeur // 3
        y = i
        liste_pour_drapeau.append(image_drapeau)
        liste_pour_drapeau.append(x)
        liste_pour_drapeau.append(y)
        liste_general.append(liste_pour_drapeau)
        i = y - 100
    return liste_general
        
        
def affiche_menu_drapeau(pays_drapeau,yPlus) :
    """!
        \brief Permer l'affichage des drapeaux verticalement. 
        Chaque image sera affiché au coordoné, enregistrer dans la liste pays_drapeau,
        x et y = y +yPlus        
        \param[in] pays_drapeau,yPlus -> Liste,entier 
        \return None
        """
    for i in range(len(pays_drapeau)) :
        total = pays_drapeau[i]
        image = total[0]
        x = total[1]
        y = total[2]
        y = y + yPlus + 2
        image.blit(x,y)
        total1 = [image,x,y]
        del total1[2]
        total1.append(y)
        truc = [total[0],x,y]
        del pays_drapeau[i]
        pays_drapeau.insert(i,truc)    


    
