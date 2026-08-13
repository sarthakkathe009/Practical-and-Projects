students = ["Ana", "Ben", "Chia", "Dev"]
marks = [[92,85,87],[81,79],[66,70,72,69],[55]]

def grade(avg: float) -> str:
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

gradebook = {}
for s,m in zip(students, marks):
    avg = sum(m)/len(m)
    gradebook[s] = grade(avg)

print("Gradebook:", gradebook)

tally = {}
for g in gradebook.values():
    tally[g] = tally.get(g, 0) + 1

print("Grade Distribution:", tally)


# Using Dictionary Comprehension
gradebook_comp = {s: grade(sum(m)/len(m)) for s, m in zip(students, marks)}
print("Gradebook (using comprehension):", gradebook_comp)

from collections import Counter
tally_comp = Counter(gradebook_comp.values())
print("Grade Distribution (using Counter):", tally_comp)