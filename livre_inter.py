# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'livre.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(785, 573)
        self.label_maison = QtWidgets.QLabel(Dialog)
        self.label_maison.setGeometry(QtCore.QRect(480, 240, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_maison.setFont(font)
        self.label_maison.setObjectName("label_maison")
        self.lineEdit_auteur = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_auteur.setGeometry(QtCore.QRect(470, 40, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_auteur.setFont(font)
        self.lineEdit_auteur.setObjectName("lineEdit_auteur")
        self.lbl_ajout_livre = QtWidgets.QLabel(Dialog)
        self.lbl_ajout_livre.setGeometry(QtCore.QRect(220, 0, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ajout_livre.setFont(font)
        self.lbl_ajout_livre.setObjectName("lbl_ajout_livre")
        self.label_erreur_annee = QtWidgets.QLabel(Dialog)
        self.label_erreur_annee.setEnabled(True)
        self.label_erreur_annee.setGeometry(QtCore.QRect(480, 220, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_annee.setFont(font)
        self.label_erreur_annee.setObjectName("label_erreur_annee")
        self.label_erreur_nb_rangee = QtWidgets.QLabel(Dialog)
        self.label_erreur_nb_rangee.setEnabled(True)
        self.label_erreur_nb_rangee.setGeometry(QtCore.QRect(10, 230, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nb_rangee.setFont(font)
        self.label_erreur_nb_rangee.setObjectName("label_erreur_nb_rangee")
        self.lineEdit_code = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_code.setGeometry(QtCore.QRect(10, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code.setFont(font)
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.pushButton_ajouter_l = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_l.setGeometry(QtCore.QRect(130, 340, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_l.setFont(font)
        self.pushButton_ajouter_l.setObjectName("pushButton_ajouter_l")
        self.lineEdit_maison = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_maison.setGeometry(QtCore.QRect(480, 270, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_maison.setFont(font)
        self.lineEdit_maison.setObjectName("lineEdit_maison")
        self.lineEdit_nb_rangee = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nb_rangee.setGeometry(QtCore.QRect(0, 180, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nb_rangee.setFont(font)
        self.lineEdit_nb_rangee.setObjectName("lineEdit_nb_rangee")
        self.label_code = QtWidgets.QLabel(Dialog)
        self.label_code.setGeometry(QtCore.QRect(10, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code.setFont(font)
        self.label_code.setObjectName("label_code")
        self.label_erreur_code_inv = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv.setEnabled(True)
        self.label_erreur_code_inv.setGeometry(QtCore.QRect(10, 130, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv.setFont(font)
        self.label_erreur_code_inv.setObjectName("label_erreur_code_inv")
        self.Date_publi = QtWidgets.QDateEdit(Dialog)
        self.Date_publi.setGeometry(QtCore.QRect(470, 140, 301, 81))
        self.Date_publi.setObjectName("Date_publi")
        self.label_auteur = QtWidgets.QLabel(Dialog)
        self.label_auteur.setGeometry(QtCore.QRect(470, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_auteur.setFont(font)
        self.label_auteur.setObjectName("label_auteur")
        self.label_nbrangee = QtWidgets.QLabel(Dialog)
        self.label_nbrangee.setGeometry(QtCore.QRect(0, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nbrangee.setFont(font)
        self.label_nbrangee.setObjectName("label_nbrangee")
        self.label_erreur_code = QtWidgets.QLabel(Dialog)
        self.label_erreur_code.setGeometry(QtCore.QRect(10, 120, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_code.setFont(font)
        self.label_erreur_code.setObjectName("label_erreur_code")
        self.lineEdit_titre = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_titre.setGeometry(QtCore.QRect(10, 280, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_titre.setFont(font)
        self.lineEdit_titre.setObjectName("lineEdit_titre")
        self.pushButton_modifier_livre = QtWidgets.QPushButton(Dialog)
        self.pushButton_modifier_livre.setGeometry(QtCore.QRect(310, 340, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier_livre.setFont(font)
        self.pushButton_modifier_livre.setObjectName("pushButton_modifier_livre")
        self.pushButton_quitter_livre = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_livre.setGeometry(QtCore.QRect(670, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_livre.setFont(font)
        self.pushButton_quitter_livre.setObjectName("pushButton_quitter_livre")
        self.label_titre_livre = QtWidgets.QLabel(Dialog)
        self.label_titre_livre.setGeometry(QtCore.QRect(10, 250, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_titre_livre.setFont(font)
        self.label_titre_livre.setObjectName("label_titre_livre")
        self.pushButton_supprimer_livre = QtWidgets.QPushButton(Dialog)
        self.pushButton_supprimer_livre.setGeometry(QtCore.QRect(490, 340, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer_livre.setFont(font)
        self.pushButton_supprimer_livre.setObjectName("pushButton_supprimer_livre")
        self.label_annee_publi = QtWidgets.QLabel(Dialog)
        self.label_annee_publi.setGeometry(QtCore.QRect(470, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_annee_publi.setFont(font)
        self.label_annee_publi.setObjectName("label_annee_publi")
        self.listView_livre = QtWidgets.QListView(Dialog)
        self.listView_livre.setGeometry(QtCore.QRect(190, 400, 451, 161))
        self.listView_livre.setObjectName("listView_livre")
        self.label_erreur_auteur = QtWidgets.QLabel(Dialog)
        self.label_erreur_auteur.setEnabled(True)
        self.label_erreur_auteur.setGeometry(QtCore.QRect(470, 90, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_auteur.setFont(font)
        self.label_erreur_auteur.setObjectName("label_erreur_auteur")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_maison.setText(_translate("Dialog", "Maison d\'édition"))
        self.lbl_ajout_livre.setText(_translate("Dialog", "Ajout de livre"))
        self.label_erreur_annee.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">annee invalide.</span></p></body></html>"))
        self.label_erreur_nb_rangee.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le numéro de rangée est invalide.</span></p></body></html>"))
        self.pushButton_ajouter_l.setText(_translate("Dialog", "Ajouter"))
        self.label_code.setText(_translate("Dialog", "code de livre"))
        self.label_erreur_code_inv.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code de livre est invalide.</span></p></body></html>"))
        self.label_auteur.setText(_translate("Dialog", "Auteur"))
        self.label_nbrangee.setText(_translate("Dialog", "nombre de rangée"))
        self.label_erreur_code.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le code de livre existe déjà.</span></p></body></html>"))
        self.pushButton_modifier_livre.setText(_translate("Dialog", "modifier"))
        self.pushButton_quitter_livre.setText(_translate("Dialog", "Quitter"))
        self.label_titre_livre.setText(_translate("Dialog", "Titre du livre"))
        self.pushButton_supprimer_livre.setText(_translate("Dialog", "supprimer"))
        self.label_annee_publi.setText(_translate("Dialog", "Année publication"))
        self.label_erreur_auteur.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Auteur invalide.</span></p></body></html>"))