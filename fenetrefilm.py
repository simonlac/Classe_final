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
        # Instancier un objet film
        fil = Film()
        # Entrée de donnée pour les attributs de l'objet film
        fil.code_document = self.lineEdit_code_film.text().capitalize()
        fil.titre = self.lineEdit_film.text().capitalize()
        fil.Nb_de_rangee = int(self.lineEdit_nb_rangee_film.text())
        fil.genre = self.lineEdit_genre.text().capitalize()
        fil.acteur_principal = self.lineEdit_acteur_prin.text().capitalize()
        fil.realisateur = self.lineEdit_realisateur.text().capitalize()
        # Booleen qui nous informe si le code du film existe ou pas dans la liste
        verifier_film = verifier_document_liste(fil.code_document)

        # Si le code du film est valide mais existe déjà dans la liste des documents (on ne peut donc pas l'ajouter)
        if verifier_film is True:
            # Effacer le lineEdit du code du document et afficher le message d'erreur
            self.lineEdit_code_film.clear()
            self.label_erreur_code_film.setVisible(True)
        # si le titre est invalide, afficher un message d'erreur
        if fil.titre == "":
            self.lineEdit_film.clear()
            self.label_erreur_film_t_inv.setVisible(True)
        # Si le code de document est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if fil.code_document == "":
            self.lineEdit_code_film.clear()
            self.label_erreur_code_inv_film.setVisible(True)
        # si le nombre de rangée est invalide, afficher un message d'erreur
        if fil.Nb_de_rangee == "":
            self.lineEdit_nb_rangee_film.clear()
            self.label_erreur_nb_rangee_film.setVisible(True)
        # Si le genre est invalide
        if fil.genre == "":
            self.lineEdit_genre.clear()
            self.label_erreur_genre.setVisible(True)
        # Si l'acteur principal est invalide
        if fil.acteur_principal == "":
            self.lineEdit_acteur_prin.clear()
            self.label_erreur_annee.setVisible(True)
        # si le réalisateur est invalide, afficher un message d'erreur
        if fil.realisateur == "":
            self.lineEdit_realisateur.clear()
            self.label_erreur_realisateur.setVisible(True)
        # Si les informations entrées sont valides et le film n'existe pas dans la liste 
        if fil.code_document != "" and fil.titre != "" and fil.Nb_de_rangee != "" and fil.genre != "" and fil.acteur_principal != "" and fil.realisateur != "" and verifier_film is False:
            # Ajouter l'objet instancié à la liste des film
            ls_film.append(fil)
            # Ajouter l'objet instancié à la liste des film
            ls_document.append(fil)
            # Ajouter les informations du livre entré au textbrowser
            self.textBrowser_film.append(fil.__str__())
            # Réinitialiser les lineEdits
            self.lineEdit_code_film.clear()
            self.lineEdit_film.clear()
            self.lineEdit_nb_rangee_film.clear()
            self.lineEdit_genre.clear()
            self.lineEdit_acteur_prin.clear()
            self.lineEdit_realisateur.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_suppriemer_film_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Instancier un objet Eudiant
        fil = Film()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        fil.code_document = self.lineEdit_code_film.text().capitalize()
        fil.titre = self.lineEdit_film.text().capitalize()
        fil.Nb_de_rangee = int(self.lineEdit_nb_rangee_film.text())
        fil.genre = self.lineEdit_genre.text().capitalize()
        fil.acteur_principal = self.lineEdit_acteur_prin.text().capitalize()
        fil.realisateur = self.lineEdit_realisateur.text().capitalize()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des étudiants
        verifier_fil = verifier_document_liste(fil.code_document)
        # Si le nom, le numéro et la date de naissance sont valides et l'étudiant existe dans la liste des étudiants:
        if fil.code_document != "" and fil.titre != "" and fil.Nb_de_rangee != "" and fil.genre != "" and fil.acteur_principal != "" and fil.realisateur != "" and verifier_fil is True:
            trouve = False
            for film in ls_film and ls_document:
                # # Chercher dans la liste des étudiants un étudiant ayant les informations entrées
                if film.code_document == self.lineEdit_code_film.text().capitalize() and film.titre == self.lineEdit_film.text().capitalize() \
                        and film.Nb_de_rangee == self.lineEdit_nb_rangee_film.text() \
                        and film.genre == self.lineEdit_genre.text().capitalize() \
                        and film.acteur_principal == self.lineEdit_acteur_prin.text().capitalize() \
                        and film.realisateur == self.lineEdit_realisateur.text().capitalize():
                    # Supprimer l'étudiant de la liste des étudiants
                    trouve = True
                    ls_film.remove(film)
                    ls_document.remove(film)
                    break
            # Si l'étudiant n'existe pas dans la liste afficher un message d'erreur dans le label_erreur_Etu_Inexistant
            if not trouve:
                self.label_erreur_code_inv_film.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'étudiant supprimé
                self.textBrowser_film.clear()
                for fi in ls_film:
                    self.textBrowser_film.append(fi.__str__())
                # Réinitialiser les lineEdit et le dateEdit
                self.lineEdit_code_film.clear()
                self.lineEdit_film.clear()
                self.lineEdit_nb_rangee_film.clear()
                self.lineEdit_genre.clear()
                self.lineEdit_acteur_prin.clear()
                self.lineEdit_realisateur.clear()
                # Si le numéro d'étudiant est valide mais existe déjà dans la liste (on ne peut donc pas l'ajouter)

        if verifier_fil is False and fil.code_document != "":
            # Effacer le lineEdit du numéro étudiant et afficher le message d'erreur
            self.lineEdit_code_film.clear()
            self.label_erreur_code_film.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        if fil.code_document == "":
            self.lineEdit_code_film.clear()
            self.label_erreur_code_inv_film.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if fil.titre == "":
            self.lineEdit_film.clear()
            self.label_erreur_film_t_inv.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if fil.Nb_de_rangee == "":
            self.lineEdit_nb_rangee_film.clear()
            self.label_erreur_nb_rangee_film.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if fil.genre == "":
            self.lineEdit_genre.clear()
            self.label_erreur_genre.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if fil.acteur_principal == "":
            self.lineEdit_acteur_prin.clear()
            self.label_erreur_annee.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if fil.realisateur == "":
            self.lineEdit_realisateur.clear()
            self.label_erreur_realisateur.setVisible(True)
