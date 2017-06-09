from cmath import phase
from math import floor
name="a=1+i, f(x)=x^2-1"
side=800
coords=2
step=2
maxcount=20
pi=3.141592653589793
#end main definitions
def root(c):
	old=c
	diff=1
	new=c
	count=0
	while abs(diff)>.01 and count<maxcount:
		#THIS IS WHERE TO PUT THE CODE FOR NEWTON
		a=1+1j
		try:
			#new=old-(old**3-1)/(3*old**2)
			#new=old-(old**3-2*old+2)/(3*old**2-2)
			new=old-a*(old**2-1)/(2*old)
		except ZeroDivisionError:
			new=c
			break
		diff=new-old
		old=new
		count+=1
	return new
def color(c):
	theta=phase(root(c))
	if 0<=theta<=pi/3:#r->y
		r=255
		g=floor((765/pi)*theta)
		b=0
	elif pi/3<theta<=2*pi/3:#y->g
		r=floor((-765/pi)*theta+510)
		g=255
		b=0
	elif 2*pi/3<theta<=pi:#g->c
		r=0
		g=255
		b=floor((765/pi)*theta-510)
	elif theta>-pi/3:#m->r
		r=255
		g=0
		b=floor((-765/pi)*theta)
	elif theta>-2*pi/3:#b->m
		r=floor((765/pi)*theta+510)
		g=0
		b=255
	else:#c->b
		r=0
		g=floor((-765/pi)*theta-510)
		b=255
	return "rgb("+str(r)+","+str(g)+","+str(b)+")"
def xy2c(x,y):
	return x/200-2+(2-y/200)*1j
def paint():
	#opening
	open("art/newton.svg","w+").write('<?xml version="1.0" standalone="no"?>')
	open("art/newton.svg","a").write('<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>Newton Fractal</desc>')
	#how many items do i draw?
	please=""
	for column in range(floor(side/step)):
		print(100*column/floor(side/step),"%")
		for row in range(floor(side/step)):
			rgb=color(xy2c(column*step,row*step))
			please+='\n<rect x="'+str(column*step)+'" y="'+str(row*step)+'" width="'+str(step)+'" height="'+str(step)+'" fill="'+rgb+'"/>'
			#print(column,row,xy2c(column*step,row*step),root(xy2c(column*step,row*step)))
	open("art/newton.svg","a").write(please)
	#end
	open("art/newton.svg","a").write('\n<text x="48" y="'+str(side-48)+'" font-family="Verdana" font-size="48">\n\t'+name+'\n</text>')
	open("art/newton.svg","a").write('\n</svg>')
print("Picasso is painting image 0")
paint()