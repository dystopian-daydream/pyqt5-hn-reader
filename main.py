import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from tabs import TabsWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initialize_window_geometry()

        self.initialize_window_title()

        self.initialize_table_widget()

        self.show()

    def initialize_window_geometry(self):
        self.initial_dimensions = dict(left=0, right=0, width=1100, height=850)
        self.setGeometry(*self.initial_dimensions.values())

    def initialize_window_title(self):
        self.title = 'PyQT5 Experiment'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('./assets/icon.png'))

    def initialize_table_widget(self):
        self.tabs_widget = TabsWidget(self)
        self.setCentralWidget(self.tabs_widget)

def initialize_style(app):
    app.setStyle("Fusion")

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)

    app.setPalette(dark_palette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    trayIcon = QSystemTrayIcon(QIcon("./assets/icon.png"), app) 
    trayIcon.show()

    initialize_style(app)
    ex = App()
    sys.exit(app.exec_())