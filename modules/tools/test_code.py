import sys, time, os
import pyperclip
import pyautogui
import pandas as pd
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, 
                               QPushButton, QComboBox, QSpinBox, QGroupBox, QLabel, QMessageBox, QProgressBar)
from PySide6.QtCore import QThread, Qt, Signal
from PySide6.QtGui import QPainter, QPixmap, QLinearGradient, QIcon

class CodeTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threads_path()
        self.set_init()
        self.layout_interface()

    def threads_path(self):
        self.progress_t = None
        self.get_position_t = None

    def set_init(self):
        self.setWindowTitle('Testar Códigos')
        self.setWindowIcon(QIcon('Icons/ico_code_test.png'))
        self.setFixedSize(400,350)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

    def layout_interface(self):
        self.index_id = 0
        self.position_chat = None
        group_index = QGroupBox('Indice')
        layout_group_index = QHBoxLayout()
        layout_group_index.setContentsMargins(20, 0,20,10)
        group_index.setLayout(layout_group_index)

        group_progress = QGroupBox('Progresso')
        layout_progress = QVBoxLayout()
        layout_progress.setContentsMargins(7,0,7,10)
        group_progress.setLayout(layout_progress)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setStyleSheet('''
                                            QProgressBar:chunk{
                                                background-color: #82f5a6;
                                            }
                                        
                                            QProgressBar{
                                                border: 1px solid black;
                                            }
                                        ''')

        layout_button_active = QHBoxLayout()

        self.start_id, self.end_id = QSpinBox(), QSpinBox()
        self.start_id.setMaximum(999999)
        self.end_id.setMaximum(999999)

        label_de = QLabel('Dê')
        label_ate = QLabel('Até')
        label_space_spin = QLabel()
        label_space_dropdown = QLabel()
        label_dropdown = QLabel('Código')
        
        label_dropdown.setFixedHeight(30)
        label_space_dropdown.setFixedHeight(10)

        code_list = ['Nenhum','[@P|numero|nome]','[@M|numero|nome]','[@N|numero|nome]','[@MA|numero|nome]','[@SK|numero|nome]']
        self.dropdown_code = QComboBox()
        self.dropdown_code.addItems(code_list)
        self.dropdown_code.currentIndexChanged.connect(self.select_drop)

        self.button_get_position = QPushButton('Pegar Posição')
        self.button_start_write = QPushButton('Começar')
        button_export_xlsx = QPushButton('Exportar Molde de Códigos')

        self.button_get_position.setFixedHeight(50)
        self.button_start_write.setFixedHeight(50)
        button_export_xlsx.setFixedHeight(80)
        
        self.button_get_position.clicked.connect(self.thread_get_pos)
        self.button_start_write.clicked.connect(self.start_write)
        button_export_xlsx.clicked.connect(self.print_excel)

        layout_group_index.addWidget(label_de)
        layout_group_index.addWidget(self.start_id)
        layout_group_index.addWidget(label_space_spin)
        layout_group_index.addWidget(label_ate)
        layout_group_index.addWidget(self.end_id)

        self.central_layout.addWidget(group_index)
        self.central_layout.addWidget(label_dropdown)
        self.central_layout.addWidget(self.dropdown_code)
        self.central_layout.addWidget(label_space_dropdown)
        self.central_layout.addLayout(layout_button_active)

        layout_button_active.addWidget(self.button_get_position)
        layout_button_active.addWidget(self.button_start_write)

        self.central_layout.addWidget(button_export_xlsx)
        self.central_layout.addWidget(group_progress)
        layout_progress.addWidget(self.progress_bar)

        if self.position_chat is None:
            self.button_start_write.setEnabled(False)


    def thread_get_pos(self):
        self.get_position_t = ThreadSystem(self.button_get_position)
        self.get_position_t.sinal.connect(self.get_position_chat)
        self.get_position_t.start()

    
    def select_drop(self):
        if self.dropdown_code.currentIndex() == 0:
            print(self.dropdown_code.currentText())

        elif self.dropdown_code.currentIndex() == 1:
            self.texto_escrito = f'[@P|{self.index_id}|Indice de Sitema: {self.index_id}]'

        elif self.dropdown_code.currentIndex() == 2:
            self.texto_escrito = f'[@M|{self.index_id}|Indice de Monstro: {self.index_id}]'

        elif self.dropdown_code.currentIndex() == 3:
            self.texto_escrito = f'[@N|{self.index_id}|Indice de NPC: {self.index_id}]'

        elif self.dropdown_code.currentIndex() == 4:
            self.texto_escrito = f'[@MA|{self.index_id}|Indice de Mapa: {self.index_id}]'
        
        elif self.dropdown_code.currentIndex() == 5:
            self.texto_escrito = f'[@SK|{self.index_id}|Indice de Magia: {self.index_id}]'
        return self.texto_escrito
    
    def start_write(self):
        if self.dropdown_code.currentIndex() == 0:
            self.message_box_show('Erro','É necessário ter algum código selecionado!')
        else:
            try:
                self.index_id = 0
                self.index_id = self.start_id.value()
                range_max = self.end_id.value()
                range_min = self.start_id.value()
                self.progress_bar.setMinimum(range_min)
                self.progress_bar.setMaximum(range_max)
                self.progress_bar.setValue(0)
                self.select_drop()
                
                self.progress_t = ThreadProgress(range_min, range_max,self.position_chat, self.progress_bar, self.select_drop, self.button_start_write, self.texto_escrito, self.index_id)
                self.progress_t.start()

            except Exception as err:
                print(err)


    def print_excel(self):
        if self.dropdown_code.currentIndex() == 0:
            self.message_box_show('Erro','É necessário ter algum código selecionado!')
        else:
            self.index_id = 0
            self.select_drop()
            self.index_id = self.start_id.value()
            range_max = self.end_id.value()
            range_min = self.start_id.value()

            code_list_save = []
            for i in range(range_min, range_max + 1):
                self.select_drop()
                code_list_save.append(self.texto_escrito)
                self.index_id += 1

            data_excel = {'Código':code_list_save,'Função':['' for i in range(code_list_save.__len__())]}
            planilha = pd.DataFrame(data_excel)
            try:
                if os.path.exists('exported'):
                    planilha.to_excel('exported/Modelo_de_Códigos.xlsx',index=False)
                    self.message_box_show('Exportado','O modelo foi exportado com sucesso!')
                else:
                    os.makedirs('exported')
                    planilha.to_excel('exported/Modelo_de_Códigos.xlsx',index=False)
                    self.message_box_show('Exportado','O modelo foi exportado com sucesso!')

            except Exception:
                self.message_box_show('Erro','Não foi possível exportar a planilha!')


    def get_position_chat(self):
        self.position_chat = pyautogui.position()
        self.button_get_position.setEnabled(True)
        self.button_start_write.setEnabled(True)
        self.message_box_show('Finalizado!',f'A posição foi pega com sucesso!\n{self.position_chat}')
    
    def message_box_show(self, title_msn, msn):
        message_window = QMessageBox(self)
        message_window.setWindowTitle(title_msn)
        message_window.setContentsMargins(0,0,23,0)
        message_window.setText(msn)
        message_window.exec()

