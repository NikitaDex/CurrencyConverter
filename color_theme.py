from PyQt5 import QtGui

def background_black(self):
	# фрейм
	self.ui.frame.setStyleSheet("background-color:#fb5b5d;")
	# какую сумму хочу конвертировать
	self.ui.input_price.setStyleSheet("background-color: #22222e;border: 2px solid #f66867;border-radius: 30;color:white;") 
	# вывод
	self.ui.output_amount.setStyleSheet("background-color: #22222e;color:white;border: 2px solid #f66867;border-radius: 30;")
	# общий фон
	self.ui.centralwidget.setStyleSheet("background-color: #22222e")
	# first box
	self.ui.first_box.setStyleSheet("background-color: #22222e;border: 2px solid #f66867 ;color:white;")
	self.ui.first_box.setFont(QtGui.QFont("MS Shell Dlg 2", 8))
	# second box
	self.ui.second_box.setStyleSheet("background-color: #22222e;border: 2px solid #f66867 ;color:white;")
	self.ui.second_box.setFont(QtGui.QFont("MS Shell Dlg 2", 8))
	# push button
	self.ui.pushButton.setStyleSheet("QPushButton{color:white;background-color: #fb5b5d;border-radius: 30;} QPushButton:pressed{background-color:#fa4244;border-radius: 30; }")
	#copy button
	self.ui.button_copy.setStyleSheet("QPushButton { background-color: #fb5b5d; border-radius: 30px;} QPushButton:pressed{ background-color:#fa4244;border-radius: 30px;}")
	# button lang
	self.ui.button_lang.setStyleSheet("QPushButton { background-color: #fb5b5d; border-radius: 30px;} QPushButton:pressed{ background-color:#fa4244;border-radius: 30px;}")
	
def background_white(self):
	# фрейм
	self.ui.frame.setStyleSheet("background-color:#39E1D9;")
	# какую сумму хочу конвертировать
	self.ui.input_price.setStyleSheet("background-color: white;border: 2px solid #39E1D9;border-radius: 30;color:black;") 
	# вывод
	self.ui.output_amount.setStyleSheet("background-color: white;color:black;border: 2px solid #39E1D9;border-radius: 30;")
	# общий фон
	self.ui.centralwidget.setStyleSheet("background-color: white")
	# first box
	self.ui.first_box.setStyleSheet("background-color: white;border: 2px solid #39E1D9 ;color:black;")
	self.ui.first_box.setFont(QtGui.QFont("MS Shell Dlg 2", 8))
	# second box
	self.ui.second_box.setStyleSheet("background-color: white;border: 2px solid #39E1D9 ;color:black;")
	self.ui.second_box.setFont(QtGui.QFont("MS Shell Dlg 2", 8))
	# push button
	self.ui.pushButton.setStyleSheet("QPushButton{color:white;background-color: #39E1D9;border-radius: 30;} QPushButton:pressed{background-color:#00C7D9;border-radius: 30; }")
	# copy button
	self.ui.button_copy.setStyleSheet("QPushButton { background-color: #39E1D9; border-radius: 30px;} QPushButton:pressed{ background-color:#00C7D9;border-radius: 30px;}")
	# lang button
	self.ui.button_lang.setStyleSheet("QPushButton { background-color: #39E1D9; border-radius: 30px;} QPushButton:pressed{ background-color:#00C7D9;border-radius: 30px;}")
	

def background_blind(self):
	# фрейм
	self.ui.frame.setStyleSheet("background-color:white;")
	# какую сумму хочу конвертировать
	self.ui.input_price.setStyleSheet("background-color: white;border: 2px solid black;border-radius: 30;color:black;") 
	# вывод
	self.ui.output_amount.setStyleSheet("background-color: white;color:black;border: 2px solid black;border-radius: 30;")
	# общий фон
	self.ui.centralwidget.setStyleSheet("background-color: white")
	# first box
	self.ui.first_box.setStyleSheet("background-color: white;border: 2px solid black ;color:black;")
	self.ui.first_box.setFont(QtGui.QFont("MS Shell Dlg 2", 10, QtGui.QFont.Bold))
	# second box
	self.ui.second_box.setStyleSheet("background-color: white;border: 2px solid black ;color:black;")
	self.ui.second_box.setFont(QtGui.QFont("MS Shell Dlg 2", 10, QtGui.QFont.Bold))
	# push button
	self.ui.pushButton.setStyleSheet("QPushButton{color:black;background-color: white;border-radius: 30;border: 2px solid black;} QPushButton:pressed{background-color:white;border-radius: 30;border: 2px solid black; }")
	# copy button
	self.ui.button_copy.setStyleSheet("QPushButton { background-color: white; border-radius: 30px;border: 2px solid black;} QPushButton:pressed{ background-color:white;border-radius: 30px;border: 2px solid black;}")
	# надпись КОНВЕРТЕР ВАЛЮТ
	self.ui.label.setStyleSheet("color:black")
	# button lang
	self.ui.button_lang.setStyleSheet("QPushButton { background-color: white; border-radius: 30px;border: 2px solid black;} QPushButton:pressed{ background-color:white;border-radius: 30px;border: 2px solid black;}")
	