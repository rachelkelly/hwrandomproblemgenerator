#creative commons 2013 rachel kelly
#a random homework problem generator for stats 243, spring 2013
#port to python 2.7, rewritten 21 november 2013 under same usage

import random

problems = []
i = 0

print "what section is today's homework?\n"
section = float(raw_input())
print "how many problems today?\n"
amount = int(raw_input())
while i < amount:
    print "what is the problem number?\n"
    problem = int(raw_input())
    problems.append(problem)
    i += 1
    
print "From section %s there are %s problems, which are the following\n" %(sect$
print(problems)

problemChoice = random.choice(problems)
#whoa, random.choice might work! thanks steve from pyladies!
print "The problem to grade is",problemChoice
