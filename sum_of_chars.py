n = input(" Enter your type rang  : ")
count = n.count('ord')
sum_letters =0
for i in range(n):
    letter = input()
    sum_letters += int(ord(letter))
print(sum_letters)
