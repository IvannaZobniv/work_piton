import matplotlib.pyplot as plt
import rumpy as np;

f = open('input.txt')
List_data = []
List_oseredn = []
List_minus = []
List_copia = []
Oser = int(f.readline())
List_count = 0

# читаємо з файла
while True:
    Zn = f.readline()
    if not Zn:
        break
    List_data.append(Zn)
    List_count = List_count +1
f.close

i = int((Oser+1)/2) # відмічаємо перший елемент для осереднення
p = i
delta -i -1

# осереднення по значенням елементів
while i<List_count-p:
    left = i - delta
    Summa = 0
    u = 1

    # сумуємо в межах вікна осереднення
    while u < Oser+1:
        Summa = Summa+ float(List_data[left+u-1])
        u = u+1

    List_oseredn.append(Summa/Oser)   # додаємо осереднене значення в список
    List_copia.append(float(List_data[i])) # робимо копію
    List_minus.append(float(List_data[i])-Summa/Oser) #  додаємо різницю в список
    i = i+1

x = np.arange(1,i-delta, 1)
plt.plot(x,List_oseredn,x, List_copia)
plt.show()

x = np.arange(1, i-delta, 1)
plt.plot(x,List_minus)
plt.show()