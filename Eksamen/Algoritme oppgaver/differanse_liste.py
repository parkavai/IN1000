def stor_forskjell(nums):
  differanse = 0
  for tall in nums:
    indeks = 0
    while (indeks < len(nums)):
      forskjell = tall - nums[indeks]
      if(forskjell > differanse):
        differanse = forskjell
      indeks += 1
  return differanse