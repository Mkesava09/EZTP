t=int(input())
r=0
f=0
if t<0 :
    f=1
    t=-t
while(t!=0):
    k=t%10
    r=r*10+k
    t=t//10
if f==1:
    print(-r)
