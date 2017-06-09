import random
sown=random.randint(0,999999)
random.seed(sown)
side=800
#opening
open("/art/"+str(sown)+".svg","w+").write('<svg width="'+str(side)+'px" height="'+str(side)+'px" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>')
open("/art/"+str(sown)+".svg","a").write(str(sown)+"</desc>")
#how many items do i draw?
max=random.randint(1,99)
#stuff
def rndpos():
	return str(random.randint(0,side))
def rndcol():
	colors=["black","blue","brown","green","grey","navy","none","orange","pink","purple","red","white","yellow"]
	return random.choice(colors)
options=["rect","circle","ellipse","line"]
for i in range(max):
	c=random.choice(options)
	if c=="circle":
		open("/art/"+str(sown)+".svg","a").write('\n<circle cx="'+rndpos()+'px" cy="'+rndpos()+'px" r="'+rndpos()+'px" fill="'+rndcol()+'"/>')
	elif c=="ellipse":
		open("/art/"+str(sown)+".svg","a").write('\n<rect cx="'+rndpos()+'px" cy="'+rndpos()+'px" rx="'+rndpos()+'px" ry="'+rndpos()+'px" fill="'+rndcol()+'"/>')
	elif c=="rect":
		open("/art/"+str(sown)+".svg","a").write('\n<rect x="'+rndpos()+'px" y="'+rndpos()+'px" width="'+rndpos()+'px" height="'+rndpos()+'px" fill="'+rndcol()+'"/>')
	elif c=="line":
		open("/art/"+str(sown)+".svg","a").write('\n<rect x1="'+rndpos()+'px" y1="'+rndpos()+'px" x2="'+rndpos()+'px" y2="'+rndpos()+'px" stroke="'+rndcol()+'"/>')
#end
open("/art/"+str(sown)+".svg","a").write('</svg>')