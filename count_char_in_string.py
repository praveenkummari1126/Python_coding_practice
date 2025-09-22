#count the frequency of the char in a string

x= "i learn python"
# creating a empty directory
y={}
for i in x:
  if i in y:
    y[i] += 1
  else:
    y[i] = 1
    
for i, x in y.items():
  print(f'{i} is repeated {x} times')

### using get function without using if -else loop

x= "i learn python"
y={}
for i in x:
  y[i]=y.get(i,0)+1
for i, x in y.items():
  print(f'{i} is repeated {x} times')


#### using counter function
from Collections import Counter
x= "i learn python"
count_chars=Counter(x)

for i, x in count_chars.items():
  print(f'{i} is repeated {x} times')



