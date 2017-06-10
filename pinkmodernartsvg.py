import random
side=800
#definitions
def rndang():
	return str(random.randint(0,359))
def rndpos():
	return str(random.randint(0,side))
def rndcol():
	col1=random.randint(0,255)
	col2=random.randint(128,255)
	return 'rgb(255,'+str(min(col1,col2))+','+str(max(col1,col2))+')'
#end main definitions
def paint():
	sown=random.randint(0,999999)
	random.seed(sown)
	please='<?xml version="1.0" standalone="no"?>\n<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>'+str(sown)+"</desc>"
	#how many items do i draw?
	max=random.randint(1,99)
	for i in range(max):
		#transformations
		transform=0
		if random.random()>.2:
			transform+=1
			please+='\n<g transform="rotate('+rndang()+')">'
		if random.random()>.2:
			transform+=1
			please+='\n<g transform="skewX('+rndang()+')">'
		if random.random()>.2:
			transform+=1
			please+='\n<g transform="skewY('+rndang()+')">'
		#shapes
		please+='\n<rect x="'+rndpos()+'" y="'+rndpos()+'" width="'+rndpos()+'" height="'+rndpos()+'" fill="'+rndcol()+'"/>'
		while transform!=0:
			please+='\n</g>'
			transform-=1
	#end
	open("art/"+str(sown)+".svg","w+").write(please+'\n</svg>')
for i in range(10):
	print("Picasso is painting image "+str(i))
	paint()