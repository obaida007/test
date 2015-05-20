import datetime as dt
import math

global_seed = 0 

class Random:
	#Random Variate Generation Class
        """There is no constant definition in python. just dont change the value of the variable
        """
        PI = 3.1415926535897932384626433832795
        #global_seed = 0
        def uniform(self,a, b):
		#print "Generating Uniform Random"
                if a > b:
                        print "Invalid arguments: a=", a, ", b=", b  #SSF_THROW exception, e.g.: SSF_THROW("invalid arguments: a=" << a << ", b=" << b);
			#raise SSF_THROW("Invalid arguments reported for uniform random number")  #define 
                if a == b:
                        return a
                else:
			#var= super(Random, self).__init__()
			#print super(Random, self).__call__()
                        #return a+(b-a)+super(Random, self).__call__() when i had Raadom(LehmerRandom) and LehmerRandom() classes.
			return a+((b-a)*self())
	def exponential(self, x):
		#print "Generating Exponential Random"
		if x <= 0:
			print "invalid argument for exponential random number: x=", x#SSF_THROW("invalid argument: x=" << x);
		#result = -1.0/x*math.log(1.0-self());
		return (-1.0/x*math.log(1.0-self()));
	def erlang(self, n, x):
		#print "Generating erlang random"
		if n<=0 or x <= 0:
			print "invalid arguments for erlang random number: n=", n,"x=",x #SSF_THROW("invalid argument: x=" << x);
		y = 0.0
		for i in range(0,n):
			y += self.exponential(x);
		return y

	def pareto(self, k, a):
		if k <= 0 or a <= 0:
			print "invalid arguments: k=", k, ", a=", a #SSF_THROW("invalid arguments: k=" << k << ", a=" << a);
		return k*pow(1.0-self(), -1.0/a)

	def normal(self, m, s):
		if s <= 0:
			print "invalid arguments: m=", m, ", s=", s #SSF_THROW ("invalid arguments: m=" << m << ", s=" << s);
		# Uses a very accurate approximation of the normal idf due to Odeh & Evans, J. Applied Statistics, 1974, vol 23, pp 96-97.           
		p0 = 0.322232431088
		q0 = 0.099348462606
		p1 = 1.0
		q1 = 0.588581570495
		p2 = 0.342242088547
		q2 = 0.531103462366
		p3 = 0.204231210245e-1
		q3 = 0.103537752850
		p4 = 0.453642210148e-4
		q4 = 0.385607006340e-2
		u = self()
		if u < 0.5:
			t = math.sqrt(-2.0*math.log(u))
		else:
			t = math.sqrt(-2.0*math.log(1.0-u))
		p = p0+t*(p1+t*(p2+t*(p3+t*p4)))
		q = q0+t*(q1+t*(q2+t*(q3+t*q4)))
		if u < 0.5:
			z = (p/q)-t
		else:
			z = t-(p/q)
		return m+s*z
	def lognormal(self,a, b):
		if b <= 0:
			print"invalid arguments: a=", a, ", b=", b #SSF_THROW("invalid arguments: a=" << a << ", b=" << b);
		result = math.exp(a+b*self.normal(0.0, 1.0))
		return result
	def chisquare(self, n):
		if n <= 0:
			print "invalid argument: n=", n#SSF_THROW("invalid argument: n=" << n);
		y = 0.0
		for i in range(0,n):
			z = self.normal(0.0, 1.0)
			y += z*z
		return y
	def student(self, n):
		if n <= 0:
			print "invalid argument: n=", n  #SSF_THROW("invalid argument: n=" << n);
		result=self.normal(0.0, 1.0)/math.sqrt(self.chisquare(n)/n)
		return result;
	def bernoulli(self, p):
		if p < 0 or p > 1:
			print "invalid argument: p=", p #SSF_THROW("invalid argument: p=" << p);
		result = self()
		if result<p:
			result = 1 
		else:
			result = 0
		return result;
		#Ternary logical operation in python:
		#a if test else b
		#>>> 'true' if True else 'false'
		#'true'
		#>>> 'true' if False else 'false'
		#'false'
	def equilikely (self, a, b):
		"Should return long variable(v typecasted)+a"
		if a > b:
			print "invalid arguments: a=", a, ", b=", b #SSF_THROW("invalid arguments: a=" << a << ", b=" << b);
		x = self()
		v = a + math.floor((b-a+1)*x)
		return v
	def binomial(self, n, p):
		if n <= 0 or p < 0 or p > 1:
			print "invalid arguments: n=", n, ", p=", p#SSF_THROW("invalid arguments: n=" << n << ", p=" << p);
		y = 0
		for i in range(0,n):
			y += self.bernoulli(p)
		return y
	def geometric(self, p):
		if p <= 0 or p >= 1: 
			print "invalid argument: p=", p #SSF_THROW("invalid argument: p=" << p);
		result = 1+(math.log(1.0-self())/math.log(1.0-p))
		return result
	def pascal(self, n, p):
		if n <= 0 or p <= 0 or p >= 1:
			print "invalid arguments: n=", n, ", p=", p # SSF_THROW("invalid arguments: n=" << n << ", p=" << p);
		y = 0
		for i in range(0,n):
			y += self.geometric(p)
		return y
	def poisson(self, m):
		if m <= 0:
			print "invalid argument: m=", m #SSF_THROW("invalid argument: m=" << m);
		y = 0
		t = math.exp(m)
		while True:
			y+=1
			t *= self()
			if t < 1.0:
				break
		y-=1
		return y

