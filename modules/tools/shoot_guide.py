import sys 
import tkinter as tk
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, 
                               QGroupBox, QSpinBox, QAbstractSpinBox, QLabel, QPushButton, 
                               QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QGradient


class ShootGuide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupInit()
        self.CreateWidgets()
        self.AddWidgets()

    def setupInit(self):
        
        self.setWindowTitle("Auxiliador de Cadeia")
        self.largura = 850
        self.altura = 690
        # pega a resolução da tela =======================
        root = tk.Tk()
        root.withdraw()
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        root.destroy()
        
        # calcula para sempre ser o centro mesmo com o tamanho
        # diferente
        x = (largura_tela - self.largura)//2
        y = (altura_tela - self.altura)//2

        # ================================================

        self.setGeometry(x,y-6,self.largura,self.altura)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)


    def CreateWidgets(self):

        # GRUPOS ===================================================

        self.group_display = QGroupBox(' Display ')
        self.group_single_skill = QGroupBox(' Penas ')
        self.group_area_skill = QGroupBox(' Magia em Área Slot 1')
        self.group_area_skill_2 = QGroupBox(' Magia em Área Slot 2')
        self.group_show_element = QGroupBox(' Elemento ')

        self.layout_display = QHBoxLayout(self.group_display)
        self.layout_single_skill = QGridLayout(self.group_single_skill)
        self.layout_area_skill = QGridLayout(self.group_area_skill)
        self.layout_area_skill_2 = QGridLayout(self.group_area_skill_2)
        self.layout_show_element = QVBoxLayout(self.group_show_element)

        self.group_display.setFixedSize(self.largura*0.968,self.altura*0.08)
        self.group_single_skill.setFixedSize(self.largura*0.7,self.altura*0.15)
        self.group_area_skill.setFixedSize(self.largura*0.7,self.altura*0.35)
        self.group_area_skill_2.setFixedSize(self.largura*0.7,self.altura*0.35)
        self.group_show_element.setFixedWidth(self.largura*0.25)
        
        self.layout_single_skill.setContentsMargins(0,0,0,0)
        self.layout_area_skill_2.setContentsMargins(0,0,0,0)

        

        # ===========================================================

        # ICONES ====================================================

        self.buttons_single = [QPushButton(f"{i}") for i in range(10)]
        self.buttons_area_skill = [QPushButton(f"{i}") for i in range(40)]
        self.buttons_area_skill_2 = [QPushButton(f"{i}") for i in range(40)]

        # ===========================================================


    def AddWidgets(self):

        # GRUPOS ADD ==================================================
        self.central_layout.addWidget(self.group_display,1,1,1,2)
        self.central_layout.addWidget(self.group_single_skill,2,1,1,1)
        self.central_layout.addWidget(self.group_area_skill,3,1,1,1)
        self.central_layout.addWidget(self.group_area_skill_2,4,1,1,1)
        self.central_layout.addWidget(self.group_show_element,2,2,3,1)
        # =============================================================

        # ADICIONA BOTÕES =============================================
        self.addButtons(0,self.buttons_single)
        self.addButtons(1,self.buttons_area_skill, self.layout_area_skill)
        self.addButtons(1,self.buttons_area_skill_2, self.layout_area_skill_2)
        
        
    def addButtons(self, mode_insert:QPushButton, buttons_target:list, layout_target:QGridLayout = None):

        # adiciona skill de alvo único ==============================
        if mode_insert == 0:
            row = 1
            for i in buttons_target:
                i.setFixedSize(40,40)
                label_lv = QLabel(f"Lv{row}")
                label_lv.setFixedSize(32,32)
                label_lv.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.layout_single_skill.addWidget(label_lv,1,row,1,1)
                self.layout_single_skill.addWidget(i,1,row,2,1)
                row += 1

        # adiciona skill de área ==============================
        if mode_insert == 1:
            row = 1
            column = 1
            for i in buttons_target:
                if row > 10:
                    column+=1
                    row = 1
                i.setFixedSize(36,36)
                if row <= 10 and column <= 1:
                    label_lv = QLabel(f"Lv{row}")
                    label_lv.setFixedSize(32,32)
                    label_lv.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    layout_target.addWidget(label_lv,1,row,1,1)
                layout_target.addWidget(i,column,row,2,1)
                row += 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShootGuide()
    window.show()
    sys.exit(app.exec())