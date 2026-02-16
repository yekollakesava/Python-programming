import random
def generate_binary(length):
  i=0
  result=""
  while i<length:
    result+=random.choice(["1","0"])
    i+=1
  print(result)

length=8
generate_binary(length)