#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
  if len(str) == 1:
    return str
  first = str[:1] #gets first letter
  last = str[-1:] #gets last letter
  
  return last + str[1:-1] + first
 
 #can use negative number as last index: 1 to -1