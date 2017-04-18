import sys
from PyQt4 import QtGui

import constant


class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.light = False
        self.build_ui()
        """self.light = False
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("Main page")

        self.pic = QtGui.QLabel(self)
        self.l1 = QtGui.QLabel(self)
        self.l1.setText("Status")
        self.pic.setGeometry(100, 100, 100, 100)
        self.l1.setGeometry(100, 300, 100, 100)
        # use full ABSOLUTE path to the image, not relative
        self.pic.setPixmap(QtGui.QPixmap(constant.IMG_DIR + "off-m.png"))

        button = QtGui.QPushButton("Button", self)
        button.setGeometry(200, 200, 80, 20)
        button.clicked.connect(self.switch_light)
        self.show()"""

    def build_ui(self):
        self.pic = QtGui.QLabel(self)
        self.pic.setPixmap(QtGui.QPixmap(constant.IMG_DIR + "off-m.png"))
        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(self.switch_light)
        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.pic, 1, 0)

        hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(grid)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Ark VPN')
        self.show()


    # Turns the light on and off
    def switch_light(self):
        if self.light:
            self.pic.setPixmap(QtGui.QPixmap(constant.IMG_DIR + "off-m.png"))
        else:
            self.pic.setPixmap(QtGui.QPixmap(constant.IMG_DIR + "green-m.png"))

        self.light = not self.light


class Simple(QtGui.QWidget):

    def __init__(self):
        super(Simple, self).__init__()
        self.setGeometry(300, 250, 250, 150)
        self.setWindowTitle("Simple Widget")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())