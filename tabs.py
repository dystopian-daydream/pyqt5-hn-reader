from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

import hn

class TabsWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QHBoxLayout(self)

        self.initialize_tab_screen()

        self.add_tabs_to_screen()

        self.add_tabs_to_widget()

        self.populate_tab_main()

        self.initialize_tab_reader()

    def initialize_tab_screen(self):
        self.tabs = QTabWidget()
        self.tab_main = QWidget()
        self.tab_reader = QWidget()
        self.tabs.resize(300,200)
    
    def add_tabs_to_screen(self):
        self.tabs.addTab(self.tab_main, "Articles")

    def populate_tab_main(self):
        self.tab_main.layout = QGridLayout(self)

        self.tab_main.article_list = QListWidget()

        list_item_style = "QListWidget::item { border: 1px solid #fff; padding: 15px; font-family: Noto Mono,Menlo,Monaco,Consolas,monospace; font-size: 25px; }"
        list_item_hover = "QListWidget::item:hover { background: #2a2a2a;  }"

        self.tab_main.article_list.setStyleSheet(list_item_style)
        self.tab_main.article_list.setStyleSheet(list_item_hover)
        self.tab_main.article_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab_main.article_list.setFont(QFont('Mono', 12, QFont.Bold))

        self.articles = hn.get_articles()

        for rank, article in self.articles.items():

            text = "\n".join([
                "",
                f"{rank}. {article['title']}",
                f"| {article['score']} points | {article.get('descendants', 0)} comments |",
                "",
            ])

            self.tab_main.article_list.insertItem(rank, text)

        self.tab_main.article_list.clicked.connect(self.article_clicked)

        self.tab_main.layout.addWidget(self.tab_main.article_list)

        self.tab_main.setLayout(self.tab_main.layout)

    def initialize_tab_reader(self):
        self.tab_reader.layout = QHBoxLayout(self)
        self.read_split = QSplitter(Qt.Horizontal)

        self.tab_reader.browser_article = QWebEngineView()
        self.read_split.addWidget(self.tab_reader.browser_article)

        self.tab_reader.browser_comments = QWebEngineView()
        self.read_split.addWidget(self.tab_reader.browser_comments)

        self.tab_reader.layout.addWidget(self.read_split)

        self.tab_reader.setLayout(self.tab_reader.layout)

    def article_clicked(self):
        item = self.tab_main.article_list.currentItem()
        
        self.set_reader_tab(self.tab_main.article_list.row(item) + 1)

    def set_reader_tab(self, article_index):
        article = self.articles.get(article_index)

        self.tab_reader.browser_comments.load(QUrl(f"https://news.ycombinator.com/item?id={article['id']}"))

        if article.get("url"):
            self.tab_reader.browser_article.load(QUrl(article['url']))
        else:
            self.tab_reader.browser_article.load(QUrl("https://i.imgur.com/cr2ml4j.gif"))


        try:
            self.tabs.addTab(self.tab_reader, "Reader")
        except:
            pass

        self.tabs.setCurrentIndex(1)


    def add_tabs_to_widget(self):
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())