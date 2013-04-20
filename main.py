#creative commons 2013 rachel kelly
#a random homework problem generator for stats 243, spring 2013

import random

problems = []
i = 0

section = float(input("what section is today's homework? "))
amount = int(input("\nhow many problems today? "))
while i < amount:
	problem = int(input("what is the problem number? "))
	problems.append(problem)
	i += 1

print("From section",section,"there are",amount,"problems, which are the following\n")
print(problems)

problemChoice = random.choice(problems)
#whoa, random.choice might work!  thanks steve from pyladies!
print("The problem to grade is",problemChoice)
