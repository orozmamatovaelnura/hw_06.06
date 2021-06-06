def func_compare(x,y):
  total=0
  for i in range(10):
    if x[i]==y[i]:
      total+=10
  return total

x , y =input().split()
if x.isalpha and y.isalpha:
  if len(x)==10 and len(y)==10:
    print(func_compare(x,y))
  else:
    print('Inputs are too short or too long !')
else:
  print('Inputs are not strings !')
   
