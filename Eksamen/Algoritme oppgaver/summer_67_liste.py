def sum67(nums):
  indeks = 0
  sjekk = 0
  sum = 0
  if(len(nums) == 0):
    return 0
  while(indeks < len(nums)):
    if(nums[indeks] == 6):
      sjekk = indeks
      while(nums[sjekk] != 7):
        sum += 0
        sjekk += 1
      indeks = sjekk
    else:
      sum += nums[indeks]
    indeks += 1
  return sum