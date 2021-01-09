# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JM1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import JM1
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from model import GoogLeNet
from PIL import Image
import numpy as np
import json
import matplotlib.pyplot as plt

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(876, 520)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predict)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 171, 191))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 149, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openimage)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(600, 220, 271, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 256, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 70, 401, 331))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 351, 291))
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(610, 20, 261, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 241, 131))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 270, 171, 131))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 50, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "开始识别"))
        self.groupBox.setTitle(_translate("Dialog", "功能区"))
        self.radioButton_2.setText(_translate("Dialog", "本地图片识别"))
        self.radioButton.setText(_translate("Dialog", "实时获取图片识别"))
        self.pushButton_3.setText(_translate("Dialog", "打开图片"))
        self.groupBox_2.setTitle(_translate("Dialog", "结果区"))
        self.groupBox_3.setTitle(_translate("Dialog", "显示区"))
        self.groupBox_4.setTitle(_translate("Dialog", "提示区"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.本次识别暂时仅限于五类花朵：雏菊、玫瑰、蒲公英、郁金香、向日葵。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.识别结果输出为相似结果最高的类别，存在一定误差。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.输入图片后请耐心等待适当时间以得到预测结果。</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "基于卷积神经网络的花朵分类识别系统"))
        self.groupBox_5.setTitle(_translate("Dialog", "帮助与建议"))
        self.pushButton_2.setText(_translate("Dialog", "错误反馈"))

    def openimage(self):
        global fname
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'E:\\deep-learning-for-image-processing-master\\tensorflow_classification\\', 'Image files(*.jpg *.gif *.png)')
        jpg = QtGui.QPixmap(fname).scaled(self.label.width(), self.label.height())
        print(fname)
        self.label.setPixmap(jpg)

        #self.Label1.setPixmap(QPixmap(fname))
        #print(imgName,imgType)
    def predict(self):
        im_height = 224
        im_width = 224

        # load image
        img = Image.open(fname)
        # resize image to 224x224
        img = img.resize((im_width, im_height))
        plt.imshow(img)

        # scaling pixel value and normalize
        img = ((np.array(img) / 255.) - 0.5) / 0.5

        # Add the image to a batch where it's the only member.
        img = (np.expand_dims(img, 0))

        # read class_indict
        try:
            json_file = open('./class_indices.json', 'r')
            class_indict = json.load(json_file)
        except Exception as e:
            print(e)
            exit(-1)

        model = GoogLeNet(class_num=5, aux_logits=False)
        model.summary()
        model.load_weights("./save_weights/myGoogLenet.h5", by_name=True)  # h5 format
        # model.load_weights("./save_weights/myGoogLeNet.ckpt")  # ckpt format
        result = model.predict(img)
        predict_class = np.argmax(result)
        print(class_indict[str(predict_class)])
        result1 = class_indict[str(predict_class)]
        self.textBrowser.setPlainText(result1)
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Widget = QMainWindow()
    ui = JM1.Ui_Dialog()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
