import random
side=800
#definitions
def rndang():
	return str(random.randint(0,359))
def rndpos():
	return random.randint(0,side)
def rndcol():
	col1=random.randint(0,255)
	col2=random.randint(128,255)
	return 'rgb(255,'+str(min(col1,col2))+','+str(max(col1,col2))+')'
#end main definitions
def paint():
	sown=random.randint(0,999999)
	random.seed(sown)
	please='<?xml version="1.0" standalone="no"?>\n<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>'+str(sown)+"</desc>"
	#space
	please+='\n<rect x="0" y="0" width="'+str(side)+'" height="'+str(side)+'" fill="black"/>'
	for i in range(99):
		#shapes
		please+='\n<circle cx="'+str(rndpos())+'" cy="'+str(rndpos())+'" r="'+str(random.randint(1,2))+'" fill="'+rndcol()+'"/>'
	#how many items do i draw?
	max=999#random.randint(99,999)
	for i in range(max):
		#transformations
		please+='\n<g transform="rotate('+rndang()+')">\n<g transform="skewX('+rndang()+')">\n<g transform="skewY('+rndang()+')">'
		#shapes
		w=str(4*rndpos()/(max-i))
		please+='\n<rect x="'+str(rndpos())+'" y="'+str(rndpos())+'" width="'+w+'" height="'+w+'" fill="'+rndcol()+'"/>'
		for i in range(3):
			please+='\n</g>'
	#end
	open("art/"+str(sown)+".svg","w+").write(please+'\n</svg>')
for i in range(10):
	print("Picasso is painting image "+str(i))
	paint()