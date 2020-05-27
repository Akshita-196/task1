n=int(input("enter the value:"))
s=0
i=0
j=1
count=0
print("Fibonacci series:",end=" ")
while count< n:
    count +=1
    print(s, end=" ")
    i=j
    j=s
    s=i+j
