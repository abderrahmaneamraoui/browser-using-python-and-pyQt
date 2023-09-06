import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        
        self.nav_bar = QToolBar()
        self.addToolBar(self.nav_bar)

        back_button = QAction("Back", self)
        back_button.setStatusTip("Back to previous page")
        back_button.triggered.connect(self.browser.back)
        self.nav_bar.addAction(back_button)

        forward_button = QAction("Forward", self)
        forward_button.setStatusTip("Forward to next page")
        forward_button.triggered.connect(self.browser.forward)
        self.nav_bar.addAction(forward_button)

        reload_button = QAction("Reload", self)
        reload_button.setStatusTip("Reload page")
        reload_button.triggered.connect(self.browser.reload)
        self.nav_bar.addAction(reload_button)

        home_button = QAction("Home", self)
        home_button.setStatusTip("Go home")
        home_button.triggered.connect(self.navigate_home)
        self.nav_bar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.nav_bar.addWidget(self.url_bar)

        stop_button = QAction("Stop", self)
        stop_button.setStatusTip("Stop loading current page")
        stop_button.triggered.connect(self.browser.stop)
        self.nav_bar.addAction(stop_button)

        self.browser.urlChanged.connect(self.update_urlbar)
        self.statusBar()

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

def main():
    app = QApplication(sys.argv)
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling) # High DPI support
    window = WebBrowser()
    window.setWindowTitle("Web Browser")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()