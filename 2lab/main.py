def count(s):
    mass = {}
    for i in s:
        mass[i] = mass.get(i, 0) + 1
    return mass

s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")

mass1 = count(s1)
mass2 = count(s2)

group1 = {}
group2 = {}

for i, j in mass1.items():
    group1.setdefault(j, []).append(i)

for i, j in mass2.items():
    group2.setdefault(j, []).append(i)

mapping = {} 

possible = True  

for mass in group1:
    if mass not in group2:
        
        possible = False
        break

    list1 = group1[mass]
    list2 = group2[mass]

    if len(list1) != len(list2):
        
        possible = False
        break

    list1.sort()
    list2.sort()
    for a, b in zip(list1, list2):
        mapping[a] = b

if not possible:
    print("Невозможно установить однозначное соответствие")
else:
    result = []
    for k in sorted(mapping.keys()):
        result.append(f"{k}={mapping[k]}")
    print(" ".join(result))
