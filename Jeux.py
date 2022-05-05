####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe fille de document
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################

from Document import *
"""
import classe mère
"""

class Jeux(Document):
     """
     classe jeux qui fait parti de la classe document
     """

     ###################################
     #####  MÉTHODE CONSTRUCTEUR  #####
     ###################################

     def __init__(self, p_code_de_document="", p_titre="", p_nb_de_rangee=0, p_createur="", p_nb_de_joueur=0,
                  p_type=""):
         """

         méthode constructeur avec paramètre de défaut
         définie les différents attributs des jeux
         """
         Document.__init__(self, p_code_de_document, p_titre, p_nb_de_rangee)  # Appel constructeur classe document
         self.__createur= p_createur
         self.__nb_de_joueur = p_nb_de_joueur
         self.type = p_type

         ##################################################
         ####   Propriétés, accesseurs et mutateurs    ####
         ####                                          ####
         ##################################################

     #propriété créateur

     def _get_createur(self):
         """
         Accès à l'attribut privée du genre
         """

         return self.__createur

     def _set_createur(self, p_createur):
         """
         mutateur de __createur
         """
         if len(p_createur) <= 100:
             self.__createur = p_createur

     createur = property(_get_createur, _set_createur)
      #propriété nb_de_joueur
     def _get_nb_de_joueur(self):
         """
         Accès à l'attribut privée du nb_de_joueur
         """

         return self.__nb_de_joueur

     def _set_nb_de_joueur(self, p_nb_de_joueur):
         """
         mutateur de __nb_joueur
         """
         if p_nb_de_joueur>= 0 or p_nb_de_joueur <= 12:
             self.__nb_de_joueur = p_nb_de_joueur

     nb_de_joueur = property(_get_nb_de_joueur, _set_nb_de_joueur)

     def __str__(self):
         """
                 Méthode spéciale d'affichage. À utiliser avec print(objet)
                 :return: Chaine à afficher
         """
         chaine_jeux = " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le code du document : " + self.code_document + "\n" + \
                       "   Le titre du jeux : " + self.titre + "\n" + \
                       "   Le nombre de la rangée : " + str(self.nb_de_rangee) + "\n" + \
                       "   Le créateur du jeux : " + self.createur + "\n" + \
                       "   Le nombre de joueur : " + str(self.nb_de_joueur) + "\n" + \
                       "   Le type de jeu: " + self.type + "\n" + \
                       "\n" + "*" * 60
         return chaine_jeux

