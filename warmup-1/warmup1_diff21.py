#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
  abs_difference = 21 - n

  #answer might be negative so need to get rid of it
  if(abs_difference < 0):
    abs_difference = -1 * abs_difference
  
  if n > 21:
    return 2 * abs_difference
  
  return abs_difference

#alternate solution
def diff21_alternate(n):
  if n <=21:
    return 21 - n
  else:
    return (n - 21) * 2
  
  #takes care of negatives