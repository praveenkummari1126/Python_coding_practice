### fetch longest substring(s) without duplicates from a string #########

#example 1: s= "abcbbeadba"
#output=bead 
#example 2:s= "ssgfjjshgsb"
#output=['sgfj', 'jshg']

s=input("enter a string to fetch longest substring(s) without duplicates example abcbbeadba: ")
result=''
#lsit to store results if multiple matches
substrings=[]
max_len=0
#using while loop to remove previous values if any duplicate char occurs and start fetching substring
while len(s)!=0:
  for i in range(1, len(s)):
    #start looking 2nd char to its previus character and so on
    if s[i] not in s[:i]:
      continue
    else:
    #if any duplicate occure we will store upto valid characters and break loop
      result=s[:i]
      break
  if len(result)>max_len:
    max_len=len(result)
    substrings = [result]
  #if same length sustring is present
  elif len(result)==max_len:
  # to avoid duplicates
    if result not in substrings:
      substrings.append(result)
  #remove the previous characters
  s=s[i:]
print("the substring for this string is(are): ", substrings)