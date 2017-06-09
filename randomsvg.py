import random
sown=random.randint(0,999999)
random.seed(sown)
side=800
#opening
open("random.svg","w").write('<svg width="'+str(side)+'px" height="'+str(side)+'px" version="1.1" xmlns="http://www.w3.org/2000/svg">\n<desc>')
open("random.svg","a").write(str(sown)+"</desc>")
#how many items do i draw?
max=random.randint(1,99)
#stuff
options=["rect"]
for i in range(max):
	c=random.choice(options)
	if c=="rect":
		x=random.randint(0,side)
		y=random.randint(0,side)
		w=random.randint(0,side)
		h=random.randint(0,side)
		open("random.svg","a").write('\n<rect x="'+str(x)+'px" y="'+str(y)+'px" width="'+str(y)+'px" height="'+str(y)+'px"/>')
#end
open("random.svg","a").write('</svg>')