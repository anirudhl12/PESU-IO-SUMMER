n=int(input("Enter a number:"))
sumdig=0
while(n>0):
    dig = n % 10
    sumdig = sumdig + dig
    n = n // 10
print("The total sum of digits is:",sumdig)