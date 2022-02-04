#Given an int n, return True if it is within 10 of 100 or 200.

def near_hundred(n):
  if 110 >= n >= 90 :
    return True
  elif 210 >= n>= 190 :
    return True
  else:
    return False
