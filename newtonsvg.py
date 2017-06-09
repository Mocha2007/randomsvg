from cmath import phase,tan,cos
from math import floor
name="a=1, f(x)=x^3-1"
side=800
coords=2
step=1
maxcount=20
pi=3.141592653589793
#end main definitions
def root(z):
	oldz=z+1
	a=1
	count=0
	while abs(z-oldz)>.01 and count<maxcount:
		oldz=z
		try:
			z=z-a*(z**3-1)/(3*z**2)#THIS IS WHERE TO PUT THE CODE FOR NEWTON
		except:
			print("Warn",z)
			break
		count+=1
	return z
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
	please='<?xml version="1.0" standalone="no"?>\n<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>Newton Fractal</desc>'
	#how many items do i draw?
	for column in range(floor(side/step)):
		print(100*column/floor(side/step),"%")
		for row in range(floor(side/step)):
			please+='\n<rect x="'+str(column*step)+'" y="'+str(row*step)+'" width="'+str(step)+'" height="'+str(step)+'" fill="'+color(xy2c(column*step,row*step))+'"/>'
	#end
	please+='\n<text x="48" y="'+str(side-48)+'" font-family="Verdana" font-size="48">\n\t'+name+'\n</text>\n</svg>'
	open("art/newton-"+name+".svg","w+").write(please)
print("Picasso is painting image 0")
paint()