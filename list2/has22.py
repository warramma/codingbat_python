def has22(nums):
  if len(nums)>0:
    prev = nums[0] #watch out if list is empty
    
    for num in nums[1::]:
      if prev == num and prev==2:
        return True
      else:
        prev = num
    return False
  else:
    return False