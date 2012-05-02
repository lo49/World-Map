#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package bouton
##  \brief Permet la gestion des boutons 
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet
import controleJeu
import fonctionGeneral

def afficher(sprite,x,y):
    """! \brief Cela permet d'afficher le bouton sur la fenêtre au coordonnée x,y
    \param[in] sprite,x,y -> sprite,entier,entier
    """
    sprite.blit(x,y)


def creer(nom):
   	"""! \brief Permet le chargement du bouton.
    	le bouton est situer dans ../data/texture/bouton/
    	\param[in] nom -> string
	\return sprite - > sprite
    	"""
    	sprite = pyglet.image.load("../data/texture/bouton/"+nom)
	return sprite

def gestionRetour(x,y):
    """! \brief Permet le retour vers le menu. """
    if x < x_max and y<y_max :
        controleJeu.modifierPage("menu")
    else : pass

def bouton_home():
    bouton_home = creer("home.png")
    global x_max,y_max
    x_max,y_max = fonctionGeneral.texture(bouton_home)
    afficher(bouton_home,0,0)
    
