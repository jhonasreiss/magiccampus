import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QScrollArea)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon, QPen
from modules.guide.labs import LabsWindow
from modules.guide.pets import PetInterface
from modules.guide.keys import KeysWindow
from modules.guide.judge import JudgeSystem
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
        self.list_buttons_name = ['MINI BOSS','ACADEMIA','MISSÕES','LABS','PETS','MODAS','LIVROS','GUILDA','PERSONAGEM','GRUPO / EQUIPE',
                                  'SOCIAL','EQUIPAMENTO','EVENTOS','TAREFAS DIÁRIAS','MISSÃO 200 PARTES','ESPELHO','TROCAR COR','MAGIAS',
                                  'CHAVES' ,'FERIADOS' ,'CASH','FLASH','ALICE','GATO DA SORTE','TABELA DE MINI', 'JULGAMENTO']
        
        self.label_img = [QLabel() for i in range(self.list_buttons_name.__len__())]
        self.buttons = [QPushButton() for i in range(self.list_buttons_name.__len__())]
        self.pix_img = [QPixmap() for i in range(self.label_img.__len__())]
        self.layout_img = [QHBoxLayout() for i in range(self.label_img.__len__())]

        for i in range(self.list_buttons_name.__len__()):
            self.pix_img[i].load('imgs/guide_icon/01.jpg')
            self.label_img[i].setPixmap(self.pix_img[i])
            self.label_img[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.layout_img[i].addWidget(self.label_img[i])
            self.layout_img[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.layout_img[i].setContentsMargins(5,5,5,5)
            self.buttons[i].setLayout(self.layout_img[i])

        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)
        self.widget_scroll = QWidget(self.area_scroll)
        self.area_scroll.setWidget(self.widget_scroll)
        self.layout_scroll = QGridLayout(self.widget_scroll)
        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #self.area_scroll.setObjectName('main_area')
        self.area_scroll.setStyleSheet('''
                        QScrollArea > QWidget > QWidget{
                            background-color: #32567d
                        }
                        QScrollBar:vertical {
                            background-color: #dddddd;
                            width: 20px; 
                        }
                        QScrollBar::handle:vertical {
                            background-color: #457dde;
                        }
                        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                            background: none;
                        }''')

        index = 0
        for i in self.buttons:
            i.setFixedSize(310,150)
            i.setEnabled(False)
            try:
                i.setText(self.list_buttons_name[index])
                i.setObjectName('main_button')
                i.setStyleSheet('''
                        QPushButton#main_button{
                            background-color: #457dde;
                            border: 1px solid white;
                            color: white;
                        }

                        QPushButton:hover#main_button{
                            background-color: white;
                            border: 1px solid white;
                            color: white;
                        }''')
            except TypeError as err:
                print('Não possui mais indice!')
            index += 1

        self.buttons[3].setEnabled(True)
        self.buttons[4].setEnabled(True)
        self.buttons[18].setEnabled(True)
        self.buttons[23].setEnabled(True)
        self.buttons[24].setEnabled(True)
        self.buttons[25].setEnabled(True)

        self.buttons[3].clicked.connect(self.openLabs)
        self.buttons[4].clicked.connect(self.openPets)
        self.buttons[18].clicked.connect(self.openKeys)
        self.buttons[23].clicked.connect(self.openKeys)
        self.buttons[24].clicked.connect(self.openKeys)
        self.buttons[25].clicked.connect(self.openJudge)

        for i in self.buttons:
            if i.isEnabled() is not True:
                i.setStyleSheet('''
                        QPushButton#main_button{
                            background-color: #8696b3;
                            border: 1px solid white;
                            color: white;
                        }''')

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

    def openLabs(self):
        self.lab_window = LabsWindow()
        self.lab_window.show()

    def openPets(self):
        self.pet_window = PetInterface()
        self.pet_window.show()

    def openKeys(self):
        self.key_window = KeysWindow()
        self.key_window.show()

    def openJudge(self):
        self.judge_window = JudgeSystem()
        self.judge_window.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        grad = QLinearGradient(0,0,0,self.height())
        grad.setColorAt(0,QColor('#035efc'))
        grad.setColorAt(1,QColor('#103c87'))
        painter.fillRect(self.rect(), grad)

if __name__ == "__main__":
    app = QApplication([])
    window = GuideInterface()
    window.show()
    sys.exit(app.exec())
