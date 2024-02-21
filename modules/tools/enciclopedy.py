import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QGroupBox, QComboBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import Qt as qt_gui, QPainter, QColor, QLinearGradient

class WindowTasks(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_init()
        self.setup_layout()
        self.setup_widget()
        self.add_widgets()

    
    def setup_init(self):
        # janela
        self.setFixedSize(800,650)
        self.setWindowTitle('Todas as Atividades')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        # ---

    def setup_layout(self):
        self.layout_header = QVBoxLayout() # responsável pelo cabeçalho
        self.layout_body = QVBoxLayout() # todo o corpo
        self.layout_footer = QVBoxLayout() # rodapé

        self.layout_header.setAlignment(qt_gui.AlignmentFlag.AlignCenter)

    def setup_widget(self):
        self.header_label = QLabel('Todas as Tarefas')
        self.header_label.setStyleSheet('font-size: 35px')

        # area scroll layout
        self.area_scroll = QScrollArea()
        self.widget_scroll = QWidget(self.area_scroll)
        self.layout_scroll = QVBoxLayout(self.widget_scroll)
        
        # area scroll setup
        self.area_scroll.setFixedHeight(500)
        self.area_scroll.setWidget(self.widget_scroll)
        self.area_scroll.setWidgetResizable(True)
        self.layout_scroll.setAlignment(qt_gui.AlignmentFlag.AlignTop)

        self.area_scroll.setStyleSheet('background-color: blue')
        

        # groupbox
        self.group_footer = QGroupBox()
        self.layout_group_footer = QHBoxLayout(self.group_footer)


    
    def add_widgets(self):
        # adicionando layouts
        self.central_layout.addLayout(self.layout_header)
        self.central_layout.addLayout(self.layout_body)
        self.central_layout.addLayout(self.layout_footer)


        # adicionando widgets
        self.layout_header.addWidget(self.header_label)
        self.layout_body.addWidget(self.area_scroll)
        self.layout_footer.addWidget(self.group_footer)

        tarefas_nome = ['Enigma','Campo de Batalha','Arena Mascote','Lagoa de dong-xuen']
        
        label_tasks = [QLabel() for i in range(len(tarefas_nome))]

        index_name = 0
        for i in tarefas_nome:
            label_tasks[index_name].setText(i)
            index_name += 1

        for i in label_tasks:
            i.setStyleSheet('''
                            QLabel{
                                border: 1px solid white; 
                                border-radius: 4px; 
                                color:white; 
                                padding-left:20px;
                            }

                            QLabel:hover{
                                background-color: cyan;
                            }
                            ''')
            i.setFixedHeight(50)
            self.layout_scroll.addWidget(i)
            

    def paintEvent(self, event):
        paint = QPainter(self)
        grad = QLinearGradient(0,0,0,100)
        grad.setColorAt(0,QColor(0, 4, 255))
        grad.setColorAt(1,QColor(0.5, 4, 140))
        grad.setColorAt(0,QColor(0, 4, 255))
        paint.fillRect(self.rect(),grad)

   

if __name__ == '__main__':
    app = QApplication()
    window = WindowTasks()
    window.show()
    sys.exit(app.exec())