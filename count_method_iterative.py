def compute(arr, size):
  if not arr:
    return size
  else:
    return compute(arr[1:], size+1)

def count(sequence):
  result = compute(sequence, 0)
  return result
  
array = [i for i in range(1, 101)]
print(count(array))
