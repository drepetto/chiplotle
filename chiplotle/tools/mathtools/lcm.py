from chiplotle.tools.mathtools.gcf import gcf

def lcm(a, b):
    ''' returns the lowest common multiple of a & b'''
    
    the_gcf = 0
    lcm = 0
    
    if a > b:
        dividend = a
        divisor = b
    else:
        dividend=b
        divisor=a
        
    the_gcf = gcf(dividend,divisor)
    lcm = (a * b) / the_gcf
    
    return lcm