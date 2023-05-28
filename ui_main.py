# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrtNSBF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 294)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.styleSheet = QFrame(self.centralwidget)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"")
        self.styleSheet.setFrameShape(QFrame.StyledPanel)
        self.styleSheet.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.frame = QFrame(self.styleSheet)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_search = QLineEdit(self.frame)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_search.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_search)

        self.pushButton_search = QPushButton(self.frame)
        self.pushButton_search.setObjectName(u"pushButton_search")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_search.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_search)


        self.verticalLayout.addWidget(self.frame)

        self.frame_info = QFrame(self.styleSheet)
        self.frame_info.setObjectName(u"frame_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_info.sizePolicy().hasHeightForWidth())
        self.frame_info.setSizePolicy(sizePolicy1)
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_info)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_info)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_nam_patient = QLabel(self.frame_2)
        self.label_nam_patient.setObjectName(u"label_nam_patient")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_nam_patient.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_nam_patient, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.frame_info)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"*{\n"
"	font: 12pt \"Segoe UI\";\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_maBN = QLabel(self.frame_4)
        self.label_maBN.setObjectName(u"label_maBN")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_maBN.sizePolicy().hasHeightForWidth())
        self.label_maBN.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_maBN.setFont(font3)
        self.label_maBN.setStyleSheet(u"#label_maBN {\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}")

        self.gridLayout.addWidget(self.label_maBN, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_sex = QLabel(self.frame_4)
        self.label_sex.setObjectName(u"label_sex")

        self.gridLayout.addWidget(self.label_sex, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_loai_vien_phi = QLabel(self.frame_4)
        self.label_loai_vien_phi.setObjectName(u"label_loai_vien_phi")

        self.gridLayout.addWidget(self.label_loai_vien_phi, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_quyen_loi = QLabel(self.frame_4)
        self.label_quyen_loi.setObjectName(u"label_quyen_loi")

        self.gridLayout.addWidget(self.label_quyen_loi, 3, 1, 1, 1)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_phonghientai = QLabel(self.frame_4)
        self.label_phonghientai.setObjectName(u"label_phonghientai")

        self.gridLayout.addWidget(self.label_phonghientai, 4, 1, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout)


        self.horizontalLayout_4.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_namsinh = QLabel(self.frame_5)
        self.label_namsinh.setObjectName(u"label_namsinh")
        sizePolicy3.setHeightForWidth(self.label_namsinh.sizePolicy().hasHeightForWidth())
        self.label_namsinh.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_namsinh, 0, 1, 1, 1)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_dia_chi = QLabel(self.frame_5)
        self.label_dia_chi.setObjectName(u"label_dia_chi")

        self.gridLayout_2.addWidget(self.label_dia_chi, 1, 1, 1, 1)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_sothe = QLabel(self.frame_5)
        self.label_sothe.setObjectName(u"label_sothe")

        self.gridLayout_2.addWidget(self.label_sothe, 2, 1, 1, 1)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_han_the = QLabel(self.frame_5)
        self.label_han_the.setObjectName(u"label_han_the")

        self.gridLayout_2.addWidget(self.label_han_the, 3, 1, 1, 1)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 1)

        self.label_ngay_vao_vien = QLabel(self.frame_5)
        self.label_ngay_vao_vien.setObjectName(u"label_ngay_vao_vien")

        self.gridLayout_2.addWidget(self.label_ngay_vao_vien, 4, 1, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_2)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_info)

        self.frame_xet_nghiem = QFrame(self.styleSheet)
        self.frame_xet_nghiem.setObjectName(u"frame_xet_nghiem")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_xet_nghiem.sizePolicy().hasHeightForWidth())
        self.frame_xet_nghiem.setSizePolicy(sizePolicy4)
        self.frame_xet_nghiem.setFrameShape(QFrame.StyledPanel)
        self.frame_xet_nghiem.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_xet_nghiem)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_search_2 = QLineEdit(self.frame_xet_nghiem)
        self.lineEdit_search_2.setObjectName(u"lineEdit_search_2")
        self.lineEdit_search_2.setFont(font)

        self.horizontalLayout_7.addWidget(self.lineEdit_search_2)

        self.pushButton_search_2 = QPushButton(self.frame_xet_nghiem)
        self.pushButton_search_2.setObjectName(u"pushButton_search_2")
        self.pushButton_search_2.setFont(font1)

        self.horizontalLayout_7.addWidget(self.pushButton_search_2)


        self.verticalLayout.addWidget(self.frame_xet_nghiem)

        self.frame_6 = QFrame(self.styleSheet)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"#label_2 {\n"
"	font: italic 8pt \"Segoe UI\";\n"
"	color: rgb(255, 0, 0);\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.styleSheet)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm theo m\u00e3 b\u1ec7nh nh\u00e2n", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm", None))
        self.label_nam_patient.setText(QCoreApplication.translate("MainWindow", u"T\u00ean b\u1ec7nh nh\u00e2n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 BN:", None))
        self.label_maBN.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.label_sex.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i vi\u1ec7n ph\u00ed:", None))
        self.label_loai_vien_phi.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Quy\u1ec1n l\u1ee3i:", None))
        self.label_quyen_loi.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ph\u00f2ng hi\u1ec7n t\u1ea1i:     ", None))
        self.label_phonghientai.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"N\u0103m sinh:", None))
        self.label_namsinh.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9:", None))
        self.label_dia_chi.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 th\u1ebb:", None))
        self.label_sothe.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"H\u1ea1n th\u1ebb:", None))
        self.label_han_the.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y v\u00e0o vi\u1ec7n:     ", None))
        self.label_ngay_vao_vien.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lineEdit_search_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm x\u00e9t nghi\u1ec7m", None))
        self.pushButton_search_2.setText(QCoreApplication.translate("MainWindow", u"Xem bi\u1ec3u \u0111\u1ed3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Created by Bs \u0110inh V\u0103n Vinh", None))
    # retranslateUi

