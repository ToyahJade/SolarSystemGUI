import sys
from PyQt4.QtGui import * 
import webbrowser
import mercury
import venus
import earth
import mars
import jupiter
import saturn
import uranus
import neptune

#Uses the same code as the main menu

class Facts(QWidget):
	def __init__(self, parent=None):
		super(Facts,self).__init__(parent)
		self.resize(575,431)
		self.setStyleSheet("background-color: black")

		image = QPixmap("sunBackground.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(0,0)

		self.mercury = QPushButton("Mercury", self)
		self.mercury.move(440,10)
		self.mercury.setStyleSheet("color: white")
		self.mercury.clicked.connect(self.Mercury)

		self.venus = QPushButton("Venus", self)
		self.venus.move(440,50)
		self.venus.setStyleSheet("color: white")
		self.venus.clicked.connect(self.Venus)

		self.earth = QPushButton("Earth", self)
		self.earth.move(440,90)
		self.earth.setStyleSheet("color: white")
		self.earth.clicked.connect(self.Earth)

		self.mars = QPushButton("Mars", self)
		self.mars.move(440,130)
		self.mars.setStyleSheet("color: white")
		self.mars.clicked.connect(self.Mars)

		self.jupiter = QPushButton("Jupiter", self)
		self.jupiter.move(440,170)
		self.jupiter.setStyleSheet("color: white")
		self.jupiter.clicked.connect(self.Jupiter)

		self.saturn = QPushButton("Saturn", self)
		self.saturn.move(440,210)
		self.saturn.setStyleSheet("color: white")
		self.saturn.clicked.connect(self.Saturn)

		self.uranus = QPushButton("Uranus", self)
		self.uranus.move(440,250)
		self.uranus.setStyleSheet("color: white")
		self.uranus.clicked.connect(self.Uranus)

		self.neptune = QPushButton("Neptune", self)
		self.neptune.move(440,290)
		self.neptune.setStyleSheet("color: white")
		self.neptune.clicked.connect(self.Neptune)

		self.pluto = QPushButton("Pluto", self)
		self.pluto.move(440,330)
		self.pluto.setStyleSheet("color: white")
		self.pluto.clicked.connect(self.Pluto)

	def Mercury(self): 
		self.slideWindow=mercury.Mercury()
		self.slideWindow.show()

	def Venus(self): 
		self.slideWindow=venus.Venus()
		self.slideWindow.show()

	def Earth(self): 
		self.slideWindow=earth.Earth()
		self.slideWindow.show()

	def Mars(self): 
		self.slideWindow=mars.Mars()
		self.slideWindow.show()

	def Jupiter(self): 
		self.slideWindow=jupiter.Jupiter()
		self.slideWindow.show()

	def Saturn(self): 
		self.slideWindow=saturn.Saturn()
		self.slideWindow.show()

	def Uranus(self): 
		self.slideWindow=uranus.Uranus()
		self.slideWindow.show()

	def Neptune(self): 
		self.slideWindow=neptune.Neptune()
		self.slideWindow.show()

	def Pluto(self): 
		webbrowser.open("https://xkcd.com/473/")


