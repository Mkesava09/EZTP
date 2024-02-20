'''def suma(a,b):
    print(a+b)
a,b=map(int,input().split())
suma(a,b)

def exp(x):
    x[1]=100
l=[10,20,30,40,50]
exp(l)
l[1]=111
print(l)

def profit(x):
    if x==0 :
        return
    else:
        x=int((x*50)-(0.7)*(x*50))
    print(x)
t=int(input())
def a(r):
    

def time(r,r1):
    print(int(r-(r1)/2))
t,t1=map(int,input().split())
time(t,t1)

t=int(input())
for i in range(t):
    n=int(input())
    c=0
    while(n>0):
        k=n%10
        if(k==4):
            c=c+1
        n=n//10
    print(c)

def fou(x):
    c=0
    while(x>0):
        k=x%10
        if(k==4):
            c+=1
        x=x//10
    print(c)
def tet(n):
    if(n>0):
        t=int(input())
        fou(t)
        tet(n-1)
    else:
        return

n=int(input())
tet(n)
'''
n=int(input())
n=n*10+3
l=n
r=0
while(l!=0):
    k=l%10
    r=r*10+k
    l=l//10
    #print(r)
r=r*10+3
t=r
m=0
while(t!=0):
    j=t%10
    m=m*10+j
    t=t//10
print(m)
        