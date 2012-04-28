#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package fonctionGeneral
##  \brief Permet la gestion des boutons 
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet

def texture(sprite):
    """! \brief Cela permet de renvoyer la texture de l'image.
    les Textures correspond a la largeur et hauteur du sprite.
    \param[in] sprite -> sprite
    \return largeur,hauteur -> entier,entier
    """
    largeur = sprite.width
    hauteur = sprite.hight
    return largeur,hauteur
def lectureDunFichier(fichier):
    """! """
