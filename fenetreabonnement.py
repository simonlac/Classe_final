####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: fenêtre abonnement
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################
# Importer la librairie QtWidgets de QtDesigner.
# Importer la boite de dialogue
# Pour le gestionnaire d'événement
from real_main import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Abbonement import *
import abonnement_inter


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
# code abonnement


def verifier_abonner_liste(p_code_abbonnement):
    """
         Vérifie si le code de l'abonner existe dans la liste des document
             :param p_code_abonnement:  le code de l'abonner
             :return: True si le code de l'abonner est trouvé dans la liste des abonners et False sinon
    """
    for elt in ls_abonner:
        if elt.p_code_abbonnement == p_code_abbonnement.capitalize():
            return True
    return False


def cacher_labels_erreur_abonner(objet):
    """
    Cacher les différents labels d'erreur abonnement
    """
    objet.label_erreur_code_abonnement.setVisible(False)
    objet.label_erreur_code_inv_abonnement.setVisible(False)
    objet.label_erreur_nom.setVisible(False)
    objet.label_erreur_code_inv_nom.setVisible(False)
    objet.label_erreur_abonnement.setVisible(False)
    objet.label_erreur_code_inv_cour_tele.setVisible(False)


class Fenetreabonnement(QtWidgets.QDialog, abonnement_inter.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetreabonnement, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des abonnement")
        cacher_labels_erreur_abonner(self)

    @pyqtSlot()
    def on_pushButton_quitter_abonner_clicked(self):
        self.close()

    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_ab_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Instancier un objet livre
        abo = Abbonement()
        # Entrée de donnée pour les attributs de l'objet Livre
        abo.code_abbonnement = self.lineEdit_code_abonnement.text().capitalize()
        abo.type_abbonnement = self.comboBox_type_abonnement.currentText()
        abo.nom = self.lineEdit_nom.text().capitalize()
        abo.duree = self.comboBox_duree.currentText()
        abo.date = int(self.lineEdit_annee_abo.text())
        abo.courriel_tele = self.lineEdit_cour_tele.text().capitalize()
        # Booleen qui nous informe si le code du livre existe ou pas dans la liste des étudiants
        verifier_abonner = verifier_abonner_liste(abo.code_abbonnement)

        # Si le code du livre est valide mais existe déjà dans la liste des documents (on ne peut donc pas l'ajouter)
        if verifier_abonner is True:
            # Effacer le lineEdit du code du document et afficher le message d'erreur
            self.lineEdit_code_abonnement.clear()
            self.label_erreur_code_abonnement.setVisible(True)
        # Si le code de document est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if abo.code_abbonnement == "":
            self.lineEdit_code_abonnement.clear()
            self.label_erreur_code_inv_abonnement.setVisible(True)
        # si le nombre de rangée est invalide, afficher un message d'erreur
        if abo.nom == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setVisible(True)
        # Si l'auteur  est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if abo.date == "":
            self.lineEdit_annee_abo.clear()
            self.label_erreur_abonnement.setVisible(True)
        # si la maison d'édition est invalide, afficher un message d'erreur
        if abo.courriel_tele == "":
            self.lineEdit_cour_tele.clear()
            self.label_erreur_code_inv_cour_tele.setVisible(True)
        # Si les informations entrées sont valides et le livre n'existe pas dans la liste des livres
        if abo.code_abbonnement != "" and abo.nom != "" and abo.date != "" and abo.courriel_tele != "" and verifier_abonner is False:
            # Ajouter l'objet instancié à la liste des livre
            ls_abonner.append(abo)
            # Ajouter les informations de l'étudiant entré au listview
            self.textBrowser_abonner.append(abo.__str__())
            # Réinitialiser les lineEdits du titre, du nb de rangée, du code de document, de l'année de publication,
            # de l'auteur et de la maison d'édition
            self.lineEdit_code_abonnement.clear()
            self.lineEdit_nom.clear()
            self.lineEdit_annee_abo.clear()
            self.lineEdit_cour_tele.clear()
