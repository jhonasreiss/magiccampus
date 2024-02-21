import sys, requests, time
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QComboBox, QLabel)
from PySide6.QtCore import QThread, Signal, QTime
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QIcon
from modules.path_img import ICON_PATH

class LookTrade(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.createWidget()
        self.addWidgets()
    
    def initUI(self):
        self.setFixedSize(600,600)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowTitle('Comerciante de Troca')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QHBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.central_layout.setContentsMargins(20,20,20,20)

        self.layouts_info = [QVBoxLayout() for i in range(2)]
        for i in self.layouts_info:
            i.setContentsMargins(10,10,10,10)

        

    def createWidget(self):
        
        

        # ESQUERDA
        trade_img = QPixmap('imgs/trade/trade.jpg')
        trade_img = trade_img.scaled(260,280)
        self.label_title = QLabel('COMERCIANTE DE EQUIPAMENTOS')

        self.label_image_map = QLabel()
        self.pixmap_map = QPixmap('')
        
        self.label_image = QLabel()
        self.label_image.setPixmap(trade_img)
        self.label_image.setStyleSheet('border: 2px solid black')
        self.label_location = QLabel('MAPA ')

        # ------ items de troca --------
        
        self.group_items = QGroupBox(' Itens de Troca ')
        self.layout_group_items = QVBoxLayout(self.group_items)

        self.label_items = [QLabel() for i in range(5)]

        # ------------------------------



        # DIREITA
        self.layout_adjust_label = QVBoxLayout()
        self.layout_adjust_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout_adjust_label.setContentsMargins(0,19,0,19)
        self.groupbox_hour_now = QGroupBox(' Hora Atual ')
        
        self.layout_groupbox_hour_now = QVBoxLayout(self.groupbox_hour_now)
        self.layout_groupbox_hour_now.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.dropdown_hour = QComboBox()
        self.dropdown_hour.addItem('Hora do PC')
        self.dropdown_hour.addItem('Hora Online')
        self.label_hour_now = QLabel('00:00:00')
        self.label_hour_now.setStyleSheet('font-size: 30px')
        self.labels_hours = [QLabel() for i in range(6)]
        list_hours = ['00:00 - 01:00',
                      '08:00 - 09:00',
                      '10:00 - 11:00',
                      '14:00 - 15:00',
                      '18:00 - 19:00',
                      '22:00 - 23:00',
                      ]
        index_hours = 0
        for i in self.labels_hours:
            i.setText(list_hours[index_hours])
            i.setStyleSheet('font-size: 25px')
            i.setAlignment(Qt.AlignmentFlag.AlignRight)
            index_hours += 1

        self.hour_thread = QWorkerThread()
        self.hour_thread.update_signal.connect(self.update_time)
        self.hour_thread.start()

    def update_time(self, current_time):
        # converter hora e minuto (valor recebido)
        self.label_hour_now.setText(current_time)
        formater_str = self.label_hour_now.text().split(':')
        get_str = formater_str = formater_str[0] + formater_str[1]
        int_get = int(get_str)
        #  =====================

        if int_get >= 0 and int_get <= 100:
            for i in self.labels_hours:
                i.setStyleSheet('color: black; font-size: 25px')
            self.labels_hours[0].setStyleSheet('color: blue; font-size: 25px')
            self.label_location.setStyleSheet('color: red;')
            self.label_location.setText('Mundo 6')

            # mapa =======================
            self.label_image_map.setStyleSheet('border: 2px solid black')
            self.pixmap_map = QPixmap('imgs/trade/map_03.jpg')
            self.pixmap_map = self.pixmap_map.scaled(260,120)
            self.label_image_map.setPixmap(self.pixmap_map)
            self.label_image_map.setEnabled(True)
            # ============================

            self.label_items[0].setText('HP')
            self.label_items[1].setText('AGI')
            self.label_items[2].setText('FOR')
            self.label_items[3].setText('ENE')
            self.label_items[4].setText('ENE')

            self.label_items[0].setStyleSheet('color: tomato')
            self.label_items[1].setStyleSheet('color: purple')
            self.label_items[2].setStyleSheet('color: blue')
            self.label_items[3].setStyleSheet('color: blue')
            self.label_items[4].setStyleSheet('color: grey')

        elif int_get >= 800 and int_get <= 900:
            for i in self.labels_hours:
                i.setStyleSheet('color: black; font-size: 25px')
            self.labels_hours[1].setStyleSheet('color: blue; font-size: 25px')
            self.label_location.setStyleSheet('color: red;')
            self.label_location.setText('Mundo 1')

            # mapa =======================
            self.label_image_map.setStyleSheet('border: 2px solid black')
            self.pixmap_map = QPixmap('imgs/trade/map_01.jpg')
            self.pixmap_map = self.pixmap_map.scaled(260,120)
            self.label_image_map.setPixmap(self.pixmap_map)
            self.label_image_map.setEnabled(True)
            # ============================

            self.label_items[0].setText('ENE')
            self.label_items[1].setText('AGI')
            self.label_items[2].setText('FOR')
            self.label_items[3].setText('HP')

            self.label_items[0].setStyleSheet('color: purple')
            self.label_items[1].setStyleSheet('color: blue')
            self.label_items[2].setStyleSheet('color: grey')
            self.label_items[3].setStyleSheet('color: grey')

        elif int_get >= 1000 and int_get <= 1100:
            for i in self.labels_hours:
                i.setStyleSheet('color: black; font-size: 25px')
            self.labels_hours[2].setStyleSheet('color: blue; font-size: 25px')
            self.label_location.setStyleSheet('color: red;')
            self.label_location.setText('Mundo 2')

            # mapa =======================
            self.label_image_map.setStyleSheet('border: 2px solid black')
            self.pixmap_map = QPixmap('imgs/trade/map_03.jpg')
            self.pixmap_map = self.pixmap_map.scaled(260,120)
            self.label_image_map.setPixmap(self.pixmap_map)
            self.label_image_map.setEnabled(True)
            # ============================

            self.label_items[0].setText('FOR')
            self.label_items[1].setText('HP')
            self.label_items[2].setText('ENE')
            self.label_items[3].setText('INT')

            self.label_items[0].setStyleSheet('color: tomato')
            self.label_items[1].setStyleSheet('color: green')
            self.label_items[2].setStyleSheet('color: green')
            self.label_items[3].setStyleSheet('color: grey')


        elif int_get >= 1400 and int_get <= 1500:
            for i in self.labels_hours:
                i.setStyleSheet('color: black; font-size: 25px')
            self.labels_hours[3].setStyleSheet('color: blue; font-size: 25px')
            self.label_location.setStyleSheet('color: red;')
            self.label_location.setText('Mundo 3')
            
            # mapa =======================
            self.label_image_map.setStyleSheet('border: 2px solid black')
            self.pixmap_map = QPixmap('imgs/trade/map_01.jpg')
            self.pixmap_map = self.pixmap_map.scaled(260,120)
            self.label_image_map.setPixmap(self.pixmap_map)
            self.label_image_map.setEnabled(True)
            # ============================

            self.label_items[0].setText('ENE')
            self.label_items[1].setText('INT')
            self.label_items[2].setText('HP')
            self.label_items[3].setText('FOR')

            self.label_items[0].setStyleSheet('color: tomato')
            self.label_items[1].setStyleSheet('color: purple')
            self.label_items[2].setStyleSheet('color: purple')
            self.label_items[3].setStyleSheet('color: green')

            


        elif int_get >= 1800 and int_get <= 1900:
            for i in self.labels_hours:
                i.setStyleSheet('color: black; font-size: 25px')
            self.labels_hours[4].setStyleSheet('color: blue; font-size: 25px')
            self.label_location.setStyleSheet('color: red;')
            self.label_location.setText('Mundo 4')

            # mapa =======================
            self.label_image_map.setStyleSheet('border: 2px solid black')
            self.pixmap_map = QPixmap('imgs/trade/map_04.jpg')
            self.pixmap_map = self.pixmap_map.scaled(260,120)
            self.label_image_map.setPixmap(self.pixmap_map)
            self.label_image_map.setEnabled(True)
            # ============================

            self.label_items[0].setText('FOR')
            self.label_items[1].setText('INT')
            self.label_items[2].setText('INT')
            self.label_items[3].setText('AGI')

            self.label_items[0].setStyleSheet('color: purple')
            self.label_items[1].setStyleSheet('color: blue')
            self.label_items[2].setStyleSheet('color: green')
            self.label_items[3].setStyleSheet('color: grey')


        elif int_get >= 2200 and int_get <= 2300:
            for i in self.labels_hours:
                i.setStyleSheet('color: black; font-size: 25px')
            self.labels_hours[5].setStyleSheet('color: blue; font-size: 25px')
            self.label_location.setStyleSheet('color: red;')
            self.label_location.setText('Mundo 5')

            # mapa =======================
            self.label_image_map.setStyleSheet('border: 2px solid black')
            self.pixmap_map = QPixmap('imgs/trade/map_01.jpg')
            self.pixmap_map = self.pixmap_map.scaled(260,120)
            self.label_image_map.setPixmap(self.pixmap_map)
            self.label_image_map.setEnabled(True)
            # ============================

            self.label_items[0].setText('INT')
            self.label_items[1].setText('AGI')
            self.label_items[2].setText('HP')
            self.label_items[3].setText('AGI')

            self.label_items[0].setStyleSheet('color: tomato')
            self.label_items[1].setStyleSheet('color: tomato')
            self.label_items[2].setStyleSheet('color: blue')
            self.label_items[3].setStyleSheet('color: green')

        else:
            self.label_location.setText('Ainda não está presente!')
            self.label_location.setStyleSheet('color: black;')

            # mapa =======================
            self.label_image_map.setStyleSheet('border: 0px solid black')
            self.pixmap_map = QPixmap('imgs/trade/map_01.jpg')
            self.pixmap_map = self.pixmap_map.scaled(260,120)
            self.label_image_map.setPixmap(self.pixmap_map)
            self.label_image_map.setEnabled(False)
            # ============================

            for i in self.labels_hours:
                i.setStyleSheet('color: black; font-size: 25px')

            for i in self.label_items:
                i.setText('')


    
    def addWidgets(self):

        self.central_layout.addLayout(self.layouts_info[0])
        self.central_layout.addLayout(self.layouts_info[1])

        # esquerda =====================================
        self.layouts_info[0].addWidget(self.label_title)
        self.layouts_info[0].addWidget(self.label_image)
        self.layouts_info[0].addWidget(self.label_location)
        self.layouts_info[0].addWidget(self.label_image_map)
        self.layouts_info[0].addWidget(self.group_items)

        for i in self.label_items:
            self.layout_group_items.addWidget(i)

        # ==============================================


        # direita ======================================
        self.layouts_info[1].addWidget(self.dropdown_hour)
        self.layouts_info[1].addLayout(self.layout_adjust_label)

        for i in self.labels_hours:
            self.layout_adjust_label.addWidget(i)

        self.layouts_info[1].addWidget(self.groupbox_hour_now)
        self.layout_groupbox_hour_now.addWidget(self.label_hour_now)
        # ==============================================

    #def paintEvent(self,event):
        #print("paintEvent foi chamado!")
        #painter = QPainter(self)
        #grad = QLinearGradient(0,0,500,0)
        #grad.setColorAt(0,QColor(10, 8, 117))
        #grad.setColorAt(1,QColor(9, 8, 59))
        #painter.fillRect(self.rect(), grad)

class QWorkerThread(QThread):

    update_signal = Signal(str)

    def run(self):
        while True:
            current_time = QTime.currentTime().toString('hh:mm:ss')
            self.update_signal.emit(current_time)
            self.sleep(1)


if __name__ == "__main__":
    app = QApplication([])
    window = LookTrade()
    window.show()
    sys.exit(app.exec())