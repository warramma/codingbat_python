def not_string(str):
  if str[0:3] == 'not':
    return str
  return 'not ' + str

#---improved solution:
def not_string_improved(str):
  if len(str) >= 3 and str[:3] == 'not':
    return str
  return 'not ' + str

#accounts for the fact that the length of the string may be less than 3
#makes use of the fact that you don't need to specify the first parameter