import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Initialize tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeCurrentTab)
        self.setCentralWidget(self.tabs)
        self.setWindowIcon(QIcon('C:\\Users\\ysfdg\\Desktop\\Flexer\\images\\logo\\logo.jpg'))

        # Create an initial tab
        self.addTab(QUrl('http://google.com'))

        navbar = QToolBar()
        self.addToolBar(navbar)


        #The paths should be updated in different computer
        new_tab_icon_path = 'C:\\Users\\ysfdg\\Desktop\\Flexer\\images\\new-tab-icon.png'
        back_icon_path = 'C:\\Users\\ysfdg\\Desktop\\Flexer\\images\\back-icon.png'
        forward_icon_path = 'C:\\Users\\ysfdg\\Desktop\\Flexer\\images\\forward-icon.png'
        home_icon_path = 'C:\\Users\\ysfdg\\Desktop\\Flexer\\images\\home-icon.png'
        reload_icon_path = 'C:\\Users\\ysfdg\\Desktop\\Flexer\\images\\reload_con.png'
        bookmark_icon_path = 'C:\\Users\\ysfdg\\Desktop\\Flexer\\images\\bookmark-icon.png'

        # Bookmark action
        bookmarkAction = QAction(QIcon(bookmark_icon_path), 'Bookmark this page', self)
        bookmarkAction.triggered.connect(self.addBookmark)
        navbar.addAction(bookmarkAction)
        self.bookmarks = []

        # Initialize the bookmark bar
        self.bookmarkBar = QToolBar("Bookmarks")
        self.bookmarkBar.setVisible(False)  # Initially hidden
        self.addToolBar(Qt.TopToolBarArea, self.bookmarkBar)

        # New Tab Button
        newTabButton = QAction(QIcon(new_tab_icon_path), 'New Tab', self)
        newTabButton.triggered.connect(lambda _: self.addTab())
        navbar.addAction(newTabButton)

        # Back Button
        backButton = QAction(QIcon(back_icon_path), 'Back', self)
        backButton.triggered.connect(lambda: self.getCurrentBrowser().back())
        navbar.addAction(backButton)

        # Forward Button
        forwardButton = QAction(QIcon(forward_icon_path), 'Forward', self)
        forwardButton.triggered.connect(lambda: self.getCurrentBrowser().forward())
        navbar.addAction(forwardButton)

        # Reload Button
        self.reloadButton = QAction(QIcon(reload_icon_path), 'Reload', self)
        self.reloadButton.triggered.connect(lambda: self.getCurrentBrowser().reload())
        navbar.addAction(self.reloadButton)

        # Connect loading signals
        self.browser.loadStarted.connect(self.onLoadStarted)
        self.browser.loadFinished.connect(self.onLoadFinished)

        homeButton = QAction(QIcon(home_icon_path), 'Home', self)
        homeButton.triggered.connect(self.gotoHomePage)
        navbar.addAction(homeButton)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigateToUrl)
        navbar.addWidget(self.urlBar)

        self.browser.urlChanged.connect(self.updateUrl)

    def gotoHomePage(self):
        self.getCurrentBrowser().setUrl(QUrl("http://google.com"))

    def navigateToUrl(self):
        url = self.urlBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, q, browser=None):
        if browser == self.getCurrentBrowser():
            self.urlBar.setText(q.toString())

    def onLoadStarted(self):
        # When loading starts, change reload button to stop button
        self.reloadButton.setText('Stop')
        self.reloadButton.disconnect()
        self.reloadButton.triggered.connect(self.browser.stop)

    def onLoadFinished(self, ok):
        # When loading finishes, change it back to reload button
        self.reloadButton.setText('Reload')
        self.reloadButton.disconnect()
        self.reloadButton.triggered.connect(self.browser.reload)

        # Modify the addTab method

    def addTab(self, url=None):
        if url is None:
            url = QUrl('http://google.com')
        browser = QWebEngineView()
        browser.setUrl(url)
        i = self.tabs.addTab(browser, 'New Tab')  # Initial title
        self.tabs.setCurrentIndex(i)

        # Connect signals
        browser.urlChanged.connect(lambda q: self.updateUrl(q, browser))
        browser.loadStarted.connect(lambda: self.onLoadStarted(browser))
        browser.loadFinished.connect(lambda _: self.onLoadFinished(browser))
        browser.titleChanged.connect(lambda title: self.updateTabTitle(i, title))

        # Add the updateTabTitle method

    def updateTabTitle(self, index, title):
        self.tabs.setTabText(index, title[:15] + '...' if len(title) > 15 else title)  # Limit title length if necessary

    def closeCurrentTab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

        # Modify these methods to interact with the current tab's browser

    def navigateToUrl(self):
        url = self.urlBar.text()
        self.getCurrentBrowser().setUrl(QUrl(url))
    def navigateToUrl(self):
        url = self.urlBar.text()
        self.getCurrentBrowser().setUrl(QUrl(url))


    def updateUrl(self, q, browser=None):
        if browser == self.getCurrentBrowser():
            self.urlBar.setText(q.toString())
            self.urlBar.setCursorPosition(0)  # Move the cursor to the start

    def onLoadStarted(self, browser):
        if browser == self.getCurrentBrowser():
            self.reloadButton.setText('Stop')
            self.reloadButton.disconnect()
            self.reloadButton.triggered.connect(self.getCurrentBrowser().stop)

    def onLoadFinished(self, browser):
        if browser == self.getCurrentBrowser():
            self.reloadButton.setText('Reload')
            self.reloadButton.disconnect()
            self.reloadButton.triggered.connect(self.getCurrentBrowser().reload)

    def getCurrentBrowser(self):
        return self.tabs.currentWidget()
    def getCurrentBrowser(self):
        return self.tabs.currentWidget()

    def addBookmark(self):
        # Get current page URL and title
        url = self.getCurrentBrowser().url().toString()
        url = self.getCurrentBrowser().url().toString()
        title = self.getCurrentBrowser().title()

        # Create a dialog to ask user for bookmark name and optional icon
        dialog = QDialog(self)
        dialog = QDialog(self)
        layout = QVBoxLayout(dialog)

        # Add widgets to dialog for name and icon selection
        nameLabel = QLabel("Enter bookmark name:")
        nameLineEdit = QLineEdit(title)
        iconLabel = QLabel("Select an icon (optional):")
        iconLineEdit = QLineEdit()
        iconButton = QPushButton("Choose Icon")
        iconButton.clicked.connect(lambda: self.selectIcon(iconLineEdit))
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(dialog.accept)
        buttonBox.rejected.connect(dialog.reject)

        # Add widgets to layout
        layout.addWidget(nameLabel)
        layout.addWidget(nameLineEdit)
        layout.addWidget(iconLabel)
        layout.addWidget(iconLineEdit)
        layout.addWidget(iconButton)
        layout.addWidget(buttonBox)

        # Show dialog and process the result
        if dialog.exec_() == QDialog.Accepted:
            bookmarkName = nameLineEdit.text()
            iconPath = iconLineEdit.text()
            icon = QIcon(iconPath) if iconPath else QIcon()

            # Add bookmark to bookmark bar and list
            bookmarkAction = QAction(icon, bookmarkName, self)
            bookmarkAction.triggered.connect(self.createBookmarkCallback(url))
            self.bookmarkBar.addAction(bookmarkAction)
            self.bookmarks.append((url, bookmarkName, iconPath))

            # Show the bookmark bar
            self.bookmarkBar.setVisible(True)

    def selectIcon(self, iconLineEdit):
        iconPath, _ = QFileDialog.getOpenFileName(self, "Select Icon", "", "Images (*.png *.xpm *.jpg *.ico)")
        if iconPath:
            iconLineEdit.setText(iconPath)

    def createBookmarkCallback(self, url):
        return lambda: self.getCurrentBrowser().setUrl(QUrl(url))

app = QApplication(sys.argv)
QApplication.setApplicationName("Flexer")
Window = MainWindow()
app.exec_()