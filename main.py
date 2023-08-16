import sys
import os
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter
from translate import translate_to_first_box, translate_to_second_box
from color_theme import *
from language import *

import requests
import tempfile, zipfile, io

import win32clipboard


url = 'http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'
r = requests.get(url)
with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
	archive.extractall('output')

copy = ""
class CurrencyConv(QtWidgets.QMainWindow):

	def __init__(self):
		super(CurrencyConv,self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.init_UI()

		self.ui.radio2.setChecked(True) 
		self.ui.radio1.clicked.connect(self.theme) 
		self.ui.radio2.clicked.connect(self.theme)
		self.ui.radio3.clicked.connect(self.theme)

		self.ui.button_lang.clicked.connect(self.change_lang_func)
	
		

	def init_UI(self):
		PATH = os.path.abspath(os.curdir)
		self.setWindowTitle("Конвертер валют")
		self.setWindowIcon(QIcon(PATH + '\\images\\banknotespaymentmoney_billetesdebanco_pag_3773.png'))

		self.ui.input_price.setPlaceholderText('У меня есть:')
		self.ui.output_amount.setPlaceholderText('Я получу:')
		self.ui.pushButton.clicked.connect(self.converter)


		self.ui.button_copy.clicked.connect(self.send_to_clipboard) ##### 3

        
	def converter(self):
		PATH = os.path.abspath(os.curdir)
		c = CurrencyConverter(PATH + '\\output\\eurofxref.csv')

		first_box = str(self.ui.first_box.currentText())
		second_box = str(self.ui.second_box.currentText())
		input_price = int(self.ui.input_price.text()) # сколько у меня есть

		output_amount = round(c.convert(input_price, '%s' % (translate_to_first_box(first_box)), '%s' % (translate_to_second_box(second_box))), 3)
		global copy
		copy = str(output_amount)
		self.ui.output_amount.setText(str(output_amount))


	def theme(self):
		if self.ui.radio1.isChecked():
			background_white(self)
		if self.ui.radio2.isChecked():
			background_black(self)
		if self.ui.radio3.isChecked():
			background_blind(self)

	global change_lang
	change_lang = 0
	def change_lang_func(self):
		global change_lang
		if change_lang % 2 == 0:
			lang_eng(self)
		if change_lang % 2 == 1:
			lang_rus(self)
		change_lang += 1


	def send_to_clipboard(self):
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()		
		win32clipboard.SetClipboardData( win32clipboard.CF_UNICODETEXT, copy) 
		win32clipboard.CloseClipboard()



app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()


sys.exit(app.exec())


