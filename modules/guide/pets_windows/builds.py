import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton,
                               QScrollArea, QComboBox, QLabel, QGroupBox, QTabWidget)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QFont, QRadialGradient, QPen

class BuildPet(QMainWindow):
    def __init__(self, index=0, name_title=None, name_id=None):
        super().__init__()
        self.index = index
        self.name_title = name_title
        self.name_id = name_id
        self.set_init()
        self.definition_group(index)
        self.magic_build(name_id)


    def set_init(self):
        if self.name_title == None:
            self.setWindowTitle('BUILD')
        else:
            self.setWindowTitle(f'BUILD de {self.name_title}')
        self.setFixedSize(1100,670)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)

    def definition_group(self,index):
        self.central_layout.setSpacing(20)
        self.central_layout.setContentsMargins(20,20,20,20)
        self.tab_book = QTabWidget()

        # groups
        self.group_builds = [QGroupBox() for i in range(2)]
        self.group_builds[0].setFixedHeight(200)
        self.group_builds[1].setFixedSize(700,200)

        # layouts
        self.layout_builds = [QVBoxLayout() for i in range(2)]
        self.layout_builds_magic = QHBoxLayout()
        self.layout_button_assets = QHBoxLayout()
        list_build = [' Pontos ',' Equipamento ']


        for group in range(2):
            self.group_builds[group].setTitle(list_build[group])
            self.group_builds[group].setLayout(self.layout_builds[group])
        
        # adicionando na layout principal
        self.central_layout.addWidget(self.group_builds[0],1,1,1,1)
        self.central_layout.addWidget(self.group_builds[1],1,2,1,1)
        self.central_layout.addWidget(self.tab_book,2,1,1,2)
 

        
        if index == 0:
            self.equipment_build(index)
        elif index == 1:
            self.equipment_build(index)
        elif index == 2:
            self.equipment_build(index)

        else:
            print("Não existe nenhum set nesse indice!")
        

    def points_build(self):
        pass

    def equipment_build(self, index):
        button_equipment = [QPushButton() for i in range(8)]

        # tratamento de fonte
        label_set_description = QLabel()
        font = QFont()
        font.setBold(True)
        font.setPixelSize(20)
        label_set_description.setFont(font)
        label_set_description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if index == 0:
            label_set_description.setText("SET - LUA SANGRENTA - FOCADO EM DANO FÍSICO")
        if index == 1:
            label_set_description.setText("SET - TROVÃO ROXO - FOCADO EM DANO MÁGICO")
        if index == 2:
            label_set_description.setText("SET - NUVEM VERDE - FOCADO EM TANKAR DANO")
        

        # adicionando imagem no button
        label_img = [QLabel() for i in range(8)]
        pix_img = [QPixmap() for i in range(8)]
        layout_set_img = [QHBoxLayout() for i in range(8)]

        for i in range(8):
            pix_img[i].load(self.list_img_path(index)[i])
            pix_img[i] = pix_img[i].scaled(48,48)

            label_img[i].setPixmap(pix_img[i])
            label_img[i].setFixedSize(48,48)
            label_img[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_img[i].setStyleSheet('''
                                       QLabel
                                       {
                                            border: 2px solid black;
                                       }

                                       QLabel:hover
                                       {
                                            border: 2px solid orange;
                                       }
                                       ''')
            
            layout_set_img[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_set_img[i].setContentsMargins(0,0,0,0)
            layout_set_img[i].addWidget(label_img[i])
            button_equipment[i].setLayout(layout_set_img[i])

        for button in button_equipment:
            button.setFixedSize(50,50)
            self.layout_button_assets.addWidget(button)

        # adicionando na layout de equipamento
        label_space = [QLabel() for i in range(2)]
        self.layout_builds[1].addWidget(label_space[0])
        self.layout_builds[1].addLayout(self.layout_button_assets)
        self.layout_builds[1].addWidget(label_set_description)
        self.layout_builds[1].addWidget(label_space[1])


    def magic_build(self,id):
        self.set_icon_book(id)


    def list_img_path(self, index):
        if index == 0:
            list_equipment = ['Imgs/equipment_pet/red/01.jpg',
                              'Imgs/equipment_pet/red/02.jpg',
                              'Imgs/equipment_pet/red/03.jpg',
                              'Imgs/equipment_pet/red/04.jpg',
                              'Imgs/equipment_pet/red/05.jpg',
                              'Imgs/equipment_pet/red/06.jpg',
                              'Imgs/natural_skill/kiki_01.jpg',
                              'Imgs/natural_skill/kiki_01.jpg']
            return list_equipment
        elif index == 1:
            list_equipment = ['Imgs/equipment_pet/purple/01.jpg',
                              'Imgs/equipment_pet/purple/02.jpg',
                              'Imgs/equipment_pet/purple/03.jpg',
                              'Imgs/equipment_pet/purple/04.jpg',
                              'Imgs/equipment_pet/purple/05.jpg',
                              'Imgs/equipment_pet/purple/06.jpg',
                              'Imgs/natural_skill/kiki_01.jpg',
                              'Imgs/natural_skill/kiki_01.jpg']
            return list_equipment
        elif index == 2:
            list_equipment = ['Imgs/equipment_pet/green/01.jpg',
                              'Imgs/equipment_pet/green/02.jpg',
                              'Imgs/equipment_pet/green/03.jpg',
                              'Imgs/equipment_pet/green/04.jpg',
                              'Imgs/equipment_pet/green/05.jpg',
                              'Imgs/equipment_pet/green/06.jpg',
                              'Imgs/natural_skill/kiki_01.jpg',
                              'Imgs/natural_skill/kiki_01.jpg']
            return list_equipment
        else:
            print('Não existe outro set além dos 3!')

    def set_icon_book(self, id):
        # aba ===================================
        tabs = [QWidget() for i in range(3)]
        layout_tab = [QHBoxLayout() for i in range(3)]
        layout_book_order = [QGridLayout() for i in range(3)]
        layout_preview_book = [QHBoxLayout() for i in range(3)]
        # ======================================

        group_preview = [QGroupBox(' Descrição ') for i in range(3)]
        group_book = [QGroupBox(' Magias ') for i in range(3)]

        layout_preview = [QVBoxLayout() for i in range(3)]
        layout_book = [QHBoxLayout() for i in range(3)]

        for i in range(3):
            group_preview[i].setFixedWidth(190)
            group_book[i].setFixedWidth(825)

            group_preview[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            group_book[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_book_order[i].setAlignment(Qt.AlignmentFlag.AlignLeft)

            group_preview[i].setLayout(layout_preview[i])
            group_book[i].setLayout(layout_book[i])

            layout_tab[i].addLayout(layout_preview_book[i])

            layout_book[i].addLayout(layout_book_order[i])
            layout_preview_book[i].addWidget(group_book[i])
            layout_preview_book[i].addWidget(group_preview[i])

        self.tab_book.addTab(tabs[0],"Principal")
        self.tab_book.addTab(tabs[1],"Super")
        self.tab_book.addTab(tabs[2],"Mega")
        
        for i in range(3):
            tabs[i].setLayout(layout_tab[i])
        
        if id == 'Luo Xiaomeng':
            self.prefab_book_main(layout_book_order[0],14, 1)
            self.prefab_book_super(layout_book_order[1],10, 1)
            self.prefab_book_mega(layout_book_order[2],8, 1)

        elif id == 'Princesa Silenciosa':
            self.prefab_book_main(layout_book_order[0],14, 7)
            self.prefab_book_super(layout_book_order[1],7, 7)
            self.prefab_book_mega(layout_book_order[2],8, 7)

        else:
            self.prefab_book_main(layout_book_order[0],15)
            self.prefab_book_super(layout_book_order[1],15)
            self.prefab_book_mega(layout_book_order[2],15)
            


    def prefab_book_main(self, ref_layout_book, quantity,index=0):

        path_ico_book = 'Imgs/livro.png'

        button_book = [QPushButton() for i in range(quantity)]
        label_background = [GradientLabelLinear() for i in range(quantity)]
        layout_background = [QHBoxLayout() for i in range(quantity)]
        layout_label_set = [QHBoxLayout() for i in range(quantity)]

        label_corner = [GradientLabel() for i in range(quantity)]
        label_description_corner = [GradientLinearH() for i in range(quantity)]
        layout_inner = [QHBoxLayout() for i in range(quantity)]

        label_img_book = [QLabel() for i in range(quantity)]
        label_description_book_main = [QLabel() for i in range(quantity)]

        layout_corner = [QHBoxLayout() for i in range(quantity)]
        layout_description_skill = [QHBoxLayout() for i in range(quantity)]

        pixmap_book = [QPixmap() for i in range(quantity)]

        # efeito no nome do livro ===================================================================

        font = [QFont() for i in range(quantity)]
        for i in font:
            i.setBold(True)

        if index == 1:
            
            label_description_book_main[0].setText('Alma do Dragão Anciã')
            label_description_book_main[1].setText('Alma do Dragão Anciã Intermediário')
            label_description_book_main[2].setText('Alma do Dragão Anciã Avançado')

            label_description_book_main[3].setText('Magia Mental')
            label_description_book_main[4].setText('Magia Mental Intermediário')
            label_description_book_main[5].setText('Magia Mental Avançado')

            label_description_book_main[6].setText('Velocidade do Leopardo')
            label_description_book_main[7].setText('Velocidade do Leopardo Intermediário')
            label_description_book_main[8].setText('Velocidade do Leopardo Avançado')

            index = 0
            for i in label_description_book_main:
                if len(i.text()) > 27:
                    font[index].setPointSize(8)
                    if len(i.text()) > 29:
                        font[index].setPointSizeF(7.7)
                        if len(i.text()) > 31:
                            font[index].setPointSize(7)
                    
                i.setFont(font[index])
                index += 1
            
            label_description_book_main[0].setStyleSheet('color: #8bf707')
            label_description_book_main[1].setStyleSheet('color: #073bf7')
            label_description_book_main[2].setStyleSheet('color: #df07f7')

            label_description_book_main[3].setStyleSheet('color: #8bf707')
            label_description_book_main[4].setStyleSheet('color: #073bf7')
            label_description_book_main[5].setStyleSheet('color: #df07f7')

            label_description_book_main[6].setStyleSheet('color: #8bf707')
            label_description_book_main[7].setStyleSheet('color: #073bf7')
            label_description_book_main[8].setStyleSheet('color: #df07f7')


        elif index == 7:
            label_description_book_main[0].setText('Auto Cura')
            label_description_book_main[1].setText('Bloquear Alvo')
            label_description_book_main[2].setText('Pele Resistente')
            label_description_book_main[3].setText('Motivação - Explosão')
            label_description_book_main[4].setText('Retardamento')

            label_description_book_main[5].setText('Proteção de Casca de Árvore')
            label_description_book_main[6].setText('Proteção de Casca de Árvore Intermediária')
            label_description_book_main[7].setText('Proteção de Casca de Árvore Avançada')

            label_description_book_main[8].setText('Concha de Eletrólise')
            label_description_book_main[9].setText('Concha de Eletrólise Intermediário')
            label_description_book_main[10].setText('Concha de Eletrólise Avançado')

            label_description_book_main[11].setText('Velocidade do Leopardo')
            label_description_book_main[12].setText('Velocidade do Leopardo Intermediário')
            label_description_book_main[13].setText('Velocidade do Leopardo Avançado')

            index = 0
            for i in label_description_book_main:
                if len(i.text()) > 27:
                    font[index].setPointSize(8)
                    if len(i.text()) > 29:
                        font[index].setPointSizeF(7.7)
                        if len(i.text()) > 31:
                            font[index].setPointSize(7)
                            if len(i.text()) > 34:
                                font[index].setPointSize(6)
                i.setFont(font[index])
                index += 1
            
            #8bf707 = verde
            #073bf7 = azul
            #df07f7 = roxo
                
            label_description_book_main[0].setStyleSheet('color: #df07f7')
            label_description_book_main[1].setStyleSheet('color: #df07f7')
            label_description_book_main[2].setStyleSheet('color: #df07f7')
            label_description_book_main[3].setStyleSheet('color: #df07f7')
            label_description_book_main[4].setStyleSheet('color: #df07f7')

            label_description_book_main[5].setStyleSheet('color: white')
            label_description_book_main[6].setStyleSheet('color: #073bf7')
            label_description_book_main[7].setStyleSheet('color: #df07f7')

            label_description_book_main[8].setStyleSheet('color: #8bf707')
            label_description_book_main[9].setStyleSheet('color: #073bf7')
            label_description_book_main[10].setStyleSheet('color: #df07f7')

            label_description_book_main[11].setStyleSheet('color: #8bf707')
            label_description_book_main[12].setStyleSheet('color: #073bf7')
            label_description_book_main[13].setStyleSheet('color: #df07f7')

        else:
            print('ainda em andamento')
            pass

        # ==========================================================================================

        line, row = 1,1
        for i in range(quantity):
            label_background[i].setLayout(layout_label_set[i])
            label_background[i].setObjectName('main')
            label_background[i].setStyleSheet('''
                                              QLabel#main
                                              {
                                                border: 1px solid black;
                                              }
                                              ''')
            layout_label_set[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_label_set[i].setContentsMargins(0,0,0,0)

            label_corner[i].setFixedSize(48,48)
            label_img_book[i].setFixedSize(48,48)
            label_description_corner[i].setFixedSize(200,48)
            label_description_book_main[i].setFixedSize(175,30)
            layout_corner[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_corner[i].setContentsMargins(0,0,0,0)
            layout_inner[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_inner[i].setContentsMargins(0,0,0,0)

            layout_inner[i].addWidget(label_corner[i])
            layout_inner[i].addWidget(label_description_corner[i])
            

            layout_background[i].addWidget(label_background[i])
            layout_background[i].setContentsMargins(0,0,0,0)
            layout_label_set[i].addLayout(layout_inner[i])

            label_corner[i].setLayout(layout_corner[i])
            label_description_corner[i].setLayout(layout_description_skill[i])

            layout_corner[i].addWidget(label_img_book[i])
            layout_description_skill[i].addWidget(label_description_book_main[i])

            label_img_book[i].setFixedSize(38,38)
            pixmap_book[i].load(path_ico_book)
            label_img_book[i].setPixmap(pixmap_book[i])

            button_book[i].setLayout(layout_background[i])
            button_book[i].setFixedSize(265,60)
            button_book[i].setContentsMargins(0,0,0,0)

            
            if line > 5:
                row += 1
                line = 1
            ref_layout_book.addWidget(button_book[i],line,row,1,1)
            line += 1


    def prefab_book_super(self, ref_layout_book, quantity,index=0):

        path_ico_book = 'Imgs/livro.png'

        button_book = [QPushButton() for i in range(quantity)]
        label_background = [GradientLabelLinear() for i in range(quantity)]
        layout_background = [QHBoxLayout() for i in range(quantity)]
        layout_label_set = [QHBoxLayout() for i in range(quantity)]

        label_corner = [GradientLabel() for i in range(quantity)]
        label_description_corner = [GradientLinearH() for i in range(quantity)]
        layout_inner = [QHBoxLayout() for i in range(quantity)]

        label_img_book = [QLabel() for i in range(quantity)]
        label_description_book_main = [QLabel() for i in range(quantity)]

        layout_corner = [QHBoxLayout() for i in range(quantity)]
        layout_description_skill = [QHBoxLayout() for i in range(quantity)]

        pixmap_book = [QPixmap() for i in range(quantity)]

        # efeito no nome do livro ===================================================================
        font = [QFont() for i in range(quantity)]
        for i in font:
            i.setBold(True)

        if index == 7:
            label_description_book_main[0].setText('Super Casaco de Casca')
            label_description_book_main[1].setText('Super Eletrólito')
            label_description_book_main[2].setText('Super escalas de dragão da armadura')
            label_description_book_main[3].setText('Super Leopardo Rápido')
            label_description_book_main[4].setText('Super Endurecimento')

            label_description_book_main[5].setText('Super Negação Sagrada')
            label_description_book_main[6].setText('Intuição Super Besta')

            index = 0
            for i in label_description_book_main:
                if len(i.text()) > 27:
                    font[index].setPointSize(8)
                    if len(i.text()) > 29:
                        font[index].setPointSizeF(7.7)
                        if len(i.text()) > 31:
                            font[index].setPointSize(7)
                            if len(i.text()) > 34:
                                font[index].setPointSize(6)
                i.setFont(font[index])
                index += 1

            for i in label_description_book_main:
                i.setStyleSheet('color: #df07f7')

        else:
            pass
    
        # ==========================================================================================

        line, row = 1,1
        for i in range(quantity):
            label_background[i].setLayout(layout_label_set[i])
            label_background[i].setObjectName('main')
            label_background[i].setStyleSheet('''
                                              QLabel#main
                                              {
                                                border: 1px solid black;
                                              }
                                              ''')
            layout_label_set[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_label_set[i].setContentsMargins(0,0,0,0)

            label_corner[i].setFixedSize(48,48)
            label_img_book[i].setFixedSize(48,48)
            label_description_corner[i].setFixedSize(200,48)
            label_description_book_main[i].setFixedSize(175,30)
            label_description_book_main[i].setFont(font)
            layout_corner[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_corner[i].setContentsMargins(0,0,0,0)
            layout_inner[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_inner[i].setContentsMargins(0,0,0,0)

            layout_inner[i].addWidget(label_corner[i])
            layout_inner[i].addWidget(label_description_corner[i])
            

            layout_background[i].addWidget(label_background[i])
            layout_background[i].setContentsMargins(0,0,0,0)
            layout_label_set[i].addLayout(layout_inner[i])

            label_corner[i].setLayout(layout_corner[i])
            label_description_corner[i].setLayout(layout_description_skill[i])

            layout_corner[i].addWidget(label_img_book[i])
            layout_description_skill[i].addWidget(label_description_book_main[i])

            label_img_book[i].setFixedSize(38,38)
            pixmap_book[i].load(path_ico_book)
            label_img_book[i].setPixmap(pixmap_book[i])

            button_book[i].setLayout(layout_background[i])
            button_book[i].setFixedSize(265,60)
            button_book[i].setContentsMargins(0,0,0,0)

            
            if line > 5:
                row += 1
                line = 1
            ref_layout_book.addWidget(button_book[i],line,row,1,1)
            line += 1


    def prefab_book_mega(self, ref_layout_book, quantity,index=0):

        path_ico_book = 'Imgs/livro.png'

        button_book = [QPushButton() for i in range(quantity)]
        label_background = [GradientLabelLinear() for i in range(quantity)]
        layout_background = [QHBoxLayout() for i in range(quantity)]
        layout_label_set = [QHBoxLayout() for i in range(quantity)]

        label_corner = [GradientLabel() for i in range(quantity)]
        label_description_corner = [GradientLinearH() for i in range(quantity)]
        layout_inner = [QHBoxLayout() for i in range(quantity)]

        label_img_book = [QLabel() for i in range(quantity)]
        label_description_book_main = [QLabel() for i in range(quantity)]

        layout_corner = [QHBoxLayout() for i in range(quantity)]
        layout_description_skill = [QHBoxLayout() for i in range(quantity)]

        pixmap_book = [QPixmap() for i in range(quantity)]

        # efeito no nome do livro ===================================================================

        if index == 1:
            #label_description_book_main[0].setText('Despertar Bestial')
            #label_description_book_main[0].setStyleSheet('color: #8bf707')
            pass
        else:
            pass

        font = QFont()
        font.setBold(True)

        # ==========================================================================================

        line, row = 1,1
        for i in range(quantity):
            label_background[i].setLayout(layout_label_set[i])
            label_background[i].setObjectName('main')
            label_background[i].setStyleSheet('''
                                              QLabel#main
                                              {
                                                border: 1px solid black;
                                              }
                                              ''')
            layout_label_set[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_label_set[i].setContentsMargins(0,0,0,0)

            label_corner[i].setFixedSize(48,48)
            label_img_book[i].setFixedSize(48,48)
            label_description_corner[i].setFixedSize(200,48)
            label_description_book_main[i].setFixedSize(175,30)
            label_description_book_main[i].setFont(font)
            layout_corner[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_corner[i].setContentsMargins(0,0,0,0)
            layout_inner[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_inner[i].setContentsMargins(0,0,0,0)

            layout_inner[i].addWidget(label_corner[i])
            layout_inner[i].addWidget(label_description_corner[i])
            

            layout_background[i].addWidget(label_background[i])
            layout_background[i].setContentsMargins(0,0,0,0)
            layout_label_set[i].addLayout(layout_inner[i])

            label_corner[i].setLayout(layout_corner[i])
            label_description_corner[i].setLayout(layout_description_skill[i])

            layout_corner[i].addWidget(label_img_book[i])
            layout_description_skill[i].addWidget(label_description_book_main[i])

            label_img_book[i].setFixedSize(38,38)
            pixmap_book[i].load(path_ico_book)
            label_img_book[i].setPixmap(pixmap_book[i])

            button_book[i].setLayout(layout_background[i])
            button_book[i].setFixedSize(265,60)
            button_book[i].setContentsMargins(0,0,0,0)

            
            if line > 5:
                row += 1
                line = 1
            ref_layout_book.addWidget(button_book[i],line,row,1,1)
            line += 1



class GradientLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: transparent;")  # Defina o fundo do widget como transparente

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QRadialGradient(self.rect().center(), self.rect().width() / 2)
        gradient.setColorAt(1, QColor(31, 31, 41))
        gradient.setColorAt(0, QColor(80, 105, 140))
        painter.fillRect(self.rect(), gradient)

        # Desenhe o contorno
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawRect(self.rect())


class GradientLabelLinear(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: transparent;")

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Desenhe o gradiente linear
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(42, 53, 71))
        gradient.setColorAt(0.5, QColor(80, 105, 140))
        gradient.setColorAt(1, QColor(42, 53, 71))
        painter.fillRect(self.rect(), gradient)
        
        # Desenhe o contorno
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawRect(self.rect())


class GradientLinearH(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: transparent;")

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Desenhe o gradiente linear
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(31, 31, 41))
        gradient.setColorAt(0.5, QColor(33, 34, 54))
        gradient.setColorAt(1, QColor(31, 31, 41))
        painter.fillRect(self.rect(), gradient)
        
        # Desenhe o contorno
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BuildPet()
    window.show()
    sys.exit(app.exec())