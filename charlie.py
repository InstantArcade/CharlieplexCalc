# Charlieplex connection calculator by Bob Hickman (InstantArcade)
# Copyright 2018 Bob Hickman
#
# Released under the MIT License
#

import sys

if len(sys.argv) < 2:
	print "Please speficy number of LEDs you want to drive"
	exit()

numLeds = int(sys.argv[1]);

if numLeds < 1 or numLeds > 1000:
	print "Please speficy number of LEDs you want to drive between (1 and 1000)"
	exit()

# formula is n * (n-1)
# calc the easy way
numPins = 2

while numPins*(numPins-1) < numLeds:
	numPins+=1

print ""
print "You need", numPins, "pins to drive", numLeds, "LEDs"
print "[You could drive a maximum of", (numPins*(numPins-1)), "LEDs with", numPins, "pins]"

# Each pair of pins is connected to two LEDs in reverse parallel to each other, e.g.
#
#			-	+			-	+					-	+							-	+									-	+											-	+
#			L0	L1	L2	L3	L4	L5	L6	L7	L8	L9	L10	L11	L12	L13	L14	L15	L16	L17	L18 L19 L20 L21 L22 L23 L24 L25 L26 L27 L28 L29 L30 L31 L32 L33 L34 L35 L36 L37 L38 L39 L40 L41
# Pin 0 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#			|	|	.	.	|	|	.	.	.	.	|	|	.	.	.	.	.	.	|	|	.	.	.	.	.	.	.	.	|	|	.	.	.	.	.	.	.	.	.	.	|	|
#			-	v	.	.	|	|	.	.	.	.	|	|	.	.	.	.	.	.	|	|	.	.	.	.	.	.	.	.	|	|	.	.	.	.	.	.	.	.	.	.	|	|
#			^	-	.	.	|	|	.	.	.	.	|	|	.	.	.	.	.	.	|	|	.	.	.	.	.	.	.	.	|	|	.	.	.	.	.	.	.	.	.	.	|	|
#			|	|	-	+	|	|	.	.	-	+	|	|	.	.	.	.	-	+	|	|	.	.	.	.	.	.	-	+	|	|	.	.	.	.	.	.	.	.	-	+	|	|
# Pin 1------------------	|	|	-------------	|	|	---------------------	|	|   -----------------------------	|	|   -------------------------------------	|	|
#			+	-	|	|	|	|	.	.	|	|	|	|	.	.	.	.	|	|	|	|	.	.	.	.	.	.	|	|	|	|	.	.	.	.	.	.	.	.	|	|	|	|
#					-	v	-	v	.	.	|	|	|	|	.	.	.	.	|	|	|	|	.	.	.	.	.	.	|	|	|	|	.	.	.	.	.	.	.	.	|	|	|	|
#					^	-	^	-	.	.	|	|	|	|	.	.	.	.	|	|	|	|	.	.	.	.	.	.	|	|	|	|	.	.	.	.	.	.	.	.	|	|	|	|
#					|	|	|	|	-	+	|	|	|	|	.	.	-	+	|	|	|	|	.	.	.	.	-	+	|	|	|	|	.	.	.	.	.	.	-	+	|	|	|	|
# Pin 2 ---------------------------------	|	|	|	|	-------------	|	|	|	|	---------------------	|	|	|	|   -----------------------------	|	|	|	|
#					+	-	+	-	|	|	|	|	|	|	.	.	|	|	|	|	|	|	.	.	.	.	|	|	|	|	|	|	.	.	.	.	.	.	|	|	|	|	|	|
#									-	v	-	v	-	v	.	.	|	|	|	|	|	|	.	.	.	.	|	|	|	|	|	|	.	.	.	.	.	.	|	|	|	|	|	|
#									^	-	^	-	^	-	.	.	|	|	|	|	|	|	.	.	.	.	|	|	|	|	|	|	.	.	.	.	.	.	|	|	|	|	|	|
#									|	|	|	|	|	|	-	+	|	|	|	|	|	|	.	.	-	+	|	|	|	|	|	|	.	.	.	.	-	+	|	|	|	|	|	|
# Pin 3 ---------------------------------------------------------	|	|	|	|	|	|	-------------	|	|	|	|	|	|	---------------------	|	|	|	|	|	|
#									+	-	+	-	+	-	|	|	|	|	|	|	|	|	.	.	|	|	|	|	|	|	|	|	.	.	.	.	|	|	|	|	|	|	|	|
#															-	v	-	v	-	v	-	v	.	.	|	|	|	|	|	|	|	|	.	.	.	.	|	|	|	|	|	|	|	|
#															^	-	^	-	^	-	^	-	.	.	|	|	|	|	|	|	|	|	.	.	.	.	|	|	|	|	|	|	|	|
#															|	|	|	|	|	|	|	|	.	.	|	|	|	|	|	|	|	|	.	.	-	+	|	|	|	|	|	|	|	|
# Pin 4 -----------------------------------------------------------------------------------------	|	|	|	|	|	|	|	|	-------------	|	|	|	|	|	|	|	|
#															+	-	+	-	+	-	+	-	|	|	|	|	|	|	|	|	|	|	.	.	|	|	|	|	|	|	|	|	|	|																							|	|	|	|	|	|	|	|
#																							-	v	-	v	-	v	-	v	-	v	.	.	|	|	|	|	|	|	|	|	|	|
#																							^	-	^	-	^	-	^	-   ^	-	.	.	|	|	|	|	|	|	|	|	|	|
#																							|	|	|	|	|	|	|	|	|	|	-	+	|	|	|	|	|	|	|	|	|	|
# Pin 5 ---------------------------------------------------------------------------------------------------------------------------------	|	|	|	|	|	|	|	|	|	|
#																							+	-	+	-	+	-	+	-	+	-	|	|	|	|	|	|	|	|	|	|	|	|
#																																	-	v	-	v	-	v	-	v	-	v	-	v
#																																	^	-	^	-	^	-	^	-   ^	-  	^	-
#																																	|	|	|	|	|	|	|	|	|	| 	|	|
# Pin 6 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#																																	+	-	+	-	+	-	+	-	+	-	+  	-

