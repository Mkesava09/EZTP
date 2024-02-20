'''for i in range(int(input())):
    t=int(input())
    if(t>98):
        print("yes")
    else:
        print("no") 

n=int(input())
while (n>0):
    t=int(input())
    if(t>98):
        print("yes")
    else:
        print("no")
    n-=1

t=int(input())
for i in range(t):
    n=int(input())
    print(100-n)
    
t=int(input())
for i in range(t):
    n,m,o,p=map(int,input().split())
    if(n-o<m-p):
        print("First")
    elif(n-o == m-p):
        print("Any")
    else:
        print("Second")


t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if n>x :
        print(abs((n-x)//4))
    else:
        print("0")
       ''' 

