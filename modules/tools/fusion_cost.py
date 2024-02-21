import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QGroupBox, QComboBox, QSpinBox, QAbstractSpinBox, QPushButton, QLabel)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon
from modules.path_img import ICON_PATH
#from path_img import ICON_PATH

class FusionCost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.createWidget()
        self.addWidgets()

    def initUI(self):
        self.setFixedSize(350,450)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowTitle('Custo de Fusão')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        
        self.central_layout.setContentsMargins(10,10,10,10)

    def createWidget(self):
        self.dropdown_quality = QComboBox()
        list_quality = ['Material Lv1 - Branco',
                        'Material Lv2 - Verde',
                        'Material Lv3 - Azul',
                        'Material Lv4 - Roxo']
        self.dropdown_quality.addItems(list_quality)

        self.int_quantity = QSpinBox()
        self.int_quantity.setMinimum(1)
        self.int_quantity.setMaximum(99999)
        self.int_quantity.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.button_calculate = QPushButton('Calcular')
        self.button_clear = QPushButton('Limpar')
        
        self.groupbox_info = QGroupBox(' Info ')
        self.layout_group_info = QVBoxLayout(self.groupbox_info)
        self.layout_group_info.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.button_calculate.clicked.connect(self.calculate)
        self.button_clear.clicked.connect(self.clearInfo)

    def addWidgets(self):
        self.central_layout.addWidget(self.dropdown_quality)
        self.central_layout.addWidget(self.int_quantity)
        self.central_layout.addWidget(self.button_calculate)
        self.central_layout.addWidget(self.groupbox_info)
        self.central_layout.addWidget(self.button_clear)

    def calculate(self):

        self.clearInfo()

        if self.dropdown_quality.currentIndex() == 0:
            if self.int_quantity.value() >= 5 and self.int_quantity.value() < 25:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv2 - Verde'))
            if self.int_quantity.value() >= 25 and self.int_quantity.value() < 125:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv2 - Verde'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 25)} unidades - material Lv3 - Azul'))
            if self.int_quantity.value() >= 125 and self.int_quantity.value() < 625:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv2 - Verde'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 25)} unidades - material Lv3 - Azul'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 125)} unidades - material Lv4 - Roxo'))
            if self.int_quantity.value() >= 625:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv2 - Verde'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 25)} unidades - material Lv3 - Azul'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 125)} unidades - material Lv4 - Roxo'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 625)} unidades - material Lv5 - Laranja'))
            if self.int_quantity.value() < 5:
                self.layout_group_info.addWidget(QLabel('Valor precisa ser maior que 4!'))

        if self.dropdown_quality.currentIndex() == 1:
            if self.int_quantity.value() >= 5 and self.int_quantity.value() < 25:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv3 - Azul'))
            if self.int_quantity.value() >= 25 and self.int_quantity.value() < 125:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv3 - Azul'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 25)} unidades - material Lv4 - Roxo'))
            if self.int_quantity.value() >= 125:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv3 - Azul'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 25)} unidades - material Lv4 - Roxo'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 125)} unidades - material Lv5 - Laranja'))
            if self.int_quantity.value() < 5:
                self.layout_group_info.addWidget(QLabel('Valor precisa ser maior que 4!'))

        if self.dropdown_quality.currentIndex() == 2:
            if self.int_quantity.value() >= 5 and self.int_quantity.value() < 25:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv4 - Roxo'))
            if self.int_quantity.value() >= 25:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv4 - Roxo'))
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 25)} unidades - material Lv5 - Laranja'))
            if self.int_quantity.value() < 5:
                self.layout_group_info.addWidget(QLabel('Valor precisa ser maior que 4!'))

        if self.dropdown_quality.currentIndex() == 3:
            if self.int_quantity.value() >= 5:
                self.layout_group_info.addWidget(QLabel(f'{int(self.int_quantity.value() / 5)} unidades - material Lv5 - Laranja'))
            if self.int_quantity.value() < 5:
                self.layout_group_info.addWidget(QLabel('Valor precisa ser maior que 4!'))

    def clearInfo(self):
        for i in reversed(range(self.layout_group_info.count())):
            item = self.layout_group_info.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.layout_group_info.removeItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FusionCost()
    window.show()
    sys.exit(app.exec())