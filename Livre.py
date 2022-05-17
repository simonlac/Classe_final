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
import la classe mère
"""


class Livre(Document):
    """
    classe Livre qui fait parti de la classe document
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, p_code_de_document="", p_titre="", p_nb_de_rangee=0,
                 p_auteur="", p_annee_publication=0, p_maison_edition=""):
        """
                   méthode constructeur avec paramètre de défaut
                   définie les différents attributs des livres
      """
        Document.__init__(self, p_code_de_document, p_titre, p_nb_de_rangee)  # Appel constructeur classe document
        self.__auteur = p_auteur
        self.__annee_publi = p_annee_publication
        self.maison_edition = p_maison_edition

        ##################################################
        ####   Propriétés, accesseurs et mutateurs    ####
        ####                                          ####
        ##################################################

        # propriété auteur

    def _get_auteur(self):
        """
          Accès à l'attribut privée de l'auteur
          """

        return self.__auteur

    def _set_auteur(self, p_auteur):
        """
          mutateur de __auteur
          """
        if len(p_auteur) <= 50:
            self.__auteur = p_auteur

    auteur = property(_get_auteur, _set_auteur)

    # propriété année_publi
    def _get_annee_publication(self):
        """
        Accès à l'attribut privée de l'année de publication
        """

        return self.__annee_publi

    def _set_annee_publication(self, p_annee_publication):
        """
        mutateur de __annee_publi
        """
        if p_annee_publication >= -3300 or p_annee_publication <= 2022:
            self.__annee_publi = p_annee_publication

    annee_publication = property(_get_annee_publication, _set_annee_publication)

    def __str__(self):
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine_livre = " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le code du document : " + self.code_document + "\n" + \
                       "   Le titre du livre : " + self.titre + "\n" + \
                       "   Le nombre de la rangée : " +  str(self.Nb_de_rangee) + "\n" + \
                       "   L'auteur du livre : " + self.auteur + "\n" + \
                       "   L'année de publication : " + str(self.annee_publication) + "\n" + \
                       "   La maison d'édition: " + self.maison_edition + "\n" + \
                       "\n" + "*" * 60
        return chaine_livre

