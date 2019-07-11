def count_evens(nums):
  """Return the number of even ints in a given array.
  """
  count = 0
  for x in nums:
    if x % 2 == 0:
      print(x)
      count += 1
  return count

print(count_evens([2, 1, 2, 3, 4]))

def big_diff(nums):
  large = 0
  small = 100000
  for x in nums:
    if x > large:
      large = x
  for x in nums:
    if x < small:
      small = x
  return large-small

print(big_diff([10, 3, 5, 7]))

def sum13(nums):
  acc = 0
  if nums == []:
    return 0
  for x in range(len(nums)):
    print(x)
    if nums[x] == 13:
      nums[x] = 0
      try:
        nums[x + 1] = 0
      except:
        acc = 0
  if nums == []:
    return 0
  for x in nums:
    acc += x
  return acc

print(sum13([1, 2, 2, 1, 13, 4]))

def sum67(nums):
  if nums == []:
    return 0
  acc = 0
  state = 1
  for x in range(len(nums)):
    if nums[x] != 6:
      if state == 1:
        acc += nums[x]
      else:
        if nums[x] == 7:
          state = 1
    else:
      state = 0
  return acc

print(sum67([1, 2, 2, 6, 99, 99, 7]))

def has22(nums):
  for x in range(len(nums)):
    if nums[x] == 2:
      try:
        if nums[x + 1] == 2:
          return True
      except:
        return False

print(has22([2, 2]))