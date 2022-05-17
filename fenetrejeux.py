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
        # Instancier un objet livre
        jeux = Jeux()
        # Entrée de donnée pour les attributs de l'objet Livre
        jeux.code_document = self.lineEdit_code_jeux.text().capitalize()
        jeux.titre = self.lineEdit_jeux.text().capitalize()
        jeux.Nb_de_rangee = int(self.lineEdit_nb_rangee_jeux.text())
        jeux.createur = self.lineEdit_createur.text().capitalize()
        jeux.nb_de_joueur = int(self.lineEdit_nb_joueur.text())
        jeux.type = self.comboBox_jeu.currentText()
        # Booleen qui nous informe si le code du livre existe ou pas dans la liste des étudiants
        verifier_jeux = verifier_document_liste(jeux.code_document)

        # Si le code du livre est valide mais existe déjà dans la liste des documents (on ne peut donc pas l'ajouter)
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
        # Si l'auteur  est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if jeux.createur == "":
            self.lineEdit_createur.clear()
            self.label_erreur_createur.setVisible(True)
        # Si la date de publication est invalide, afficher un message d'erreur
        if jeux.nb_de_joueur == "" or 0:
            self.lineEdit_nb_joueur.clear()
            self.label_erreur_nb_joueur.setVisible(True)
        # si la maison d'édition est invalide, afficher un message d'erreur
        # Si les informations entrées sont valides et le livre n'existe pas dans la liste des livres
        if jeux.code_document != "" and jeux.titre != "" and jeux.Nb_de_rangee != "" and jeux.createur != "" and jeux.nb_de_joueur != "" and verifier_jeux is False:
            # Ajouter l'objet instancié à la liste des livre
            ls_jeux.append(jeux)
            # Ajouter l'objet instancié à la liste des documents
            ls_document.append(jeux)
            # Ajouter les informations de l'étudiant entré au listview
            self.textBrowser_jeux.append(jeux.__str__())
            # Réinitialiser les lineEdits du titre, du nb de rangée, du code de document, de l'année de publication,
            # de l'auteur et de la maison d'édition
            self.lineEdit_code_jeux.clear()
            self.lineEdit_jeux.clear()
            self.lineEdit_nb_rangee_jeux.clear()
            self.lineEdit_createur.clear()
            self.lineEdit_nb_joueur.clear()
