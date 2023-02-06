import rumpy as np
import pandas as pd

df = pd.read_table('lab1.txt', names = ['id',])
r=np.linspace(0,1,11)
b=[]
for i in range(0, len(r)-1):
    c = []
    for y in df['id']:
        if y>r[i] and y<r[i+1]:
            c.append(y)
    # print(c)

    b.append(i+1)
    # print(i)

    b.append(r[i])
    # print(r[i])

    b.append(r[i+1])
    # print(r[i+1])

    b.append(np.mean(c))
    # print(np.mean(c))

    b.append(len(c))
    # print(len(c))

with open('new_list_file.txt', 'w') as f:
    for i in b:
        f.write("%s\n" % str(min(df['id'])))
        f.write("%s\n" % str(max(df['id'])))

df.hist(bins=10)

