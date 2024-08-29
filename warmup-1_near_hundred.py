#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

def near_hundred(n):
  within100 = abs(100-n)
  within200 = abs(200-n)
  return (within100 <= 10 or within200 <=10)