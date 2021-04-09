char1 = input("Letter 1 ")
char2 = input("Letter 2 ")
c = ord(char1)
d = ord(char2)
s = ""
for x in range(c+1,d):
  s += chr(x) + " " 
 
print(s)
