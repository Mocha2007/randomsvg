import random
side=800
#definitions
def rndpos():
	return str(random.randint(0,side))
def rndpts():
	x=side/2
	y=side/2
	chain=""
	for i in range(9999):
		if random.random()>.5:
			x+=random.choice([-1,1])
		else:
			y+=random.choice([-1,1])
		chain+=str(x)+","+str(y)+" "
	return chain
#end main definitions
def paint():
	sown=random.randint(0,999999)
	random.seed(sown)
	#opening
	open("art/"+str(sown)+".svg","w+").write('<?xml version="1.0" standalone="no"?>')
	open("art/"+str(sown)+".svg","a").write('<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>')
	open("art/"+str(sown)+".svg","a").write(str(sown)+"</desc>")
	#how many items do i draw?
	max=random.randint(1,99)
	open("art/"+str(sown)+".svg","a").write('\n<polyline stroke="black" stroke-width="2" points=\n"'+rndpts()+'"/>')
	#end
	open("art/"+str(sown)+".svg","a").write('\n</svg>')
for i in range(10):
	print("Picasso is painting image "+str(i))
	paint()