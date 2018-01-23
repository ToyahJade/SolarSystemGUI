import sys
from PyQt4.QtGui import * 
import webbrowser

class Neptune(QWidget):
	def __init__(self, parent=None):
		super(Neptune,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("neptune.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblNepTxt = QLabel(self)
		lblNepTxt.move(400, 30)
		lblNepTxt.setWordWrap(True)
		lblNepTxt.setStyleSheet("color: white")
		lblNepTxt.setText("Neptune is the eighth planet from the Sun making it the most distant in the solar system. This gas giant planet may have formed much closer to the Sun in early solar system history before migrating to its present position.")

		self.nepInf = QPushButton("Weblink to More Information", self)
		self.nepInf.move(500,300)
		self.nepInf.setStyleSheet("color: white")
		self.nepInf.clicked.connect(self.NepInf)

	def NepInf(self): 
		webbrowser.open("http://space-facts.com/neptune/")