#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package controleJeu
##  \brief Gère les pages pour afficher au joueur
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet

def lirePage() :
        """! \brief Lit dans quelle 'page' ce trouve le joueur
        \return page -> Texte
        """
        page_txt = open("../data/texte/page.txt","r")
        page = page_txt.readline()
        page_txt.close()
        page = page.split()
        page = page[1]
        return page
    
    
    
    
def modifierPage(page) :
        """! \brief Modifie la page actuelle du joueur
        \param[in] page -> Texte
        """
        page_txt = open("../data/texte/page.txt", "w")
        page_txt.write("page " + page)
        page_txt.close()
