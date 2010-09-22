
def pascal_row(n):
   '''Returns the nth row of Pascal's Triangle.'''

   if not isinstance(n, int):
      raise TypeError('n must be int.')
   if n < 1:
      raise ValueError('n must be greater equal 1.')

   result = [1]
   x,numerator = 1, n
   for denominator in range(1, n // 2 + 1):
      # print(numerator,denominator,x)
      x *= numerator
      x /= denominator
      result.append(x)
      numerator -= 1
   if n&1 == 0:
      ## n is even
      result.extend(reversed(result[:-1]))
   else:
      result.extend(reversed(result)) 
   return result

