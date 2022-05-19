####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: fenêtre emprunt
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################
# Importer la librairie QtWidgets de QtDesigner.
# Pour le gestionnaire d'événement
# Importer la boite de dialogue
from real_main import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import emprunt_inter
from Emprunt import *


######################################################
###### DÉFINITIONS DE LA CLASSE emprunt ######
######################################################
ls_emprunt = []
# code emprunt
def verifier_emprunt(p_code_emprunt):
    """
         Vérifie si le code d'emprunt existe dans la liste des emprunts
             :param p_code-emprunt:  le numéro de l'emprunt
             :return: True si l'emprunt est trouvé dans la liste des emprunts et False sinon
    """
    for elt in ls_emprunt:
        if elt.code_emprunt == p_code_emprunt.capitalize():
            return True
    return False

def cacher_labels_erreur_emprunt(objet):
    """
    Cacher les différents labels d'erreur emprunt
    """
    objet.label_erreur_code_emprunt.setVisible(False)
    objet.label_erreur_code_inv_emprunt.setVisible(False)
    objet.label_erreur_code_inv_document_emprunt.setVisible(False)
    objet.label_erreur_code_inv_abonnement_emprunt.setVisible(False)
    objet.label_erreur_emprunt.setVisible(False)
class Fenetreemprunt(QtWidgets.QDialog, emprunt_inter.Ui_emprunt):
    def __init__(self, parent=None):
        super(Fenetreemprunt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des emprunts")
        cacher_labels_erreur_emprunt(self)


    @pyqtSlot()
    def on_pushButton_quitter_emprunt_clicked(self):
        self.close()

    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_em_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Instancier un objet Emprunt
        em = Emprunt()
        # Entrée de donnée pour les attributs de l'objet emprunt
        em.code_emprunt= self.lineEdit_code_emprunt.text().capitalize()
        em.list = self.lineEdit_code_document_emprunt.text().capitalize()
        em.date_emprunt= self.Date_emprunt.date()
        em.abonner = self.lineEdit_code_abonnement_emprunt.text().capitalize()
        # Booleen qui nous informe si le code d'emprunt existe déjà
        verifier_em = verifier_emprunt(em.code_emprunt)

        # Si le code d'emprunt est valide mais existe déjà dans la liste des emprunts (on ne peut donc pas l'ajouter)
        if verifier_em is True :
            # Effacer le lineEdit du code d'emprunt et afficher le message d'erreur
            self.lineEdit_code_emprunt.clear()
            self.label_erreur_code_emprunt.setVisible(True)
        # si le code de document est invalide, afficher un message d'erreur
        if em.list == "":
             self.lineEdit_code_document_emprunt.clear()
             self.label_erreur_code_inv_document_emprunt.setVisible(True)
        # Si le code d'emprunt est invalide, effacer le lineEdit du code d'emprunt et afficher un message d'erreur
        if em.code_emprunt == "":
            self.lineEdit_code_emprunt.clear()
            self.label_erreur_code_inv_emprunt.setVisible(True)
        # Si le code d'abonner est invalide, effacer le lineEdit du code d'abonner  et afficher un message d'erreur
        if em.abonner == "":
            self.lineEdit_code_abonnement_emprunt.clear()
            self.label_erreur_code_inv_abonnement_emprunt.setVisible(True)
        # Si la date de naissance est invalide, afficher un message d'erreur
        if em.date_emprunt == "":
             self.label_erreur_emprunt.setVisible(True)
        # Si les informations entrées sont valides et l'emprunt n'existe pas dans la liste des emprunt
        if em.list != "" and em.abonner != "" and em.code_emprunt != ""and em.date_emprunt != "" and verifier_em is False:
            #Ajouter l'emprunt instancié à la liste des emprunts
            ls_emprunt.append(em)
            # Ajouter les informations de l'emprunt entré au TextBrowser
            self.textBrowser_emprunt.append(em.__str__())
            # Réinitialiser les lineEdits
            self.lineEdit_code_emprunt.clear()
            self.lineEdit_code_abonnement_emprunt.clear()
            self.Date_emprunt.setDate(QDate(2000, 1, 1))
            self.lineEdit_code_document_emprunt.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_emprunt_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Instancier un emprunt
        emp = Emprunt()
        # Entrée de donnée pour les attributs de l'objet emprunt
        emp.code_emprunt = self.lineEdit_code_emprunt.text().capitalize()
        emp.list = self.lineEdit_code_document_emprunt.text().capitalize()
        emp.date_emprunt = self.Date_emprunt.date()
        emp.abonner = self.lineEdit_code_abonnement_emprunt.text().capitalize()
        # Booleen qui nous informe si l'emprunt existe ou pas dans la liste
        verifier_emprun = verifier_emprunt(emp.code_emprunt)
        # les caractéristiques de l'emprunt existe dans la liste :
        if emp.code_emprunt != "" and emp.list != "" and emp.date_emprunt != ""and emp.abonner != "" and verifier_emprun is True:
            trouve = False
            for emprunt in ls_emprunt:
                # # Chercher dans la liste des emprunt un emprunt ayant les informations entrées
                if emprunt.code_emprunt == self.lineEdit_code_emprunt.text().capitalize() and emprunt.abonner == self.lineEdit_code_abonnement_emprunt.text().capitalize() \
                        and emprunt.list == self.lineEdit_code_document_emprunt.text().capitalize() \
                        and emprunt.date_emprunt == self.Date_emprunt.date():
                    # Supprimer l'emprunt de la liste
                    trouve = True
                    ls_emprunt.remove(emprunt)
                    break
            # Si l'emprunt n'existe pas dans la liste afficher un message d'erreur
            if not trouve:
                self.label_erreur_code_inv_emprunt.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'emprunt supprimé
                self.textBrowser_emprunt.clear()
                for emprunt in ls_emprunt:
                 self.textBrowser_emprunt.append(emprunt.__str__())
                # Réinitialiser les lineEdit
                self.lineEdit_code_emprunt.clear()
                self.lineEdit_code_abonnement_emprunt.clear()
                self.Date_emprunt.setDate(QDate(2000, 1, 1))
                self.lineEdit_code_document_emprunt.clear()
                # Si le code d'emprunt est valide mais existe déjà dans la liste (on ne peut donc pas l'ajouter)
        if verifier_emprun is False and emp.code_emprunt != "":
            # Effacer le lineEdit du numéro d'emprunt et afficher le message d'erreur
            self.lineEdit_code_emprunt.clear()
            self.label_erreur_code_emprunt.setVisible(True)
        # si le code d'abonner est invalide, afficher un message d'erreur
        if emp.abonner == "":
            self.lineEdit_code_abonnement_emprunt.clear()
            self.label_erreur_code_inv_abonnement_emprunt.setVisible(True)
        # Si le numéro de document est invalide, afficher un message d'erreur
        if emp.list == "":
            self.lineEdit_code_document_emprunt.clear()
            self.label_erreur_code_inv_document_emprunt.setVisible(True)
            # Si la date d'emprunt est invalide, afficher un message d'erreur
        if emp.date_emprunt == "":
            self.label_erreur_emprunt.setVisible(True)

