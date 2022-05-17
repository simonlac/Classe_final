####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: fenêtre livre
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################
# Importer la librairie QtWidgets de QtDesigner.
# Pour le gestionnaire d'événement

# Importer la boite de dialogue


from real_main import *
import livre_inter
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Livre import *


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
    from real_main import ls_document
    for elt in ls_document and ls_livre and ls_film and ls_jeux:
        if elt.code_document == p_code_de_document.capitalize():
            return True
    return False


def cacher_labels_erreur_livre(objet):
    """
     Cacher les différents labels d'erreur de livre
    """
    objet.label_erreur_code.setVisible(False)
    objet.label_erreur_code_inv.setVisible(False)
    objet.label_erreur_nb_rangee.setVisible(False)
    objet.label_erreur_auteur.setVisible(False)
    objet.label_erreur_annee.setVisible(False)
    objet.label_erreur_annee_2.setVisible(False)
    objet.label_erreur_livre_t_inv.setVisible(False)


class Fenetrelivre(QtWidgets.QDialog, livre_inter.Ui_livre):
    def __init__(self, parent=None):
        super(Fenetrelivre, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des livres")
        cacher_labels_erreur_livre(self)

    @pyqtSlot()
    def on_pushButton_quitter_livre_clicked(self):
        self.close()

        # Utiliser le décorateur ici pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute
        # deux fois

    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_l_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Instancier un objet livre
        liv = Livre()
        # Entrée de donnée pour les attributs de l'objet Livre
        liv.code_document = self.lineEdit_code.text().capitalize()
        liv.titre = self.lineEdit_titre.text().capitalize()
        liv.Nb_de_rangee = int(self.lineEdit_nb_rangee.text())
        liv.auteur = self.lineEdit_auteur.text().capitalize()
        liv.annee_publication = int(self.lineEdit.text())
        liv.maison_edition = self.lineEdit_maison.text().capitalize()
        # Booleen qui nous informe si le code du livre existe ou pas dans la liste des étudiants
        verifier_livre = verifier_document_liste(liv.code_document)

        # Si le code du livre est valide mais existe déjà dans la liste des documents (on ne peut donc pas l'ajouter)
        if verifier_livre is True:
            # Effacer le lineEdit du code du document et afficher le message d'erreur
            self.lineEdit_code.clear()
            self.label_erreur_code.setVisible(True)
        # si le titre est invalide, afficher un message d'erreur
        if liv.titre == "":
            self.lineEdit_titre.clear()
            self.label_erreur_livre_t_inv.setVisible(True)
        # Si le code de document est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if liv.code_document == "":
            self.lineEdit_code.clear()
            self.label_erreur_code_inv.setVisible(True)
        # si le nombre de rangée est invalide, afficher un message d'erreur
        if liv.Nb_de_rangee == "":
            self.lineEdit_nb_rangee.clear()
            self.label_erreur_nb_rangee.setVisible(True)
        # Si l'auteur  est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
        if liv.auteur == "":
            self.lineEdit_auteur.clear()
            self.label_erreur_auteur.setVisible(True)
        # Si la date de publication est invalide, afficher un message d'erreur
        if liv.annee_publication == "":
            self.lineEdit.clear()
            self.label_erreur_annee.setVisible(True)
        # si la maison d'édition est invalide, afficher un message d'erreur
        if liv.maison_edition == "":
            self.lineEdit_maison.clear()
            self.label_erreur_annee_2.setVisible(True)
        # Si les informations entrées sont valides et le livre n'existe pas dans la liste des livres
        if liv.code_document != "" and liv.titre != "" and liv.Nb_de_rangee != "" and liv.auteur != "" and liv.annee_publication != "" and liv.maison_edition != "" and verifier_livre is False:
            # Ajouter l'objet instancié à la liste des livre
            ls_livre.append(liv)
            # Ajouter l'objet instancié à la liste des documents
            ls_document.append(liv)
            # Ajouter les informations de l'étudiant entré au listview
            self.textBrowser_livre.append(liv.__str__())
            # Réinitialiser les lineEdits du titre, du nb de rangée, du code de document, de l'année de publication,
            # de l'auteur et de la maison d'édition
            self.lineEdit_code.clear()
            self.lineEdit_titre.clear()
            self.lineEdit_nb_rangee.clear()
            self.lineEdit_auteur.clear()
            self.lineEdit_maison.clear()
            self.lineEdit.clear()

    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_livre_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier
        """
        # Instancier un objet Eudiant
        liv = Livre()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        liv.code_document = self.lineEdit_code.text().capitalize()
        liv.titre = self.lineEdit_titre.text().capitalize()
        liv.Nb_de_rangee = int(self.lineEdit_nb_rangee.text())
        liv.auteur = self.lineEdit_auteur.text().capitalize()
        liv.annee_publication = int(self.lineEdit.text())
        liv.maison_edition = self.lineEdit_maison.text().capitalize()
        # Booleen qui nous informe si le code du livre existe ou pas dans la liste des étudiants
        verifier_livre = verifier_document_liste(liv.code_document)
        # Si le numéro d'étudiant est valide mais existe déjà dans la liste des étudiants (on ne peut donc pas l'ajouter)
        if verifier_livre is False and liv.code_document != "":
            # Effacer le lineEdit du numéro étudiant et afficher le message d'erreur
            # si le titre est invalide, afficher un message d'erreur
            if liv.titre == "":
                self.lineEdit_titre.clear()
                self.label_erreur_livre_t_inv.setVisible(True)
            # Si le code de document est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
            if liv.code_document == "":
                self.lineEdit_code.clear()
                self.label_erreur_code_inv.setVisible(True)
            # si le nombre de rangée est invalide, afficher un message d'erreur
            if liv.Nb_de_rangee == "":
                self.lineEdit_nb_rangee.clear()
                self.label_erreur_nb_rangee.setVisible(True)
            # Si l'auteur  est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
            if liv.auteur == "":
                self.lineEdit_auteur.clear()
                self.label_erreur_auteur.setVisible(True)
            # Si la date de publication est invalide, afficher un message d'erreur
            if liv.annee_publication == "":
                self.lineEdit.clear()
                self.label_erreur_annee.setVisible(True)
            # si la maison d'édition est invalide, afficher un message d'erreur
            if liv.maison_edition == "":
                self.lineEdit_maison.clear()
                self.label_erreur_annee_2.setVisible(True)
            # Si les informations entrées sont valides et l'étudiant n'existe pas dans la liste des étudiants
            if liv.code_document != "" and liv.titre != "" and liv.Nb_de_rangee != "" and liv.auteur != "" and liv.annee_publication != "" and liv.maison_edition != "" and verifier_livre is True:
                for lie in ls_livre:
                    # Chercher dans la liste des étudiants un étudiant ayant le numéro d'étudiant entré
                    if lie.code_document == self.lineEdit_code.text():
                        # Apporter les modifications aux attributs Nom_Etud, Programme et Date_Naiss
                        lie.titre = self.lineEdit_titre.text().capitalize()
                        lie.Nb_de_rangee = int(self.lineEdit_nb_rangee.text())
                        lie.auteur = self.lineEdit_auteur.text().capitalize()
                        lie.annee_publication = int(self.lineEdit.text())
                        lie.maison_edition = self.lineEdit_maison.text().capitalize()
            # Effacer le textBowser
            self.textBrowser_livre.clear()
            # Après modifications, réfficher tous les étudiants de la liste dans le textBrowser
            for lie in ls_livre:
                self.textBrowser_livre.append(lie.__str__())
            # Réinitialiser les lineEdits du numéro et du nom et le dateEdit
            self.lineEdit_code.clear()
            self.lineEdit_titre.clear()
            self.lineEdit_nb_rangee.clear()
            self.lineEdit_auteur.clear()
            self.lineEdit_maison.clear()
            self.lineEdit.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_livre_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Instancier un objet Eudiant
        liv = Livre()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        liv.code_document = self.lineEdit_code.text().capitalize()
        liv.titre = self.lineEdit_titre.text().capitalize()
        liv.Nb_de_rangee = int(self.lineEdit_nb_rangee.text())
        liv.auteur = self.lineEdit_auteur.text().capitalize()
        liv.annee_publication = int(self.lineEdit.text())
        liv.maison_edition = self.lineEdit_maison.text().capitalize()
        # Booleen qui nous informe si le code du livre existe ou pas dans la liste des étudiants
        verifier_livre = verifier_document_liste(liv.code_document)
        # Si le nom, le numéro et la date de naissance sont valides et l'étudiant existe dans la liste des étudiants:
        if liv.code_document != "" and liv.titre != "" and liv.Nb_de_rangee != "" and liv.auteur != "" and liv.annee_publication != "" and liv.maison_edition != "" and verifier_livre is True:
            trouve = False
            for liv in ls_livre:
                # # Chercher dans la liste des étudiants un étudiant ayant les informations entrées
                if liv.code_document == self.lineEdit_code.text() and liv.titre == self.lineEdit_titre.text().capitalize() \
                        and liv.Nb_de_rangee == int(self.lineEdit_nb_rangee.text()) \
                        and liv.auteur == self.lineEdit_auteur.text().capitalize() \
                        and liv.annee_publication == int(self.lineEdit.text().capitalize()) \
                        and liv.maison_edition == self.lineEdit_maison.text().capitalize():
                    # Supprimer l'étudiant de la liste des étudiants
                    trouve = True
                    ls_livre.remove(liv)
                    break
            # Si l'étudiant n'existe pas dans la liste afficher un message d'erreur dans le label_erreur_Etu_Inexistant
            if not trouve:
                self.label_erreur_code_inv.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'étudiant supprimé
                self.textBrowser_livre.clear()
                for liv in ls_livre:
                    self.textBrowser_livre.append(liv.__str__())
                # Réinitialiser les lineEdit et le dateEdit
                self.lineEdit_code.clear()
                self.lineEdit_titre.clear()
                self.lineEdit_nb_rangee.clear()
                self.lineEdit_auteur.clear()
                self.lineEdit_maison.clear()
                self.lineEdit.clear()

                # Si le numéro d'étudiant est valide mais existe déjà dans la liste (on ne peut donc pas l'ajouter)
        if verifier_livre is False and liv.code_document != "":
            if liv.titre == "":
                self.lineEdit_titre.clear()
                self.label_erreur_livre_t_inv.setVisible(True)
            # Si le code de document est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
            if liv.code_document == "":
                self.lineEdit_code.clear()
                self.label_erreur_code_inv.setVisible(True)
            # si le nombre de rangée est invalide, afficher un message d'erreur
            if liv.Nb_de_rangee == "":
                self.lineEdit_nb_rangee.clear()
                self.label_erreur_nb_rangee.setVisible(True)
            # Si l'auteur  est invalide, effacer le lineEdit du code de document  et afficher un message d'erreur
            if liv.auteur == "":
                self.lineEdit_auteur.clear()
                self.label_erreur_auteur.setVisible(True)
            # Si la date de publication est invalide, afficher un message d'erreur
            if liv.annee_publication == "":
                self.lineEdit.clear()
                self.label_erreur_annee.setVisible(True)
            # si la maison d'édition est invalide, afficher un message d'erreur
            if liv.maison_edition == "":
                self.lineEdit_maison.clear()
                self.label_erreur_annee_2.setVisible(True)
