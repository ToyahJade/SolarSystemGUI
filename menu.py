import sys
from PyQt4.QtGui import * 
import webbrowser
import earthSlide
import planets
import scale
import stages

class Window(QWidget):
	def __init__(self, parent=None):
		super(Window,self).__init__(parent)
		self.resize(500,500)
		self.earth = QPushButton("Earth-Like Planets Simulation",self)
		self.earth.move(10,10)
		self.earth.resize(self.earth.sizeHint())
		self.earth.setToolTip("Temp desc")
		self.earth.clicked.connect(self.slide)
		self.slideWindow = None

		self.planets = QPushButton("Descriptions of the Planets", self)
		self.planets.clicked.connect(self.info)
		self.planets.move(10,50)

		self.scale = QPushButton("The Planets to Scale", self)
		self.scale.clicked.connect(self.toScale)
		self.scale.move(10, 90)

		self.xkcd = QPushButton("The Stages of Making This Project", self)
		self.xkcd.clicked.connect(self.web)
		self.xkcd.move(10, 130)

	def slide(self): 
		self.slideWindow=earthSlide.earthLike()
		self.slideWindow.show()

	def info(self):
		self.slideWindow=planets.Facts()
		self.slideWindow.show()

	def toScale(self):
		self.slideWindow=scale.Scale()
		self.slideWindow.show()

	def web(self):
		self.slideWindow=stages.Stages()
		self.slideWindow.show()
		

app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()