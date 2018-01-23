import sys
from PyQt4.QtGui import * 
import webbrowser

class Stages(QWidget):
	def __init__(self, parent=None):
		super(Stages,self).__init__(parent)
		self.resize(800,637)
		self.setStyleSheet("background-color: black")

		image = QPixmap("buzz.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(0,0)

		self.denial = QPushButton("Denial", self)
		self.denial.move(150,70)
		self.denial.setStyleSheet("color: white")
		self.denial.clicked.connect(self.Denial)

		self.anger = QPushButton("Anger", self)
		self.anger.move(250,70)
		self.anger.setStyleSheet("color: white")
		self.anger.clicked.connect(self.Anger)

		self.bargaining = QPushButton("Bargaining", self)
		self.bargaining.move(350,70)
		self.bargaining.setStyleSheet("color: white")
		self.bargaining.clicked.connect(self.Bargaining)

		self.depression = QPushButton("Depression", self)
		self.depression.move(450,70)
		self.depression.setStyleSheet("color: white")
		self.depression.clicked.connect(self.Depression)

		self.acceptance = QPushButton("Acceptance", self)
		self.acceptance.move(550,70)
		self.acceptance.setStyleSheet("color: white")
		self.acceptance.clicked.connect(self.Acceptance)

	def Denial(self): 
		webbrowser.open("https://xkcd.com/353/")

	def Anger(self): 
		webbrowser.open("https://xkcd.com/1739/")

	def Bargaining(self): 
		webbrowser.open("https://xkcd.com/323/")

	def Depression(self): 
		webbrowser.open("https://xkcd.com/1421/")

	def Acceptance(self): 
		webbrowser.open("https://xkcd.com/844/")

		
