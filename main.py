import sys, time
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QProgressBar,QLabel, QPushButton)
from PySide6.QtGui import QPainter, QPixmap, QIcon
from PySide6.QtCore import Qt, QThread, Signal
from modules.interface import interfaceApp
from modules.path_img import ICON_PATH, BACKGROUND_PATH


class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setSetup()
        self.createWidget()
        self.insertWidget()

        

    def openInterface(self):
        self.interface_window = interfaceApp()
        self.interface_window.show()
        self.close()
        
        

    def setSetup(self):
        self.setFixedSize(600,600)
        self.setWindowTitle('Guia Definitivo Magic Campus Brasil')
        self.setWindowIcon(QIcon(ICON_PATH))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

    def createWidget(self):

        self.empty_label_h = QLabel()
        self.empty_label_h2 = QLabel()

        self.empty_label_v = QLabel()
        self.empty_label_v2 = QLabel()

        self.empty_label_h.setFixedWidth(0)
        self.empty_label_h2.setFixedWidth(285)

        self.empty_label_v.setFixedHeight(150)
        self.empty_label_v2.setFixedHeight(50)

        self.layout_adjust = QHBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedSize(235,25)

        self.worker_thread = WorkerThread()
        self.worker_thread.update_signal.connect(self.update_progress_bar)
        self.worker_thread.update_signal.connect(self.check_progress)
        self.start_task()

        
        self.progress_bar.setStyleSheet('''
        QProgressBar{
            text-align: center;
            border: 1px solid red;                  
        }

        QProgressBar::chunk{
            background-color: red;                
        }

                                        ''')

    def insertWidget(self):

        self.central_layout.addWidget(self.empty_label_v)
        self.central_layout.addWidget(self.empty_label_v2)

        self.central_layout.addLayout(self.layout_adjust)
        self.layout_adjust.addWidget(self.empty_label_h)
        self.layout_adjust.addWidget(self.progress_bar)
        self.layout_adjust.addWidget(self.empty_label_h2)

        

    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap(BACKGROUND_PATH)
        painter.drawPixmap(0,0,pixmap)

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def start_task(self):
        self.progress_bar.setValue(0)
        self.worker_thread.start()

    def check_progress(self, value):
        if value == 100:
            self.window_interface = interfaceApp()
            self.window_interface.show()
            self.close()
        
        
        
class WorkerThread(QThread):
    update_signal = Signal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.1)
            self.update_signal.emit(i)
        
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec())