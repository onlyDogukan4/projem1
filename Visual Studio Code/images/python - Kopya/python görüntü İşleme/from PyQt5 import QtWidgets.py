import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    app=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()

    pencere.setWindowTitle("pyQt5 Ders 1")

    



    figo=QtWidgets.QPushButton("figen")
    bilo=QtWidgets.QPushButton("bülent")
    düzen=QtWidgets.QHBoxLayout()
    düzen.addWidget(bilo)
    düzen.addWidget(figo)
    pencere.setLayout(düzen)


    etiket3=QtWidgets.QLabel(pencere)
    etiket3.setPixmap(QtGui.QPixmap("4oz.png"))
    etiket3.move(150,250)
    etiket4=QtWidgets.QLabel(pencere)
    etiket4.setText("hereeeee")
    etiket4.move(250,200)
    buton3=QtWidgets.QPushButton(pencere)
    buton3.setText("tamam")
    buton3.move(180,300)


    okay=QtWidgets.QPushButton("tamam")
    cancel=QtWidgets.QPushButton("İptal")
    h_box=QtWidgets.QHBoxLayout()
    



    pencere.setGeometry(450,300,500,500)
    pencere.show()

    sys.exit(app.exec_())
    
Pencere()

