#!/usr/bin/python
from random import LehmerRandom
from random import Random

print "Simulation Model Main File.\n"

"""
 Asking random.py for a random using lehmer or any other mechanism.
"""
rng = LehmerRandom()
ivar = rng.uniform(4,5)
print "Lehmer uniform random value=",ivar, "\n"

rng = LehmerRandom()
ivar = rng.exponential(2)
print "Lehmer exponential random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.erlang(2,10)
print "Lehmer erlang random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.pareto(3,8)
print "Lehmer pareto random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.normal(2,10)
print "Lehmer nornal random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.lognormal(3,8)
print "Lehmer lognormal random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.chisquare(4)
print "Lehmer chisquare random value=",ivar,"\n"


rng = LehmerRandom()
ivar = rng.student(3)
print "Lehmer student random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.bernoulli(0.2)
print "Lehmer bernoulli random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.equilikely(3,8)
print "Lehmer equilikely random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.binomial(3,0.4)
print "Lehmer binomial random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.geometric(0.2)
print "Lehmer geometric random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.pascal(3,0.8)
print "Lehmer pascal random value=",ivar,"\n"

rng = LehmerRandom()
ivar = rng.poisson(3)
print "Lehmer poisson random value=",ivar,"\n"



