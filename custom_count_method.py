def count(sequence):
  if not sequence:
    return 0
  else:
    return 1+count(sequence[1:])
    
array = [i for i in range(1, 101)]
print(count(array))
