import sys
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea)

class LabsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Labirintos (Lv50 - Lv150)')
        self.setFixedSize(920, 650)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

        self.area_scroll = QScrollArea()
        self.widget_scroll = QWidget(self.area_scroll)
        self.layout_scroll = QVBoxLayout(self.widget_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.area_scroll.setWidget(self.widget_scroll)
        self.area_scroll.setWidgetResizable(True)

        self.adjust_url_web_view('https://www.youtube.com/embed/4-egHaIoZtg') #50
        self.adjust_url_web_view('https://www.youtube.com/embed/ewAb9Bi8xlc') #60 - 80
        self.adjust_url_web_view('https://www.youtube.com/embed/ILHzKWoeWew') #90
        self.adjust_url_web_view('https://www.youtube.com/embed/H5QzKZ3ZiU8') #100 x
        self.adjust_url_web_view('https://www.youtube.com/embed/7cBtAoQvSrI') #120 x
        self.adjust_url_web_view('https://www.youtube.com/embed/xeps8wLbp7o') #160

        

        self.adjust_url_web_view('https://www.youtube.com/embed/Tpqh0-4HBdA') # raivosos x


        self.central_layout.addWidget(self.area_scroll)


    def adjust_url_web_view(self, url):
        video_lab = QWebEngineView()
        video_lab.setUrl(QUrl(url))
        video_lab.setFixedSize(860,480)
        html_content = f"""
        <html>
        <head></head>
        <body style="margin:0">
            <iframe width="852" height="480" src="{url}" title="Labirinto do 50 Magic Campus" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </body>
        </html>
        """
        #video_lab.setHtml(html_content)
        self.layout_scroll.addWidget(video_lab)
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LabsWindow()
    window.show()
    sys.exit(app.exec())