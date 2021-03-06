# Write a function called fizzbuzz that does the following:
# If a number is divisible by 3, it should print fizz 
# If a number is divisible by 5, it should print buzz
# If a number is divisible by both 3 and 5, it should print fizzbuzz
# Hint: to check if a number n is divible by number m use the modulo % operator
# e.g 4 % 3 > 0 so not divisible by 3
# e.g 6 % 3 = 0, so yes divisible by 3


# number = int(input('What number would you like?'))

def fizzbuzz(number):
  storage = []
  if number % 3 == 0:
    storage.append('fizz')
  if number % 5 == 0:
    storage.append('buzz')  
  return ("".join(storage))


def init():
  counter = 1
  while counter <= 100:
    number = counter
    print(number , " -> " , fizzbuzz(number))
    counter += 1
    
init()

#fizzbuzz(number)



