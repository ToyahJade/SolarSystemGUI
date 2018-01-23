import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scipy.constants import au
from turtle import *
import solarSystem

#This creates sliders for the solar system:

class earthLike(QWidget):
	def __init__(self, parent=None):
		super(earthLike,self).__init__(parent)
		self.resize(500,500)
		self.setStyleSheet("background-color: black")

		layout = QVBoxLayout()

		#For the mass of the sun.
		self.lblSunMass = QLabel()
		layout.addWidget(self.lblSunMass)
		self.sunmass = QSlider(Qt.Horizontal)
		self.sunmass.setMinimum(100000)
		self.sunmass.setMaximum(500000)
		self.sunmass.setTickInterval(1)
		#The display needs to be updated when the slider is moved:
		self.sunmass.valueChanged.connect(self.Update)
		layout.addWidget(self.sunmass)

		#Mercury mass
		self.lblMercMass = QLabel()
		layout.addWidget(self.lblMercMass)
		self.mercmass = QSlider(Qt.Horizontal)
		self.mercmass.setMinimum(10)
		self.mercmass.setMaximum(50)
		self.mercmass.setTickInterval(0.0001)
		self.mercmass.valueChanged.connect(self.Update)
		layout.addWidget(self.mercmass)

		#Mercury position
		self.lblMercPos = QLabel()
		layout.addWidget(self.lblMercPos)
		self.mercpos = QSlider(Qt.Horizontal)
		self.mercpos.setMinimum(10)
		self.mercpos.setMaximum(50)
		self.mercpos.setTickInterval(1)
		self.mercpos.valueChanged.connect(self.Update)
		layout.addWidget(self.mercpos)
		
		#Mercury velocity
		self.lblMercVel = QLabel()
		layout.addWidget(self.lblMercVel)
		self.mercvel = QSlider(Qt.Horizontal)
		self.mercvel.setMinimum(300)
		self.mercvel.setMaximum(600)
		self.mercvel.setTickInterval(1)
		self.mercvel.valueChanged.connect(self.Update)
		layout.addWidget(self.mercvel)

		#Venus
		self.lblVenMass = QLabel()
		layout.addWidget(self.lblVenMass)
		self.venmass = QSlider(Qt.Horizontal)
		self.venmass.setMinimum(200)
		self.venmass.setMaximum(600)
		self.venmass.setTickInterval(1)
		self.venmass.valueChanged.connect(self.Update)
		layout.addWidget(self.venmass)

		self.lblVenPos = QLabel()
		layout.addWidget(self.lblVenPos)
		self.venpos = QSlider(Qt.Horizontal)
		self.venpos.setMinimum(50)
		self.venpos.setMaximum(100)
		self.venpos.setTickInterval(1)
		self.venpos.valueChanged.connect(self.Update)
		layout.addWidget(self.venpos)
		
		self.lblVenVel = QLabel()
		layout.addWidget(self.lblVenVel)
		self.venvel = QSlider(Qt.Horizontal)
		self.venvel.setMinimum(2000)
		self.venvel.setMaximum(5000)
		self.venvel.setTickInterval(1)
		self.venvel.valueChanged.connect(self.Update)
		layout.addWidget(self.venvel)

		#Earth
		self.lblEarthMass = QLabel()
		layout.addWidget(self.lblEarthMass)
		self.earthmass = QSlider(Qt.Horizontal)
		self.earthmass.setMinimum(400)
		self.earthmass.setMaximum(800)
		self.earthmass.setTickInterval(1)
		self.earthmass.valueChanged.connect(self.Update)
		layout.addWidget(self.earthmass)

		self.lblEarthPos = QLabel()
		layout.addWidget(self.lblEarthPos)
		self.earthpos = QSlider(Qt.Horizontal)
		self.earthpos.setMinimum(75)
		self.earthpos.setMaximum(125)
		self.earthpos.setTickInterval(1)
		self.earthpos.valueChanged.connect(self.Update)
		layout.addWidget(self.earthpos)
		
		self.lblEarthVel = QLabel()
		layout.addWidget(self.lblEarthVel)
		self.earthvel = QSlider(Qt.Horizontal)
		self.earthvel.setMinimum(10000)
		self.earthvel.setMaximum(50000)
		self.earthvel.setTickInterval(1)
		self.earthvel.valueChanged.connect(self.Update)
		layout.addWidget(self.earthvel)

		#Mars
		self.lblMarsMass = QLabel()
		layout.addWidget(self.lblMarsMass)
		self.marsmass = QSlider(Qt.Horizontal)
		self.marsmass.setMinimum(400)
		self.marsmass.setMaximum(800)
		self.marsmass.setTickInterval(1)
		self.marsmass.valueChanged.connect(self.Update)
		layout.addWidget(self.marsmass)

		self.lblMarsPos = QLabel()
		layout.addWidget(self.lblMarsPos)
		self.marspos = QSlider(Qt.Horizontal)
		self.marspos.setMinimum(125)
		self.marspos.setMaximum(175)
		self.marspos.setTickInterval(1)
		self.marspos.valueChanged.connect(self.Update)
		layout.addWidget(self.marspos)
		
		self.lblMarsVel = QLabel()
		layout.addWidget(self.lblMarsVel)
		self.marsvel = QSlider(Qt.Horizontal)
		self.marsvel.setMinimum(100)
		self.marsvel.setMaximum(500)
		self.marsvel.setTickInterval(1)
		self.marsvel.valueChanged.connect(self.Update)
		layout.addWidget(self.marsvel)

		#Plot it!
		self.plot = QPushButton("Show Solar System",self)
		self.plot.setToolTip("Plot using your values! Please exit the plot before trying a new one")
		self.plot.setStyleSheet("color: white")
		self.plot.clicked.connect(self.Plot)
		layout.addWidget(self.plot)

		#I would like to add a button that resetsult values
		self.reset = QPushButton("Reset",self)
		self.reset.setToolTip("Resets the sliders to their default values")
		self.reset.setStyleSheet("color: white")
		self.reset.clicked.connect(self.Reset)
		layout.addWidget(self.reset)
		
		self.setLayout(layout)
		self.Reset()

	def Reset(self):
		#Set all the default values:
		#Sliders only use integer numbers, so divisions and 
		#multiplications are done later to account for this:
		self.marsvel.setSliderPosition(241)
		self.marspos.setSliderPosition(152)
		self.marsmass.setSliderPosition(642)
		self.earthvel.setSliderPosition(29783)
		self.earthpos.setSliderPosition(100)
		self.earthmass.setSliderPosition(597)
		self.venvel.setSliderPosition(3502)
		self.venpos.setSliderPosition(73)
		self.venmass.setSliderPosition(487)
		self.mercvel.setSliderPosition(474)
		self.mercpos.setSliderPosition(39)
		self.mercmass.setSliderPosition(33)
		self.sunmass.setSliderPosition(198892)

	def Update(self):
		#Add labels which update with new values. Make these
		#white so they can be seen.
		self.lblSunMass.setStyleSheet("color: white")
		self.lblSunMass.setText("Mass of the Sun: " + str(self.sunmass.value()/10000.0) + "e30kg")
		self.lblMercMass.setStyleSheet("color: white")
		self.lblMercMass.setText("Mass of Mercury: " + str(self.mercmass.value()/10.0) + "e23kg")
		self.lblMercPos.setStyleSheet("color: white")
		self.lblMercPos.setText("Distance between Mercury and the Sun: " + str(self.mercpos.value()/100.0) + "AU")
		self.lblMercVel.setStyleSheet("color: white")
		self.lblMercVel.setText("Initial velocity of Mercury: " + str(self.mercvel.value()*100) + "m/s")
		self.lblVenMass.setStyleSheet("color: white")
		self.lblVenMass.setText("Mass of Venus: " + str(self.venmass.value()/100.0) + "e24kg")
		self.lblVenPos.setStyleSheet("color: white")
		self.lblVenPos.setText("Distance between Venus and the Sun: " + str(self.venpos.value()/100.0) + "AU")
		self.lblVenVel.setStyleSheet("color: white")
		self.lblVenVel.setText("Initial velocity of Venus: " + str(self.venvel.value()*10) + "m/s")
		self.lblEarthMass.setStyleSheet("color: white")
		self.lblEarthMass.setText("Mass of Earth: " + str(self.earthmass.value()/100.0) + "e24kg")
		self.lblEarthPos.setStyleSheet("color: white")
		self.lblEarthPos.setText("Distance between Earth and the Sun: " + str(self.earthpos.value()/100.0) + "AU")
		self.lblEarthVel.setStyleSheet("color: white")
		self.lblEarthVel.setText("Initial velocity of Earth: " + str(self.earthvel.value()) + "m/s")
		self.lblMarsMass.setStyleSheet("color: white")
		self.lblMarsMass.setText("Mass of Mars: " + str(self.marsmass.value()/100.0) + "e23kg")
		self.lblMarsPos.setStyleSheet("color: white")
		self.lblMarsPos.setText("Distance between Mars and the Sun: "+str(self.marspos.value()/100.0) + "AU")
		self.lblMarsVel.setStyleSheet("color: white")
		self.lblMarsVel.setText("Initial velocity of Mars: "+str(self.marsvel.value()*100) + "m/s")
		

	def Plot(self):
		#Use these values for the plot, but make them the
		#coorect ones (mentioned earlier)
		solarSystem.main(self.sunmass.value()*10**25,
			self.mercmass.value()*10**22,
			self.mercpos.value()*au/100.0,
			self.mercvel.value()*100,
			self.venmass.value()*10**22,
			self.venpos.value()*au/100.0,
			self.venvel.value()*10,
			self.earthmass.value()*10**22,
			self.earthpos.value()*au/100.0,
			self.earthvel.value(),
			self.marsmass.value()*10**21,
			self.marspos.value()*au/100.0,
			self.marsvel.value()*100)