#Given a string, return a new string where the first and last chars have been
#exchanged.

#HAD TO LOOK AT THE SOLUTION FOR THIS ONE

def front_back(str):
  if len(str) <= 1 :
    return str
  n = str[1:-1]
  return str[len(str)-1] + n + str[0]
