import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QGroupBox, QPushButton, QLabel,
                               QScrollArea)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon
from modules.tools.fusion_calculate import WindowCalculate
from modules.tools.search_trade import LookTrade
from modules.tools.fusion_cost import FusionCost
from modules.tools.exp_table import ExpTable
from modules.tools.test_code import CodeTest
from modules.tools.auto_capture import CaptureWindow
from modules.path_img import ICON_PATH

class MenuTools(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.createWidget()
        self.addWidgets()
    
    def initUI(self):
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowTitle('Ferramentas')
        self.setFixedSize(900,600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QHBoxLayout()
        self.central_widget.setLayout(self.central_layout)

    def createWidget(self):
        self.area_scroll = QScrollArea()
        self.widget_scroll = QWidget(self.area_scroll)
        self.layout_scroll = QGridLayout(self.widget_scroll)

        self.area_scroll.setWidget(self.widget_scroll)
        self.area_scroll.setWidgetResizable(True)

        self.area_scroll.setStyleSheet('''
                                        QScrollArea > QWidget > QWidget{
                                            background-color: #457dde;
                                        }
                                       
                                        QScrollBar:vertical {
                                            background-color: #dddddd;
                                            width: 20px; 
                                        }

                                        QScrollBar::handle:vertical {
                                            background-color: blue;
                                        }

                                        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                                            background: none;
                                        }
                                       ''')
        
        list_name_action = ['Fusão de Materiais',
                            'Comerciante de Equipamentos',
                            'Custo de Fusão',
                            'Auxiliador de Cadeia (AM)',
                            'Chat Externo',
                            'Captura Automática',
                            'Eventos Ativos',
                            'Códigos',
                            'Tabela de EXP',
                            'Simulador de Dano',
                            'Advinhar Automático',
                            'Baixar Pack (Flash + Navegador)',
                            'Teste de Códigos'
                            ]
        self.button_action = [QPushButton() for i in range(list_name_action.__len__())]

        self.button_action[0].clicked.connect(self.openFusionCalculate)
        self.button_action[1].clicked.connect(self.openSearchTrade)
        self.button_action[2].clicked.connect(self.openCostFusion)
        self.button_action[8].clicked.connect(self.openExpTable)
        self.button_action[5].clicked.connect(self.openCaptureMob)
        self.button_action[12].clicked.connect(self.openTestCode)

        index_name = 0
        for i in self.button_action:
            i.setText(list_name_action[index_name])
            i.setFixedHeight(140)
            i.setEnabled(False)
            index_name += 1

        self.button_action[0].setEnabled(True)
        self.button_action[1].setEnabled(True)
        self.button_action[2].setEnabled(True)
        self.button_action[8].setEnabled(True)
        self.button_action[5].setEnabled(True)
        self.button_action[12].setEnabled(True)

        

    def addWidgets(self):
        self.central_layout.addWidget(self.area_scroll)

        row = 1
        column = 1
        for i in self.button_action:
            if row > 3:
                column += 1
                row = 1
            self.layout_scroll.addWidget(i,column,row,1,1)
            row += 1

    def openFusionCalculate(self):
        self.window_fusion_calculate = WindowCalculate()
        self.window_fusion_calculate.show()

    def openSearchTrade(self):
        self.window_trade = LookTrade()
        self.window_trade.show()

    def openCostFusion(self):
        self.window_cost = FusionCost()
        self.window_cost.show()

    def openExpTable(self):
        self.window_cost = ExpTable()
        self.window_cost.show()

    def openCaptureMob(self):
        self.mob_cap = CaptureWindow()
        self.mob_cap.show()

    def openTestCode(self):
        self.window_code_test = CodeTest()
        self.window_code_test.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MenuTools()
    window.show()
    sys.exit(app.exec())