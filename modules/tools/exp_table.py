import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                               QSpinBox, QLabel, QGroupBox, QTabWidget, QLineEdit, QErrorMessage)
from PySide6.QtGui import QPixmap, QFont, QIcon
from PySide6.QtCore import Qt, QThread, Signal

class ExpTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabela de EXP')
        self.setFixedSize(760,680)
        self.setWindowIcon(QIcon('Icons/icon_main.png'))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.central_layout.setContentsMargins(0,5,0,10)

        self.list_value = {1:'0',
                           2:'72',
                           3:'285',
                           4:'568',
                           5:'849',
                           6:'1387',
                           7:'2198',
                           8:'3289',
                           9:'4583',
                           10:'5278',
                           11:'7261',
                           12:'12873',
                           13:'23781',
                           14:'35605',
                           15:'41579',
                           16:'48091',
                           17:'55154',
                           18:'62780',
                           19:'70986',
                           20:'79783',
                           21:'89184',
                           22:'171424',
                           23:'189825',
                           24:'209337',
                           25:'229978',
                           26:'251770',
                           27:'274735',
                           28:'298889',
                           29:'324254',
                           30:'350849',
                           31:'378691',
                           32:'647575',
                           33:'695841',
                           34:'746178',
                           35:'798613',
                           36:'853174',
                           37:'909890',
                           38:'968786',
                           39:'1029890',
                           40:'1093230',
                           41:'1158830',
                           42:'1831133',
                           43:'1935923',
                           44:'2044200',
                           45:'2156007',
                           46:'2271377',
                           47:'2390351',
                           48:'2512962',
                           49:'2639247',
                           50:'2769243',
                           51:'2902984',
                           52:'4329157',
                           53:'4530396',
                           54:'4737116',
                           55:'4949366',
                           56:'5167194',
                           57:'5390648',
                           58:'5619775',
                           59:'5854621',
                           60:'6095235',
                           61:'6341662',
                           62:'9045195',
                           63:'9399363',
                           64:'9761694',
                           65:'10132247',
                           66:'10511082',
                           67:'10898263',
                           68:'11293847',
                           69:'11697896',
                           70:'12110467',
                           71:'16679586',
                           72:'17251643',
                           73:'17835277',
                           74:'18430565',
                           75:'19037585',
                           76:'19656142',
                           77:'20287120',
                           78:'20929787',
                           79:'21584483',
                           80:'22251287',
                           81:'22930268',
                           82:'30667134',
                           83:'50148734',
                           84:'63496189',
                           85:'65343243',
                           86:'67222095',
                           87:'69132926',
                           88:'71075911',
                           89:'73051232',
                           90:'75059063',
                           91:'154199166',
                           92:'192173310',
                           93:'197286133',
                           94:'202479566',
                           95:'207754025',
                           96:'213109928',
                           97:'218547688',
                           98:'224067720',
                           99:'229670429',
                           100:'235356228',
                           101:'241125519',
                           102:'361785218',
                           103:'493976949',
                           104:'505739038',
                           105:'517667332',
                           106:'529762611',
                           107:'542025640',
                           108:'554457190',
                           109:'567058023',
                           110:'579828900',
                           111:'592770578',
                           112:'692971123',
                           113:'708653358',
                           114:'724498791',
                           115:'740507425',
                           116:'756679260',
                           117:'773014293',
                           118:'789512528',
                           119:'806173961',
                           120:'822998596',
                           121:'839986430',
                           122:'1179298923',
                           123:'1203852125',
                           124:'1228640946',
                           125:'1367634969',
                           126:'1395191401',
                           127:'1423004871',
                           128:'1571998331',
                           129:'1602686512',
                           130:'1633653151',
                           131:'1921036445',
                           132:'2219620225',
                           133:'2848163096',
                           134:'2848163096',
                           135:'3178391467',
                           136:'3519437316',
                           137:'3871435281',
                           138:'4234520003',
                           139:'4608826122',
                           140:'4994488279',
                           141:'5391641112',
                           142:'5719708431',
                           143:'6056994871',
                           144:'6578910322',
                           145:'6943762790',
                           146:'7320061257',
                           147:'7778897094',
                           148:'8145270812',
                           149:'8521081848',
                           150:'9092866636'
                           }

        self.list_value_2 = {1:'72',
                           2:'285',
                           3:'568',
                           4:'849',
                           5:'1387',
                           6:'2198',
                           7:'3289',
                           8:'4583',
                           9:'5278',
                           10:'7261',
                           11:'12873',
                           12:'23781',
                           13:'35605',
                           14:'41579',
                           15:'48091',
                           16:'55154',
                           17:'62780',
                           18:'70986',
                           19:'79783',
                           20:'89184',
                           21:'171424',
                           22:'189825',
                           23:'209337',
                           24:'229978',
                           25:'251770',
                           26:'274735',
                           27:'298889',
                           28:'324254',
                           29:'350849',
                           30:'378691',
                           31:'647575',
                           32:'695841',
                           33:'746178',
                           34:'798613',
                           35:'853174',
                           36:'909890',
                           37:'968786',
                           38:'1029890',
                           39:'1093230',
                           40:'1158830',
                           41:'1831133',
                           42:'1935923',
                           43:'2044200',
                           44:'2156007',
                           45:'2271377',
                           46:'2390351',
                           47:'2512962',
                           48:'2639247',
                           49:'2769243',
                           50:'2902984',
                           51:'4329157',
                           52:'4530396',
                           53:'4737116',
                           54:'4949366',
                           55:'5167194',
                           56:'5390648',
                           57:'5619775',
                           58:'5854621',
                           59:'6095235',
                           60:'6341662',
                           61:'9045195',
                           62:'9399363',
                           63:'9761694',
                           64:'10132247',
                           65:'10511082',
                           66:'10898263',
                           67:'11293847',
                           68:'11697896',
                           69:'12110467',
                           70:'16679586',
                           71:'17251643',
                           72:'17835277',
                           73:'18430565',
                           74:'19037585',
                           75:'19656142',
                           76:'20287120',
                           77:'20929787',
                           78:'21584483',
                           79:'22251287',
                           80:'22930268',
                           81:'30667134',
                           82:'50148734',
                           83:'63496189',
                           84:'65343243',
                           85:'67222095',
                           86:'69132926',
                           87:'71075911',
                           88:'73051232',
                           89:'75059063',
                           90:'154199166',
                           91:'192173310',
                           92:'197286133',
                           93:'202479566',
                           94:'207754025',
                           95:'213109928',
                           96:'218547688',
                           97:'224067720',
                           98:'229670429',
                           99:'235356228',
                           100:'241125519',
                           101:'361785218',
                           102:'493976949',
                           103:'505739038',
                           104:'517667332',
                           105:'529762611',
                           106:'542025640',
                           107:'554457190',
                           108:'567058023',
                           109:'579828900',
                           110:'592770578',
                           111:'692971123',
                           112:'708653358',
                           113:'724498791',
                           114:'740507425',
                           115:'756679260',
                           116:'773014293',
                           117:'789512528',
                           118:'806173961',
                           119:'822998596',
                           120:'839986430',
                           121:'1179298923',
                           122:'1203852125',
                           123:'1228640946',
                           124:'1367634969',
                           125:'1395191401',
                           126:'1423004871',
                           127:'1571998331',
                           128:'1602686512',
                           129:'1633653151',
                           130:'1921036445',
                           131:'2219620225',
                           132:'2848163096',
                           133:'2848163096',
                           134:'3178391467',
                           135:'3519437316',
                           136:'3871435281',
                           137:'4234520003',
                           138:'4608826122',
                           139:'4994488279',
                           140:'5391641112',
                           141:'5719708431',
                           142:'6056994871',
                           143:'6578910322',
                           144:'6943762790',
                           145:'7320061257',
                           146:'7778897094',
                           147:'8145270812',
                           148:'8521081848',
                           149:'9092866636'
                           }

        self.group_box = [QGroupBox() for i in range(3)]
        list_title = ['Calcular EXP','EXP neceessária para upar','EXP simplificada']
        self.layout_box = [QVBoxLayout() for i in range(3)]
        self.layout_box[0].setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_box[1].setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_box[2].setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_box[1].setContentsMargins(0,0,0,15)
        self.layout_box[2].setContentsMargins(0,0,0,15)

        index = 0
        for i in self.group_box:
            i.setTitle(list_title[index])
            i.setLayout(self.layout_box[index])
            i.setFixedWidth(240)
            index += 1

        self.pixmap = QPixmap('Imgs/Tabela de EXP.jpg')
        self.adjust_size(0)
        label_table = QLabel()
        label_table.setPixmap(self.pixmap)
        label_table.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.central_layout.addWidget(label_table)
        
        # aba 1
        self.layout_calculate = QHBoxLayout()
        self.input_value = [QSpinBox() for i in range(2)]
        self.input_value[0].valueChanged.connect(self.verification_input)
        self.input_value[1].valueChanged.connect(self.verification_input)
        self.label_lv_begin = QLabel('Level Inicial')
        self.label_lv_end = QLabel('Level Final')
        self.button_calculate = QPushButton('Calcular')
        self.layout_button_aling = QHBoxLayout()
        self.layout_button_aling.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_calculate.clicked.connect(lambda: self.thread_system(self.calculate))

        # aba 2
        self.layout_calculate_2 = QHBoxLayout()
        self.input_value_2 = QSpinBox()
        self.input_exp_value = QLineEdit()
        self.button_calculate_2 = QPushButton('Calcular')
        self.layout_button_aling_2 = QHBoxLayout()
        self.layout_button_aling_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_calculate_2.clicked.connect(lambda: self.thread_system(self.calculate_for_input))
        

        self.exp_preview = QLabel()
        self.exp_preview_simp = QLabel()
        self.exp_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.size_font(self.exp_preview, 10)
        self.size_font(self.exp_preview_simp, 25)
        
        self.input_value[0].setMaximum(150)
        self.input_value[0].setMinimum(1)
        self.input_value[1].setMaximum(150)
        self.input_value[1].setMinimum(1)
        self.input_value_2.setMaximum(149)
        self.input_value_2.setMinimum(1)
        self.input_exp_value.setMaxLength(12)
        self.button_calculate.setFixedWidth(60)
        self.button_calculate_2.setFixedWidth(60)

        # tab =======================
        self.tab_lv = QTabWidget()
        self.setStyleSheet('''
                           QTabBar::tab { 
                                height: 40px; 
                                width: 109px; 
                           }
                           ''')
        self.tab_lv.currentChanged.connect(self.change_text)
        self.tab_calculate_lv()
        self.tab_calculate_exp()
        # ==========================

        self.central_layout.addLayout(self.layout_calculate)
        for i in self.group_box:
            self.layout_calculate.addWidget(i)

        self.layout_box[0].addWidget(self.tab_lv)
        self.layout_box[1].addWidget(self.exp_preview)
        self.layout_box[2].addWidget(self.exp_preview_simp)

    def change_text(self, index):
        if index == 0:
            self.group_box[1].setTitle('EXP neceessária para upar')
            self.group_box[2].setTitle('EXP simplificada')
            self.exp_preview.setText('')
            self.exp_preview_simp.setText('')

        elif index == 1:
            self.group_box[1].setTitle('Quantidade de aumento de LV')
            self.group_box[2].setTitle('Exp de Sobra')
            self.exp_preview.setText('')
            self.exp_preview_simp.setText('')

    def verification_input(self):
            if self.input_value[0].value() > self.input_value[1].value():
                self.input_value[1].setStyleSheet('color: red')
            else:
                self.input_value[1].setStyleSheet('color: black')

    def tab_calculate_lv(self):
        tab = QWidget()
        layout_tab = QVBoxLayout()
        layout_tab.addWidget(self.label_lv_begin)
        layout_tab.addWidget(self.input_value[0])
        layout_tab.addWidget(self.label_lv_end)
        layout_tab.addWidget(self.input_value[1])
        layout_tab.addLayout(self.layout_button_aling)
        self.layout_button_aling.addWidget(self.button_calculate)
        tab.setLayout(layout_tab)
        self.tab_lv.addTab(tab,'Calcular por LV')

    def tab_calculate_exp(self):
        tab = QWidget()
        layout_tab = QVBoxLayout()
        layout_tab.addWidget(QLabel('Lv Atual'))
        layout_tab.addWidget(self.input_value_2)
        layout_tab.addWidget(QLabel('EXP Atual'))
        layout_tab.addWidget(self.input_exp_value)
        layout_tab.addLayout(self.layout_button_aling_2)
        self.layout_button_aling_2.addWidget(self.button_calculate_2)
        tab.setLayout(layout_tab)
        self.tab_lv.addTab(tab,'Calcular por EXP')

        
    def size_font(self, label: QLabel, size):
        size_font = label.font()
        current_size = size_font.pointSize()
        new_font = QFont(size_font)
        new_font.setPointSize(current_size + size)
        label.setFont(new_font)

    def adjust_size(self, size=0):
        size_formatter_x = 750 - size
        size_formatter_y = 438 - size
        self.pixmap = self.pixmap.scaled(size_formatter_x,size_formatter_y)

    def thread_system(self, func):
        self.worker = TheadFunction()
        self.worker.py_signal.connect(func)
        self.worker.start()

    def calculate(self):
        try:
            self.exp_preview_simp.setStyleSheet('font-size: 45px')
            start_key = int(self.input_value[0].value())
            end_key = int(self.input_value[1].value())

            if end_key < start_key:
                self.erro_message_display('O Level Inicial não pode ser maior que o Level Final!')
            else:
                start_key, end_key = min(start_key, end_key), max(start_key, end_key)

                total_exp = 0
                for key in range(start_key, end_key + 1):
                    total_exp += int(self.list_value[key])

                value_exp = total_exp
                formater = f"{value_exp:,}"
                result = formater.replace(',','.')
                self.exp_preview.setText(result)
                self.display_simplified_result(value_exp)
        except:
            pass

    def erro_message_display(self,message):
        error_message = QErrorMessage()
        error_message.setWindowTitle('Error')
        error_message.showMessage(message)
        error_message.exec()

    def display_simplified_result(self, result):
        if 100 <= result < int('1000'):
            self.exp_preview_simp.setText(f"{result // 100}")
        elif 1000 <= result < 1000000:
            self.exp_preview_simp.setText(f"{result // 1000}K")
        elif int('1000000') <= result < int('1000000000'):
            self.exp_preview_simp.setText(f"{result // int('1000000')}KK")
        elif result >= int('1000000000'):
            self.exp_preview_simp.setText(f"{result // int('1000000000')}KKK")
        else:
            self.exp_preview_simp.setText(str(result))


    def calculate_for_input(self):
        try:
            self.exp_preview_simp.setStyleSheet('font-size: 25px')
            start_key = self.input_value_2.value()
            end_key = int(self.input_exp_value.text())

            if end_key is None or end_key != 0:
                lv_up = 0
                while start_key < len(self.list_value_2):
                    target_exp = self.list_value_2[start_key]
    
                    if end_key >= int(target_exp):
                        end_key -= int(target_exp)
                        lv_up += 1
                        start_key += 1
                    else:
                        break

                formater = f"{end_key:,}"
                result = formater.replace(',','.')
                if lv_up > 0 and lv_up < 2:
                    self.exp_preview.setText(f'Aumentará \n{lv_up} Level!')
                elif lv_up > 1:
                    self.exp_preview.setText(f'Aumentará \n{lv_up} Leveis!')
                else:
                    self.exp_preview.setText('Experiência\nInsuficiente!')
                self.exp_preview_simp.setText(result)

        except ValueError:
            self.erro_message_display(f'Erro: Campo EXP ATUAL não pode conter letras somente números!')


class TheadFunction(QThread):
    py_signal = Signal()

    def run(self):
        self.py_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpTable()
    window.show()
    sys.exit(app.exec())