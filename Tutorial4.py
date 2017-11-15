num = input("Pick a Number to easily get its divisors")
zero=0
one=1
negnum=int(zero)-int(num)
numtbl=range(int(negnum), int(num))
for elem in numtbl:
  add=int(num)%elem
  if elem==0:
    print(elem)
  print(numtbl)
