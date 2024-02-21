import sys
import os
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, 
                               QGroupBox, QLabel, QLineEdit, QComboBox, QDoubleSpinBox,QPushButton, QScrollArea,
                               QDialog, QCheckBox)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient

class KeysWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.create_element()
        self.insert_elements()

    def setup_ui(self):
        self.setWindowTitle('Chaves')
        self.setFixedSize(900,650)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QHBoxLayout()
        self.central_widget.setLayout(self.central_layout)

    def create_element(self):
        self.layout_elements = [QVBoxLayout() for i in range(2)]
        self.buttons_options = [QPushButton() for i in range(7)]

        self.buttons_options[0].clicked.connect(self.add_keys)
        self.buttons_options[1].clicked.connect(self.default_data)
        self.buttons_options[2].clicked.connect(self.clear_panel)
        self.buttons_options[3].clicked.connect(self.filter_options)

        self.layout_elements[0].setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_elements[0].setContentsMargins(0,0,0,0)

        self.list_name_buttons = ['Adicionar','Restaurar','Limpar','Filtrar', 'Organizar','Exportar / Salvar','Sair']

        self.area_scroll = QScrollArea()
        self.area_scroll.setWidgetResizable(True)
        self.widget_scroll = QWidget(self.area_scroll)
        self.layout_scroll = QVBoxLayout(self.widget_scroll)
        self.area_scroll.setWidget(self.widget_scroll)

        self.area_scroll.setStyleSheet("background-color: #499cf5;")
                                            

        self.layout_scroll.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_scroll.setContentsMargins(1,10,0,0)

        self.default_data()


    def insert_elements(self):

        index = 0
        for i in self.buttons_options:
            i.setFixedSize(150,80)
            i.setText(self.list_name_buttons[index])
            self.layout_elements[0].addWidget(i)
            index += 1

        self.layout_elements[1].addWidget(self.area_scroll)

        for i in self.layout_elements:
            self.central_layout.addLayout(i)

    # ==== window ================
    def add_keys(self):
        self.add_keys_window = AddFunction()
        self.add_keys_window.exec()

    def filter_options(self):
        self.filter_window = FilterWindow()
        self.filter_window.exec()

    # ===========================

    def default_data(self):
        label_info = []

        for i in reversed(range(self.layout_scroll.count())):
            item = self.layout_scroll.itemAt(i)
            if item.widget():
                item.widget().deleteLater()  # Remova o widget
            elif item.layout():
                self.removeChildren(item.layout())  # Remova os widgets no layout
            self.layout_scroll.removeItem(item)

        local_file = 'JSON'
        name_file = 'list_keys.json'
        self.PATH_FILE = os.path.join(local_file, name_file)
        with open(self.PATH_FILE) as file:
            dados = json.load(file)

        label_info = [QLabel() for i in range(len(dados))]
        
        for i in range(len(dados)):
            text_formatter = f'{str(dados[i]["inventario"]).title()} - {dados[i]["sistema"]} - {str(dados[i]["atributo"]).upper()} - {dados[i]["valor"]} - {str(dados[i]["tipo"]).upper()} - {dados[i]["mapa"]}'
            label_info[i].setText(text_formatter)

        for i in label_info:
            i.setStyleSheet('''
                            QLabel{
                                border: 0px solid blue; 
                                padding: 40px 5px; 
                                border-radius: 9px;
                                background-color: white;
                            }
                            QLabel:hover{
                                background-color: #e0dede;
                            }
                            ''')
            i.setFixedWidth(705)
            self.layout_scroll.addWidget(i)
    
    def clear_panel(self):
        for i in reversed(range(self.layout_scroll.count())):
            item = self.layout_scroll.itemAt(i)
            if item.widget():
                item.widget().deleteLater()  # Remova o widget
            elif item.layout():
                self.removeChildren(item.layout())  # Remova os widgets no layout
            self.layout_scroll.removeItem(item)


    # ==================== carrega os dados ========================================================================
    def load_filter(self, index):
        label_info = []

        for i in reversed(range(self.layout_scroll.count())):
            item = self.layout_scroll.itemAt(i)
            if item.widget():
                item.widget().deleteLater()  # Remova o widget
            elif item.layout():
                self.removeChildren(item.layout())  # Remova os widgets no layout
            self.layout_scroll.removeItem(item)

        local_file = 'JSON'
        name_file = 'list_keys.json'
        self.PATH_FILE = os.path.join(local_file, name_file)
        with open(self.PATH_FILE) as file:
            dados = json.load(file)

        label_info = [QLabel() for i in range(len(dados))]
        
        for i in range(len(dados)):

            # base 1
            if index == 0:
                text_formatter = f'{dados[i]["inventario"]}'
                label_info[i].setText(text_formatter)

            if index == 1:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["sistema"]}'
                label_info[i].setText(text_formatter)

            if index == 2:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["sistema"]} - {dados[i]["atributo"]}'
                label_info[i].setText(text_formatter)

            if index == 3:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["sistema"]} - {dados[i]["atributo"]} - {dados[i]["valor"]}'
                label_info[i].setText(text_formatter)

            if index == 4:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["sistema"]} - {dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]}'
                label_info[i].setText(text_formatter)

            if index == 5:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["sistema"]} - {dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]} - {dados[i]["mapa"]}'
                label_info[i].setText(text_formatter)

            #base2
            if index == 6:
                text_formatter = f'{dados[i]["sistema"]}'
                label_info[i].setText(text_formatter)

            if index == 7:
                text_formatter = f'{dados[i]["sistema"]} - {dados[i]["atributo"]}'
                label_info[i].setText(text_formatter)

            if index == 8:
                text_formatter = f'{dados[i]["sistema"]} - {dados[i]["atributo"]} - {dados[i]["valor"]}'
                label_info[i].setText(text_formatter)

            if index == 9:
                text_formatter = f'{dados[i]["sistema"]} - {dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]}'
                label_info[i].setText(text_formatter)

            if index == 10:
                text_formatter = f'{dados[i]["sistema"]} - {dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]} - {dados[i]["mapa"]}'
                label_info[i].setText(text_formatter)


            #base 3
            if index == 11:
                text_formatter = f'{dados[i]["atributo"]}'
                label_info[i].setText(text_formatter)

            if index == 12:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["atributo"]}'
                label_info[i].setText(text_formatter)

            if index == 13:
                text_formatter = f'{dados[i]["atributo"]} - {dados[i]["valor"]}'
                label_info[i].setText(text_formatter)

            if index == 14:
                text_formatter = f'{dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]}'
                label_info[i].setText(text_formatter)

            if index == 15:
                text_formatter = f'{dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]} - {dados[i]["mapa"]}'
                label_info[i].setText(text_formatter)

            if index == 16:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["atributo"]} - {dados[i]["valor"]}'
                label_info[i].setText(text_formatter)

            if index == 16:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]}'
                label_info[i].setText(text_formatter)

            if index == 17:
                text_formatter = f'{dados[i]["inventario"]} - {dados[i]["atributo"]} - {dados[i]["valor"]} - {dados[i]["tipo"]} - {dados[i]["mapa"]}'
                label_info[i].setText(text_formatter)

            # --------------------------------

        for i in label_info:
            i.setStyleSheet('''
                            QLabel{
                                border: 0px solid blue;
                                background-color: white;
                                padding: 40px 5px; 
                                border-radius: 9px;
                            }
                            QLabel:hover{
                                background-color: #e0dede;
                            }
                            ''')
            i.setFixedWidth(705)
            self.layout_scroll.addWidget(i)

    # ===========================================================================================================================
            

    def paintEvent(self, event):
        painter = QPainter(self)
        grad = QLinearGradient(0,0,500,500)
        grad.setColorAt(0,QColor(6, 92, 184))
        grad.setColorAt(1,QColor(2, 59, 120))
        painter.fillRect(self.rect(),grad)


