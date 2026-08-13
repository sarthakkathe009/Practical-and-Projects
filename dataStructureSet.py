numbers={1,2,3,4,3,5}
print(numbers)

chars=set("banana")
print(chars)

empty_set=set()
print(type(empty_set))


ev_set={n**2 for n in range(10) if n%2==0}
print(ev_set)


a = {1,2,3,4}
b = {3,4,5,6}

print("Union:",a | b)
print("Intersection:",a & b)
print("Difference:",a - b)
print("Symmetric Difference:",a ^ b)
print("===============")
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))