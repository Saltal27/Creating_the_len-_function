def LEN(string):
  number_of_letters = 0
  for letter in string:
    number_of_letters += 1
  return number_of_letters

print(LEN("Omar"))