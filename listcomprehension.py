list=[1,2,3,4,5,6]
r=[i+1 for i in list]
f=[i+5 for i in list]
n=[i for i in list if i%2==0]
h=[i for i in list if i%2!=0]
print(r,f,n)