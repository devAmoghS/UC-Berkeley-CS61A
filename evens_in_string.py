def evens(sequence):
  result = ""
  # if given sequence is empty, return nothing
  if len(sequence) == 0:
    print("Sequnce is empty")
  else:
    # if the first element of string is even and not a ' '
    if (sequence[0] != " ") and (int(sequence[0])%2 == 0):
      result = result + sequence[0]
      result = result + " "
    evens(sequence[1:])
  print(result)
  
soem_list = "3 4 5 9 1 7 6"
answer = evens(soem_list)
print(answer) # should print "4 6"