#	def permute(self, n, long* array):
#		if(n <= 0 || !array) 
#			print"invalid arguments: n=", n, ", array=", array #SSF_THROW("invalid arguments: n=" << n << ", array=" << array);
#		for i in range (0,n):
#			array[i] = i
#		for i in range (0,n-1):
#			j = self.equilikely(i, n-1)
#			if i != j:
#				tmp = array[i]
#				array[i] = array[j]
#				array[j] = tmp


class LehmerRandom(Random):
	multiplier = 48271  #a 
	modulus = 2147483647 #m
	max_streams = 256 #ms
	jump_multiplier = 22925 #js
	quotient = modulus/multiplier
	remainder = modulus%multiplier
	jump_quotient = modulus/jump_multiplier
	jump_remainder = modulus%jump_multiplier
	#private vabiables declared in lehmer.h|below
	seed = 0
	init_seed = 0
	stream_index = 0
	num_streams = 0
	
	#Default constructor needs to set when an object is created.
	def setLehmerRandomParameters(self, a, m, ms, js):
		self.multiplier = a
		self.modulus = m
		self.max_streams = ms
		self.jump_multiplier = js
		self.quotient = m/a
		self.remainder = m%a
		self.jump_quotient = m/js
		self.jump_remainder = m%js
	#default constructors are accepted in python. Constructor to set seed
	def __init__(self, myseed=0, stream_index=0, nstreams=1): #sets the seed
		assert self.multiplier < self.modulus, "multiplier is not smaller than modulus"
		assert self.remainder < self.quotient, "remainder is not smaller than quotient"
		#must be modulus compatible
		self.setSeed(myseed)
		num_streams = nstreams
		if stream_index < 0 or stream_index >= num_streams:
			print "invalid arguments: stream_index=" , stream_index, ", num_streams=", num_streams
		if num_streams > self.max_streams:
			print "exceeding the max number of streams"
		for j in range (1,stream_index):
			self.seed = self.jump_multiplier*(self.seed%self.jump_quotient)-self.jump_remainder*(self.seed/self.jump_quotient)
			if self.seed <= 0:
				self.seed += self.modulus
	#another function to set seed
	def setSeed(self, myseed):
		#print  "setting seed"
		if myseed == 0:
			self.seed = self.make_new_seed()
		else:
			self.seed = myseed+global_seed
			#self.seed = myseed+random.global_seed
			self.seed = self.multiplier*(self.seed%self.quotient)-self.remainder*(self.seed/self.quotient)
			#draw one number so the seed is not predictable
		if self.seed <= 0:
			self.seed += self.modulus
			self.init_seed = self.seed
		#print "self.seed=", self.seed
	# The following function generates a random seed based on xorshift random number generation for c (converted for python). system microsecond is taken to make sure that different objects has different seeds
	def make_new_seed(self):
		#print "making new seed"
		self.x = x =  dt.datetime.now().microsecond  #Make sure all the objects have different seed
	        self.y = 362436069
	        self.z = 521288629
	        self.w = 88675123
	        t = self.x ^ (self.x<<11) & 0xffffffff                   # <-- keep 32 bits
	        self.x = self.y
	        self.y = self.z
	        self.z = self.w
	        w = self.w
	        self.w = (w ^ (w >> 19) ^(t ^ (t >> 8))) & 0xffffffff    # <-- keep 32 bits
	        return self.w		
    # Overloaded operator equivalent that will generate the Random number
	def __call__(self):
		self.seed = self.multiplier*(self.seed%self.quotient)-self.remainder*(self.seed/self.quotient)
		
		if self.seed <= 0:
			self.seed += self.modulus
		#print "In __call__:self.seed=",self.seed, ", self.modulus=", self.modulus
		#lehmer_rand=float(self.seed) / float(self.modulus)
		#print lehmer_rand
		return float(self.seed) / float(self.modulus)


