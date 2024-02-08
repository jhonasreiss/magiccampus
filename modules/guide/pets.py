import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton,
                               QScrollArea, QComboBox, QLabel, QGroupBox)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QFont, QRadialGradient
from pets_windows.builds import BuildPet

class PetInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_init()
        self.set_widget()
        self.set_in_layout()

    def set_init(self):
        self.setWindowTitle('Pet')
        self.setFixedSize(680,600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

    def set_widget(self):
        # layouts
        self.open_window = []
        self.area_widgets = QScrollArea()
        self.area_visior = QWidget(self.area_widgets)
        self.area_widgets.setWidget(self.area_visior)
        self.area_widgets.setWidgetResizable(True)

        self.layout_header = QHBoxLayout()
        self.layout_content = QGridLayout(self.area_visior)

        # widgets
        self.dropdowns_filter = [QComboBox() for i in range(2)]
        list_type = ['Todos','Besta','Dragão','Mecânico','Planta','Demônio','Pessoa']
        list_lv = ['Todos','Lv10','Lv20','Lv50','Lv80']
        self.dropdowns_filter[0].addItems(list_type)
        self.dropdowns_filter[1].addItems(list_lv)

        # button background ===============================================
        path_images = ['Imgs/pets/01.png','Imgs/pets/02.png','Imgs/pets/03.png',
                       'Imgs/pets/04.png','Imgs/pets/05.png','Imgs/pets/06.png',
                       'Imgs/pets/07.png','Imgs/pets/08.png','Imgs/pets/09.png',
                       'Imgs/pets/10.png','Imgs/pets/11.png','Imgs/pets/12.png',
                       'Imgs/pets/13.png','Imgs/pets/14.png','Imgs/pets/15.png',
                       'Imgs/pets/16.png','Imgs/pets/17.png','Imgs/pets/18.png',
                       'Imgs/pets/19.png','Imgs/pets/20.png','Imgs/pets/21.png',
                       'Imgs/pets/22.png','Imgs/pets/23.png','Imgs/pets/24.png',
                       'Imgs/pets/25.png','Imgs/pets/26.png','Imgs/pets/27.png',
                       'Imgs/pets/28.png','Imgs/pets/29.png','Imgs/pets/30.png',
                       'Imgs/pets/31.png','Imgs/pets/36.png','Imgs/pets/37.png',
                       'Imgs/pets/33.png','Imgs/pets/32.png','Imgs/pets/38.png',
                       'Imgs/pets/39.png','Imgs/pets/35.png','Imgs/pets/34.png']
        
        self.slot_button = []
        index = 0
        for path_img in path_images:
            pixmap = QPixmap(path_img)
            layout_btn = QHBoxLayout()
            button_pet = QPushButton()
            self.slot_button.append(button_pet)
            button_pet.setLayout(layout_btn)
            label_img = QLabel()
            label_img.setPixmap(pixmap)
            label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_btn.addWidget(label_img)
            index += 1

        index = 0
        for button in self.slot_button:
            button.setFixedSize(200,300)
            button.clicked.connect(lambda _=None,idx=index: self.open_info(idx))
            index += 1
        # =================================================================
        

        self.label_filter = [QLabel() for i in range(2)]
        self.label_filter[0].setText('Tipo')
        self.label_filter[1].setText('Lv')

        for label in self.label_filter:
            label.setFixedWidth(50)


    def set_in_layout(self):
        self.central_layout.addLayout(self.layout_header)
        self.central_layout.addWidget(self.area_widgets)

        self.layout_header.addWidget(self.label_filter[0])
        self.layout_header.addWidget(self.dropdowns_filter[0])
        self.layout_header.addWidget(self.label_filter[1])
        self.layout_header.addWidget(self.dropdowns_filter[1])

        row = 1
        line = 1
        for button in self.slot_button:
            self.layout_content.addWidget(button, line, row, 1, 1)
            row += 1
            if row > 3:
                line += 1
                row = 1

    def open_info(self, id:int):
        
        #instance class
        self.open_window = WindowOpen()

        # layouts
        layout_main_info = QHBoxLayout() #layout principal [armazena as outras layouts dentro]
        layout_img_pet = QVBoxLayout() #layout onde fica a imagem do pet
        layout_info_pet = QVBoxLayout() #layout onde fica as informações do pet
        layout_img_icon = QHBoxLayout() #layout que fica dentro da layout_img_pet
        layout_name_pet = QVBoxLayout() #layout para o nome do pet

        layout_img_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_img_pet.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_name_pet.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        #groups
        group_display_pet = [QGroupBox() for i in range(2)]
        group_img_icon = QGroupBox()
        group_img_icon.setFixedSize(225,250)
        group_img_icon.setLayout(layout_img_icon)

        group_display_pet[0].setLayout(layout_img_pet)
        group_display_pet[0].setFixedWidth(250)
        group_display_pet[0].setTitle('Imagem')
        group_display_pet[1].setLayout(layout_info_pet)
        group_display_pet[1].setTitle('Informações')

        group_name_pet = QGroupBox()
        group_name_pet.setLayout(layout_name_pet)
        group_name_pet.setFixedSize(225,250)

        #dropdowns
        dropdown_pet_mode = QComboBox()
        dropdown_pet_mode.setFixedWidth(225)
        list_mode_type = ['Normal','Evoluído']
        dropdown_pet_mode.addItems(list_mode_type)

        #add widget
        layout_main_info.addWidget(group_display_pet[0])
        layout_img_pet.addWidget(group_img_icon)
        layout_img_pet.addWidget(group_name_pet)
        layout_img_pet.addWidget(dropdown_pet_mode)
        layout_main_info.addWidget(group_display_pet[1])

        label_space = QLabel()
        label_space.setFixedHeight(3)
        layout_img_pet.addWidget(label_space)

        #add layout
        self.open_window.central_layout.addLayout(layout_main_info)

        if id == 0:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/01.png','Luo Xiaomeng',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Pessoa\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 1:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/02.png','Pequena Menina Dragão',17,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Dragão\nCLASSIFICAÇÃO: Atacante Único',13,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 2:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/03.png','Charme Canção',29,'Ideal para as classes: \nSE - Soldado Engenheiro \nLA - Lutador Artista\n\nTIPO: Demônio\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 3:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/04.png','Cogumelo \nRelâmpago',20,'Ideal para as classes: \n- Todas\n- Serve apenas para caçar\n\nTIPO: Demônio\nCLASSIFICAÇÃO: Caça',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 4:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/05.png','Barbie Coelho',30,'Ideal para as classes: \nCS - Caçador do Sol\nMF - Médico da Felicidade\n\nTIPO: Pessoa\nCLASSIFICAÇÃO: Atacante \n-Único \n-Área',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 5:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/06.png','Espinhosa',30,'Ideal para as classes: \nSE - Soldade Engenheiro\nAM - Atirador Mágico\n\nTIPO: Planta\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 6:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/07.png','Princesa \nSilenciosa',20,'\nIdeal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 7:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/08.png','Tigre Dourado do Ano Novo',15,'Ideal para as classes: \nCS - Caçador do Sol\nMF - Médico da Felicidade\nME - Músico Espiritual\n\nTIPO: Besta\nCLASSIFICAÇÃO: Atacante Único',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 8:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/09.png','Abacaxi',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 9:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/10.png','Anjo Principe',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 10:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/11.png','Pequena Princesa Demônio',15,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 11:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/12.png','Dragão Divino',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 12:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/13.png','Anjo Impertinente',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 13:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/14.png','Demônio da Doçura',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 14:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/15.png','Touro do Ano Novo',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 15:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/16.png','Dragão Douding',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 16:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/17.png','Enfermeira MM',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 17:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/18.png','Besta do Guardião Elfo',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 18:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/19.png','Lobo com Pele de Ovelha',15,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 19:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/20.png','Princesa Serpente',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 20:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/21.png','Ryoko',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 21:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/22.png','Pegasus',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 22:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/23.png','Ovelha de Guerra',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 23:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/24.png','Ming',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 24:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/25.png','Leitão',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 25:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/26.png','Rato',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 26:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/27.png','Cão da Sorte',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 27:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/28.png','Wukong',30,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 28:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/29.png','Princesa de Jade',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 29:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/30.png','Princesa Ametista',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
        
        elif id == 30:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/31.png','Princesa Silenciosa 2',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 31:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/36.png','Menina Dragão',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 32:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/37.png','Irmã da Menina Dragão',15,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 33:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/33.png','Princesa Cogumelo Relâmpago',13,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 34:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/32.png','Ovelha II',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 35:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/38.png','Guarras Longas',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 36:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/39.png','Principe da Fênix',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 37:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/35.png','Boi do Ano Novo',15,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)

        elif id == 38:
            self.remove_child(layout_img_icon,layout_name_pet)
            self.adjust_icon_display('Imgs/pets/34.png','Maru',20,'Ideal para as classes: \nAM - Atirador Mágico \nLA - Lutador Artista\n\nTIPO: Máquina\nCLASSIFICAÇÃO: Suporte',15,layout_img_icon, layout_name_pet)
            self.adjust_information_display('01_status.png',layout_info_pet,id)
                

        #show window
        self.open_window.show()


    def remove_child(self, parent_target:list, second_target:list):
        try:
            if parent_target.count() > 0:
                item = parent_target.takeAt(0)
                widget = item.widget()
                widget.setParent(None)

            while second_target.count():
                item = second_target.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
        except TypeError as err:
            print(f'Erro ocorrido por não haver filho dentro da layout: {err}')


    def adjust_icon_display(self, path_img_dir:str, pet_name_str:str, size_name_font:int, description:str, size_description_font: int, layout_ref_img, layout_ref_name_pet):
        
        # imagem
        pixmap = QPixmap(path_img_dir)
        label_img = QLabel()
        label_img.setPixmap(pixmap)

        # nome do pet
        self.label_name = QLabel(pet_name_str)
        self.label_name.setStyleSheet(f'font-size: {size_name_font}px')
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
        # descrição
        label_description = QLabel(description)
        label_description.setStyleSheet(f'font-size: {size_description_font}px')
        label_description.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # titulo da janela
        self.open_window.setWindowTitle(f'Informações de {self.label_name.text()}')

        # adicionando widgets
        layout_ref_img.addWidget(label_img)
        layout_ref_name_pet.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_ref_name_pet.addWidget(self.label_name)
        layout_ref_name_pet.addWidget(label_description)


    def adjust_information_display(self, path_img_status, layout_ref:QVBoxLayout, index):
        pixmap_status = QPixmap(f'Imgs/graph_pet/{path_img_status}')
        label_img = QLabel()
        label_img.setPixmap(pixmap_status)
        label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_name_skill = QLabel()
        label_description_skill = QLabel()

        # abre 2 janelas ===============================================
        button_build_system = QPushButton('Build')
        button_build_system.setFixedHeight(55)

        button_get_pet = QPushButton('Onde Conseguir')
        button_get_pet.setFixedHeight(55)
        # ==============================================================

        group_natural_skills = QGroupBox(' Magia Nativa ')
        group_natural_skills.setFixedHeight(98)
        group_description_skill = QGroupBox(' Descrição ')
        group_description_skill.setFixedSize(250,120)

        layout_group_skills = QHBoxLayout()
        layout_description_skill = QVBoxLayout()
        layout_description_skill.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_package_pet = QVBoxLayout()

        if index == 0:
            button_build_system.clicked.connect(lambda: self.open_build(1,'Luo Xiaomeng'))
            list_ref_ico = ['Imgs/natural_skill/unicornio_01.jpg','Imgs/natural_skill/unicornio_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Chifre Consagrado - ATIVAR',f'Gasta 60% de MP e cura 1 alvo, \ntambém possui 10% de chance \nde limpar debuff.',label_name_skill,label_description_skill), lambda: self.description_skill('Vitalidade 100x - ATIVAR',f'Gasta 12% de MP e cura 10 alvos!',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 1:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/empregada_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Feitiço do Dragão - ATIVAR',f'65% de causar 250% de dano mágico\na 1 alvo e 50% de chance\nde curar ou dar dano no alvo.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 2:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/charme_canção_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('A Alma está Presa - ATIVAR',f'70% de chance de acerto\nImpede o alvo de receber\ncura e ser ressucitado.\nDura 2 Rodadas',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 3:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/cogumelo_relâmpago_01.jpg','Imgs/natural_skill/cogumelo_relâmpago_02.jpg','Imgs/natural_skill/cogumelo_relâmpago_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Fúria do Trovão - ATIVAR',f'Ocasiona dano fixo em 10 alvos\n(1061 - 1624) de dano mágico.',label_name_skill,label_description_skill),lambda: self.description_skill('Faícas de Relâmpago - ATIVAR',f'Desfere 75% de dano mágico a 1 alvo.',label_name_skill,label_description_skill),lambda: self.description_skill('Recargas de Relâmpago - ATIVAR',f'Restaura o HP em:\n([11-12]vezes os pontos em espirito)\n1 alvo.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 4:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/barbie_coelho_01.jpg','Imgs/natural_skill/barbie_coelho_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Aura Sortuda - ATIVAR',f'Gasta 60% de MP\nColoca escudo em 2 Alvos\nResiste a 3 ataques.\nDura 4 Rodadas',label_name_skill,label_description_skill),lambda: self.description_skill('Coração Batendo - ATIVAR',f'Ocasiona 120% de Dano Mágico em 1 alvo\npossui chance adicional de atacar\nnovamente de forma crítica e com\ndano multiplicado.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 5:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/cici_01.jpg','Imgs/natural_skill/cici_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Pluma Espinhosa - ATIVAR',f'Reduz todo o dano causado\npelo alvo em 30%.\nDura 3 Rodadas',label_name_skill,label_description_skill),lambda: self.description_skill('Espelho - ATIVAR',f'Reflete parte do dano ao atacante\ne reduz uma parte do dano recebido\ndo atacante.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 6:
            button_build_system.clicked.connect(lambda: self.open_build(2, 'Princesa Silenciosa'))
            list_ref_ico = ['Imgs/natural_skill/princesa_silenciosa_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Tática tentadora - ATIVAR',f'60% de chance de ocasionar confusão em \n2 alvos.\nDura 2 Rodadas',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 7:
            button_build_system.clicked.connect(lambda: self.open_build(0))
            list_ref_ico = ['Imgs/natural_skill/tigre_dourado_do_ano_novo_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Sede de Sangue - PASSIVA',f'Cada dano que você causar\n10% desse dano retorna para\nrestaurar seu HP.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)
            
        elif index == 8:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/abacaxi_01.jpg','Imgs/natural_skill/abacaxi_02.jpg','Imgs/natural_skill/abacaxi_01.jpg','Imgs/natural_skill/abacaxi_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Espinhos Venenosos Grupais - ATIVAR',f'77% chance de envenenar 4 alvos\ndebuff de envenamento reduz 0.3%\nde ataque mágico em dano no alvo.\nDura 3 Rodadas',label_name_skill,label_description_skill), 
                                    lambda: self.description_skill('Proteção da Natureza Grupal - ATIVAR',f'Aumenta a defesa física e mágica de 4\nem 1000 e recupera certa quantidade\nde HP por rodada.\nDura 4 Rodadas',label_name_skill,label_description_skill), 
                                    lambda: self.description_skill('Espinhos Venenosos Individual - ATIVAR',f'88% chance de envenenar 1 alvo\ndebuff de envenamento reduz 0.3%\nde ataque mágico em dano no alvo.\nDura 3 Rodadas',label_name_skill,label_description_skill), 
                                    lambda: self.description_skill('Proteção da Natureza Individual - ATIVAR',f'Aumenta a defesa física e mágica de 1 alvo\nem 1000 e recupera certa quantidade\nde HP por rodada.\nDura 4 Rodadas',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 9:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/principe_anjo_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Aprimoramento de Fé - ATIVAR',f'Consome 90% do próprio HP e MP\nAumenta bastante: velocidade, crítico e\nredução física e mágica.\nDura 5 Rodadas',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 10:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/princesa_demonio_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Bombardeio de Energia - ATIVAR',f'Desfere dano fixo a 10 alvos.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 11:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/dragão_divino_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Contra-Ataque Intermediário - PASSIVA',f'Aumenta permanentemente sua taxa de\ncontra-ataque em 5%.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 12:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/anjo_impertinente_01.jpg','Imgs/natural_skill/anjo_impertinente_02.jpg','Imgs/natural_skill/anjo_impertinente_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Palavra Melosa - ATIVAR',f'Desfere dano a 10 alvos equivalente a\n100 - 134 de dano fixo.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Glória do Cupido - ATIVAR',f'Restaura o HP em 6x os pontos em espiríto.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Flecha do Cupido - ATIVAR',f'Desfere em 1 alvo dano equivalente\na 45% de ataque mágico.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 13:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/demonio_doçura_01.jpg','Imgs/natural_skill/demonio_doçura_02.jpg','Imgs/natural_skill/demonio_doçura_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Flecha do Demônio - ATIVAR',f'Desfere dano a 1 alvo equivalente a\n110% de ataque mágico.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Truque de Amor - ATIVAR',f'Desfere dano a 2 alvos equivalente a\n70% de ataque mágico.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Palavra Melosa - ATIVAR',f'Desfere dano a 10 alvos equivalente a\n100 - 134 de dano fixo.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 14:
            button_build_system.clicked.connect(lambda: self.open_build(0))
            buttons_natural_skills = []

        elif index == 15:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/dragão_bebê_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Contra-Ataque Intermediário - PASSIVA',f'Aumenta permanentemente sua taxa de\ncontra-ataque em 5%.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 16:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/enfermeiraMM_01.jpg','Imgs/natural_skill/enfermeiraMM_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Cura Amorosa - ATIVAR',f'Recupera HP de 1 alvo em \n13,5x pontos em espiríto.\n',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Escudo Amoroso - ATIVAR',f'Ao receber ataque mágico recupera\naté 12% do HP máximo.\nDura 3 Rodadas.',label_name_skill,label_description_skill),]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 17:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/besta_guardian_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Cuidados Especiais - ATIVAR',f'Protege 1 alvo e diminui a defesa física em\n50% e aumenta a taxa de contra-ataque\nem 5%.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 18:
            button_build_system.clicked.connect(lambda: self.open_build(0))
            buttons_natural_skills = []

        elif index == 19:
            button_build_system.clicked.connect(lambda: self.open_build(0))
            list_ref_ico = ['Imgs/natural_skill/kiki_01.jpg','Imgs/natural_skill/kiki_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Herança Naga - PASSIVA',f'Cada ataque desferido possui 10% de\nchance de causar debuff aleatório em\n1 alvo. debuff: (corta-cura, queima de MP)\nDura 1 Rodada',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Sangue Louco - ATIVAR',f'Se seu HP estiver em 70% ou menos\nvai ocasionar 235% de ataque físico\nse estiver com 30% de HP vai ocasionar\n265% de ataque físico.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 20:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/ryoko_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Escudo Mágico - ATIVAR',f'Gasta 60% de MP máximo e cria um escudo sobre\n1 alvo e suporta 3 ataques, o dano dos ataques\nsuportados é igual a 50% do MP do conjurador\nDura 4 Rodadas.',label_name_skill,label_description_skill,font_size=10)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 21:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/pegasus_01.jpg','Imgs/natural_skill/pegasus_02.jpg','Imgs/natural_skill/pegasus_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Contra-Feitiço - PASSIVA',f'Quando atacado possui chance de \ncontra-atacar usando a magia \nCRIAÇÃO DE PAUSA.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('A Trajetória de Deus - PASSIVA',f'Quando atacado possui 7% de chance\nde não sofrer dano.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Criação de Pausa - ATIVAR',f'Causa dano equivalente a 220% de ataque \nmágico em 1 alvo.',label_name_skill,label_description_skill),]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 22:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/ovelha_de_guerra_01.jpg','Imgs/natural_skill/ovelha_de_guerra_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Punho de Choque - ATIVAR',f'Reduz o livrar da morte de 1 alvo em 10 e desfere\ndano equivalente a 150% do ataque físico.\nPossui chance de buffar o alvo com bonus\nde 5% de ataque duplo.',label_name_skill,label_description_skill, font_size=10),
                                    lambda: self.description_skill('Corpo de Ferro - PASSIVA',f'Aumenta em 5 o livrar da morte e o anti-crítico.',label_name_skill,label_description_skill,font_size=10)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 23:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/ming_01.jpg','Imgs/natural_skill/ming_02.jpg','Imgs/natural_skill/ming_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Pêssego - ATIVAR',f'Restaura o HP equivalente a 95% do ataque \nmágico e possui uma certa chance de \nreceber o debuff de recuperação de HP.\nDura 2 Rodadas',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Nirvana - PASSIVA',f'Ao usar a mágia PÊSSEGO possui uma\ncerta chance de ativar o debuff\nde melhora de defesa.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Deus Abençoe - PASSIVA',f'Aumento na chance de ganho de prêmios.',label_name_skill,label_description_skill),]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 24:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/leitão_01.jpg','Imgs/natural_skill/leitão_02.jpg','Imgs/natural_skill/leitão_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Fortalecer a Voz - ATIVAR',f'Ocasiona dano equivalente a 100% do ataque\nmágico e possui uma certa chance de ocasionar\npânico no alvo. Pânico reduz HP do alvo equivalente\na 16% do ataque mágico do conjurador.\nDura 3 Rodadas',label_name_skill,label_description_skill,font_size=9),
                                    lambda: self.description_skill('Corpo do Porco Dourado - PASSIVA',f'A cada rodada adiciona um escudo no alvo\ncom menor % de HP e absorva 10% do dano \nbaseado na mana do conjurador.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Ciclo da Vida - PASSIVA',f'Possui 50% de chance de curar 1 alvo \ncom menor % de HP na equipe em um\ntotal equivalente a 10% do ataque mágico\ndo conjurador.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 25:
            button_build_system.clicked.connect(lambda: self.open_build(0))
            list_ref_ico = ['Imgs/natural_skill/rato_01.jpg','Imgs/natural_skill/rato_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Balde de Ouro - PASSIVA',f'Quanto menor for a % do HP mais o\ndano final ele dará em sua habilidade.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Balde de Riqueza - PASSIVA',f'Após eliminar o alvo com seu ataque\nrecupera 15% do seu HP máximo.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 26:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/cão_da_sorte_01.jpg','Imgs/natural_skill/cão_da_sorte_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Ling - ATIVAR',f'Causa dano fixo, quanto maior o nível maior o dano,\napós o uso aumentará a resistência a debuff em 1\nrodada quando houver possibilidade ele colocará\num debuff no alvo por 1 rodada.',label_name_skill,label_description_skill,10),
                                    lambda: self.description_skill('Remanescente - ATIVAR',f'Se atacar o alvo com debuff do Ling usando\nessa magia e não matar o alvo você ficará\ncom tontura.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 27:
            button_build_system.clicked.connect(lambda: self.open_build(0))
            list_ref_ico = ['Imgs/natural_skill/variedade_01.jpg','Imgs/natural_skill/variedade_02.jpg','Imgs/natural_skill/variedade_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Cajado de Wukong - ATIVAR',f'Ataca 1 alvo causando dano equivalente \na 140% de ataque físico podendo ocasionar \nalgum desses debuffs: \n(tontura, envenenamento, fraqueza).',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Dança Inigualável - PASSIVA',f'Depois de matar algum alvo usando a magia \nCAJADO DE WUKONG ele irá efetuar \noutro ataque acertando 1 alvo aleatório.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Transposição de Mudança - PASSIVA',f'Possui uma certa chance de limpar \ntodos os debuffs do corpo.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 28:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/jade_01.jpg','Imgs/natural_skill/jade_02.jpg','Imgs/natural_skill/jade_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Nove Fases do Dragão - ATIVAR',f'Abençoa todos os aliados. Os aliados que estão sob \na benção recebem um aumento de 5% de ataque \nduplo, 10% de defesa dupla e 10% de limite de HP. \nDura 3 Rodadas',label_name_skill,label_description_skill,10),
                                    lambda: self.description_skill('Poder do Dragão - PASSIVA',f'Aumento permanente de 100 de velocidade, \n5% de lesão física e 5% de lesão mágica.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Sopro da Destruição - ATIVAR',f'Ocasiona dano equivalente a 160% de ataque \nmágico em 3 alvos e possui 50% de chance de \ncausar tontura. Dura 1 Rodada',label_name_skill,label_description_skill,10)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 29:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/ametista_01.jpg','Imgs/natural_skill/ametista_02.jpg','Imgs/natural_skill/ametista_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Nether Basalt - ATIVAR',f'Causa dano iagual a 25% do Ataque + 15% \ndo limite de HP em 4 alvos. Possui 50% de \nchance de causar tontura nos alvos. \nDura 1 Rodada',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Ataque de Dissuasão - ATIVAR',f'Atinge 4 alvos inimigos e causa redução de \nataque e velocidade em 5%, possui 10% de \nchance de limpar 1 buff do inimigo.\nDura 1 Rodada',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Tempo de Caça - ATIVAR',f'Aumenta a velocidade e o acerto em 10% em \n10 alvos. \nDura 5 Rodadas',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 30:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/princesa_silenciosa2_01.jpg','Imgs/natural_skill/princesa_silenciosa2_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Defensor - PASSIVA',f'Quando recebe cura aumenta em 25% os \nefeitos da cura.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Visão Realmente Paralisada - ATIVAR',f'Possui 65% de chance de debuffar 4 alvos \ncom petroquímica. \nDura 2 Rodadas',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 31:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/menina_dragão_01.jpg','Imgs/natural_skill/menina_dragão_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Pupila Congelante - PASSIVA',f'Aumenta em 5% a chance de debuffar \n(envenenamento, ironia, sono, \nconfusão, petroquimica e tontura).',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Net Alma da Camisa - PASSIVA',f'Reduz uma certa quantidade de defesa e \naumenta o acerto.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 32:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/irmã_dragão_01.jpg','Imgs/natural_skill/irmã_dragão_02.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Magia de Purificação - PASSIVA',f'Possui uma chance de limpar debuff do \ncorpo.',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Resistência Dracônica - PASSIVA',f'25% de chance de aumentar a resistência a \nDebuff.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 33:
            button_build_system.clicked.connect(lambda: self.open_build(1))
            list_ref_ico = ['Imgs/natural_skill/cogumelo_relâmpago_01.jpg','Imgs/natural_skill/cogumelo_relâmpago_02.jpg','Imgs/natural_skill/cogumelo_relâmpago_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Fúria do Trovão - ATIVAR',f'Ocasiona dano fixo em 10 alvos\n(1061 - 1624) de dano mágico.',label_name_skill,label_description_skill),lambda: self.description_skill('Faícas de Relâmpago - ATIVAR',f'Desfere 75% de dano mágico a 1 alvo.',label_name_skill,label_description_skill),lambda: self.description_skill('Recargas de Relâmpago - ATIVAR',f'Restaura o HP em:\n([11-12]vezes os pontos em espirito)\n1 alvo.',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 34:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/ovelha_01.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Bombardear - ATIVAR',f'Possui 60% de chance de por 4 alvos em \ntontura.\nDura 0 Rodada',label_name_skill,label_description_skill)]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 35:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            buttons_natural_skills = []

        elif index == 36:
            button_build_system.clicked.connect(lambda: self.open_build(2))
            list_ref_ico = ['Imgs/natural_skill/fenix_01.jpg','Imgs/natural_skill/fenix_02.jpg','Imgs/natural_skill/fenix_03.jpg']
            buttons_natural_skills = [QPushButton() for i in range(list_ref_ico.__len__())]
            list_set_description = [lambda: self.description_skill('Golpe Brutal - ATIVAR',f'Causa dano igual a 120% do ataque e \npossui 20% de chance de adicionar redução \nem 50% na defesa e velocidade do alvo. \nDura 1 Rodada',label_name_skill,label_description_skill),
                                    lambda: self.description_skill('Batismo de Luz - ATIVAR',f'Há uma chance de remover debuff de 2 aliados \ne adicionar buff de meditação, meditação aumenta \nresistência a debuff em 10%. \nDura 3 Rodadas',label_name_skill,label_description_skill,10),
                                    lambda: self.description_skill('Coração de Pedra - PASSIVA',f'Cada rodada remove 1 debuff.',label_name_skill,label_description_skill),]
            index = 0
            for i in buttons_natural_skills:
                i.clicked.connect(list_set_description[index])
                index += 1
            self.icon_set_skill(buttons_natural_skills, list_ref_ico)

        elif index == 37: 
            button_build_system.clicked.connect(lambda: self.open_build(0))
            buttons_natural_skills = []

        elif index == 38:
            button_build_system.clicked.connect(lambda: self.open_build(0))
            buttons_natural_skills = []
            
        else:
            buttons_natural_skills = [QPushButton() for i in range(2)]

        # limpa skill
        while layout_group_skills.count():
                item = layout_group_skills.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
        # ======================================

        group_natural_skills.setLayout(layout_group_skills)
        group_description_skill.setLayout(layout_description_skill)
        

        if buttons_natural_skills is not None:
            for i in buttons_natural_skills:
                i.setFixedSize(50,50)
                layout_group_skills.addWidget(i)
        
        layout_description_skill.addWidget(label_name_skill)
        layout_description_skill.addWidget(label_description_skill)

        layout_ref.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_ref.addWidget(label_img)
        layout_ref.addWidget(group_natural_skills)
        layout_ref.addWidget(group_description_skill)
        layout_ref.addWidget(button_build_system)
        layout_ref.addWidget(button_get_pet)

    # botões das magias nativas
    def icon_set_skill(self, button_ref:list, list_path:list):
        
        pixmap_ico_skill = [QPixmap() for i in range(list_path.__len__())]
        label_ico_skill = [QLabel() for i in range(list_path.__len__())]
        layout_ico_skill = [QHBoxLayout() for i in range(list_path.__len__())]

        
        for i in range(list_path.__len__()):

            pixmap_ico_skill[i].load(list_path[i])
            pixmap_ico_skill[i] = pixmap_ico_skill[i].scaled(48,48)

            label_ico_skill[i].setPixmap(pixmap_ico_skill[i])
            label_ico_skill[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_ico_skill[i].setFixedSize(48,48)
            label_ico_skill[i].setStyleSheet('''QLabel{
                                                        border: 2px solid black;
                                                    }
                                                 
                                                    QLabel:hover{
                                                        border: 2px solid blue;
                                                    }
                                                ''')

            layout_ico_skill[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_ico_skill[i].setContentsMargins(0,0,0,0)
            layout_ico_skill[i].addWidget(label_ico_skill[i])

            button_ref[i].setLayout(layout_ico_skill[i])
            button_ref[i].setContentsMargins(0,0,0,0)

    # ================================================================================

    def description_skill(self, name_skill: str,description: str, name_label: QLabel, description_label: QLabel, font_size: int=11):
        font_bold = QFont()
        font_bold.setBold(True)
        name_label.setFont(font_bold)
        name_label.setText(name_skill)
        description_label.setText(description)
        description_label.setStyleSheet(f'font-size: {font_size}px')

    def open_build(self, index, name_build=None):
        self.window_build = BuildPet(index,self.label_name.text(),name_build)
        self.window_build.show()


class WindowOpen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(550,600)
        self.setWindowTitle('Info')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PetInterface()
    window.show()
    sys.exit(app.exec())