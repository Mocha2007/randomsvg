import random
sown=random.randint(0,999999)
random.seed(sown)
side=800
#opening
open("art/"+str(sown)+".svg","w+").write('<?xml version="1.0" standalone="no"?>')
open("art/"+str(sown)+".svg","a").write('<svg width="'+str(side)+'" height="'+str(side)+'" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>')
open("art/"+str(sown)+".svg","a").write(str(sown)+"</desc>")
#how many items do i draw?
max=random.randint(1,99)
#stuff
def rndang():
	return str(random.randint(0,359))
def rndpos():
	return str(random.randint(0,side))
def rndcol():
	colors=["black","blue","brown","green","grey","navy","none","orange","pink","purple","red","white","yellow"]
	return random.choice(colors)
def rndstr():
	char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"'"]+[' ']*9
	length=random.randint(1,99)
	string=''
	for i in range(length):
		string+=random.choice(char)
	return string
options=["rect","circle","ellipse","line","text"]
for i in range(max):
	#transformations
	transform=0
	if random.random()>.2:
		transform+=1
		open("art/"+str(sown)+".svg","a").write('\n<g transform="rotate('+rndang()+')">')
	if random.random()>.2:
		transform+=1
		open("art/"+str(sown)+".svg","a").write('\n<g transform="skewX('+rndang()+')">')
	if random.random()>.2:
		transform+=1
		open("art/"+str(sown)+".svg","a").write('\n<g transform="skewY('+rndang()+')">')
	#shapes
	c=random.choice(options)
	if c=="circle":
		open("art/"+str(sown)+".svg","a").write('\n<circle cx="'+rndpos()+'" cy="'+rndpos()+'" r="'+rndpos()+'" fill="'+rndcol()+'"/>')
	elif c=="ellipse":
		open("art/"+str(sown)+".svg","a").write('\n<ellipse cx="'+rndpos()+'" cy="'+rndpos()+'" rx="'+rndpos()+'" ry="'+rndpos()+'" fill="'+rndcol()+'"/>')
	elif c=="rect":
		open("art/"+str(sown)+".svg","a").write('\n<rect x="'+rndpos()+'" y="'+rndpos()+'" width="'+rndpos()+'" height="'+rndpos()+'" fill="'+rndcol()+'"/>')
	elif c=="line":
		open("art/"+str(sown)+".svg","a").write('\n<line x1="'+rndpos()+'" y1="'+rndpos()+'" x2="'+rndpos()+'" y2="'+rndpos()+'" stroke="'+rndcol()+'"/>')
	elif c=="text":
		open("art/"+str(sown)+".svg","a").write('\n<text x="'+rndpos()+'" y="'+rndpos()+'" font-family="Verdana" font-size="48" stroke="'+rndcol()+'">\n\t'+rndstr()+'\n</text>')
	while transform!=0:
		open("art/"+str(sown)+".svg","a").write('\n</g>')
		transform-=1
#end
open("art/"+str(sown)+".svg","a").write('\n</svg>')