def count_hi(str):
  hi_count = 0
  for i in range(1,len(str)):
    if(str[i-1] + str[i] == 'hi'):
      hi_count += 1
    
  return hi_count
  