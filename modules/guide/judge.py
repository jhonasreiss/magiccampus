import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QLabel,
                               QScrollArea)
from PySide6.QtGui import Qt, QPainter, QColor, QPixmap, QLinearGradient, QFont

class JudgeSystem(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.layoutInit()


    def initUI(self):
        self.setWindowTitle('Terra Julgamento')
        self.setFixedSize(900,600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QHBoxLayout()
        self.central_widget.setLayout(self.central_layout)


    def layoutInit(self):
        # Scroll Area =======================================
        self.area_scroll = QScrollArea()
        self.widget_scroll_area = QWidget(self.area_scroll)
        self.layout_area = QVBoxLayout(self.widget_scroll_area)
        self.area_scroll.setWidget(self.widget_scroll_area)
        self.area_scroll.setWidgetResizable(True)
        self.central_layout.addWidget(self.area_scroll)
        #====================================================
        
        style = '''
                QScrollArea > QWidget > QWidget{
                    background-color: #63270f;
                    border-left: 2px solid black;
                    border-right: 1px solid black;
                    border-top: 2px solid black;
                    border-bottom: 2px solid black;
                }

                QScrollBar::handle:vertical {
                    background-color: #cc4008;
                }

                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    background: none;
                }
                '''
        self.area_scroll.setStyleSheet(style)
        self.layout_area.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_img_01 = QLabel()
        label_img_01.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap_label_01 = QPixmap()
        pixmap_label_01.load('Imgs/judge/02.jpg')
        label_img_01.setPixmap(pixmap_label_01)

        label_img_02 = QLabel()
        label_img_02.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap_label_02 = QPixmap()
        pixmap_label_02.load('Imgs/judge/01.jpg')
        label_img_02.setPixmap(pixmap_label_02)

        label_text = [QLabel() for i in range(10)]
        label_img = [QPixmap() for i in range(10)]
        font_base = [QFont() for i in range(10)]

        list_img_path = ['Imgs/judge/02.jpg',
                         'Imgs/judge/03.jpg',
                         '',
                         '',
                         '',
                         '',
                         '',
                         '',
                         '',
                         '',
                         ''
                         ]

        for i in font_base:
            i.setBold(True)
            i.setPointSize(20)

        for i in range(label_img.__len__()):
            label_img[i].load(list_img_path[i])

        label_text[0].setFont(font_base[0])
        label_text[2].setFont(font_base[1])
        label_text[3].setFont(font_base[2])
        label_text[5].setFont(font_base[3])
        label_text[6].setFont(font_base[4])
        label_text[7].setFont(font_base[5])
        label_text[8].setFont(font_base[6])

        label_text[0].setFixedHeight(50)
        label_text[2].setFixedHeight(60)
        label_text[3].setFixedHeight(80)
        label_text[5].setFixedHeight(80)
        label_text[6].setFixedHeight(140)
        label_text[7].setFixedHeight(80)
        label_text[8].setFixedHeight(80)

        label_text[0].setText('Terra Julgamento é aberto no LV130')
        label_text[1].setPixmap(label_img[0])

        label_text[2].setText('Julgamento é divido em DESAFIO e cada desafio possui um CHEFE')
        label_text[3].setText('1° Desafio\nMate o CHEFE que fica no centro')
        label_text[4].setPixmap(label_img[1])

        label_text[5].setText('2° Desafio\nMate todos os CHEFES em ordem')
        label_text[6].setText('3° Desafio\nMate todos os CHEFES Diferentes\nDepois volte para o centro\ne mate o último CHEFE')
        label_text[7].setText('4° Desafio\n')
        label_text[8].setText('5° Desafio\n')
        
        for i in label_text:
            i.setStyleSheet('color: white')
            i.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if label_text:
                self.layout_area.addWidget(i)



    def paintEvent(self, event):
        paint = QPainter(self)
        grad = QLinearGradient(0,0,0,self.height())
        grad.setColorAt(0,QColor('#c71010'))
        grad.setColorAt(1,QColor('#9c3811'))
        paint.fillRect(self.rect(), grad)

if __name__ == "__main__":
    app = QApplication([])
    window = JudgeSystem()
    window.show()
    sys.exit(app.exec())