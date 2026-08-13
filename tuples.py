x = ("Glenn", "Sally", "Joseph")
print(x[2])

y = (1, 9, 2)
print(y)
print("Max:", max(y))

t = tuple()
print("Functions used with tuples:", dir(t))

(s,t) = (5, 10)
print("s:", s)
print("t:", t)

#Tuple Operations
d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

print((0,1,2) < (5,1,2))


c = {'a':10,'c':22,'b':10}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp,reverse=True)
print(tmp)

#Using Comprehension
c = {'a':10 , 'c':22 , 'b':1}
print(sorted([(v,k) for k,v in c.items()]))