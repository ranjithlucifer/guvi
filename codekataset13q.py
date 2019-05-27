n=input()
if (n>='a' and n<='z') or (n>='A' and n<='B'): 
  if n=='a' or n=='e' or n=='i' or n=='o' or n=='u': print("Vowel")
  else: print("Consonant")
elif n>='0' and n<='9': print("Digit")
else: print("Invalid")
