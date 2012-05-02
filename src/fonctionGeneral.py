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
    hauteur = sprite.height
    return largeur,hauteur

def lectureDunFichier(fichier):
    """! \brief Lit un fichier et renvoie une liste.
    \param[in] fichier,mode -> String,String
    \return Liste_texte -> Liste
    """
    ##Ouverture du fichier
    fichier = open("../data/texte/"+fichier,"r")
    ## Liste que l'on renvera
    Liste_texte = []
    for ligne in fichier:
        ligne = ligne.split()
        if ligne == []:
            pass
        else: Liste_texte.append(ligne)
    fichier.close()
    return Liste_texte    

def modificationTexture(image,largeurNouvelle,hauteurNouvelle):
    """! \brief Modifie la taille d'une image
    \param[in] image,largeurNouvelle,hauteurNouvelle -> Sprite,entier,entier
    \return nouvelleImage -> Sprite
    """
    nouvelleImage = image.get_texture()                                                                                                  
    nouvelleImage.width = int(largeurNouvelle)                                                                                                                                                                  
    nouvelleImage.height = int(hauteurNouvelle)
    return nouvelleImage

def affiche_chargement_image(Nomsprite,x,y):
    """! \brief Charge l'image et l'affiche au coordonnée x,y
    \param[in] Nomsprite,x,y -> string,entier,entier.
    """
    image = pyglet.image.load("../data/texture/image/"+Nomsprite)
    image.blit(x,y)
