import sys
from PyQt4.QtGui import * 
import webbrowser

class Jupiter(QWidget):
	def __init__(self, parent=None):
		super(Jupiter,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("jupiter.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblJupTxt = QLabel(self)
		lblJupTxt.move(400, 30)
		lblJupTxt.setWordWrap(True)
		lblJupTxt.setStyleSheet("color: white")
		lblJupTxt.setText("The planet Jupiter is the fifth planet out from the Sun, and is two and a half times more massive than all the other planets in the solar system combined. It is made primarily of gases and is therefore known as a gas giant.")

		self.jupInf = QPushButton("Weblink to More Information", self)
		self.jupInf.move(500,300)
		self.jupInf.setStyleSheet("color: white")
		self.jupInf.clicked.connect(self.JupInf)

	def JupInf(self): 
		webbrowser.open("http://space-facts.com/jupiter/")