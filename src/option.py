#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package option
##  \brief Gestion des Options
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet,option_config

def window():
    """! \brief Retourne la largeur et la hauteur de la fenêtre de jeu.
    \return largeur,hauteur -> entier,entier
    """
    Largeur_fenetre,Longueur_fenetre,ON_OFF_musique,ON_OFF_son = option_config.lecture_option()
    return Largeur_fenetre,Longueur_fenetre


