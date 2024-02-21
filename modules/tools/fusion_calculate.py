import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QSpinBox, QAbstractSpinBox, QScrollArea)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon
from modules.path_img import ICON_PATH
import random

class WindowCalculate(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.createWidget()
        self.addWidgets()


    def initUI(self):
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowTitle('Fusionar Materiais')
        self.setFixedSize(600,600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.central_layout.setContentsMargins(30,30,30,30)
        self.central_widget.setStyleSheet('color: white')

    def createWidget(self):
        self.list_fusion = []
        self.success_index = 0
        self.failed_index = 0
        self.chance = 0
        self.cost = 0

        self.layout_top = QGridLayout()

        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)

        self.widget_scroll = QWidget(self.area_scroll)
        self.layout_scroll = QVBoxLayout(self.widget_scroll)
        self.area_scroll.setWidget(self.widget_scroll)

        self.label_porcents = QLabel('Porcentagem de Sucesso')
        self.label_multiply = QLabel('Fusões Consecutivas')
        self.label_base = QLabel('Base')
        self.int_porcents = QSpinBox()
        self.int_porcents.setMinimum(1)
        self.int_porcents.setMaximum(100)
        self.int_porcents.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.int_x = QSpinBox()
        self.int_x.setMaximum(9999)
        self.int_x.setMinimum(1)
        self.int_x.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.int_base = QSpinBox()
        self.int_base.setMaximum(1)
        self.int_base.setMaximum(5)
        self.int_base.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.layout_results = QHBoxLayout()
        self.label_succes = QLabel('Sucesso: 0')
        self.label_fails = QLabel('Falha: 0')
        self.label_chance = QLabel('Tentativas: 0')
        self.label_cost = QLabel('Materiais Gastos: 0')

        self.button_calculate = QPushButton('Calcular')
        self.button_calculate.clicked.connect(self.calculateRate)
        self.button_calculate.setFixedHeight(40)


        self.button_clear = QPushButton('Limpar')
        self.button_clear.clicked.connect(self.clearList)
        self.button_clear.setFixedHeight(40)


        self.stylizedWidgets()

    def addWidgets(self):
        self.central_layout.addLayout(self.layout_top)

        self.layout_top.addWidget(self.label_porcents,1,1,1,1)
        self.layout_top.addWidget(self.int_porcents,2,1,1,1)
        self.layout_top.addWidget(self.label_multiply,1,2,1,1)
        self.layout_top.addWidget(self.int_x,2,2,1,1)
        self.layout_top.addWidget(self.label_base,1,3,1,1)
        self.layout_top.addWidget(self.int_base,2,3,1,1)

        self.central_layout.addLayout(self.layout_results)
        self.layout_results.addWidget(self.label_succes)
        self.layout_results.addWidget(self.label_fails)
        self.layout_results.addWidget(self.label_chance)
        self.layout_results.addWidget(self.label_cost)

        self.central_layout.addWidget(self.area_scroll)
        self.central_layout.addWidget(self.button_calculate)
        self.central_layout.addWidget(self.button_clear)

    def stylizedWidgets(self):
        self.int_porcents.setStyleSheet('''
                                        
                                        QSpinBox{
                                            background: rgba(28, 66, 128, 80%);
                                            opacity: 30%;
                                            color: white;
                                            border: 1px solid rgb(45, 147, 224);
                                            border-radius: 5px;
                                         }
                                        
                                        
                                        ''')
        
        self.int_x.setStyleSheet('''
                                        
                                        QSpinBox{
                                            background: rgba(28, 66, 128, 80%);
                                            opacity: 30%;
                                            color: white;
                                            border: 1px solid rgb(45, 147, 224);
                                            border-radius: 5px;
                                         }
                                        
                                        ''')
        
        self.int_base.setStyleSheet('''
                                        
                                        QSpinBox{
                                            background: rgba(28, 66, 128, 80%);
                                            opacity: 30%;
                                            color: white;
                                            border: 1px solid rgb(45, 147, 224);
                                            border-radius: 5px;
                                         }
                                        
                                        ''')

        self.area_scroll.setStyleSheet('''
                                         QWidget{
                                            background: rgba(28, 66, 128, 50%);
                                            opacity: 30%;
                                            color: white;
                                            border: 1px solid rgb(45, 147, 224);
                                            border-radius: 5px;
                                        }

                                        QScrollBar:vertical {
                                        width: 10px;  /* Largura da barra de rolagem */
                                        }
                                       
                                        QScrollBar::handle:vertical {
                                        background: rgb(45, 147, 224); /* Cor do manipulador (barra de rolagem) */
                                        }
            
                                       QScrollBar::add-page:vertical,
                                       QScrollBar::sub-page:vertical {
                                       background: none; /* Remove a área dos botões de rolagem */
                                       }

                                       QScrollBar::add-line:vertical,
                                       QScrollBar::sub-line:vertical {
                                       width: 0;  /* Largura zero para ocultar os botões de rolagem */
                                    }
                                       

                                         ''')
        
        self.button_calculate.setStyleSheet('''
                                         QPushButton{
                                            background: rgba(28, 66, 128, 90%);
                                            opacity: 30%;
                                            color: white;
                                            border: 1px solid rgb(45, 147, 224);
                                            border-radius: 5px;
                                         }
                                       
                                        QPushButton:hover{
                                            
                                        }

                                        QPushButton:pressed{
                                            background: rgb(45, 147, 224);
                                        }
                                         ''')
        
        self.button_clear.setStyleSheet('''
                                         QPushButton{
                                            background: rgba(28, 66, 128, 90%);
                                            opacity: 30%;
                                            color: white;
                                            border: 1px solid rgb(45, 147, 224);
                                            border-radius: 5px;
                                         }
                                       
                                        QPushButton:hover{
                                            
                                        }

                                        QPushButton:pressed{
                                            background: rgb(45, 147, 224);
                                        }
                                         ''')

    def calculateRate(self):
        
        if self.int_x.value() <= 0:
            self.int_x.setValue(1)

        for i in range(self.int_x.value()):
            probability = Probability(random.randint(0,100))
            result = probability.prob(int(self.int_porcents.value()))

            formater_str = result.split(' ')
            abstract_value = formater_str

            if abstract_value[0] == 'Sucesso':
                self.success_index += 1
                self.label_succes.setText(f'Sucesso: {self.success_index}')
            

            if abstract_value[0] == 'Falha':
                self.failed_index += 1
                self.label_fails.setText(f'Falha: {self.failed_index}')
        
            self.chance += 1
            self.cost += self.int_base.value()
            self.label_chance.setText(f'Tentativas: {self.chance}')
            self.label_cost.setText(f'Materiais Gastos: {self.cost}')

            self.list_fusion.append(result)
            label_prefab = QLabel(result)
            label_prefab.setFixedHeight(20)
            self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignTop)
            self.layout_scroll.addWidget(label_prefab)

    def clearList(self):
        self.list_fusion.clear()
        self.chance = 0
        self.success_index = 0
        self.failed_index = 0
        self.cost = 0
        self.label_chance.setText(f'Tentativas: {self.chance}')
        self.label_fails.setText(f'Falha: {self.failed_index}')
        self.label_succes.setText(f'Sucesso: {self.success_index}')
        self.label_cost.setText(f'Materiais Gastos: {self.cost}')
        
       

        for i in reversed(range(self.layout_scroll.count())):
            item = self.layout_scroll.itemAt(i)
            if item.widget():
                item.widget().deleteLater()  # Remova o widget
            elif item.layout():
                self.removeChildren(item.layout())  # Remova os widgets no layout
            self.layout_scroll.removeItem(item)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        grad = QLinearGradient(0,0,500,500)
        grad.setColorAt(0,QColor(21, 99, 209))
        grad.setColorAt(0.2,QColor(14, 53, 107))
        grad.setColorAt(0.5,QColor(21, 99, 209))
        grad.setColorAt(0.8,QColor(16, 42, 79))
        grad.setColorAt(1,QColor(21, 99, 209))
        painter.fillRect(self.rect(), grad)


class Probability():

    def __init__(self, input):
        self.input = input
    
    def prob(self, porcents):
        if self.input >= 0 and self.input <= porcents:
            return f'Sucesso {porcents}%!'
        return f'Falha {porcents}%!'


if __name__ == "__main__":
    app = QApplication([])
    window = WindowCalculate()
    window.show()
    sys.exit(app.exec())