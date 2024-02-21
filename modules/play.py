import sys
import os
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                               QLabel, QDialog, QLineEdit, QGroupBox, QSpinBox, QErrorMessage, QComboBox, QScrollArea)
from PySide6.QtCore import Qt


class Play(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_init()
        self.default_slot()
        

    def set_init(self):
        self.width_main = 340
        self.height_main = 500
        self.setFixedSize(self.width_main,self.height_main)
        self.setWindowTitle('Launcher')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

    def default_slot(self):
        self.layout_general = QHBoxLayout()
        self.central_layout.addLayout(self.layout_general)
        scroll_area_perfil = QScrollArea()
        widget_perfil = QWidget(scroll_area_perfil)
        self.layout_perfils = QHBoxLayout(widget_perfil)
        self.layout_perfils.setAlignment(Qt.AlignmentFlag.AlignLeft)
        scroll_area_perfil.setWidget(widget_perfil)
        scroll_area_perfil.setWidgetResizable(True)
        self.layout_general.addWidget(scroll_area_perfil)

        try:
            if os.path.exists('JSON/perfil.json'):
                
                with open('JSON/perfil.json','r') as file:
                    data_perfil = json.load(file)

                row = 0
                line = 0
                for i in range(data_perfil.__len__()):
                    if i == 0:
                        self.width_main += 300
                    if i == 1:
                        self.width_main += 310


                    self.setFixedWidth(self.width_main)
                    self.perfil_display(data_perfil[i]['caminho'])
                    line += 1

                self.add_perfil()

            else:
               self.add_perfil()

        except TypeError as err:
            print(err)


    def add_perfil(self):
        button_create_slot = QPushButton('+')
        button_create_slot.clicked.connect(self.create_slot)
        button_create_slot.setStyleSheet('''
                                              QPushButton{
                                              color: #636363;
                                              font-size: 80px; 
                                              border: 1px solid grey;
                                              }

                                              QPushButton:hover{
                                              background-color: #d1d1d1;
                                              }
                                              ''')
        button_create_slot.setFixedSize(300,440)
        self.layout_perfils.addWidget(button_create_slot)


    def perfil_display(self, function_click):
        button_create_slot = QPushButton()
        button_create_slot.clicked.connect(self.function_load_launch)
        button_create_slot.setStyleSheet('''
                                              QPushButton{
                                              color: #636363;
                                              font-size: 80px; 
                                              border: 1px solid grey;
                                              }

                                              QPushButton:hover{
                                              background-color: #d1d1d1;
                                              }
                                              ''')
        button_create_slot.setFixedSize(300,440)
        self.layout_perfils.addWidget(button_create_slot)

    def function_load_launch(self, path):
        try:
            os.startfile(path)
        except Exception as err:
            print('Caminho inválido!')

    def create_slot(self):
        self.create = WindowCreate(550,300)
        self.create.exec()

    def atualizar_perfis(self):
        self.limpar_layout(self.layout_perfils)

        try:
            if os.path.exists('JSON/perfil.json'):
                
                with open('JSON/perfil.json','r') as file:
                    data_perfil = json.load(file)
                
                self.width_main = 340
                self.height_main = 500

                self.setFixedSize(self.width_main, self.height_main)

                for i in range(data_perfil.__len__()):
                    if i == 0:
                        self.width_main += 300
                    if i == 1:
                        self.width_main += 310

                    self.setFixedWidth(self.width_main)
                    self.perfil_display(data_perfil[i]['caminho'])
                self.add_perfil()

            else:
               self.add_perfil()

        except TypeError as err:
            print(err)

    def limpar_layout(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                sublayout = item.layout()
                if sublayout is not None:
                    self.limpar_layout(sublayout)
            

class WindowCreate(QDialog):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle('Perfil')
        self.central_layout = QVBoxLayout()
        self.setLayout(self.central_layout)

        self.ui_init()


    def ui_init(self):
        self.layout_form = QVBoxLayout()
        self.list_actions = []
        group_choose_path = QGroupBox('Caminho')
        group_choose_path.setFixedHeight(110)
        layout_group_path = QVBoxLayout()
        group_choose_path.setLayout(layout_group_path)
        self.layout_form.addWidget(group_choose_path)

        self.line_path_edit = QLineEdit()
        layout_group_path.addWidget(self.line_path_edit)

        label_title = QLabel('Nome do Título')
        self.line_title = QLineEdit()


        self.group_char_name = QGroupBox()
        self.height_group = 80
        self.group_char_name.setFixedHeight(self.height_group)
        self.layout_char_name = QVBoxLayout()
        self.group_char_name.setLayout(self.layout_char_name)

        layout_button_active = QHBoxLayout()
        button_apply = QPushButton('Aplicar')
        button_apply.clicked.connect(self.apply_check)
        button_apply.setFixedHeight(40)
        button_apply.setStyleSheet('background-color: #3d7eb8; border: 1px solid black; font-size: 20px')

        label_char = QLabel('Personagens')
        button_more_name_char = QPushButton('+')
        button_more_name_char.setFixedHeight(40)
        button_more_name_char.setStyleSheet('background-color: #59b83d; border: 1px solid black; font-size: 30px')

        button_minus_name_char = QPushButton('-')
        button_minus_name_char.setFixedHeight(40)
        button_minus_name_char.setStyleSheet('background-color: #b83d49; border: 1px solid black; font-size: 30px')
        
        self.layout_form.addWidget(label_title)
        self.layout_form.addWidget(self.line_title)
        self.layout_form.addWidget(label_char)
        self.layout_form.addWidget(self.group_char_name)

        self.layout_char_name.addLayout(layout_button_active)
        layout_button_active.addWidget(button_more_name_char)
        layout_button_active.addWidget(button_minus_name_char)
        layout_button_active.addWidget(button_apply)

        button_more_name_char.clicked.connect(lambda: self.more_char_name(self.layout_char_name))
        button_minus_name_char.clicked.connect(self.delete_slot_name)

        self.current_slots = 0
        # adiciona na layout final
        self.central_layout.addLayout(self.layout_form)

    def test_child(self):
        try:
            self.list_actions = []
            for i in range(self.layout_char_name.count()):
                layouts = self.layout_char_name.itemAt(i).layout()
                self.list_actions.append(layouts)
            
            self.list_actions.pop(0)
            for n in self.list_actions:
                #items para retornar valor 
                #[1,2,4] QlineEdit, dropdown, spinbox
                
                nickname = n.itemAt(1).widget()
                dropdown = n.itemAt(4).widget()
                lv_spin = n.itemAt(7).widget()
                
                nickname.setText('Buffador')
                dropdown.setCurrentIndex(2)
                lv_spin.setValue(5)
                # ====================================

        except Exception as err:
            print('erro!')

    def apply_check(self):
        try:
            
            

            if os.path.exists('JSON/perfil.json'):
                with open('JSON/perfil.json','r') as file:
                    self.list_json = json.load(file)
            else:
                self.list_json = []

            if self.current_slots < 1:
                self.message_error('É necessário pelo menos 1 nick salvo!')
            else:
                save_file = {'caminho':self.line_path_edit.text(),
                             'titulo':self.line_title.text()}
                
                self.list_json.append(save_file)
                with open('JSON/perfil.json','w') as file:
                    json.dump(self.list_json, file, indent=2)
                
                window.atualizar_perfis()
                self.close()

        except Exception as err:
            print(err)

    def delete_slot_name(self):
        try:
            if self.current_slots < 1:
                self.message_error('Não possui nicks para apagar!')
            else:
                self.height -= 50
                self.setFixedHeight(self.height)
                self.height_group -= 50
                self.group_char_name.setFixedHeight(self.height_group)

                last_index = self.layout_char_name.count() - 1
                last_layout = self.layout_char_name.itemAt(last_index).layout()
                self.layout_char_name.removeItem(last_layout)

                self.remove_layout(last_layout)
                self.current_slots -= 1
        except Exception as err:
            print(err)

    def remove_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                self.delete_layout(item.layout())
        layout.deleteLater()

    def more_char_name(self, ref_layout:QVBoxLayout, space: int = 20): 
        try:
            
            if self.current_slots < 3:
                layout_info = QHBoxLayout()
                self.height += 50
                self.setFixedHeight(self.height)
                self.height_group += 50
                self.group_char_name.setFixedHeight(self.height_group)

                label_nickname = QLabel('Nick')
                label_class = QLabel('Classe')
                label_lv = QLabel('Lv')
                label_space = QLabel()
                label_space.setFixedWidth(space)

                line_name_char = QLineEdit()
                line_name_char.setFixedWidth(150)
                list_class = ['Soldado Engenheiro','Lutador Artista','Caçador do Sol','Atirador Mágico','Médico da Felicidade','Músico Espiritual']
                dropdown_class = QComboBox()
                dropdown_class.addItems(list_class)
                dropdown_class.setFixedWidth(140)
                spin_lv = QSpinBox()
        
                spin_lv.setMinimum(1)
                spin_lv.setMaximum(160)
                spin_lv.setFixedWidth(50)


                layout_info.addWidget(label_nickname)
                layout_info.addWidget(line_name_char)
                layout_info.addWidget(label_space)
                layout_info.addWidget(label_class)
                layout_info.addWidget(dropdown_class)
                layout_info.addWidget(label_space)
                layout_info.addWidget(label_lv)
                layout_info.addWidget(spin_lv)

                ref_layout.addLayout(layout_info)
                self.current_slots += 1
                self.test_child()
            else:
                self.message_error('Já alcançou o máximo de nicks!')
        except TypeError as err:
            self.message_error(f'erro: {err}')
    
    def message_error(self, msn):
        message_window = QErrorMessage(self)
        message_window.setWindowTitle('Erro')
        message_window.showMessage(msn)
        message_window.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Play()
    window.show()
    sys.exit(app.exec())
