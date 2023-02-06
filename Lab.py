with open('lab1.txt') as f:
    massA = []

    for i in f.readlines():
        massA.append(float(i))
mx = max(massA)
mn = min(massA)
difference = mx-mn
kilkidiap = int(input())
krok = difference/kilkidiap
print(max(massA))
print(min(massA))
print(krok)

massB = [[]for i in range(kilkidiap)]

for A in massA:
    for i2 in range(kilkidiap):
        if A >=mn+krok*i2 and A < mn + krok*(i2+1):
            massB[i2].append(A)
massB[kilkidiap-1].append(mx)

with open('output.txt', 'w') as fs:

    for i in range(kilkidiap):
        print("Діапазон №:", i+1,"Початок діапазону:", round(mn+krok*i,9),"Кінекь діапазону:", round(mn+krok*i,9),
              "Середнє значення діапазону:", round(sum(massB[i])/len(massB[i]),9),"Кількість значення що ....:")  # треба дописати рядок
    print("максимальне значення:", max(massA),file=fs)
    print("мінімальне значення:", min(massA), file=fs)
