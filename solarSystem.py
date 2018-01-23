import numpy as np
from scipy.constants import G, au
from turtle import *


#Importing G from scipy means I have G, I also have one AU as
#au from scipy

#We also need to define how many pixels each distace will be.
SCALE = 250/au

screen=None


class Planet(Turtle):
	"""This represents a body, such as a planet,
	which acts according to gravity.

	Attributes:
	mass: the mass of the body in kg
	vx, vy: the velocity of the body in the x and y 
			direction respectively. Measured in m/s
	px, py: the position of the body in the x and y
			direction respectively. Measured in m"""
	

	#Constuctor defaults to massless body if nothing is defined:
	def __init__(self,name = "Planet", mass = None, px = 0.0, vy = 0.0, color="#000000",image=""):
		super(Planet,self).__init__()
		self.name = name
		self.mass = mass
		self.vx = 0.0
		self.px = px
		self.vy = vy
		self.py = 0.0
		self.pencolor(color)
		self.shape(image)

	#We must then determine the gravitational force between
	#bodies
	def force(self, other):
		"""This retuens the force exerted on one body by
		the other."""

		#This will not work if both bodies are the same, 
		#so an error will be returned:
		if self is other:
			raise ValueError("Attraction of object %r to itself requested"
				% self.name)

		#Begin by calculating the distance between the bodies
		sx = self.px
		sy = self.py
		ox = other.px
		oy = other.py
		dx = (ox - sx)
		dy = (oy - sy)
		dist = np.sqrt(dx**2 + dy**2)

		#GET RID OF THIS LATER
		# Report an error if the distance is zero; otherwise we'll
		# get a ZeroDivisionError exception further down.
		if dist == 0:
			raise ValueError("Collision between objects %r and %r"
				% (self.name, other.name))

		#The gravitaional force can then be calculated
		f = G * self.mass * other.mass / dist**2
		#Since forve is directional, this needs to be
		#accounted for in the code:
		#arctan2 allows for arctan with two arguments
		angle = np.arctan2(dy, dx)
		fx = np.cos(angle) * f
		fy = np.sin(angle) * f
		return fx, fy

def update_info(step, planets):
	"""(int, [Planet])
	
	Displays information about the status of the simulation.
	"""
	for planet in planets:
		s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
			planet.name, planet.px/au, planet.py/au, planet.vx, planet.vy)
 


#The positions of the planets will need to be updated
def update(planets):
	"""This causes the simulation to be a loop, so will
	update the positions of the planets"""

	#The time step can be one day, so the Earth will have
	#~365 updates to do one full orbit of the sun.
	dt = 86400

	#Create the path the planet is taking:
	for planet in planets:
		planet.penup()

		step = 1 
		while True:
			update_info(step, planets)
			step += 1

			grav = {}
			for planet in planets:
				#All of the forces acting on each body need
				#to be computed
				tot_fx = tot_fy = 0.0
				for other in planets: 
					#The planets are not vain like us mortals.
					#They are not attracted to themselves.
					if planet is other:
						continue
					fx, fy = planet.force(other)
					tot_fx += fx
					tot_fy += fy

				#Record the total force
				grav[planet] = (tot_fx, tot_fy)

			#The velocity of the planet depends on the force:
			for planet in planets:
				fx, fy = grav[planet]
				planet.vx += fx / planet.mass * dt
				planet.vy += fy / planet.mass * dt

				#The positions of the planets then need to 
				#be updated based on this:
				planet.px += planet.vx * dt
				planet.py += planet.vy * dt
				planet.goto(planet.px * SCALE, planet.py * SCALE)
				planet.dot(3)

#Name our variables to be determined by sliders: 
def main(sunmass, mercmass, mercpos, mercvel, venmass, venpos, venvel, earthmass, earthpos, earthvel, marsmass, marspos, marsvel):
	screen = Screen()

	#Add shapes for each planet:
	bgcolor("black")
	screen.addshape("sun.gif")
	screen.addshape("mercury1.gif")
	screen.addshape("venus1.gif")
	screen.addshape("earth1.gif")
	screen.addshape("mars1.gif")

	sun = Planet("Sun",sunmass,0,0, "#FB7700", "sun.gif")

	mercury = Planet("Mercury", mercmass, mercpos, mercvel,"#686868","mercury1.gif")

	venus = Planet("Venus", venmass, venpos, venvel,"#DACCAF","venus1.gif")

	earth = Planet("Earth", earthmass, earthpos, earthvel, "#0C3857","earth1.gif")

	mars = Planet("Mars", marsmass, marspos, marsvel, "#94765E", "mars1.gif")

	update([sun, earth, venus, mercury, mars])
	screen = None

if __name__ == '__main__':
	main()
