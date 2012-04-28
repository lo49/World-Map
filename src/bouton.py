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

def afficher(sprite,x,y):
    """! \brief Cela permet d'afficher le bouton sur la fenêtre au coordonnée x,y
    \param[in] sprite,x,y -> sprite,entier,entier
    \return None
    """
    sprite.blit(x,y)
    return None


def creer(nom):
   	"""! \brief Permet le chargement du bouton.
    	le bouton est situer dans ../data/texture/bouton/
    	\param[in] nom -> string
	\return sprite - > sprite
    	"""
    	sprite = pyglet.image.load("../data/texture/bouton/"+nom)
	return sprite
	return

