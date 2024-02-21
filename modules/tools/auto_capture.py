import sys, os
import pyautogui
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton,
                               QSpinBox, QComboBox, QProgressBar, QGroupBox, QCheckBox, QMessageBox)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QPixmap

class CaptureWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_set()
        self.adjust_elements()


    def init_set(self):
        os.system('cls')
        self.setFixedSize(400,430)
        self.setWindowTitle('Captura Automática')
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)


    def adjust_elements(self):
        # 2 layouts principais ficará um acima do outro
        self.group_pattern = [QGroupBox() for i in range(2)]
        self.group_progess = QGroupBox(' Progresso ')
        self.group_progess.setContentsMargins(0,10,0,0)
        self.group_progess.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_progress = QHBoxLayout()
        self.group_progess.setLayout(self.layout_progress)
        self.group_progess.setFixedHeight(80)
        self.layout_pattern = [QHBoxLayout() for i in range(2)]
        self.layout_options = [QVBoxLayout() for i in range(2)]
        self.layout_icon_mob = QHBoxLayout()
        self.group_pattern[0].setTitle('Opções')
        self.group_pattern[1].setTitle('Item de Captura')
        
        # itens de captura
        self.layout_item_use = [QHBoxLayout() for _ in range(2)]
        self.group_item_use = [QGroupBox() for _ in range(2)]

        self.group_item_use[0].setTitle('( % ) de Captura')
        self.group_item_use[1].setTitle('Pontos de Captura')

        self.button_item_id = [QPushButton() for i in range(4)]

        pixmap_item = [QPixmap() for i in range(4)]
        label_item = [QLabel() for i in range(4)]
        layout_item = [QHBoxLayout() for i in range(4)]

        list_path_item = ['Imgs/mobs_img/cap_01.jpg','Imgs/mobs_img/cap_02.jpg','Imgs/mobs_img/cap_03.jpg','Imgs/mobs_img/cap_04.jpg']

        for i in range(4):
            pixmap_item[i].load(list_path_item[i])
            pixmap_item[i] = pixmap_item[i].scaled(40,40)
            label_item[i].setPixmap(pixmap_item[i])
            label_item[i].setFixedSize(40,40)
            label_item[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_item[i].setStyleSheet('''
                                            QLabel{
                                                border: 2px solid black;
                                            }
                                         
                                            QLabel:hover{
                                                border: 2px solid green;
                                            }
                                        ''')
            layout_item[i].addWidget(label_item[i])
            layout_item[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_item[i].setContentsMargins(0,0,0,0)
            self.button_item_id[i].setLayout(layout_item[i])

        self.layout_item_use[0].addWidget(self.button_item_id[0])
        self.layout_item_use[0].addWidget(self.button_item_id[1])
        self.layout_item_use[1].addWidget(self.button_item_id[2])
        self.layout_item_use[1].addWidget(self.button_item_id[3])

        index = 0
        for i in self.button_item_id:
            i.setFixedSize(40,40)
            index += 1

        index = 0
        for i in self.group_item_use:
            i.setAlignment(Qt.AlignmentFlag.AlignCenter)
            i.setLayout(self.layout_item_use[index])
            index += 1

        # componentes
        self.dropdown_map = QComboBox()
        list_map = ['Pantanal das Nuvens','Espaço Zen','Subúrbio Leste','Lago do Sol Norte','Ilha do Sol','Pradaria Ta-Ke','Areia do Mar Vago',
                    'Vila do Sol','Lago do Sol Sul','Floresta Yu-Feng','Caminho do Bambu','Terra das Rochas Mágicas','Bacia do Vale LingLan',
                    'Vale do Demônio','Terra da Luz Perdida','Terra das Ilusões','Terra das Promessas','Oasis do Ceú','Pantanal Proibido',
                    'Caminho dos Raivosos','Abismo da Calmaria','Terra da Escalada a Nuvem','Duo-la Neve','Paraíso da Sakura Dançante',
                    'Campo da Rocha Gelada','Meilin Nevada','Abismo Polar','Planalto do Sol Nascente','Floresta Adormecida','Montanhas yun-Lu',
                    'Terra do Guardião','Antigas Ruínas','Aldeia Solitária','Selva Encantada','Templo Espiritual','Campo de Neve','Porto Noturno',
                    'Ilha da Morte','Cidade Caída','Cidade do Céu']
        self.dropdown_map.addItems(list_map)
        self.progress_bar = QProgressBar()
        self.label_hunter = QLabel('Caça Automática?')
        self.label_capture = QLabel('Quantidade de Captura')
        self.check_hunter = QCheckBox()
        self.spin_capture = QSpinBox()
        self.spin_capture.setMinimum(0)
        self.spin_capture.setMaximum(99)
        self.check_hunter.setText('Ativar')
        self.button_start = QPushButton('Começar')
        self.button_start.clicked.connect(self.finished_task)
        self.layout_options[0].setContentsMargins(15,0,15,5)

        #layouts
        self.button_item_capture = [QPushButton() for i in range(4)]
        self.layout_options[0].addWidget(self.label_hunter)
        self.layout_options[0].addWidget(self.check_hunter)
        self.layout_options[0].addWidget(self.label_capture)
        self.layout_options[0].addWidget(self.spin_capture)
        self.layout_options[0].addWidget(self.button_start)

        self.layout_options[1].addWidget(self.dropdown_map)
        self.layout_options[1].addLayout(self.layout_icon_mob)

        #styles
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet('''
                                            QProgressBar::Chunk
                                            {
                                                background-color: blue;
                                                
                                            }
                                            QProgressBar
                                            {
                                                border: 1px solid black;
                                                color: black;
                                                text-align: center;
                                            }
                                        
                                        ''')
        

        for i in self.button_item_capture:
            i.setFixedSize(80,80)

        for i in self.layout_options:
            self.layout_pattern[0].addLayout(i)
            

        index = 0
        for i in self.group_pattern:
            i.setLayout(self.layout_pattern[index])
            self.central_layout.addWidget(i)
            index += 1

        index = 0
        for i in self.group_item_use:
            i.setFixedSize(160,110)
            self.layout_pattern[1].addWidget(i)
            index += 1
    

        self.central_layout.addWidget(self.group_progess)
        self.layout_progress.addWidget(self.progress_bar)
        

        self.index_icon_mob()
        self.dropdown_map.currentIndexChanged.connect(self.index_icon_mob)


    def finished_task(self):
        message = QMessageBox(self)
        message.setFixedSize(300, 200)
        message.setWindowTitle('Tarefa Finalizada')
        
        label_message = QLabel('Sua tarefa de captura automática\nfoi concluída com sucesso!')
        label_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout_message = QVBoxLayout()
        layout_message.addWidget(label_message)
        message.setLayout(layout_message)

        message.exec()


    def index_icon_mob(self):
        index = self.dropdown_map.currentIndex()
        
        if index == 0:
            path_image_mob = []
            id_path = [1,2,3,4]
            self.insert_path_list(f'Imgs/mobs_img/0{id_path[0]}.jpg',f'Imgs/mobs_img/0{id_path[1]}.jpg',f'Imgs/mobs_img/0{id_path[2]}.jpg',f'Imgs/mobs_img/0{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 1:
            path_image_mob = []
            id_path = [5,6,7,8]
            self.insert_path_list(f'Imgs/mobs_img/0{id_path[0]}.jpg',f'Imgs/mobs_img/0{id_path[1]}.jpg',f'Imgs/mobs_img/0{id_path[2]}.jpg',f'Imgs/mobs_img/0{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 2:
            path_image_mob = []
            id_path = [9,10,11,12]
            self.insert_path_list(f'Imgs/mobs_img/0{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 3:
            path_image_mob = []
            id_path = [13,14,15,16]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 4:
            path_image_mob = []
            id_path = [17,18,19,20]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 5:
            path_image_mob = []
            id_path = [21,22,23,24]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 6:
            path_image_mob = []
            id_path = [25,26,27,28]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 7:
            path_image_mob = []
            id_path = [29,30,31,32]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 8:
            path_image_mob = []
            id_path = [33,34,35,36]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 9:
            path_image_mob = []
            id_path = [37,38,39,40]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 10:
            path_image_mob = []
            id_path = [41,42,43,44]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 11:
            path_image_mob = []
            id_path = [45,46,47,48]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 12:
            path_image_mob = []
            id_path = [49,50,51,52]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 13:
            path_image_mob = []
            id_path = [53,54,55,56]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 14:
            path_image_mob = []
            id_path = [57,58,59,60]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 15:
            path_image_mob = []
            id_path = [61,62,63,64]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 16:
            path_image_mob = []
            id_path = [65,66,67,68]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 17:
            path_image_mob = []
            id_path = [69,70,71,72]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 18:
            path_image_mob = []
            id_path = [73,74,75,76]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 19:
            path_image_mob = []
            id_path = [77,78,79,80]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 20:
            path_image_mob = []
            id_path = [81,82,83,84]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 21:
            path_image_mob = []
            id_path = [85,86,87,88]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 22:
            path_image_mob = []
            id_path = [89,90,91,92]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 23:
            path_image_mob = []
            id_path = [93,94,95,96]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 24:
            path_image_mob = []
            id_path = [97,98,99,100]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 25:
            path_image_mob = []
            id_path = [101,102,103,104]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 26:
            path_image_mob = []
            id_path = [105,106,107,108]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 27:
            path_image_mob = []
            id_path = [109,110,111,112]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 28:
            path_image_mob = []
            id_path = [113,114,115,116]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 29:
            path_image_mob = []
            id_path = [117,118,119,120]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 30:
            path_image_mob = []
            id_path = [121,122,123,124]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 31:
            path_image_mob = []
            id_path = [125,126,127,128]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 32:
            path_image_mob = []
            id_path = [129,130,131,132]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 33:
            path_image_mob = []
            id_path = [133,134,135,136]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 34:
            path_image_mob = []
            id_path = [137,138,139,140]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 35:
            path_image_mob = []
            id_path = [141,142,143,144]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 36:
            path_image_mob = []
            id_path = [145,146,147,148]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 37:
            path_image_mob = []
            id_path = [149,150,151,152]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 38:
            path_image_mob = []
            id_path = [153,154,155,156]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        elif index == 39:
            path_image_mob = []
            id_path = [157,158,159,160]
            self.insert_path_list(f'Imgs/mobs_img/{id_path[0]}.jpg',f'Imgs/mobs_img/{id_path[1]}.jpg',f'Imgs/mobs_img/{id_path[2]}.jpg',f'Imgs/mobs_img/{id_path[3]}.jpg',list_path=path_image_mob)
            self.load_info(path_image_mob)

        


    def load_info(self, path_ref:list):

        try:
            while self.layout_icon_mob.count():
                item = self.layout_icon_mob.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
        except:
            pass

        button_mob_icon = [QPushButton() for i in range(4)]
        for _ in button_mob_icon:
            _.setFixedSize(50,50)
            self.layout_icon_mob.addWidget(_)

        pixmap = [QPixmap() for i in range(4)]
        layout_img = [QHBoxLayout() for i in range(4)]
        label_img = [QLabel() for i in range(4)]

        for i in range(4):
            pixmap[i].load(path_ref[i])
            pixmap[i] = pixmap[i].scaled(50,50)
            label_img[i].setFixedSize(50,50)
            label_img[i].setPixmap(pixmap[i])
            label_img[i].setStyleSheet('''
                                            QLabel{
                                                border: 3px solid black;
                                            }
                                       
                                            QLabel:hover{
                                                border: 3px solid blue;
                                            }
                                        ''')
            layout_img[i].addWidget(label_img[i])
            label_img[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_img[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_img[i].setContentsMargins(0,0,0,0)
            button_mob_icon[i].setLayout(layout_img[i])


    def insert_path_list(self, *args, list_path:list):
        for i in args:
            list_path.append(i)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaptureWindow()
    window.show()
    sys.exit(app.exec())