class MersenneTwisterRandom(Random):
	def __init__(self,one_seed):
		self.seed(one_seed)
		self.randInt()
	def __init__(self,big_seed, seed_len):
		self.seed(big_seed,seed_len)
		self.randInt()
	def rand(self):
		return self.randInt() * (1.0/4294967295.0)
	def rand(self,n):
		return self.rand() * n
	def randExc(self,):
		return self.randInt() * (1.0/4294967296.0)
	def randExc(self,n):
		return self.randExc() * n
	def randDblExc(self,):
		return self.randInt() + 0.5 * (1.0/4294967296.0)
	def randDblExc(self,n):
		return self.randDblExc() * n
	#def rand53():
	#	uint32 a = randInt() >> 5, b = randInt() >> 6
	#	return (a * 67108864.0 + b) * (1.0/9007199254740992.0); // by Isaku Wada
	def randNorm(self, mean, variance):
		# Return a real number from a normal (Gaussian) distribution with given
		# mean and variance by Box-Muller method
		r = math.sqrt(-2.0 * math.log(1.0-self.randDblExc())) * variance
		phi = 2.0 * 3.14159265358979323846264338328 * self.randExc()
		return mean + r * math.cos(phi)
	def randInt(self):
		# pull a 32-bit integer from the generator state; every other
		# access function simply transforms the numbers extracted here
		return 5
		
		#if left == 0:
		#	reload()
		#left-=1
		#register uint32 s1;
		#s1 = *pNext++;
		#s1 ^= (s1 >> 11);
		#s1 ^= (s1 << 7) & 0x9d2c5680UL;
		#s1 ^= (s1 << 15) & 0xefc60000UL;
		#return (s1 ^ (s1 >> 18));

	def randInt(self,n):
		# find which bits are used in n; optimized by Magnus Jonsson
		# (magnus@smartelectronix.com)
		used = n
		return 5
		#used |= used >> 1;
		#used |= used >> 2;
		#used |= used >> 4;
		#used |= used >> 8;
		#used |= used >> 16;
		# draw numbers until one is found in [0,n]
		#do {
		#i = randInt() & used; // toss unused bits to shorten search
		#} while(i > n);
		#return i;
		#}
	def seed(self, one_seed):
		if one_seed == 0:
			one_seed = self.make_new_seed();
		initialize(one_seed+global_seed)
		reload()

	def seed(big_seed, seed_len):
		# seed the generator with an array of uint32's; there are 2^19937-1
		# possible initial states, this function allows all of those to be
		# accessed by providing at least 19937 bits (with a default seed
		# length of N = 624 uint32's); any bits above the lower 32 in each
		# element are discarded
		#initialize(19650218UL);
		#register int i = 1;
		#register uint32 j = 0;
		#register int k = (N > seed_len ? N : seed_len);
		#for(; k; --k) {
		#state[i] = state[i] ^ ((state[i-1] ^ (state[i-1] >> 30)) * 1664525UL);
		#state[i] += ((big_seed[j]+global_seed) & 0xffffffffUL) + j;
		#state[i] &= 0xffffffffUL;
		#++i; ++j;
		#if(i >= N) { state[0] = state[N-1]; i = 1; }
		#if(j >= seed_len) j = 0;
		#}
		#for(k = N - 1; k; --k) {
		#state[i] = state[i] ^ ((state[i-1] ^ (state[i-1] >> 30)) * 1566083941UL);
		#state[i] -= i;
		#state[i] &= 0xffffffffUL;
		#++i;
		#if(i >= N) { state[0] = state[N-1]; i = 1; }
		#}
		#state[0] = 0x80000000UL; // MSB is 1, assuring non-zero initial array
		#reload();
		#}
		print "hello"
	def initialize(self,seed):
		# initialize generator state with seed; see Knuth TAOCP Vol 2, 3rd
		# Ed, p.106 for multiplier; in previous versions, most significant
		# bits (MSBs) of the seed affect only MSBs of the state array
		# (modified 9 Jan 2002 by Makoto Matsumoto)
		#register uint32 *s = state;
		#register uint32 *r = state;
		#register int i = 1;
		#*s++ = seed & 0xffffffffUL;
		#for(; i < N; ++i) {
		#*s++ = (1812433253UL * (*r ^ (*r >> 30)) + i) & 0xffffffffUL;
		#r++;
		print "initialize"
	def reload(self):
		# generate N new values in state; made clearer and faster by
		# Matthew Bellew (matthew.bellew@home.com)
		#register uint32 *p = state;
		#register int i;
		#for(i = N - M; i--; ++p)
		#*p = twist(p[M], p[0], p[1]);
		#for(i = M; --i; ++p)
		#*p = twist(p[M-N], p[0], p[1]);
		#*p = twist(p[M-N], p[0], state[0]);
		#left = N, pNext = state;
		print "reload"
	def  save(self, saveArray):
		#register uint32 *sa = saveArray;
		#register const uint32 *s = state;
		#register int i = N;
		#for(; i--; *sa++ = *s++) {}
		#*sa = left;
		print "save"
	def load(self, loadArray):
		#register uint32 *s = state;
		#register uint32 *la = loadArray;
		#register int i = N;
		#for(; i--; *s++ = *la++) {}
		#left = *la;
		#pNext = &state[N-left];
		print "save"	
	def make_new_seed(self):
		#print "making new seed"
		self.x = x =  dt.datetime.now().microsecond  #Make sure all the objects have different seed
	        self.y = 362436069
	        self.z = 521288629
	        self.w = 88675123
	        t = self.x ^ (self.x<<11) & 0xffffffff                   # <-- keep 32 bits
	        self.x = self.y
	        self.y = self.z
	        self.z = self.w
	        w = self.w
	        self.w = (w ^ (w >> 19) ^(t ^ (t >> 8))) & 0xffffffff    # <-- keep 32 bits
	        return self.w		
    # Overloaded operator equivalent that will generate the Random number





#contenten of main.py file in same directory
"""
#!/usr/bin/python
from random import LehmerRandom
from random import Random

print "Simulation Model Main File.\n"
rng = LehmerRandom()
ivar = rng.uniform(4,5)
print "Lehmer uniform random value=",ivar, "\n"

rng = LehmerRandom()
ivar = rng.exponential(2)

"""

