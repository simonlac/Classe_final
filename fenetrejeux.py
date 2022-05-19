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
from Jeux import *
from PyQt5.QtCore import pyqtSlot
import jeux_inter
from PyQt5 import QtWidgets


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


def cacher_labels_erreur_jeux(objet):
    """
    Cacher les différents labels d'erreur de jeux
    """
    objet.label_erreur_code_jeux.setVisible(False)
    objet.label_erreur_code_inv_jeux.setVisible(False)
    objet.label_erreur_nb_rangee_jeux.setVisible(False)
    objet.label_erreur_createur.setVisible(False)
    objet.label_erreur_nb_joueur.setVisible(False)


class Fenetrejeux(QtWidgets.QDialog, jeux_inter.Ui_jeux):
    def __init__(self, parent=None):
        super(Fenetrejeux, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des jeux")
        cacher_labels_erreur_jeux(self)

    @pyqtSlot()
    def on_pushButton_quitter_jeux_clicked(self):
        self.close()

    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_j_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Instancier un objet jeux
        jeux = Jeux()
        # Entrée de donnée pour les attributs de l'objet jeux
        jeux.code_document = self.lineEdit_code_jeux.text().capitalize()
        jeux.titre = self.lineEdit_jeux.text().capitalize()
        jeux.Nb_de_rangee = int(self.lineEdit_nb_rangee_jeux.text())
        jeux.createur = self.lineEdit_createur.text().capitalize()
        jeux.nb_de_joueur = int(self.lineEdit_nb_joueur.text())
        jeux.type = self.comboBox_jeu.currentText()
        # Booleen qui nous informe si le code du jeux existe ou pas dans la liste des jeux
        verifier_jeux = verifier_document_liste(jeux.code_document)

        # Si le code du jeux est valide mais existe déjà dans la liste des documents (on ne peut donc pas l'ajouter)
        if verifier_jeux is True:
            # Effacer le lineEdit du code du document et afficher le message d'erreur
            self.lineEdit_code_jeux.clear()
            self.label_erreur_code_jeux.setVisible(True)
        # si le titre est invalide, afficher un message d'erreur
        if jeux.titre == "":
            self.lineEdit_jeux.clear()
            self.label_erreur_code_inv_jeux.setVisible(True)
        # Si le code de document est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if jeux.code_document == "":
            self.lineEdit_code_jeux.clear()
            self.label_erreur_code_inv_jeux.setVisible(True)
        # si le nombre de rangée est invalide, afficher un message d'erreur
        if jeux.Nb_de_rangee == 0 or "":
            self.lineEdit_nb_rangee_jeux.clear()
            self.label_erreur_nb_rangee_jeux.setVisible(True)
        # Si le créateur  est invalide, effacer le lineEdit du créateur  et afficher un message d'erreur
        if jeux.createur == "":
            self.lineEdit_createur.clear()
            self.label_erreur_createur.setVisible(True)
        # Si le nombre de joueur est invalide, afficher un message d'erreur
        if jeux.nb_de_joueur == "" or 0:
            self.lineEdit_nb_joueur.clear()
            self.label_erreur_nb_joueur.setVisible(True)
        # Si les informations entrées sont valides et le jeux n'existe pas dans la liste
        if jeux.code_document != "" and jeux.titre != "" and jeux.Nb_de_rangee != "" and jeux.createur != "" and jeux.nb_de_joueur != "" and verifier_jeux is False:
            # Ajouter l'objet instancié à la liste des jeux
            ls_jeux.append(jeux)
            # Ajouter l'objet instancié à la liste des documents
            ls_document.append(jeux)
            # Ajouter les informations du jeux entré au textbrowser
            self.textBrowser_jeux.append(jeux.__str__())
            # Réinitialiser les lineEdits
            self.lineEdit_code_jeux.clear()
            self.lineEdit_jeux.clear()
            self.lineEdit_nb_rangee_jeux.clear()
            self.lineEdit_createur.clear()
            self.lineEdit_nb_joueur.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_jeux_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Instancier un objet Eudiant
        global jeu
        je = Jeux()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        je.code_document = self.lineEdit_code_jeux.text().capitalize()
        je.titre = self.lineEdit_jeux.text().capitalize()
        je.Nb_de_rangee = int(self.lineEdit_nb_rangee_jeux.text())
        je.createur = self.lineEdit_createur.text().capitalize()
        je.nb_de_joueur = int(self.lineEdit_nb_joueur.text())
        je.type = self.comboBox_jeu.currentText()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des étudiants
        verifier_je = verifier_document_liste(je.code_document)
        # Si le nom, le numéro et la date de naissance sont valides et l'étudiant existe dans la liste des étudiants:
        if je.code_document != "" and je.titre != "" and je.Nb_de_rangee != "" and je.createur != "" and je.nb_de_joueur != "" and verifier_je is True:
            trouve = False
            for jeu in ls_jeux and ls_jeux:
                # # Chercher dans la liste des étudiants un étudiant ayant les informations entrées
                if jeu.code_document == self.lineEdit_code_jeux.text().capitalize() and jeu.titre == self.lineEdit_jeux.text().capitalize() \
                        and jeu.Nb_de_rangee == self.lineEdit_nb_rangee_jeux.text() \
                        and jeu.createur == self.lineEdit_createur.text().capitalize() \
                        and jeu.nb_de_joueur == self.lineEdit_nb_joueur.text().capitalize() \
                        and jeu.type == self.comboBox_jeu.currentText():
                    # Supprimer l'étudiant de la liste des étudiants
                    trouve = True
                    ls_jeux.remove(jeu)
                    ls_jeux.remove(jeu)
                    break
            # Si l'étudiant n'existe pas dans la liste afficher un message d'erreur dans le label_erreur_Etu_Inexistant
            if not trouve:
                self.label_erreur_code_inv_jeux.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'étudiant supprimé
                self.textBrowser_jeux.clear()
                for fi in ls_film:
                    self.textBrowser_jeux.append(fi.__str__())
                # Réinitialiser les lineEdit et le dateEdit
                self.lineEdit_code_jeux.clear()
                self.lineEdit_jeux.clear()
                self.lineEdit_nb_rangee_jeux.clear()
                self.lineEdit_createur.clear()
                self.lineEdit_nb_joueur.clear()
                # Si le numéro d'étudiant est valide mais existe déjà dans la liste (on ne peut donc pas l'ajouter)
        if verifier_je is False and jeu.code_document !="":
            # Effacer le lineEdit du code du document et afficher le message d'erreur
            self.lineEdit_code_jeux.clear()
            self.label_erreur_code_jeux.setVisible(True)
        # si le titre est invalide, afficher un message d'erreur
        if jeu.titre == "":
            self.lineEdit_jeux.clear()
            self.label_erreur_code_inv_jeux.setVisible(True)
        # Si le code de document est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if jeu.code_document == "":
            self.lineEdit_code_jeux.clear()
            self.label_erreur_code_inv_jeux.setVisible(True)
        # si le nombre de rangée est invalide, afficher un message d'erreur
        if jeu.Nb_de_rangee == 0 or "":
            self.lineEdit_nb_rangee_jeux.clear()
            self.label_erreur_nb_rangee_jeux.setVisible(True)
        # Si le créateur  est invalide, effacer le lineEdit du créateur  et afficher un message d'erreur
        if jeu.createur == "":
            self.lineEdit_createur.clear()
            self.label_erreur_createur.setVisible(True)
        # Si le nombre de joueur est invalide, afficher un message d'erreur
        if jeu.nb_de_joueur == "" or 0:
            self.lineEdit_nb_joueur.clear()
            self.label_erreur_nb_joueur.setVisible(True)

