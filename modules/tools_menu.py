import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon
from modules.tools.fusion_calculate import WindowCalculate
from modules.tools.search_trade import LookTrade
from modules.tools.fusion_cost import FusionCost
from modules.tools.exp_table import ExpTable
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
        self.setFixedSize(800,600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)

    def createWidget(self):
        self.button_action = [QPushButton() for i in range(12)]
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
                            'Baixar Pack (Flash + Navegador)'
                            ]
        
        self.button_action[0].clicked.connect(self.openFusionCalculate)
        self.button_action[1].clicked.connect(self.openSearchTrade)
        self.button_action[2].clicked.connect(self.openCostFusion)
        self.button_action[8].clicked.connect(self.openExpTable)

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

    def addWidgets(self):
        row = 1
        column = 1
        for i in self.button_action:
            if row > 4:
                column += 1
                row = 1
            self.central_layout.addWidget(i,row,column,1,1)
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

if __name__ == "__main__":
    app = QApplication([])
    window = MenuTools()
    window.show()
    sys.exit(app.exec())