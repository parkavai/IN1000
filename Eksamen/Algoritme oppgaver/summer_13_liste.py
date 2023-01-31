def sum13(nums):
  sum = 0
  indeks = 0
  if(len(nums) == 0):
    return 0
  while(indeks < len(nums)):
    if(nums[indeks] == 13):
      indeks += 2
    else:
      sum += nums[indeks]
      indeks += 1
  return sum