import math
def num():
	s=0
	c=0
	p=0
	cu=0
	scu=0
	d=0
	a=open("numeros.txt")
	n=a.readline()
	n=n.rstrip("\n")
	n=int(n)
	while(n!=''):
		n2=int(n)
		s=s+n2
		c=c+1
		cu=n2*n2
		scu=scu+cu
		d=math.sqrt(scu/c)
		n=a.readline()
	p=s/c
	print("La sumatoria de todos los numero es: ",s)
	print("Todos los numero leidos son: ",c)
	print("El primedio es: ",p)
	print("La desviacion estandar es: ",d)
num()