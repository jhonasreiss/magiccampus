import sys
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QUrl

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Magic Campus')
        self.setFixedSize(900,650)
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.central_layout)

        self.web_view = QWebEngineView(self)
        self.central_layout.addWidget(self.web_view)
        self.load_flash_content()

    def load_flash_content(self):
        flash_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flash Player</title>
        </head>
        <body style="margin: 0; overflow: hidden;">
            <embed type="application/x-shockwave-flash" src="GameLoader.swf?v=0.9.9a33.168" width="1050" height="665" style="undefined" id="game" name="game" bgcolor="#000000" quality="high" align="middle" allowscriptaccess="sameDomain" menu="false" pluginspage="http://www.adobe.com/go/getflashplayer" flashvars="user=10027129118&amp;pass=5d63915268426eafc3b4f998c95dd2b9&amp;version=0.9.9a33.168&amp;isExpand=true">
        </body>
        </html>
        """

        flash_html_2 = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flash Player</title>
        </head>
        <body style="margin: 0; overflow: hidden; background-color: black">
            <embed type="application/x-shockwave-flash" src="GameLoader.swf?v=0.9.9a33.168" width="1050" height="665" style="undefined" id="game" name="game" bgcolor="#000000" quality="high" align="middle" allowscriptaccess="sameDomain" menu="false" pluginspage="https://archive.org/details/flashplayer_32_sa_202104" flashvars="user=10027129118&amp;pass=5d63915268426eafc3b4f998c95dd2b9&amp;version=0.9.9a33.168&amp;isExpand=true">
        </body>
        </html>
        """

        # Carregue o conteúdo HTML na QWebEngineView
        self.web_view.setHtml(flash_html_2)
        
        
        

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())