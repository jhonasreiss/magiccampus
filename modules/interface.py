import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon
from modules.path_img import ICON_PATH
from modules.tools_menu import MenuTools
from modules.guide.guide_interface import GuideInterface

class interfaceApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupWidget()
        self.CreateWidgets()
        self.AddWidgets()

    def setupWidget(self):
        self.setFixedSize(1200,600)
        self.setWindowTitle('Bem vindo ao guia! Sinta-se livre para explorar!')
        self.setWindowIcon(QIcon(ICON_PATH))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.central_layout.setContentsMargins(30,10,30,0)

    def CreateWidgets(self):
        self.layout_buttons = QGridLayout()
        self.layout_warning = QHBoxLayout()
        self.layout_warning.setAlignment(Qt.AlignmentFlag.AlignCenter)
       

        self.label_empty = QLabel()
        self.label_empty.setFixedHeight(10)

        self.label_warning = QLabel('Política de Privacidade | Termos de Uso')
        self.label_warning.setStyleSheet('color: white')
        self.buttons_menu = [QPushButton() for i in range(8)]
        list_name_buttons = ['Jogar',
                             'Atualização',
                             'Novidades',
                             'Guia',
                             'Ferramentas',
                             'Créditos',
                             'Opções',
                             'Sair'
                             ]

        self.buttons_menu[3].clicked.connect(self.openGuideMenu)
        self.buttons_menu[4].clicked.connect(self.openToolsMenu)
        self.buttons_menu[7].clicked.connect(lambda: self.close())

        label_background = [QLabel() for i in range(8)]
        layouts_background = [QHBoxLayout() for i in range(8)]
        list_background = [QPixmap('imgs/Buttons/button_jogar.jpg'),
                           QPixmap('imgs/Buttons/button_atualizar.jpg'),
                           QPixmap('imgs/Buttons/button_novidades.jpg'),
                           QPixmap('imgs/Buttons/button_guia.jpg'),
                           QPixmap('imgs/Buttons/button_ferramentas.jpg'),
                           QPixmap('imgs/Buttons/button_creditos.jpg'),
                           QPixmap('imgs/Buttons/button_opções.jpg'),
                           QPixmap('imgs/Buttons/button_sair.jpg')
                           ]
        index_bg = 0
        
        for i in list_background:
            i = i.scaled(365,170)

        for i in label_background:
            i.setStyleSheet('''QLabel{
                                border: 5px solid rgb(30, 83, 186);
                                border-radius: 4px;
                            }
                            QLabel:hover{
                                border: 5px solid white;
                            }
                            ''')
            i.setPixmap(list_background[index_bg])
            index_bg += 1

        index = 0
        for i in self.buttons_menu:
            i.setText(list_name_buttons[index])
            i.setFixedSize(365,170)
            i.setLayout(layouts_background[index])

            layouts_background[index].setContentsMargins(0,0,0,0)
            layouts_background[index].addWidget(label_background[index])

            index += 1



    def AddWidgets(self):
        self.central_layout.addWidget(self.label_empty)
        self.central_layout.addLayout(self.layout_buttons)

        row = 1
        column = 1
        for i in self.buttons_menu:
            if row > 3:
                column += 1
                row = 1
            self.layout_buttons.addWidget(i,column,row,1,1)
            row += 1

        self.central_layout.addLayout(self.layout_warning)
        self.layout_warning.addWidget(self.label_warning)


    def openGuideMenu(self):
        self.window_guide = GuideInterface()
        self.window_guide.show()

    def openToolsMenu(self):
        self.window_tools = MenuTools()
        self.window_tools.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        grad = QLinearGradient(0,0,500,500)
        grad.setColorAt(0,QColor(50, 118, 250))
        grad.setColorAt(0.3,QColor(1, 43, 128))
        grad.setColorAt(0.5,QColor(4, 18, 46))
        grad.setColorAt(0.8,QColor(1, 43, 128))
        grad.setColorAt(1,QColor(50, 118, 250))
        painter.fillRect(self.rect(),grad)


if __name__ == "__main__":
    app = QApplication([])
    window = interfaceApp()
    window.show()
    sys.exit(app.exec())
    
