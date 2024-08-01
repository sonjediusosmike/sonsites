import sys
import subprocess
from PyQt5.QtNetwork import QNetworkProxy
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5 import QtCore
from PyQt5 import QtGui
from tabs import TabbedBrowser

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('sonsite.png'))
        self.setWindowTitle('sonsites')
        self.showMaximized()
        self.tabbed_browser = TabbedBrowser(self)
        self.setCentralWidget(self.tabbed_browser)
        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = navbar.addAction('Back')
        back_btn.triggered.connect(self.back)

        # Forward button
        forward_btn = navbar.addAction('Forward')
        forward_btn.triggered.connect(self.forward)

        # Reload button
        reload_btn = navbar.addAction('Reload')
        reload_btn.triggered.connect(self.reload)

        # Custom Home button
        home_btn = navbar.addAction('Home')
        home_btn.triggered.connect(self.navigate_home)

        # New Tab button
        new_tab_btn = navbar.addAction('New Tab')
        new_tab_btn.triggered.connect(self.tabbed_browser.add_tab)

        # Close button
        close_button = navbar.addAction('close')
        close_button.triggered.connect(self.close)

        # Bing Button
        bing_btn = navbar.addAction('Bing')
        bing_btn.triggered.connect(self.navigate_bing)

        # DuckDuckGo Button
        ddg_btn = navbar.addAction('DuckDuckGo')
        ddg_btn.triggered.connect(self.navigate_ddg)
        # Yandex Button
        ddg_btn = navbar.addAction('Yandex')
        ddg_btn.triggered.connect(self.navigate_yandex)
        # Youtube Button
        ddg_btn = navbar.addAction('Youtube')
        ddg_btn.triggered.connect(self.navigate_yt)
        # Brave Button
        brave_btn = navbar.addAction('Brave')
        brave_btn.triggered.connect(self.navigate_brave)
    def back(self):
        self.tabbed_browser.current_browser().back()

    def forward(self):
        self.tabbed_browser.current_browser().forward()

    def reload(self):
        self.tabbed_browser.current_browser().reload()

    def navigate_home(self):
        self.tabbed_browser.current_browser().setUrl(QUrl('https://www.google.com/'))
    def navigate_bing(self):
        self.tabbed_browser.current_browser().setUrl(QUrl('https://www.bing.com/'))
    def navigate_ddg(self):
        self.tabbed_browser.current_browser().setUrl(QUrl('https://duckduckgo.com/?t='))
    def navigate_yandex(self):
        self.tabbed_browser.current_browser().setUrl(QUrl('https://yandex.com/'))
    def navigate_yt(self):
        self.tabbed_browser.current_browser().setUrl(QUrl('https://youtube.com'))
    def navigate_brave(self):
        self.tabbed_browser.current_browser().setUrl(QUrl('https://search.brave.com/'))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())
