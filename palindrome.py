w=["madam","radar","abc"]
r=[i for i in w if i==i[::-1]]
t=[i for i in range(1,6)]
l=[j for j in range(2,6)]
c=[x for x in t if x in l]
print(r)
print("List t:", t)
print("List l:", l)
print("Same elements:",c)
