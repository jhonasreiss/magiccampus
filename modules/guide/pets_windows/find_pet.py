import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton,
                               QScrollArea, QComboBox, QLabel, QGroupBox)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QFont

class FindPet(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_init()

    def set_init(self):
        self.setWindowTitle('Pet')
        self.setFixedSize(680,600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FindPet()
    window.show()
    sys.exit(app.exec())