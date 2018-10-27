# CharlieplexCalc
A Python script that calculates charlieplexing pinouts and logic tables.

Run the script with the desired number of LEDs to drive (up to 999), and it will output the pinouts, logic table, and Ardunio code header to help you set up and program your CharliePlexed LEDs.


## Usage
`charlie.py <numleds>`

e.g
`> python charlie.py 12`

### Output
```
You need 4 pins to drive 12 LEDs
[You could drive a maximum of 12 LEDs with 4 pins]

Pin   1 >    1-   2+   5-   6+  11-  12+
Pin   2 >    1+   2-   3-   4+   9-  10+
Pin   3 >    3+   4-   5+   6-   7-   8+
Pin   4 >    7+   8-   9+  10-  11+  12-

Logic table     1    2    3    4
Led   1   >    LO   HI   IN   IN
Led   2   >    HI   LO   IN   IN
Led   3   >    IN   LO   HI   IN
Led   4   >    IN   HI   LO   IN
Led   5   >    LO   IN   HI   IN
Led   6   >    HI   IN   LO   IN
Led   7   >    IN   IN   LO   HI
Led   8   >    IN   IN   HI   LO
Led   9   >    IN   LO   IN   HI
Led  10   >    IN   HI   IN   LO
Led  11   >    LO   IN   IN   HI
Led  12   >    HI   IN   IN   LO

int numPins = 4;
int numLeds = 12;
byte	ledPins[][4] ={
	{ 0,1,2,2 },
	{ 1,0,2,2 },
	{ 2,0,1,2 },
	{ 2,1,0,2 },
	{ 0,2,1,2 },
	{ 1,2,0,2 },
	{ 2,2,0,1 },
	{ 2,2,1,0 },
	{ 2,0,2,1 },
	{ 2,1,2,0 },
	{ 0,2,2,1 },
	{ 1,2,2,0 },
	};
```
