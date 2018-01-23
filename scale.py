import sys
from PyQt4.QtGui import * 

#Uses the same code as the main menu

class Scale(QWidget):
	def __init__(self, parent=None):
		super(Scale,self).__init__(parent)
		self.resize(815,270)
		self.setStyleSheet("background-color: black")

		#This adds the image of each planet
		image = QPixmap("mercury2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,136)

		lblMercury = QLabel(self)
		lblMercury.move(10, 242)
		lblMercury.setWordWrap(True)
		lblMercury.setStyleSheet("color: #686868")
		lblMercury.setText("Mercury")

		image = QPixmap("venus2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(90,132)

		lblVenus = QLabel(self)
		lblVenus.move(80, 242)
		lblVenus.setWordWrap(True)
		lblVenus.setStyleSheet("color: #DACCAF")
		lblVenus.setText("Venus")

		image = QPixmap("earth2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(150,132)

		lblEarth = QLabel(self)
		lblEarth.move(140, 242)
		lblEarth.setWordWrap(True)
		lblEarth.setStyleSheet("color: #0C3857")
		lblEarth.setText("Earth")

		image = QPixmap("mars2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(215,135)

		lblMars = QLabel(self)
		lblMars.move(200, 242)
		lblMars.setWordWrap(True)
		lblMars.setStyleSheet("color: #94765E")
		lblMars.setText("Mars")

		image = QPixmap("jupiter2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(250, 72)

		lblJupiter = QLabel(self)
		lblJupiter.move(295, 242)
		lblJupiter.setWordWrap(True)
		lblJupiter.setStyleSheet("color: #814F2A")
		lblJupiter.setText("Jupiter")

		image = QPixmap("saturn2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(390, 12)

		lblSaturn = QLabel(self)
		lblSaturn.move(490, 242)
		lblSaturn.setWordWrap(True)
		lblSaturn.setStyleSheet("color: #E1C27B")
		lblSaturn.setText("Saturn")
		
		image = QPixmap("uranus2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(665, 114)

		lblUranus = QLabel(self)
		lblUranus.move(670, 242)
		lblUranus.setWordWrap(True)
		lblUranus.setStyleSheet("color: #CEF7F8")
		lblUranus.setText("Uranus")

		image = QPixmap("neptune2.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(750, 114)

		lblNeptune = QLabel(self)
		lblNeptune.move(745, 242)
		lblNeptune.setWordWrap(True)
		lblNeptune.setStyleSheet("color: #4670FF")
		lblNeptune.setText("Neptune")