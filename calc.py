import re
while True:
    n = int(input("Number of Classes: "))
    if n > 0 and n < 9:
        break
grade = []
g = []
nc = 0
pc = 0
for i in range(n):
    g = str(input(f"Grade {i + 1}: "))
    if len(g) == 1:
        if g[0].upper() == 'A':
            gr = 4
        elif g[0].upper() == 'B':
            gr = 3
        elif g[0].upper() == 'C':
            gr = 2
        elif g[0].upper() == 'D':
            gr = 1
        elif g[0].upper() == 'F':
            gr = 0
        else:
            print("Invalid Grade")
            g = str(input("Grade: "))
    if len(g) == 2:
        if g[0].upper() == 'A':
            gr = 4
        elif g[0].upper() == 'B':
            gr = 3
        elif g[0].upper() == 'C':
            gr = 2
        elif g[0].upper() == 'D':
            gr = 1
        elif g[0].upper() == 'F':
            gr = 0
        else:
            print("Invalid Grade")
            g = str(input("Grade: "))
        if g[1] == '-':
            gr -= 1/3
        elif g[1] == '+':
            gr += 1/3
    g = gr
    grade.append(g)
h = input("Are you in Honors Classes (y/n): ")
h = h.lower()
sg = sum(grade)
if re.search("^y(es)?$", h):
    y = int(input("How many: "))
    if y > n:
        print("Impossible")
    else:
        sg += y
        print(f"Unweighted GPA: {sum(grade) / n}")
        print(f"Weighted GPA: {sg / n}")
if re.search("^no?$", h):
    print(f"GPA: {sum(grade) / n}")
d = input("Do you have a target GPA? (y/n):  ")
d = d.lower()
if re.search("^y(es)?$", d):
    t = float(input("What is your target Unweighted GPA: "))
    if t > 4:
        print("Invalid")
        t = float(input("What is your target Unweighted GPA: "))
    diff = (t * n) - (sum(grade))
    fix = (diff) * 3
    fix = int(fix) + 1
    print(f"You need {fix} positive sign changes(i.e B to B+ or A- to A)")
if re.search("^no?$", d):
    exit