def pigLatin(word):
  if isPigLatin(word):
    result = word + 'ay'
    print(result)
  else:
    new_word = word[1:] + word[0]
    pigLatin(new_word)
    
def isPigLatin(word):
  vowels = ('a', 'e', 'i', 'o', 'u')
  return word[0] in vowels
  
input_word = "python"
pigLatin(input_word) # prints onpythay