# 	 	ODD		EVEN Pin
# ODD	+		-		
# EVEN 	-		+	
# Led

# Manual calculated
# 0*-1				+4			+6			+8			+10			+12
# P0 > L 0-, L 1+, L 4-, L 5+, L10-, L11+, L18-, L19+, L28-, L29+, L40-, L41+

# 1*0				+2			+6			+8			+10			+12
# P1 > L 0+, L 1-, L 2-, L 3+, L 8-, L 9+, L16-, L17+, L26-, L27+, L38-, L39+

# 2*1				+2			+2			+8			+10			+12
# P2 > L 2+, L 3-, L 4+, L 5-, L 6-, L 7+, L14-, L15+, L24-, L25+, L36-, L37+

# 3*2				+2			+2			+2			+10			+12
# P3 > L 6+, L 7-, L 8+, L 9-, L10+, L11-, L12-, L13+, L22-, L23+, L34-, L35+

# 4*3				+2			+2			+2			+2			+12
# P4 > L12+, L13-, L14+, L15-, L16+, L17-, L18+, L19-, L20-, L21+, L32-, l33+

# 5*4				+2			+2			+2			+2			+2
# P5 > L20+, L21-, L22+, L23-, L24+, L25-, L26+, L27-, L28+, L29-, L30-, L31+

# 6*5				+2			+2			+2			+2			+2
# P6 > L30+, L31-, L32+, L33-, L34+, L35-, L36+, L37-, L38+, L39-, L40+, L41-

# Generated from the code below
# You need 7 pins to drive 42 LEDs
# Pin 0 > L0- L1+ L4- L5+ L10- L11+ L18- L19+ L28- L29+ L40- L41+
# Pin 1 > L0+ L1- L2- L3+ L8- L9+ L16- L17+ L26- L27+ L38- L39+
# Pin 2 > L2+ L3- L4+ L5- L6- L7+ L14- L15+ L24- L25+ L36- L37+
# Pin 3 > L6+ L7- L8+ L9- L10+ L11- L12- L13+ L22- L23+ L34- L35+
# Pin 4 > L12+ L13- L14+ L15- L16+ L17- L18+ L19- L20- L21+ L32- L33+
# Pin 5 > L20+ L21- L22+ L23- L24+ L25- L26+ L27- L28+ L29- L30- L31+
# Pin 6 > L30+ L31- L32+ L33- L34+ L35- L36+ L37- L38+ L39- L40+ L41-

class LED:
	posPin = -1
	negPin = -1

ledData = [ LED() for i in range(numLeds)]

# Print out the connections to leach LED
for pin in range( numPins ):
	print ""
	print "Pin {n:3d} > ".format(n=pin+1), 

	reverse_polarity = 0
	led = pin*(pin-1)
	numloops = 0
	offset = 4

	if( pin == 0 ):
		pinstep = 4
		reverse_polarity = 1
	else:
		pinstep = 2

	# import pdb; pdb.set_trace()
	while led < (numLeds):
		if( reverse_polarity == 0 ):
			if( led+1 >= numLeds ):
				print "{n:3d}{k}".format(n=led+1,k='+'),
			else:
				print "{n:3d}{x} {m:3d}{y}".format(n=led+1,x='+',m=led+2,y='-'),
			ledData[led].posPin = pin
			if( led+1 < numLeds ):
				ledData[led+1].negPin = pin
		else:
			if( led+1 >= numLeds ):
#				print "L{0}{1}".format(led+1,'-'),
				print "{n:3d}{k}".format(n=led+1,k='-'),
			else:
#				print "L{0}{1} L{2}{3}".format(led+1,'-',led+2,'+'),
				print "{n:3d}{x} {m:3d}{y}".format(n=led+1,x='-',m=led+2,y='+'),
			if( led+1 < numLeds ):
				ledData[led+1].posPin = pin
			ledData[led].negPin = pin

		offset += 2
		led += pinstep

		if( numloops >= pin-1 ):
			pinstep = offset
			reverse_polarity = 1
		else:
			pinstep = 2

		numloops += 1

print ""
print ""
print "Logic table  ",

for pin in range( numPins ):
	print "{num:3d}".format(num=pin+1),
	print "",

for led in range( numLeds ):
	print ""
	print "Led {num:3d}   >   ".format( num=led+1 ),
	for pin in range ( numPins ):
		if( ledData[led].posPin == pin ):
			print "HI  ",
		elif( ledData[led].negPin == pin ):
			print "LO  ",
		else:
			print "IN  ",

# Output actual code for arduino
#
# Table looks like this...
#
#byte ledPins[][7] = {
#  {2,1,0,2,2,2,2},
#  };

print ""
print ""
print "int numPins = "+str(numPins)+";"
print "int numLeds = "+str(numLeds)+";"
print "byte	ledPins[]["+str(numPins)+"] ={"
for led in range( numLeds ):
	line = ""
	print "	{",
#	print "Led {num:3d}   >   ".format( num=led+1 ),
	for pin in range ( numPins ):
		if( ledData[led].posPin == pin ):
			line += "1"
		elif( ledData[led].negPin == pin ):
			line += "0"
		else:
			line += "2"
		if( pin < numPins-1):
			line += ","
	print line,
	print "},"
print "	};"




