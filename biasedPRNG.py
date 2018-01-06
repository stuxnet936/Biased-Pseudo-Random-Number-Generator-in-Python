import ctypes
import time

state = int(str(time.time()).split('.')[1]) #using time for seeding
nos = []

def rand():
	global state
	state = ctypes.c_uint64(state).value
	state = state * 6364136223846793005 + 1442695040888963407
	state = int(bin(state)[2:66],2)		#pull the most signigicant 64 bits
	x = state							#state is preserved 		
	rotationCount = x>>59				#take the first 5 bits from x for rotation
	x = rotateRight(bin(x)[7:39], rotationCount)
	return x

def rotateRight(b, n):
	'''
	rotate the bits of input by n
	rotateRight('11110000',2) = '00111100'
	'''
	l = len(b)
	finalBits = b[n:l] + b[0:n]
	return int(finalBits, 2)

def run():
	reask = True
	while reask:
		try:
			n = int(input("How many numbers to generate: "))
			reask = False
		except ValueError as e:
			continue

	while len(nos) < n:
		r = rand()/(2**32)
		if r < 0.73:						#to insert bias
			x = 1
			while (x <= 5):					
				x = rand()					#return integer is of 32 bits
				x = int(x/2**32 * 10)		#to normalize the value in bounds of 0-9
			nos.append(x+1)
		else:
			x = 6
			while (x > 5):
				x = rand()
				x = int(x/2**32 * 10)
			nos.append(x+1)
	generateOutput(n)


def generateOutput(n):
	c1=0			#count fornumbers greater than 5
	c2=0
	for i in range(0, len(nos)):
		if int(nos[i])>5:
			c1 = c1+1
		else:
			c2= c2+1
	s = 'Freqency of Numbers 6-10: ' + str(c1/n*100) + '\n'+ 'Freqency of Numbers 1-5: '+ str(c2/n*100)+ '\n'
	f = open('./report.txt', 'w')
	s = s + str(nos)
	f.write(s)

if __name__ == "__main__":
	run()