
def check_banana():
	c=0
	n=0
	archivo=open ("banana.rtf")
	lineas=archivo.readlines()
	for line in lineas:
		palabras=line.split(' ')
		for s in palabras:
			if s.lower()=='banana':
				n=n+1
		lineas=archivo.readlines()
	return n
d=check_banana()
print ("La palabra Banana se encontro ",d, " beses ")