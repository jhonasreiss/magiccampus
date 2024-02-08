import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon
#from modules.path_img import ICON_PATH

class GuideInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupWidget()
        self.CreateWidgets()
        self.AddWidgets()

    def setupWidget(self):
        self.setFixedSize(1000,600)
        self.setWindowTitle('GUIA')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

    def CreateWidgets(self):
        self.buttons = [QPushButton() for i in range(21)]
        self.list_buttons_name = ['MINI BOSS','ACADEMIA','MISSÕES','LABS','PETS','MODAS','LIVROS','GUILDA','PERSONAGEM','GRUPO / EQUIPE',
                                  'SOCIAL','EQUIPAMENTO','EVENTOS','TAREFAS DIÁRIAS','MISSÃO 200 PARTES','ESPELHO','TROCAR COR','MAGIAS',
                                  'CHAVES' ,'FERIADOS' ,'CASH','FLASH','ALICE']
        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)
        self.widget_scroll = QWidget(self.area_scroll)
        self.area_scroll.setWidget(self.widget_scroll)
        self.layout_scroll = QGridLayout(self.widget_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignCenter)

        index = 0
        for i in self.buttons:
            i.setFixedSize(310,150)
            i.setEnabled(False)
            try:
                i.setText(self.list_buttons_name[index])
            except TypeError as err:
                print('Não possui mais indice!')
            index += 1

    def AddWidgets(self):

        self.central_layout.addWidget(self.area_scroll)

        row = 1
        column = 1
        for i in self.buttons:
            if row > 3:
                column += 1
                row = 1
            self.layout_scroll.addWidget(i, column, row, 1, 1)
            row += 1

if __name__ == "__main__":
    app = QApplication([])
    window = GuideInterface()
    window.show()
    sys.exit(app.exec())
