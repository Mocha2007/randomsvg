import random
side=800
#definitions
def rndang():
	return str(random.randint(0,359))
def rndpos():
	return random.randint(0,side)
def rndimg():
	galaxy=['https://upload.wikimedia.org/wikipedia/commons/d/dc/Ngc.galaxy.arp.750pix.jpg','https://upload.wikimedia.org/wikipedia/commons/1/17/NGC_7217_Hubble.jpg','https://upload.wikimedia.org/wikipedia/commons/3/39/NGC_4314HST1998-21-b-full.jpg','https://upload.wikimedia.org/wikipedia/commons/2/21/NGC_1022_-HST09042_h3-R814G606B450.png','https://upload.wikimedia.org/wikipedia/commons/4/4b/NGC_1427_HST_10911_R814GB475.png','http://upload.wikimedia.org/wikipedia/commons/4/4a/2MASX_J00482185-2507365_by_HST.jpg','https://upload.wikimedia.org/wikipedia/commons/3/3c/N1309.jpg']
	return random.choice(galaxy)
#end main definitions
def paint():
	sown=random.randint(0,999999)
	random.seed(sown)
	please='<?xml version="1.0" standalone="no"?>\n<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n<desc>'+str(sown)+"</desc>"
	#space
	please+='\n<rect x="0" y="0" width="'+str(side)+'" height="'+str(side)+'" fill="#000"/>'
	for i in range(222):
		#shapes
		please+='\n<circle cx="'+str(rndpos())+'" cy="'+str(rndpos())+'" r="'+str(2*random.random())+'" fill="#fff"/>'
	#how many items do i draw?
	max=999
	for i in range(max):
		#transformations
		please+='\n<g transform="rotate('+rndang()+')">\n<g transform="skewX('+rndang()+')">\n<g transform="skewY('+rndang()+')">'
		#shapes
		w=str(4*rndpos()/(max-i))
		please+='\n<image x="'+str(rndpos())+'" y="'+str(rndpos())+'" width="'+w+'" height="'+w+'" xlink:href="'+rndimg()+'"></image>'
		for i in range(3):
			please+='\n</g>'
	#end
	open("art/"+str(sown)+".svg","w+").write(please+'\n</svg>')
for i in range(10):
	print("Picasso is painting image "+str(i))
	paint()