class ThreadSystem(QThread):
    sinal = Signal()

    def __init__(self, button_locker: QPushButton):
        super().__init__()
        self.button_locker = button_locker

    def run(self):
        self.button_locker.setEnabled(False)
        time.sleep(2)
        self.button_locker.setEnabled(True)
        self.sinal.emit()
        

class ThreadProgress(QThread):
    sinal = Signal()
    update_bar_value = Signal(int)
    def __init__(self, min, max, position_chat, bar:QProgressBar, load_func,button_locker:QPushButton, text_ref, index_ref):
        super().__init__()
        self.min = min
        self.max = max

        self.position_chat = position_chat
        self.bar = bar

        self.load_func = load_func
        self.button_locker = button_locker

        self.text_ref = text_ref
        self.index_ref = index_ref

    def run(self):
        self.button_locker.setEnabled(False)
        self.bar.setMinimum(self.min-1)
        self.bar.setMaximum(self.max)

        
        for i in range(self.min, self.max + 1):
            pyautogui.click(self.position_chat)
            pyperclip.copy(self.load_func())
            time.sleep(0.3)
            pyautogui.hotkey('ctrl','v')
            self.update_bar()
            time.sleep(1)
            pyautogui.press('ENTER')
            self.index_ref += 1
            
        self.button_locker.setEnabled(True)
        self.sinal.emit()

    def update_bar(self):
        self.bar.setValue(self.index_ref)

if __name__ == '__main__':
    app = QApplication()
    window = CodeTest()
    window.show()
    sys.exit(app.exec())