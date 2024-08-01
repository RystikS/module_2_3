i=0
number = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while i <= len(number):
  if number[i] > 0:
    print(number[i])
    i=i+1
  else:
    i=i+1
    break
print(number[i])