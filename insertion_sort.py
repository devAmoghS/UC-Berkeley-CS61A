def insertionSort(array):
  if len(array) <= 1:
    return array
  else:
    return insertOne(array[0], insertionSort(array[1:]))
  
def insertOne(key, arr):
  if len(arr) == 0:
    return [key]
  else:
    if key < arr[0]:
      return [key] + arr
    else:
      return arr[0:1] + insertOne(key, arr[1:])
  
seq = [7,5,2,1,6,9]
answer = insertionSort(seq)
print(answer) # prints [1, 2, 5, 6, 7, 9]
