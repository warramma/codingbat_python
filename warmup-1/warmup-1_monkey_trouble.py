
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
  if(not a_smile and not b_smile) or (a_smile and b_smile):
    return True
  else:
    return False
  
#----alternate solutions

#return((not a_smile and not b_smile) or (a_smile and b_smile))

#return (a_smile == b_smile)
#if they're not equal, then one must be false, therefore, we're not in trouble