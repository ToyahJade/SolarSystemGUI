import sys
from PyQt4.QtGui import * 
import webbrowser

#uses same code as main menu

class Earth(QWidget):
	def __init__(self, parent=None):
		super(Earth,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("earth.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblEarthTxt = QLabel(self)
		lblEarthTxt.move(400, 30)
		lblEarthTxt.setWordWrap(True)
		lblEarthTxt.setStyleSheet("color: white")
		lblEarthTxt.setText("Earth is the third planet from the Sun and is the largest of the terrestrial planets. The Earth is the only planet in our solar system not to be named after a Greek or Roman deity. The Earth was formed approximately 4.54 billion years ago and is the only known planet to support life.")

		self.earthInf = QPushButton("Weblink to More Information", self)
		self.earthInf.move(500,300)
		self.earthInf.setStyleSheet("color: white")
		self.earthInf.clicked.connect(self.EarthInf)

	def EarthInf(self): 
		webbrowser.open("http://space-facts.com/earth/")