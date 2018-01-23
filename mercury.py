import sys
from PyQt4.QtGui import * 
import webbrowser

class Mercury(QWidget):
	def __init__(self, parent=None):
		super(Mercury,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("mercury.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblMercTxt = QLabel(self)
		lblMercTxt.move(400, 30)
		lblMercTxt.setWordWrap(True)
		lblMercTxt.setStyleSheet("color: white")
		lblMercTxt.setText("Mercury is the closest planet to the Sun and due to its proximity it is not easily seen except during twilight. For every two orbits of the Sun, Mercury completes three rotations about its axis and up until 1965 it was thought that the same side of Mercury constantly faced the Sun. Thirteen times a century Mercury can be observed from the Earth passing across the face of the Sun in an event called a transit.")

		self.mercInf = QPushButton("Weblink to More Information", self)
		self.mercInf.move(500,300)
		self.mercInf.setStyleSheet("color: white")
		self.mercInf.clicked.connect(self.MercInf)

	def MercInf(self): 
		webbrowser.open("http://space-facts.com/mercury/")