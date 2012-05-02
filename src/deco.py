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
        
        
def affiche_menu_drapeau(liste_drapeau,yPlus) :
    """! \brief Permer l'affichage des drapeaux verticalement. 
        Chaque image sera affiché au coordoné, enregistrer dans la liste pays_drapeau,
        x et y = y +yPlus        
        \param[in] pays_drapeau,yPlus -> Liste,entier 
        \return liste_drapeau -> Liste
        """
    for i in range(len(liste_drapeau)) :
        total = liste_drapeau[i]
        image = total[0]
        x = total[1]
        y = total[2]
        y = y + yPlus + 2
        image.blit(x,y)
        total1 = [image,x,y]
        del total1[2]
        total1.append(y)
        truc = [total[0],x,y]
        del liste_drapeau[i]
        liste_drapeau.insert(i,truc)
    ## on touche si besoin a la liste_drapeau :
    liste_drapeau = boucle_de_drapeau(liste_drapeau)
    return liste_drapeau

def boucle_de_drapeau(liste_drapeau):
    """! \brief Remet les drapeaux à la fin de la liste et au nouvelle coordonnée.
    Elle permetra de créer un affichage infini des drapeaux dans le menu.
    \param[in] liste_drapeau -> Liste
    \return liste_drapeau -> Liste
    """
    ## On regarde le premier élement de la liste et on regarde si il est dans le
    ## cadre de la fenetre
    drapeau1 = liste_drapeau[0]
    ## on prend le coordonnée y en position 3 de la liste drapeau1
    y_drapeau1 = drapeau1[2]
    largeur,hauteur = option.window()
    ## si il n'est plus dans le cadre on le supprime et on le rajoute a la fin
    ## avec un nouveau y le positionnant en y
    if y_drapeau1 > hauteur :
        del liste_drapeau[0]
        ## On lit le dernier drapeau de la liste:
        drapeau_fin = liste_drapeau[int(len(liste_drapeau) -1)]
        y_drapeauFin = drapeau_fin[2]
        y_drapeauNouveau = y_drapeauFin - 100
        drapeauAjouter = []
        drapeauAjouter.append(drapeau1[0])
        drapeauAjouter.append(drapeau1[1])
        drapeauAjouter.append(y_drapeauNouveau)
        liste_drapeau.append(drapeauAjouter)
    else : pass
    return liste_drapeau


        


    
