#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package texte
##  \brief Permet la gestion des boutons 
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet

def affiche(texte):
	"""! \brief affiche le texte.
	\param[in] texte -> Text
	"""
	texte.draw()
def choix_couleur(nbr_couleur):
	"""! \brief Choisie la couleur.
	rouge,vert,bleu,blanc,noir,orange,violet,gris,marron,rose
	  0		1	 2	  3		4	  5		6	   7	8	   9
	param[in] nbr_couleur -> entier
	return couleurs -> tuple
	"""
	rouge,vert,bleu = (255,0,0,255),(0,255,0,255),(0,0,255,255)
    blanc,noir,orange = (0,0,0,0),(255,255,255,255),(248,139,11,255)
    violet,gris,marron,rose = (229,22,197,255),(142,138,141,255),(184,130,14,255),(251,11,175,255)  
    couleurs = [rouge,vert,bleu,blanc,noir,orange,violet,gris,marron,rose]
    couleurs = couleurs[choix_couleur]
	return couleurs

## def choix_size(nbr_size):
	

def creer(texte,x,y,couleur=5,size=5):
	"""! \brief permet de créer un objet texte en pyglet.
	\param[in] texte,couleur -> str,entier,entier
	return texte -> Text
	"""
	couleur = choix_couleur(couleur)
	size = choix_size(size)
	
	

