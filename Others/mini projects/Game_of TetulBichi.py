import random
print """ Instruction: 
 """
sw = input("starts with: ")
pl = sw/2
cm = sw -pl
while pl>0 and cm>0:
	pli = input('pl input(1-%d): '%pl)
	if pli%2==0:
		a = "even"
	else:
		a = "odd"
	l = [1,2]
	cmc = random.choice(l)
	if cmc == 1:
		b = 'odd'
	else:
		b = 'even'
	print "com choice: ",b
	if a == b:
		cm = cm+pli
		pl = pl - pli
	print "now com has: ",cm, "you have: ",pl
	if cm<=0 or pl <=0:
		break
	cmc2 = random.randint(1,cm)
	print cmc2
	
	print "determine odd or even(1/2): ",
	plc = input()
	if plc == 2:
		a = "even"
	else:
		a = "odd"	
	if cmc2%2 == 0:
		b = 'even'
	else:
		b = 'odd'
	print "com choice: ",cmc2
	if a == b:
		cm = cm-cmc2
		pl = pl + cmc2

	print "now com has: ",cm, "you have: ",pl
print "\n \nGAME OvEr"	
if cm > pl:
	print "com wins"
else:
	print "You win"