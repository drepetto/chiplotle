## TODO: this can be removed. Replaced with a Python dictionary.
#def lookup_char(character):
#	if character == 'a':
#		return a
#	elif character == 'b':
#		return b
#	elif character == 'c':
#		return c
#	elif character == 'd':
#		return d
#	elif character == 'e':
#		return e
#	elif character == 'f':
#		return f
#	elif character == 'g':
#		return g
#	elif character == 'h':
#		return h
#	elif character == 'i':
#		return i
#	elif character == 'j':
#		return j
#	elif character == 'k':
#		return k
#	elif character == 'l':
#		return l
#	elif character == 'm':
#		return m
#	elif character == 'n':
#		return n
#	elif character == 'o':
#		return o
#	elif character == 'p':
#		return p
#	elif character == 'q':
#		return q
#	elif character == 'r':
#		return r
#	elif character == 's':
#		return s
#	elif character == 't':
#		return t
#	elif character == 'u':
#		return u
#	elif character == 'v':
#		return v
#	elif character == 'w':
#		return w
#	elif character == 'x':
#		return x
#	elif character == 'y':
#		return y
#	elif character == 'z':
#		return z
#	elif character == '-':
#		return dash
#	elif character == '!':
#		return bang


char_dict = {'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g, 'h':h,
   'i':i, 'j':j, 'k':k, 'l':l, 'm':m, 'n':n, 'o':o, 'p':p, 'q':q, 'r':r,
   's':s, 't':t, 'u':u, 'v':v, 'w':w, 'x':x, 'y':y, 'z':z, '-':dash, 
   '!':bang}

# a_ b_ etc are backwards characters for iron on transfers 

a = [
	0,0,0,
	0,0,0,
	1,1,1,
	1,0,1,
	1,1,1,
	0,0,1,
	0,0,0
]

a_ = [
	0,0,0,
	0,0,0,
	1,1,1,
	1,0,1,
	1,1,1,
	1,0,0,
	0,0,0
]

b= [
	1,0,0,
	1,0,0,
	1,1,1,
	1,0,1,
	1,1,1,
	0,0,0,
	0,0,0
]

b_= [
	0,0,1,
	0,0,1,
	1,1,1,
	1,0,1,
	1,1,1,
	0,0,0,
	0,0,0
]
				
c= [
	0,0,0,
	0,0,0,
	1,1,1,
	1,0,0,
	1,1,1,
	0,0,0,
	0,0,0
]

c_= [
	0,0,0,
	0,0,0,
	1,1,1,
	0,0,1,
	1,1,1,
	0,0,0,
	0,0,0
]

d= [
	0,0,1,
	0,0,1,
	1,1,1,
	1,0,1,
	1,1,1, 
	0,0,0,
	0,0,0
]

d_= [
	1,0,0,
	1,0,0,
	1,1,1,
	1,0,1,
	1,1,1, 
	0,0,0,
	0,0,0
]

e= [
	0,0,0,
	1,1,1,
	1,0,0,
	1,1,1,
	1,0,0, 
	1,1,1,
	0,0,0
]

e_= [
	0,0,0,
	1,1,1,
	0,0,1,
	1,1,1,
	0,0,1, 
	1,1,1,
	0,0,0
]
					
i= [
	0,1,0,
	0,0,0,
	0,1,0,
	0,1,0,
	0,1,0,
	0,0,0,
	0,0,0
]

i_= i

k= [
	1,0,0,
	1,0,0,
	1,0,1,
	1,1,0,
	1,0,1,
	0,0,0,
	0,0,0
]

k_= [
	0,0,1,
	0,0,1,
	1,0,1,
	0,1,1,
	1,0,1,
	0,0,0,
	0,0,0
]
			
l= [
	0,1,0,
	0,1,0,
	0,1,0,
	0,1,0,
	0,1,0,
	0,0,0,
	0,0,0
]
			
l_= l
	
m= [
	1,0,1,
	1,0,1,
	1,1,1,
	1,1,1,
	1,0,1,
	0,0,0,
	0,0,0
]
	
m_= m
			
n= [
	0,0,0,
	0,0,0,
	1,1,1,
	1,0,1,
	1,0,1,
	0,0,0,
	0,0,0
]

n_= n
	
o= [
	0,0,0,
	0,0,0,
	1,1,1,
	1,0,1,
	1,1,1,
	0,0,0,
	0,0,0
]

o_= o
				
r= [
	0,0,0,
	0,0,0,
	1,1,1,
	1,0,0,
	1,0,0,
	0,0,0,
	0,0,0
]

r_= [
	0,0,0,
	0,0,0,
	1,1,1,
	0,0,1,
	0,0,1,
	0,0,0,
	0,0,0
]

t= [
	0,1,0,
	0,1,0,
	1,1,1,
	0,1,0,
	0,1,0,
	0,0,0,
	0,0,0
]

t_= t
				
y= [
	0,0,0,
	0,0,0,
	1,0,1,
	1,0,1,
	1,1,1,
	0,0,1,
	1,1,1
]

y_= [
	0,0,0,
	0,0,0,
	1,0,1,
	1,0,1,
	1,1,1,
	1,0,0,
	1,1,1
]
		
dash= dash_
	0,0,0,
	0,0,0,
	0,0,0,
	1,1,1,
	0,0,0,
	0,0,0,
	0,0,0	
]


bang= bang_
	0,0,0,
	0,1,0,
	0,1,0,
	0,1,0,	
	0,0,0,
	0,1,0,
	0,0,0
]

