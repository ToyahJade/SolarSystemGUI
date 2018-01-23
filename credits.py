import sys
from PyQt4.QtGui import * 

class Credits(QWidget):
	def __init__(self, parent=None):
		super(Credits,self).__init__(parent)
		self.resize(685, 384)
		self.setStyleSheet("background-color: black")

		image = QPixmap("pluto.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(0, 0)

		lblThanks = QLabel(self)
		lblThanks.move(50, 100)
		#lblThanks.setWordWrap(True)
		lblThanks.setStyleSheet("color: white")
		lblThanks.setText("With special thanks to:")

		lblNasa = QLabel(self)
		lblNasa.move(50, 150)
		#lblNasa.setWordWrap(True)
		lblNasa.setStyleSheet("color: white")
		lblNasa.setText("NASA, for images of the Earth from the moon, \nBuzz Aldrin and Pluto")

		lblSun = QLabel(self)
		lblSun.move(50, 200)
		#lblSun.setWordWrap(True)
		lblSun.setStyleSheet("color: white")
		lblSun.setText("http://www.space.com for an image of the Sun")

		lblFacts = QLabel(self)
		lblFacts.move(50, 250)
		#lblFacts.setWordWrap(True)
		lblFacts.setStyleSheet("color: white")
		lblFacts.setText("http://space-facts.com for images of the planets \nand planetarty facts")

		lblFacts = QLabel(self)
		lblFacts.move(50, 300)
		#lblFacts.setWordWrap(True)
		lblFacts.setStyleSheet("color: white")
		lblFacts.setText("Randall Munroe at http://xkcd.com/ for his awesome \nwebcomics")