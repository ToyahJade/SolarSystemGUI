import sys
from PyQt4.QtGui import * 
import webbrowser
import earthSlide
import planets
import scale
import stages
import credits

#This is the codde which opens the main menu.

class Window(QWidget):
	def __init__(self, parent=None):
		super(Window,self).__init__(parent)
		#To determine the size of the window:
		#(The size is so that the image used takes up the whole window)
		self.resize(1000, 693)
		#Setting the background color means if the window is maximized
		#it will have a black background. It also sets the buttons to 
		#be black.
		self.setStyleSheet("background-color: black")

		#I think it makes the program pretty to use pictures, so I found
		#a nice one for the menu
		image = QPixmap("background.gif")
		im = QLabel(self)
		#This part actually puts the image in the window
		im.setPixmap(image)
		#Placing it at (0,0) means it will take up the whole window
		im.move(0,0)

		#The first button here is for the LaTex document:
		self.doc = QPushButton("LaTeX Documentation", self)
		#This is where I have decided to place it:
		self.doc.move(700,140)
		#It's helpful to have a mouse-over:
		self.doc.setToolTip("Opens a pdf of the documentation describing this program")
		#The font color of the button needs to be white so that it stands
		#out on the black background
		self.doc.setStyleSheet("color: white")
		#And then make it so clicking the button takes us to the document...
		self.doc.clicked.connect(self.Doc)

		#Same again for the simulation
		self.earth = QPushButton("Earth-Like Planets Simulation",self)
		self.earth.move(200,140)
		self.earth.setToolTip("Opens a simulation for a solar system consisting of Earth-like planets and a Sun only")
		self.earth.setStyleSheet("color: white")
		self.earth.clicked.connect(self.slide)
		self.slideWindow = None

		#For the menu for descriptions of the planets:
		self.planets = QPushButton("Descriptions of the Planets", self)
		self.planets.move(200,180)
		self.planets.setToolTip("Opens a menu displaying the name of each planet in the solar system. Clicking on a planet will open a window with information on that planet.")
		self.planets.setStyleSheet("color: white")		
		self.planets.clicked.connect(self.info)

		#Opens a window with images of the planets to scale
		self.scale = QPushButton("The Planets to Scale", self)
		self.scale.move(200, 220)
		self.scale.setToolTip("Opens a window displaying images of the planets to scale with respect to one another")
		self.scale.setStyleSheet("color: white")
		self.scale.clicked.connect(self.toScale)

		#A link to something I had a little fun with...
		self.xkcd = QPushButton("The Stages of Making This Project", self)
		self.xkcd.move(700, 180)
		self.xkcd.setToolTip("This one is a surprise!")
		self.xkcd.setStyleSheet("color: white")
		self.xkcd.clicked.connect(self.web)


		#And some credits to my sources of information and images:
		self.cred = QPushButton("Credits", self)
		self.cred.clicked.connect(self.Credits)
		self.cred.setStyleSheet("color: white")
		self.cred.move(700, 220)

	def Doc(self):
		#This will open the pdf of my LaTeX report
		webbrowser.open("documentation.pdf")

	def slide(self): 
		#This opens a new window, which is created using code 
		#from earthSlide.py
		self.slideWindow=earthSlide.earthLike()
		self.slideWindow.show()

	def info(self):
		#Opens a window using code from planets.py
		self.slideWindow=planets.Facts()
		self.slideWindow.show()

	def toScale(self):
		#Opens a window using code from scale.py
		self.slideWindow=scale.Scale()
		self.slideWindow.show()

	def web(self):
		#Opens a window using code from stages.py
		self.slideWindow=stages.Stages()
		self.slideWindow.show()

	def Credits(self):
		#Opens a window using code from credits.py
		self.slideWindow = credits.Credits()
		self.slideWindow.show()
		
#Finally, the menu window can be opened:
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()