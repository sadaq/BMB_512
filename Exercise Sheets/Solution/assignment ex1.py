#Assignment 1.1:
1.	 x = 1:
1 is assigned to the variable “x”.
2.	x = y:
The value of variable “y” should be assigned to variable “x”, as “y” is not defined so it shows the following Nameerror:  “NameError: name 'y' is not defined”.
3.	1 = x:
It shows a syntax error:  SyntaxError: can't assign to literal.
4.	x = x + 1:
It adds 1 with the value of variable “x” and assigns the new value in the variable “x”.
5.	x += 3:
It is similar to the x = x + 3, adds 3 with the value of variable “x” and assigns the new value in the variable “x”.
6.	x %= 4:
It divides the value of variable “x” by 4 and assigns the reminder to the variable “x”

Assignment 1.2:
1.	5:
Type: int
2.	5.0
Type: float
3.	“bingo”:
Type: str
4.	‘bingo’:
Type: str
5.	“””bingo”””:
Type: str
6.	“”verb””:
Type: SyntaxError: invalid syntax
7.	Verb:
Type: NameError: name 'Verb' is not defined
8.	True:
Type: bool



Assignment 1.3:
1.	One = “Now the winter of our discontent is turned glorious summer.”
2.	Two = “What comes around goes around.”
3.	Three = “Couldn’t, Shouldn’t, Wouldn’t” 
Or
Three = “Couldn\’t, Shouldn\’t, Wouldn\’t”  
Or 
Three = “”” Couldn’t, Shouldn’t, Wouldn’t  ”””
4.	 Four = “ \”Impossible, isn\’t it?\”, said the cat and vanished.”
Or
Four = “”” ”Impossible, isn’t it?”, said the cat and vanished. “””


Assignment 1.4:
Combining “Stan Laurel” & “Oliver Hardy”:
By concatenating the two strings can be combined as follows-
 “Stan Laurel” + “Oliver Hardy”


Assignment 1.5:
Combining “Stan Laurel” & “Oliver Hardy” separated by a space:
By concatenating the two strings and a white space “ “ as follows-
 “Stan Laurel” + ” ” + “Oliver Hardy”


Assignment 1.6:
“bla” * 5 
Assignment 1.7:
s[-3:]


Assignment 1.8:
names = “Stan Laurel & Oliver Hardy”
names.split(' ')[0]
names.split(' ')[-1]



Assignment 1.9:
bl = "bl"
vowel = "aeiou"
c = ""
for letter in vowel:
    t = bl + letter
    c = c + t
print c
