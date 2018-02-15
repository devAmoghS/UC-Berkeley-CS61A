# <--Helper functions-->
def double(z):
  return z+z

def half(z):
  return z//2

def isEven(z):
  return (z%2) == 0

# Quick multipy function
def quickMultiply(x,y,result=0):
  if x == 0 or y == 0:
    pass
  elif(isEven(y)):
    result = quickMultiply(double(x), half(y), result)
  else:
    y = y - 1
    result = result + x
    result = quickMultiply(x, y, result)
  return result
	
answer = quickMultiply(10, 30)
print(answer) # prints 300
