####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: fenêtre film
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################
# Importer la librairie QtWidgets de QtDesigner.
# Pour le gestionnaire d'événement
# Importer la boite de dialogue


from real_main import *
from Film import *
import film_inter
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

ls_document = []
ls_livre = []
ls_jeux = []
ls_film = []


def verifier_document_liste(p_code_de_document):
    """
         Vérifie si le code de document existe dans la liste des document
             :param p_code_de_document:  le code de document
             :return: True si lecode de document est trouvé dans la liste des documents et False sinon
    """
    for elt in ls_document and ls_livre and ls_film and ls_jeux:
        if elt.code_document == p_code_de_document.capitalize():
            return True
    return False


def cacher_labels_erreur_film(objet):
    """
    Cacher les différents labels d'erreur de film
    """
    objet.label_erreur_code_film.setVisible(False)
    objet.label_erreur_code_inv_film.setVisible(False)
    objet.label_erreur_nb_rangee_film.setVisible(False)
    objet.label_erreur_genre.setVisible(False)
    objet.label_erreur_annee.setVisible(False)
    objet.label_erreur_realisateur.setVisible(False)
    objet.label_erreur_film_t_inv.setVisible(False)


class Fenetrefilm(QtWidgets.QDialog, film_inter.Ui_film):
    def __init__(self, parent=None):
        super(Fenetrefilm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des film")
        cacher_labels_erreur_film(self)

    @pyqtSlot()
    def on_pushButton_quitter_film_clicked(self):
        self.close()

    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_f_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Instancier un objet livre
        fil = Film()
        # Entrée de donnée pour les attributs de l'objet Livre
        fil.code_document = self.lineEdit_code_film.text().capitalize()
        print(fil.code_document)
        fil.titre = self.lineEdit_film.text().capitalize()
        print(fil.titre)
        fil.Nb_de_rangee = int(self.lineEdit_nb_rangee_film.text())
        print(fil.Nb_de_rangee)
        fil.genre = self.lineEdit_genre.text().capitalize()
        print(fil.genre)
        fil.acteur_principal = self.lineEdit_acteur_prin.text().capitalize()
        print(fil.acteur_principal)
        fil.realisateur = self.lineEdit_realisateur.text().capitalize()
        print(fil.realisateur)