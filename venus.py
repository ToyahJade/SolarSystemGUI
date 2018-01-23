import sys
from PyQt4.QtGui import * 
import webbrowser

class Venus(QWidget):
	def __init__(self, parent=None):
		super(Venus,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("venus.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblVenTxt = QLabel(self)
		lblVenTxt.move(400, 30)
		lblVenTxt.setWordWrap(True)
		lblVenTxt.setStyleSheet("color: white")
		lblVenTxt.setText("Venus is the second planet from the Sun and is the second brightest object in the night sky after the Moon. Named after the Roman goddess of love and beauty, Venus is the second largest terrestrial planet and is sometimes referred to as the Earths sister planet due the their similar size and mass. The surface of the planet is obscured by an opaque layer of clouds made up of sulphuric acid.")

		self.venInf = QPushButton("Weblink to More Information", self)
		self.venInf.move(500,300)
		self.venInf.setStyleSheet("color: white")
		self.venInf.clicked.connect(self.VenInf)

	def VenInf(self): 
		webbrowser.open("http://space-facts.com/venus/")