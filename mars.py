import sys
from PyQt4.QtGui import * 
import webbrowser

class Mars(QWidget):
	def __init__(self, parent=None):
		super(Mars,self).__init__(parent)
		self.resize(900,350)
		self.setStyleSheet("background-color: black")
		
		image = QPixmap("mars.gif")
		im = QLabel(self)
		im.setPixmap(image)
		im.move(30,30)

		lblMarTxt = QLabel(self)
		lblMarTxt.move(400, 30)
		lblMarTxt.setWordWrap(True)
		lblMarTxt.setStyleSheet("color: white")
		lblMarTxt.setText("Mars is the fourth planet from the Sun and is the second smallest planet in the solar system. Named after the Roman god of war, Mars is also often described as the Red Planet due to its reddish appearance. Mars is a terrestrial planet with a thin atmosphere composed primarily of carbon dioxide.")

		self.marInf = QPushButton("Weblink to More Information", self)
		self.marInf.move(500,300)
		self.marInf.setStyleSheet("color: white")
		self.marInf.clicked.connect(self.MarInf)

	def MarInf(self): 
		webbrowser.open("http://space-facts.com/mars/")