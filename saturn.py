import sys
from PyQt4.QtGui import * 
import webbrowser

class Saturn(QWidget):
	def __init__(self, parent=None):
		super(Saturn,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("saturn.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblSatTxt = QLabel(self)
		lblSatTxt.move(400, 30)
		lblSatTxt.setWordWrap(True)
		lblSatTxt.setStyleSheet("color: white")
		lblSatTxt.setText("Saturn is the sixth planet from the Sun and the most distant that can be seen with the naked eye. Saturn is the second largest planet and is best known for its fabulous ring system that was first observed in 1610 by the astronomer Galileo Galilei. Like Jupiter, Saturn is a gas giant and is composed of similar gasses including hydrogen, helium and methane.")

		self.satInf = QPushButton("Weblink to More Information", self)
		self.satInf.move(500,300)
		self.satInf.setStyleSheet("color: white")
		self.satInf.clicked.connect(self.SatInf)

	def SatInf(self): 
		webbrowser.open("http://space-facts.com/saturn/")