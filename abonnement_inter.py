# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abonnement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(822, 593)
        self.label_erreur_abonnement = QtWidgets.QLabel(Dialog)
        self.label_erreur_abonnement.setEnabled(True)
        self.label_erreur_abonnement.setGeometry(QtCore.QRect(500, 210, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_abonnement.setFont(font)
        self.label_erreur_abonnement.setObjectName("label_erreur_abonnement")
        self.pushButton_ajouter_ab = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_ab.setGeometry(QtCore.QRect(560, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_ab.setFont(font)
        self.pushButton_ajouter_ab.setObjectName("pushButton_ajouter_ab")
        self.lineEdit_nom = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nom.setGeometry(QtCore.QRect(20, 260, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nom.setFont(font)
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.label_erreur_code_inv_cour_tele = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv_cour_tele.setEnabled(True)
        self.label_erreur_code_inv_cour_tele.setGeometry(QtCore.QRect(500, 300, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_cour_tele.setFont(font)
        self.label_erreur_code_inv_cour_tele.setObjectName("label_erreur_code_inv_cour_tele")
        self.label_type_abonnement = QtWidgets.QLabel(Dialog)
        self.label_type_abonnement.setGeometry(QtCore.QRect(20, 110, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_type_abonnement.setFont(font)
        self.label_type_abonnement.setObjectName("label_type_abonnement")
        self.comboBox_type_abonnement = QtWidgets.QComboBox(Dialog)
        self.comboBox_type_abonnement.setGeometry(QtCore.QRect(20, 150, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_type_abonnement.setFont(font)
        self.comboBox_type_abonnement.setObjectName("comboBox_type_abonnement")
        self.comboBox_type_abonnement.addItem("")
        self.comboBox_type_abonnement.addItem("")
        self.comboBox_type_abonnement.addItem("")
        self.lbl_ajout_abonnement = QtWidgets.QLabel(Dialog)
        self.lbl_ajout_abonnement.setGeometry(QtCore.QRect(250, -10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ajout_abonnement.setFont(font)
        self.lbl_ajout_abonnement.setObjectName("lbl_ajout_abonnement")
        self.label_duree = QtWidgets.QLabel(Dialog)
        self.label_duree.setGeometry(QtCore.QRect(510, -10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_duree.setFont(font)
        self.label_duree.setObjectName("label_duree")
        self.label_erreur_code_inv_abonnement = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv_abonnement.setEnabled(True)
        self.label_erreur_code_inv_abonnement.setGeometry(QtCore.QRect(20, 90, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_abonnement.setFont(font)
        self.label_erreur_code_inv_abonnement.setObjectName("label_erreur_code_inv_abonnement")
        self.label_erreur_code_abonnement = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_abonnement.setGeometry(QtCore.QRect(20, 80, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_code_abonnement.setFont(font)
        self.label_erreur_code_abonnement.setObjectName("label_erreur_code_abonnement")
        self.label_date_abonnement = QtWidgets.QLabel(Dialog)
        self.label_date_abonnement.setGeometry(QtCore.QRect(500, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_date_abonnement.setFont(font)
        self.label_date_abonnement.setObjectName("label_date_abonnement")
        self.label_cour_tele = QtWidgets.QLabel(Dialog)
        self.label_cour_tele.setGeometry(QtCore.QRect(500, 230, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_cour_tele.setFont(font)
        self.label_cour_tele.setObjectName("label_cour_tele")
        self.label_erreur_code_inv_nom = QtWidgets.QLabel(Dialog)
        self.label_erreur_code_inv_nom.setEnabled(True)
        self.label_erreur_code_inv_nom.setGeometry(QtCore.QRect(20, 320, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_nom.setFont(font)
        self.label_erreur_code_inv_nom.setObjectName("label_erreur_code_inv_nom")
        self.pushButton_modifier_abonnement = QtWidgets.QPushButton(Dialog)
        self.pushButton_modifier_abonnement.setGeometry(QtCore.QRect(370, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier_abonnement.setFont(font)
        self.pushButton_modifier_abonnement.setObjectName("pushButton_modifier_abonnement")
        self.label_nom = QtWidgets.QLabel(Dialog)
        self.label_nom.setGeometry(QtCore.QRect(20, 230, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nom.setFont(font)
        self.label_nom.setObjectName("label_nom")
        self.label_code_abonnement = QtWidgets.QLabel(Dialog)
        self.label_code_abonnement.setGeometry(QtCore.QRect(20, 0, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code_abonnement.setFont(font)
        self.label_code_abonnement.setObjectName("label_code_abonnement")
        self.label_erreur_nom = QtWidgets.QLabel(Dialog)
        self.label_erreur_nom.setGeometry(QtCore.QRect(20, 310, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_nom.setFont(font)
        self.label_erreur_nom.setObjectName("label_erreur_nom")
        self.lineEdit_code_abonnement = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_code_abonnement.setGeometry(QtCore.QRect(20, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code_abonnement.setFont(font)
        self.lineEdit_code_abonnement.setObjectName("lineEdit_code_abonnement")
        self.pushButton_supprimer_abonnement = QtWidgets.QPushButton(Dialog)
        self.pushButton_supprimer_abonnement.setGeometry(QtCore.QRect(170, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer_abonnement.setFont(font)
        self.pushButton_supprimer_abonnement.setObjectName("pushButton_supprimer_abonnement")
        self.comboBox_duree = QtWidgets.QComboBox(Dialog)
        self.comboBox_duree.setGeometry(QtCore.QRect(510, 30, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_duree.setFont(font)
        self.comboBox_duree.setObjectName("comboBox_duree")
        self.comboBox_duree.addItem("")
        self.comboBox_duree.addItem("")
        self.comboBox_duree.addItem("")
        self.lineEdit_cour_tele = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_cour_tele.setGeometry(QtCore.QRect(500, 260, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_cour_tele.setFont(font)
        self.lineEdit_cour_tele.setObjectName("lineEdit_cour_tele")
        self.pushButton_quitter_abonner = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_abonner.setGeometry(QtCore.QRect(690, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_abonner.setFont(font)
        self.pushButton_quitter_abonner.setObjectName("pushButton_quitter_abonner")
        self.lineEdit_annee_abo = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_annee_abo.setGeometry(QtCore.QRect(490, 150, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_annee_abo.setFont(font)
        self.lineEdit_annee_abo.setObjectName("lineEdit_annee_abo")
        self.textBrowser_abonner = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_abonner.setGeometry(QtCore.QRect(220, 390, 441, 161))
        self.textBrowser_abonner.setObjectName("textBrowser_abonner")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_erreur_abonnement.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">annee invalide.</span></p></body></html>"))
        self.pushButton_ajouter_ab.setText(_translate("Dialog", "Ajouter"))
        self.label_erreur_code_inv_cour_tele.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le courriel ou num??ro de t??l??phone est invalide.</span></p></body></html>"))
        self.label_type_abonnement.setText(_translate("Dialog", "Type d\'abonnement"))
        self.comboBox_type_abonnement.setItemText(0, _translate("Dialog", "standard"))
        self.comboBox_type_abonnement.setItemText(1, _translate("Dialog", "premium"))
        self.comboBox_type_abonnement.setItemText(2, _translate("Dialog", "deluxe"))
        self.lbl_ajout_abonnement.setText(_translate("Dialog", "Abonnement"))
        self.label_duree.setText(_translate("Dialog", "Dur??e"))
        self.label_erreur_code_inv_abonnement.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code d\'abonnement est invalide.</span></p></body></html>"))
        self.label_erreur_code_abonnement.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le code d\'abonnement existe d??j??.</span></p></body></html>"))
        self.label_date_abonnement.setText(_translate("Dialog", "Ann??e d\'abonnement"))
        self.label_cour_tele.setText(_translate("Dialog", "Courriel ou t??l??phone"))
        self.label_erreur_code_inv_nom.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le nom est invalide.</span></p></body></html>"))
        self.pushButton_modifier_abonnement.setText(_translate("Dialog", "modifier"))
        self.label_nom.setText(_translate("Dialog", "Nom"))
        self.label_code_abonnement.setText(_translate("Dialog", "code d\'abonnement"))
        self.label_erreur_nom.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">le nom existe d??j??</span></p><p><span style=\" color:#ff0000;\"><br/></span></p></body></html>"))
        self.pushButton_supprimer_abonnement.setText(_translate("Dialog", "Suprimmer"))
        self.comboBox_duree.setItemText(0, _translate("Dialog", "1 an"))
        self.comboBox_duree.setItemText(1, _translate("Dialog", "2 ans"))
        self.comboBox_duree.setItemText(2, _translate("Dialog", "4 ans"))
        self.pushButton_quitter_abonner.setText(_translate("Dialog", "Quitter"))
