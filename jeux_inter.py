# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jeux.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jeux(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(818, 584)
        self.lineEdit_nb_rangee_jeux = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nb_rangee_jeux.setGeometry(QtCore.QRect(10, 180, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nb_rangee_jeux.setFont(font)
        self.lineEdit_nb_rangee_jeux.setObjectName("lineEdit_nb_rangee_jeux")
        self.comboBox_jeu = QtWidgets.QComboBox(Dialog)
        self.comboBox_jeu.setGeometry(QtCore.QRect(480, 230, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_jeu.setFont(font)
        self.comboBox_jeu.setObjectName("comboBox_jeu")
        self.comboBox_jeu.addItem("")
        self.comboBox_jeu.addItem("")
        self.comboBox_jeu.addItem("")
        self.pushButton_ajouter_j = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_j.setGeometry(QtCore.QRect(140, 340, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_j.setFont(font)
        self.pushButton_ajouter_j.setObjectName("pushButton_ajouter_j")
        self.pushButton_modifier_jeux_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_modifier_jeux_2.setGeometry(QtCore.QRect(320, 340, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier_jeux_2.setFont(font)
        self.pushButton_modifier_jeux_2.setObjectName("pushButton_modifier_jeux_2")
        self.lineEdit_nb_joueur = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nb_joueur.setGeometry(QtCore.QRect(480, 130, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nb_joueur.setFont(font)
        self.lineEdit_nb_joueur.setObjectName("lineEdit_nb_joueur")
        self.lbl_ajout_jeu = QtWidgets.QLabel(Dialog)
        self.lbl_ajout_jeu.setGeometry(QtCore.QRect(230, 0, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ajout_jeu.setFont(font)
        self.lbl_ajout_jeu.setObjectName("lbl_ajout_jeu")
        self.label_erreur_nb_joueur = QtWidgets.QLabel(Dialog)
        self.label_erreur_nb_joueur.setEnabled(True)
        self.label_erreur_nb_joueur.setGeometry(QtCore.QRect(480, 180, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nb_joueur.setFont(font)
        self.label_erreur_nb_joueur.setObjectName("label_erreur_nb_joueur")
        self.label_erreur_nb_rangee_jeux = QtWidgets.QLabel(Dialog)
        self.label_erreur_nb_rangee_jeux.setEnabled(True)
        self.label_erreur_nb_rangee_jeux.setGeometry(QtCore.QRect(20, 230, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nb_rangee_jeux.setFont(font)
        self.label_erreur_nb_rangee_jeux.setObjectName("label_erreur_nb_rangee_jeux")
        self.label_nb_rangee_jeux = QtWidgets.QLabel(Dialog)
        self.label_nb_rangee_jeux.setGeometry(QtCore.QRect(10, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nb_rangee_jeux.setFont(font)
        self.label_nb_rangee_jeux.setObjectName("label_nb_rangee_jeux")
        self.lineEdit_createur = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_createur.setGeometry(QtCore.QRect(480, 40, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_createur.setFont(font)
        self.lineEdit_createur.setObjectName("lineEdit_createur")
        self.pushButton_supprimer_jeux = QtWidgets.QPushButton(Dialog)
        self.pushButton_supprimer_jeux.setGeometry(QtCore.QRect(500, 340, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer_jeux.setFont(font)
        self.pushButton_supprimer_jeux.setObjectName("pushButton_supprimer_jeux")
        self.label_erreur_code_jeux = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_jeux.setGeometry(QtCore.QRect(10, 120, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_code_jeux.setFont(font)
        self.label_erreur_code_jeux.setObjectName("label_erreur_code_jeux")
        self.label_titre_jeux = QtWidgets.QLabel(Dialog)
        self.label_titre_jeux.setGeometry(QtCore.QRect(20, 250, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_titre_jeux.setFont(font)
        self.label_titre_jeux.setObjectName("label_titre_jeux")
        self.label_createur = QtWidgets.QLabel(Dialog)
        self.label_createur.setGeometry(QtCore.QRect(480, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_createur.setFont(font)
        self.label_createur.setObjectName("label_createur")
        self.label_code_jeux = QtWidgets.QLabel(Dialog)
        self.label_code_jeux.setGeometry(QtCore.QRect(10, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code_jeux.setFont(font)
        self.label_code_jeux.setObjectName("label_code_jeux")
        self.label_erreur_createur = QtWidgets.QLabel(Dialog)
        self.label_erreur_createur.setEnabled(True)
        self.label_erreur_createur.setGeometry(QtCore.QRect(480, 80, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_createur.setFont(font)
        self.label_erreur_createur.setObjectName("label_erreur_createur")
        self.lineEdit_jeux = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_jeux.setGeometry(QtCore.QRect(20, 280, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_jeux.setFont(font)
        self.lineEdit_jeux.setObjectName("lineEdit_jeux")
        self.pushButton_quitter_jeux = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_jeux.setGeometry(QtCore.QRect(680, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_jeux.setFont(font)
        self.pushButton_quitter_jeux.setObjectName("pushButton_quitter_jeux")
        self.label_erreur_code_inv_jeux = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv_jeux.setEnabled(True)
        self.label_erreur_code_inv_jeux.setGeometry(QtCore.QRect(10, 130, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_jeux.setFont(font)
        self.label_erreur_code_inv_jeux.setObjectName("label_erreur_code_inv_jeux")
        self.lineEdit_code_jeux = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_code_jeux.setGeometry(QtCore.QRect(10, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code_jeux.setFont(font)
        self.lineEdit_code_jeux.setObjectName("lineEdit_code_jeux")
        self.label_type_jeu = QtWidgets.QLabel(Dialog)
        self.label_type_jeu.setGeometry(QtCore.QRect(480, 200, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_type_jeu.setFont(font)
        self.label_type_jeu.setObjectName("label_type_jeu")
        self.label_nb_joueur = QtWidgets.QLabel(Dialog)
        self.label_nb_joueur.setGeometry(QtCore.QRect(480, 100, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nb_joueur.setFont(font)
        self.label_nb_joueur.setObjectName("label_nb_joueur")
        self.textBrowser_jeux = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_jeux.setGeometry(QtCore.QRect(200, 400, 441, 161))
        self.textBrowser_jeux.setObjectName("textBrowser_jeux")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox_jeu.setItemText(0, _translate("Dialog", "Jeu de cartes"))
        self.comboBox_jeu.setItemText(1, _translate("Dialog", "Jeu vidéo"))
        self.comboBox_jeu.setItemText(2, _translate("Dialog", "jeu de table"))
        self.pushButton_ajouter_j.setText(_translate("Dialog", "Ajouter"))
        self.pushButton_modifier_jeux_2.setText(_translate("Dialog", "modifier"))
        self.lbl_ajout_jeu.setText(_translate("Dialog", "Ajout de jeux"))
        self.label_erreur_nb_joueur.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">nombre de joueur invalide.</span></p></body></html>"))
        self.label_erreur_nb_rangee_jeux.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le numéro de rangée est invalide.</span></p></body></html>"))
        self.label_nb_rangee_jeux.setText(_translate("Dialog", "nombre de rangée"))
        self.pushButton_supprimer_jeux.setText(_translate("Dialog", "supprimer"))
        self.label_erreur_code_jeux.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le code de jeux existe déjà.</span></p></body></html>"))
        self.label_titre_jeux.setText(_translate("Dialog", "Titre du jeux"))
        self.label_createur.setText(_translate("Dialog", "créateur"))
        self.label_code_jeux.setText(_translate("Dialog", "code de jeux"))
        self.label_erreur_createur.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">créateur invalide.</span></p></body></html>"))
        self.pushButton_quitter_jeux.setText(_translate("Dialog", "Quitter"))
        self.label_erreur_code_inv_jeux.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code de jeux est invalide.</span></p></body></html>"))
        self.label_type_jeu.setText(_translate("Dialog", "type de jeu"))
        self.label_nb_joueur.setText(_translate("Dialog", "nombre de joueur"))
