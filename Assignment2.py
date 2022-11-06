count=2
while count<=100:
  flag=True
  i=2
  while i<=count/2:
    if(count%i==0):
      flag=False
      break
    i=i+1
  if(flag):
    print(count)
  count=count+1
print("Hey Bro done!")
