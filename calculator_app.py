import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        ##Buttons#########################
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter', clicked=self.func_result)
        btn_clear = qtw.QPushButton('Clear', clicked=self.func_clear)
        btn_0 = qtw.QPushButton('0', clicked=lambda: self.num_press('0'))
        btn_0.setStyleSheet("background-color: red")
        btn_1 = qtw.QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_1.setStyleSheet("background-color: red")
        btn_2 = qtw.QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_2.setStyleSheet("background-color: red")
        btn_3 = qtw.QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_3.setStyleSheet("background-color: red")
        btn_4 = qtw.QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_4.setStyleSheet("background-color: red")
        btn_5 = qtw.QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_5.setStyleSheet("background-color: red")
        btn_6 = qtw.QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_6.setStyleSheet("background-color: red")
        btn_7 = qtw.QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_7.setStyleSheet("background-color: red")
        btn_8 = qtw.QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_8.setStyleSheet("background-color: red")
        btn_9 = qtw.QPushButton('9', clicked=lambda: self.num_press('9'))
        btn_9.setStyleSheet("background-color: red")

        btn_plus = qtw.QPushButton('+', clicked=lambda: self.func_press('+'))
        btn_plus.setStyleSheet("background-color: green")
        btn_minus = qtw.QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_minus.setStyleSheet("background-color: green")
        btn_mult = qtw.QPushButton('*', clicked=lambda: self.func_press('*'))
        btn_mult.setStyleSheet("background-color: green")
        btn_divid = qtw.QPushButton('/', clicked=lambda: self.func_press('/'))
        btn_divid.setStyleSheet("background-color: green")
        btn_mod = qtw.QPushButton('%\nremainder', clicked=lambda: self.func_press('%'))
        btn_mod.setStyleSheet("background-color: green")
        btn_power = qtw.QPushButton('^', clicked=lambda: self.func_press('**'))
        btn_power.setStyleSheet("background-color: green")

        ##ading buttons to their places######

        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_1, 2, 0)
        container.layout().addWidget(btn_2, 2, 1)
        container.layout().addWidget(btn_3, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_4, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_6, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn_7, 4, 0)
        container.layout().addWidget(btn_8, 4, 1)
        container.layout().addWidget(btn_9, 4, 2)
        container.layout().addWidget(btn_mult, 4, 3)
        container.layout().addWidget(btn_power, 5, 2)
        container.layout().addWidget(btn_0, 5, 1)
        container.layout().addWidget(btn_mod, 5, 0)
        container.layout().addWidget(btn_divid, 5, 3)
        self.layout().addWidget(container)

    def num_press(self, key_value):
        self.temp_nums.append(key_value)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, key_operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(key_operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        if self.result_field == '':
            self.result_field.setText('')
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def func_clear(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
