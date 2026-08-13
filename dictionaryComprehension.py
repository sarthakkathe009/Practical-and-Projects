names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
scores = [88, 92, 85, 90, 95, 88]

report={}
for i in range(len(names)):
    report[names[i]]=scores[i]
print(report)

squares = {n: n**2 for n in range(1,6)}
print(squares)
cubes = {n: n**3 for n in range(1,11) if n % 2 == 0}
print(cubes)

def grade(score):
    return 'PASS'if score >= 40 else 'FAIL'

results = {f"Student{i}": grade(score) for i, score in enumerate([90,85,90,75], start=1)}
print(results)

original = {'IN': 'India', 'US': 'United States', 'UK': 'United Kingdom'}
inverted = {v: k for k, v in original.items()}
print(inverted)