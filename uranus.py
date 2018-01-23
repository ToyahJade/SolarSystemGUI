import sys
from PyQt4.QtGui import * 
import webbrowser

class Uranus(QWidget):
	def __init__(self, parent=None):
		super(Uranus,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("uranus.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblUrTxt = QLabel(self)
		lblUrTxt.move(400, 30)
		lblUrTxt.setWordWrap(True)
		lblUrTxt.setStyleSheet("color: white")
		lblUrTxt.setText("Uranus is the seventh planet from the Sun. It is not visible to the naked eye, and became the first planet discovered with the use of a telescope. Uranus is tipped over on its side with an axial tilt of 98 degrees. It is often described as rolling around the Sun on its side.")

		self.urInf = QPushButton("Weblink to More Information", self)
		self.urInf.move(500,300)
		self.urInf.setStyleSheet("color: white")
		self.urInf.clicked.connect(self.UrInf)

	def UrInf(self): 
		webbrowser.open("http://space-facts.com/uranus/")