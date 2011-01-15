def gcf(dividend, divisor):
    ''' returns the greatest common factor of dividend, divisor'''
    
    reminder = -1
    while reminder !=0:
        qoutient = dividend / divisor
        reminder = dividend % divisor
        if reminder != 0:
            dividend = divisor
            divisor = reminder
    gcf = divisor
    return divisor