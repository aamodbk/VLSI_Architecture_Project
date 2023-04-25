import random
import numpy as np
import sys
import subprocess
 
sys.stdout = open('logfile_cell2_delay.txt','a')
#file = open('initial_w1.txt','a')

#f = open("initial_11.txt", "r")
#print(f.read(50))


W = 0.5
c1 = 0.8
c2 = 0.7 

#n_iterations = int(input("Inform the number of iterations: "))
#target_error = float(input("Inform the target error: "))
#n_particles = int(input("Inform the number of particles: "))

n_iterations =200 
target_error = .0000000000000000000000000000000000000000000000000000000000000000000000000000000001
n_particles = 100

class Particle():
	def __init__(self): # constructors
		
		
		#aa= random.randint(120,480)


		self.position = np.array([random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000)])
		#print("The initialised random position is ", self.position)
		#for 5 variables
		#self.position = np.array([130+(random.random()*10),130+(random.random()*10),130+(random.random()*10),130+(random.random()*10),130+(random.random()*10)])
		# particle.position is an array that holds the values of all the five variables
		self.pbest_position = self.position
		self.pbest_value = float('inf')
		self.velocity = np.array([0,0,0,0,0,0,0,0]) # matrix with one row ie initial velocity

	def __str__(self):
		print(" Co-ordinates are :", self.position )
	
	def move(self):
		self.position = self.position + self.velocity       # is this performing vector addition ?
		for ii in range (38):
			if self.position[ii]<120:
				self.position[ii] = 120
		for ig in range (38):
			if self.position[ig]>2000:
				self.position[ig] = 2000


class Space():

	def __init__(self, target, target_error, n_particles):
		self.target = target # final min pdp to be achieved
		self.target_error = target_error
		self.n_particles = n_particles # number of particles
		self.particles = [] # a list that contains nothing
		# self.particles is a list of all 500 particles
		self.gbest_value = float('inf')
		#bb= random.randint(120,480)
		self.gbest_position = np.array([random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000),random.randint(150,2000)])
		#print("The initialized random value is" , )

#        self.gbest_position = np.array([random.random()*50, random.random()*50, random.random()*50, random.random()*50, random.random()*50])


	def print_particles(self):
		for particle in self.particles:
			# this loop goes through each element of the list
			#print(self.particles)
			particle.__str__()


	def fitness(self, particle):
		width_file = open("width_delay_file_cell2.dat","w")
		width_file.write(str(particle.position[0])+"e-09"+" "+str(particle.position[1])+"e-09"+" "+str(particle.position[2])+"e-09"+" "+str(particle.position[3])+"e-09"+" "+str(particle.position[4])+"e-09"+" "+str(particle.position[5])+"e-09"+" "+str(particle.position[6])+"e-09"+" "+str(particle.position[7])+"e-09"+" ")
		#width_file.write(particle.position[1]+"n"+" ")
		width_file.close()
		print("\n")
		print("Fittness function called for" ,str(particle.position[0])+"e-09"+" "+str(particle.position[1])+"e-09"+" "+str(particle.position[2])+"e-09"+" "+str(particle.position[3])+"e-09"+" "+str(particle.position[4])+"e-09"+" "+str(particle.position[5])+"e-09"+" "+str(particle.position[6])+"e-09"+" "+str(particle.position[7])+"e-09"+" ")
		print("   ")
		print("yes1")
		subprocess.call("./simulate.sh", shell=True)
		print("yes2")
		delay_file = open("delay_file_cell2.dat","r") 
		string = delay_file.readline() 
		try:
			delay_read = float(string)
		except:
			string1 = '100e-06' 
			delay_read = float(string1)
			pass
		
		print("Its String value is" , string)
		
		
		delay_file.close() 

		# call the ocean script and return the value
		# call the bash script once , take the value into this python file and return from this function
		return delay_read
			
	def set_pbest(self):
		for particle in self.particles:
			fitness_cadidate = self.fitness(particle)
			if(particle.pbest_value > fitness_cadidate):
				particle.pbest_value = fitness_cadidate
				particle.pbest_position = particle.position 
				print (" particle personal best position :", particle.pbest_position , "particle personal best value" , particle.pbest_value )    
			if(self.gbest_value > fitness_cadidate):
				self.gbest_value = fitness_cadidate
				self.gbest_position = particle.position
				print(" global best position :", particle.pbest_position , "global best value" , particle.pbest_value )

	def move_particles(self):
		for particle in self.particles:
			global W
			# is this performing vector addition ?
			new_velocity = (W*particle.velocity) + (c1*random.random()) * (particle.pbest_position - particle.position) + (random.random()*c2) * (self.gbest_position - particle.position)
			particle.velocity = new_velocity
			particle.move()




			#print("The position of ")
			# index through all the elements of the list


			

space_object = Space(1, target_error, n_particles) # object instantiation
particles_vector = [Particle() for _ in range(space_object.n_particles)] 
# creates a list of 500 objects of class particle

# object instantiation
# _ implies ignore
# 500 objects of the class particles are created and stored in a list
space_object.particles = particles_vector
#space_object.print_particles()
# prints only the initial values

iteration = 0
while(iteration < n_iterations):
	
	print("Iteration number :", iteration)
	space_object.print_particles()
	print("\n\n\n\n")
	print("yes")

	space_object.set_pbest()    
	#space_object.set_gbest()

	# this is only to decide when to stop , it is optional
	if(abs(space_object.gbest_value - space_object.target) <= space_object.target_error):
		break
	
	# prints the co-ordinates of particle 1 in each iteration.
	#print("Co-ordinates @ iteration", iteration , "is" , particles_vector[1].position)
	

	space_object.move_particles()
	iteration += 1
	
	print("The best value is: ", space_object.gbest_position, " in n_iterations: ", iteration)
print("\n\n\nDONE")
