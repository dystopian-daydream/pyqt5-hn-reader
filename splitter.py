import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        topleft = QFrame()
        #topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        #bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(textedit)
        splitter1.browser = QWebEngineView()
        splitter1.browser.load(QUrl("https://www.google.com"))
        splitter1.addWidget(splitter1.browser)
        splitter1.setSizes([100,200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setSizes([600,200])

        hbox.addWidget(splitter2)
		
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
		
        self.initial_dimensions = dict(left=0, right=0, width=1100, height=850)
        self.setGeometry(*self.initial_dimensions.values())
        self.setWindowTitle('QSplitter demo')
        self.show()
		
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()