class AddFunction(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adicionar Chave")
        self.setFixedSize(400, 500)
        self.central_layout = QVBoxLayout()
        self.setLayout(self.central_layout)
        self.group_inputs = [QGroupBox() for i in range(6)]
        self.layout_group = [QVBoxLayout() for i in range(6)]
        self.input_line = [QLineEdit() for i in range(3)]

        self.list_attr = ['HP','MP','Ataque Físico','Ataque Mágico','Taxa Crítica (CRIT)','Ignorar',
                          'Acréscimo de Dano Crítico (Quebrar)','Dano Físico Final','Dano Mágico Final','Anti-Morte','Velocidade','Acerto',
                          'Acerto de Debuff','Esquivar','Anti-Ignorar','Anti-Crítico','Defesa Física','Defesa Mágica',
                          'Redução de Dano Mágico','Redução de Dano Físico','Resistência ao Debuff','Contra-Ataque',
                          'Acerto de Debuff','Ataque Seguido']
        self.list_type_key = ['PS','BT','PL','MC','DM','DG','BOSS']

        self.dropdown_attr = QComboBox()
        self.dropdown_type_key = QComboBox()

        self.float_attr_value = QDoubleSpinBox()
        self.float_attr_value.setMaximum(9999.9999)

        self.dropdown_attr.addItems(self.list_attr)
        self.dropdown_type_key.addItems(self.list_type_key)

        self.layout_group[2].addWidget(self.dropdown_attr)
        self.layout_group[3].addWidget(self.float_attr_value)
        self.layout_group[4].addWidget(self.dropdown_type_key)
        self.layout_group[0].addWidget(self.input_line[0])
        self.layout_group[1].addWidget(self.input_line[1])
        self.layout_group[5].addWidget(self.input_line[2])


        for i in range(self.layout_group.__len__()):
            self.group_inputs[i].setLayout(self.layout_group[i])
           

        self.group_inputs[0].setTitle('Nome da Chave no Inventário')
        self.group_inputs[1].setTitle('Nome da Chave no Sistema')
        self.group_inputs[2].setTitle('Atributo Bônus')
        self.group_inputs[3].setTitle('Valor do Atributo')
        self.group_inputs[4].setTitle('Tipo de Chave')
        self.group_inputs[5].setTitle('Mapa de Drop')

        self.button_confirm = QPushButton('Adicionar')
        self.button_confirm.setFixedHeight(55)
        self.button_confirm.clicked.connect(self.add_info)

        for i in self.group_inputs:
            self.central_layout.addWidget(i)
        
        self.central_layout.addWidget(self.button_confirm)

    
    def add_info(self):
        data_info = {'inventario': self.input_line[0].text().lower(),
                     'sistema': self.input_line[1].text().lower(),
                     'atributo': self.dropdown_attr.currentText().lower(),
                     'valor': self.float_attr_value.value(),
                     'tipo': self.dropdown_type_key.currentText().lower(),
                     'mapa': self.input_line[2].text().lower()}
        
        local_file = 'JSON'
        name_file = 'list_keys.json'
        self.PATH_FILE = os.path.join(local_file, name_file)

        try:
            # Verifica se o arquivo existe antes de tentar lê-lo
            if os.path.exists(self.PATH_FILE):
                # Verifica se o arquivo não está vazio
                if os.path.getsize(self.PATH_FILE) > 0:
                    with open(self.PATH_FILE, 'r') as file:
                        exists_data = json.load(file)
                else:
                    # Se o arquivo estiver vazio, inicializa a lista vazia
                    exists_data = []
            else:
                # Se o arquivo não existir, inicializa a lista vazia
                exists_data = []

            # Adiciona os novos dados à lista existente
            exists_data.append(data_info)

            # Salva a lista atualizada de volta no arquivo JSON
            with open(self.PATH_FILE, 'w') as file:
                json.dump(exists_data, file, indent=2)
                print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar dados: {str(e)}")

        for i in self.input_line:
            i.clear()

   
        
        
class FilterWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filtrar")
        self.setFixedSize(250, 350)
        self.central_layout = QVBoxLayout()
        self.setLayout(self.central_layout)

        #====== groupbox ======
        self.group_filter = QGroupBox('Filtrar por')
        self.layout_group_filter = QVBoxLayout() 
        self.group_filter.setLayout(self.layout_group_filter)

        #====== buttons =======
        self.check_filter = [QCheckBox() for i in range(6)]
        self.confirm_button = QPushButton('Aplicar')
        self.confirm_button.clicked.connect(self.confirm_filter)
        list_name_button = ['Nome','Nome no Sistema','Atributo','Valor','Tipo','Drop']

        #====== adicionar =====

        index = 0
        
        for i in self.check_filter:
            i.setText(list_name_button[index])
            self.layout_group_filter.addWidget(i)
            index += 1
        self.central_layout.addWidget(self.group_filter)
        self.central_layout.addWidget(self.confirm_button)
        

    def confirm_filter(self):
        cond_01 = self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and not self.check_filter[2].isChecked() and not self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_01_02 = self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and not self.check_filter[2].isChecked() and not self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_01_03 = self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and not self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_01_04 = self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_01_05 = self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_01_06 = self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and self.check_filter[5].isChecked()


        cond_02 = not self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and not self.check_filter[2].isChecked() and not self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_02_01 = not self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and not self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_02_02 = not self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_02_03 = not self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_02_04 = not self.check_filter[0].isChecked() and self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and self.check_filter[5].isChecked()


        cond_03 = not self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and not self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_03_01 = not self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_03_02 = not self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_03_03 = not self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and self.check_filter[5].isChecked()

        cond_03_04 = self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and not self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_03_05 = self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and not self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_03_06 = self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and  self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and not self.check_filter[5].isChecked()

        cond_03_07 = self.check_filter[0].isChecked() and not self.check_filter[1].isChecked() \
        and self.check_filter[2].isChecked() and self.check_filter[3].isChecked() \
        and self.check_filter[4].isChecked() and self.check_filter[5].isChecked()



        if cond_01:
            window.load_filter(0)
        elif cond_01_02:
            window.load_filter(1)
        elif cond_01_03:
            window.load_filter(2)
        elif cond_01_04:
            window.load_filter(3)
        elif cond_01_05:
            window.load_filter(4)
        elif cond_01_06:
            window.load_filter(5)

        elif cond_02:
            window.load_filter(6)
        elif cond_02_01:
            window.load_filter(7)
        elif cond_02_02:
            window.load_filter(8)
        elif cond_02_03:
            window.load_filter(9)
        elif cond_02_04:
            window.load_filter(10)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeysWindow()
    window.show()
    sys.exit(app.exec())