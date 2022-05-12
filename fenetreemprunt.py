# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import emprunt_inter


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreemprunt(QtWidgets.QDialog, emprunt_inter.Ui_emprunt):
    def __init__(self, parent=None):
        super(Fenetreemprunt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des emprunts")


    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()

