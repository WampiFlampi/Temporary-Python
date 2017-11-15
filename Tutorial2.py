number = input("Place your number here!")
check = int(number) % 2
number = int(number)
if number == 0:
  print("neither even nor odd")
else:
  if check == 1:
    print("the number is odd")
  else:
    print("the number is even")
