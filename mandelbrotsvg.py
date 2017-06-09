from cmath import phase
from math import floor
name="mandelbrot"
side=800
coords=2
step=1
maxcount=100
pi=3.141592653589793
#end main definitions
def root(c):
	z=0
	count=0
	while abs(z)<=2 and count<maxcount:
		z=z**2+c
		count+=1
	if abs(z)<=2:return True
	return False
def color(c):
	if root(c)==True:return "#000"
	return "#fff"
def xy2c(x,y):
	return x/200-2+(2-y/200)*1j
def paint():
	#opening
	open("art/mandelbrot.svg","w+").write('<?xml version="1.0" standalone="no"?>')
	open("art/mandelbrot.svg","a").write('<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>'+name+'</desc>')
	#how many items do i draw?
	please=""
	for column in range(floor(side/step)):
		print(100*column/floor(side/step),"%")
		for row in range(floor(side/step)):
			rgb=color(xy2c(column*step,row*step))
			if rgb=="#000":
				please+='\n<rect x="'+str(column*step)+'" y="'+str(row*step)+'" width="'+str(step)+'" height="'+str(step)+'" fill="'+rgb+'"/>'
			#print(column,row,xy2c(column*step,row*step),root(xy2c(column*step,row*step)))
	open("art/mandelbrot.svg","a").write(please)
	#end
	open("art/mandelbrot.svg","a").write('\n<text x="48" y="'+str(side-48)+'" font-family="Verdana" font-size="48">\n\t'+name+'\n</text>')
	open("art/mandelbrot.svg","a").write('\n</svg>')
print("Picasso is painting image 0")
paint()