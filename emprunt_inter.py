# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emprunt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_emprunt(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(885, 586)
        self.lineEdit_code_document_emprunt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_code_document_emprunt.setGeometry(QtCore.QRect(40, 190, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code_document_emprunt.setFont(font)
        self.lineEdit_code_document_emprunt.setObjectName("lineEdit_code_document_emprunt")
        self.listView_document = QtWidgets.QListView(Dialog)
        self.listView_document.setGeometry(QtCore.QRect(290, 380, 221, 171))
        self.listView_document.setObjectName("listView_document")
        self.label_erreur_code_inv_document_emprunt = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv_document_emprunt.setEnabled(True)
        self.label_erreur_code_inv_document_emprunt.setGeometry(QtCore.QRect(40, 230, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_document_emprunt.setFont(font)
        self.label_erreur_code_inv_document_emprunt.setObjectName("label_erreur_code_inv_document_emprunt")
        self.label_date_emprunt = QtWidgets.QLabel(Dialog)
        self.label_date_emprunt.setGeometry(QtCore.QRect(500, 160, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_date_emprunt.setFont(font)
        self.label_date_emprunt.setObjectName("label_date_emprunt")
        self.listView_abonnement = QtWidgets.QListView(Dialog)
        self.listView_abonnement.setGeometry(QtCore.QRect(60, 380, 221, 171))
        self.listView_abonnement.setObjectName("listView_abonnement")
        self.lineEdit_code_emprunt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_code_emprunt.setGeometry(QtCore.QRect(40, 60, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code_emprunt.setFont(font)
        self.lineEdit_code_emprunt.setObjectName("lineEdit_code_emprunt")
        self.Date_emprunt = QtWidgets.QDateEdit(Dialog)
        self.Date_emprunt.setGeometry(QtCore.QRect(500, 190, 301, 81))
        self.Date_emprunt.setObjectName("Date_emprunt")
        self.label_erreur_code_emprunt = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_emprunt.setGeometry(QtCore.QRect(40, 110, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_code_emprunt.setFont(font)
        self.label_erreur_code_emprunt.setObjectName("label_erreur_code_emprunt")
        self.label_code_emprunt = QtWidgets.QLabel(Dialog)
        self.label_code_emprunt.setGeometry(QtCore.QRect(40, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code_emprunt.setFont(font)
        self.label_code_emprunt.setObjectName("label_code_emprunt")
        self.lineEdit_code_abonnement_emprunt = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_code_abonnement_emprunt.setGeometry(QtCore.QRect(470, 60, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code_abonnement_emprunt.setFont(font)
        self.lineEdit_code_abonnement_emprunt.setObjectName("lineEdit_code_abonnement_emprunt")
        self.listView_emprunt = QtWidgets.QListView(Dialog)
        self.listView_emprunt.setGeometry(QtCore.QRect(520, 380, 221, 171))
        self.listView_emprunt.setObjectName("listView_emprunt")
        self.pushButton_quitter_emprunt = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_emprunt.setGeometry(QtCore.QRect(740, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_emprunt.setFont(font)
        self.pushButton_quitter_emprunt.setObjectName("pushButton_quitter_emprunt")
        self.label_code_abonnement_emprunt = QtWidgets.QLabel(Dialog)
        self.label_code_abonnement_emprunt.setGeometry(QtCore.QRect(470, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code_abonnement_emprunt.setFont(font)
        self.label_code_abonnement_emprunt.setObjectName("label_code_abonnement_emprunt")
        self.label_erreur_code_inv_emprunt = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv_emprunt.setEnabled(True)
        self.label_erreur_code_inv_emprunt.setGeometry(QtCore.QRect(40, 120, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_emprunt.setFont(font)
        self.label_erreur_code_inv_emprunt.setObjectName("label_erreur_code_inv_emprunt")
        self.pushButton_supprimer_emprunt = QtWidgets.QPushButton(Dialog)
        self.pushButton_supprimer_emprunt.setGeometry(QtCore.QRect(120, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer_emprunt.setFont(font)
        self.pushButton_supprimer_emprunt.setObjectName("pushButton_supprimer_emprunt")
        self.label_erreur_emprunt = QtWidgets.QLabel(Dialog)
        self.label_erreur_emprunt.setEnabled(True)
        self.label_erreur_emprunt.setGeometry(QtCore.QRect(510, 270, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_emprunt.setFont(font)
        self.label_erreur_emprunt.setObjectName("label_erreur_emprunt")
        self.label_erreur_code_inv_abonnement_emprunt = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv_abonnement_emprunt.setEnabled(True)
        self.label_erreur_code_inv_abonnement_emprunt.setGeometry(QtCore.QRect(470, 110, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_abonnement_emprunt.setFont(font)
        self.label_erreur_code_inv_abonnement_emprunt.setObjectName("label_erreur_code_inv_abonnement_emprunt")
        self.pushButton_ajouter_em = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_em.setGeometry(QtCore.QRect(510, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_em.setFont(font)
        self.pushButton_ajouter_em.setObjectName("pushButton_ajouter_em")
        self.pushButton_modifier_emprunt = QtWidgets.QPushButton(Dialog)
        self.pushButton_modifier_emprunt.setGeometry(QtCore.QRect(320, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier_emprunt.setFont(font)
        self.pushButton_modifier_emprunt.setObjectName("pushButton_modifier_emprunt")
        self.lbl_ajout_emprunt = QtWidgets.QLabel(Dialog)
        self.lbl_ajout_emprunt.setGeometry(QtCore.QRect(320, -10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ajout_emprunt.setFont(font)
        self.lbl_ajout_emprunt.setObjectName("lbl_ajout_emprunt")
        self.label_code_document_emprunt = QtWidgets.QLabel(Dialog)
        self.label_code_document_emprunt.setGeometry(QtCore.QRect(40, 160, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code_document_emprunt.setFont(font)
        self.label_code_document_emprunt.setObjectName("label_code_document_emprunt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_erreur_code_inv_document_emprunt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code de document est invalide.</span></p></body></html>"))
        self.label_date_emprunt.setText(_translate("Dialog", "Date d\'emprunt"))
        self.label_erreur_code_emprunt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le code d\'emprunt existe déjà.</span></p></body></html>"))
        self.label_code_emprunt.setText(_translate("Dialog", "code d\'emprunt"))
        self.pushButton_quitter_emprunt.setText(_translate("Dialog", "Quitter"))
        self.label_code_abonnement_emprunt.setText(_translate("Dialog", "code abonnement"))
        self.label_erreur_code_inv_emprunt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code d\'emprunt est invalide.</span></p></body></html>"))
        self.pushButton_supprimer_emprunt.setText(_translate("Dialog", "supprimer"))
        self.label_erreur_emprunt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">annee invalide.</span></p></body></html>"))
        self.label_erreur_code_inv_abonnement_emprunt.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code d\'abonnement est invalide.</span></p></body></html>"))
        self.pushButton_ajouter_em.setText(_translate("Dialog", "Ajouter"))
        self.pushButton_modifier_emprunt.setText(_translate("Dialog", "modifier"))
        self.lbl_ajout_emprunt.setText(_translate("Dialog", "Emprunt"))
        self.label_code_document_emprunt.setText(_translate("Dialog", "code document"))
