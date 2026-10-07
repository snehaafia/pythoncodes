ch = input("enter a character: ")

if ch.islower():
    print("small letter")
elif ch.isupper():
    print("capital letter")
elif ch.isdigit():
    print("digit")
else:
    print("punctuation")

    
#exercise2
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a > b and a > c:
    print("largest:", a)
elif b > a and b > c:
    print("largest:", b)
else:
    print("largest:", c)




#exercise3
n = int(input("enter N: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("sum =", sum)


#exercise4

n = input("enter a number: ")

if n == n[::-1]:
    print("palindrome")
else :
    print("not palindrome")


