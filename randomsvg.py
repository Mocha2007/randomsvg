import random
side=800
#definitions
def rndang():
	return str(random.randint(0,359))
def rndpos():
	return str(random.randint(0,side))
def rndcol():
	colors=["black","blue","brown","chartreuse","cyan","green","grey","navy","none","orange","pink","purple","red","tan","white","yellow"]
	return random.choice(colors)
def rndstr():
	char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"'"]+[' ']*9
	length=random.randint(1,99)
	string=''
	for i in range(length):
		string+=random.choice(char)
	return string
def rndpts():
	x=int(rndpos())
	y=int(rndpos())
	chain=""
	for i in range(random.randint(3,9999)):
		if random.random()>.5:
			x+=random.choice([-1,1])
		else:
			y+=random.choice([-1,1])
		chain+=str(x)+","+str(y)+" "
	return chain
options=["rect","circle","ellipse","line","text","polyline"]
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
		c=random.choice(options)
		if c=="circle":please+='\n<circle cx="'+rndpos()+'" cy="'+rndpos()+'" r="'+rndpos()+'" fill="'+rndcol()+'"/>'
		elif c=="ellipse":please+='\n<ellipse cx="'+rndpos()+'" cy="'+rndpos()+'" rx="'+rndpos()+'" ry="'+rndpos()+'" fill="'+rndcol()+'"/>'
		elif c=="line":please+='\n<line x1="'+rndpos()+'" y1="'+rndpos()+'" x2="'+rndpos()+'" y2="'+rndpos()+'" stroke="'+rndcol()+'" stroke-width="2"/>'
		elif c=="rect":please+='\n<rect x="'+rndpos()+'" y="'+rndpos()+'" width="'+rndpos()+'" height="'+rndpos()+'" fill="'+rndcol()+'"/>'
		elif c=="text":please+='\n<text x="'+rndpos()+'" y="'+rndpos()+'" font-family="Verdana" font-size="48" fill="'+rndcol()+'">\n\t'+rndstr()+'\n</text>'
		elif c=="polyline":please+='\n<polyline stroke="'+rndcol()+'" stroke-width="2" points=\n"'+rndpts()+'"/>'
		while transform!=0:
			please+='\n</g>'
			transform-=1
	#end
	open("art/"+str(sown)+".svg","w+").write(please+'\n</svg>')
for i in range(10):
	print("Picasso is painting image "+str(i))
	paint()