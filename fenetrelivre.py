# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import livre_inter


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrelivre(QtWidgets.QDialog, livre_inter.Ui_livre):
    def __init__(self, parent=None):
        super(Fenetrelivre, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des livres")


    @pyqtSlot()
    def on_pushButton_quitter_livre_clicked(self):
        self.close()