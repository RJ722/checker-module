This is basically a tester of the function random.random() in the random module (Python3)

What it Tests?
=============

It tests that all the numbers so generated are equally probable to lie anywhere between 0 and 1 , i.e. they are truly random in sense and do not crowd up in a particular interval.

How it does?
=============

What it exactly does is that it takes two inputs from the user:
	
	1) How many random numbers to be generated??

		It tells the computer that how many random number have to be generated in order to get tested.

	2) How many intervals to be generated??

		Now, the range between 0 and 1 is broken into this very number of intervals.eg. when input is 2 the intervals so created will be:
			1) [0, 0.5)
			2) [0.5, 1)

	Now, what it will do is that it will randomly generate numbers using function random.random() and in the end will give the count of the number of numbers appearing in a particular interval and it should be more or less the same.

NOTE:
-----

1)	For simplification and minimzing the round-off error, the intervals to be provided should be an exponent of 2. A list of such numbers has been publi8shed near the input field for the purpose.


2)	There are default values for the number of random numbers to be generated = 1000 and number of intrevls to be created = 4 ( Just for fun and lazy purposes :) for people like me! )

What I intend to do in future?
----------------------------

That it shall give an error mesage when it so happen that the function random.random() is giving a biased result and otherwise it should give a message stating the account of randomness ( entropy :) ) 

