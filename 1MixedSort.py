a=[int(i)for i in input().split()]
a=a[0:len(a)]
s=sorted(a)
mid=len(s)//2
r=s[:mid]+s[len(s):mid-1:-1]
for i in r:
    print(i,end=" ")
print()
