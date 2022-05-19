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
        if elt.code_abbonnement == p_code_abbonnement.capitalize():
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
        # Instancier un objet abonnement
        abo = Abbonement()
        # Entrée de donnée pour les attributs de l'objet abonnement
        abo.code_abbonnement = self.lineEdit_code_abonnement.text().capitalize()
        abo.type_abbonnement = self.comboBox_type_abonnement.currentText()
        abo.nom = self.lineEdit_nom.text().capitalize()
        abo.duree = self.comboBox_duree.currentText()
        abo.date = int(self.lineEdit_annee_abo.text())
        abo.courriel_tele = self.lineEdit_cour_tele.text().capitalize()
        # Booleen qui nous informe si le code de l'abonnement existe ou pas dans la liste des abonnement
        verifier_abonner = verifier_abonner_liste(abo.code_abbonnement)

        # Si le code de l'abonnement est valide mais existe déjà dans la liste  (on ne peut donc pas l'ajouter)
        if verifier_abonner is True:
            # Effacer le lineEdit du code de l'abonnement et afficher le message d'erreur
            self.lineEdit_code_abonnement.clear()
            self.label_erreur_code_abonnement.setVisible(True)
        # Si le code de l'abonnement est invalide, effacer le lineEdit du code de l'abonnement  et afficher un message d'erreur
        if abo.code_abbonnement == "":
            self.lineEdit_code_abonnement.clear()
            self.label_erreur_code_inv_abonnement.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        if abo.nom == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setVisible(True)
        # Si la date est invalide, effacer le lineEdit de la date et afficher un message d'erreur
        if abo.date == "":
            self.lineEdit_annee_abo.clear()
            self.label_erreur_abonnement.setVisible(True)
        # si le courriel ou télé est invalide, afficher un message d'erreur
        if abo.courriel_tele == "":
            self.lineEdit_cour_tele.clear()
            self.label_erreur_code_inv_cour_tele.setVisible(True)
        # Si les informations entrées sont valides et l' abonnement n'existe pas dans la liste
        if abo.code_abbonnement != "" and abo.nom != "" and abo.date != "" and abo.courriel_tele != "" and verifier_abonner is False:
            # Ajouter l'objet instancié à la liste
            ls_abonner.append(abo)
            # Ajouter les informations de l'abonnement au textbrowser
            self.textBrowser_abonner.append(abo.__str__())
            # Réinitialiser les lineEdits
            self.lineEdit_code_abonnement.clear()
            self.lineEdit_nom.clear()
            self.lineEdit_annee_abo.clear()
            self.lineEdit_cour_tele.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_abonnement_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """

        # Instancier un objet abonner
        abonn = Abbonement()
        # Entrée de donnée pour les attributs de l'objet abonner
        abonn.code_abbonnement = self.lineEdit_code_abonnement.text().capitalize()
        abonn.type_abbonnement = self.comboBox_type_abonnement.currentText()
        abonn.nom = self.lineEdit_nom.text().capitalize()
        abonn.duree = self.comboBox_duree.currentText()
        abonn.date = int(self.lineEdit_annee_abo.text())
        abonn.courriel_tele = self.lineEdit_cour_tele.text().capitalize()
        # Booleen qui nous informe si le numéro d'abonner existe ou pas dans la liste des abonners
        verifier_abo = verifier_abonner_liste(abonn.code_abbonnement)
        # si toute les caractéristiques existe dans la liste des étudiants:
        if abonn.code_abbonnement != "" and abonn.nom != "" and abonn.date != "" and abonn.courriel_tele != "" and verifier_abo is True:
            trouve = False
            for abon in ls_abonner:
                # # Chercher dans la liste des abonners un abonnement ayant les informations entrées
                if abon.date == self.lineEdit_annee_abo.text() and abon.nom == self.lineEdit_nom.text().capitalize() \
                        and abon.type_abonnement == self.comboBox_type_abonnement.currentText() \
                        and abon.duree == self.comboBox_duree.currentText() \
                        and abon.code_abbonnement == self.lineEdit_code_abonnement.text().capitalize() \
                        and abon.courriel_tele == self.lineEdit_cour_tele.text().capitalize():
                    # Supprimer l'abonner de la liste
                    trouve = True
                    ls_abonner.remove(abon)
                    break
            # Si l'abonner n'existe pas dans la liste afficher un message d'erreur
            if not trouve:
                self.label_erreur_code_inv_abonnement.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'étudiant supprimé
                self.textBrowser_abonner.clear()
                for elt in ls_abonner:
                    self.textBrowser_abonnerr.append(elt.__str__())
                # Réinitialiser les lineEdit
                self.lineEdit_code_abonnement.clear()
                self.lineEdit_nom.clear()
                self.lineEdit_annee_abo.clear()
                self.lineEdit_cour_tele.clear()
                # Si le code d'abonnement est valide mais existe déjà dans la liste (on ne peut donc pas l'ajouter)
        if verifier_abo is False and abonn.code_abbonnement != "":
            # Effacer le lineEdit du code d'abonner et afficher le message d'erreur
            self.lineEdit_numero.clear()
            self.label_erreur_Etu_Inexistant.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        # Si le code de l'abonnement est invalide, effacer le lineEdit du code de l'abonnement  et afficher un message d'erreur
        if abonn.code_abbonnement == "":
                self.lineEdit_code_abonnement.clear()
                self.label_erreur_code_inv_abonnement.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        if abonn.nom == "":
                self.lineEdit_nom.clear()
                self.label_erreur_nom.setVisible(True)
        # Si la date est invalide, effacer le lineEdit de la date et afficher un message d'erreur
        if abonn.date == "":
                self.lineEdit_annee_abo.clear()
                self.label_erreur_abonnement.setVisible(True)
        # si le courriel ou télé est invalide, afficher un message d'erreur
        if abonn.courriel_tele == "":
                self.lineEdit_cour_tele.clear()
                self.label_erreur_code_inv_cour_tele.setVisible(True)
