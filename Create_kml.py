import math
import numpy as np
f = open('Data1.txt')
f1 = open('data_out.kml', 'w')
Mag = []
List_count = 0

# читаємо дані координат з файла
AY = f.readline()
AX = f.readline()
BY = f.readline()
BX = f.readline()
Zn = f.readline()

# читаємо значення магнітного поля
while True:
    Zn = f.readline()
    if not Zn:
        break
    List_count = List_count + 1
    Mag.append(float(Zn))

Tmax = max(Mag)
Tmin = min(Mag)
Ts = Tmin+ (Tmax-Tmin)/2

deltaX = float(BX)-float(AX)
deltaY = float(BY)-float(AY)
delta = math.sqrt(deltaX*deltaX+deltaY*deltaY)/List_count
kut = math.atan(float(BY)-float(AY))/(float(BX)-float(AX))

# формуємо вихідний файл
f1.write('<?xml version="1.0 encoding="UTF-8"?>' + '\n')
f1.write('<kml xmlns= "http://earth.google.com/kml/2.2" >' + '\n')
f1.write('  <Document>' + '\n')
f1.write('    <Placemark>' + '\n')
f1.write('      <name>Міст Патона</name>' + '\n')
f1.write('      <description>Графік магнітного поля</description>' + '\n')
f1.write('      <Style>' + '\n')
f1.write('        <LineStyle>' + '\n')
f1.write('          <color>A600FF00</color>' + '\n')
f1.write('          <width>3</width>' + '\n')
f1.write('        </LineStyle>' + '\n')
f1.write('      </Style>' + '\n')
f1.write('      <LineString>' + '\n')
f1.write('        <extrude>1</extrude>' + '\n')
s ='       <coordinates>'
i = 0
while i <List_count:
    s = s + str(i*delta*math.cos(kut) - (Mag[i]-Ts)*0.00002*math.sin(kut)+float(AX)) + ','
    s = s + str(i * delta * math.sin(kut) + (Mag[i] - Ts) * 0.00002 * math.cos(kut) + float(AY)) + ',0 '
    i = i+1
s=s + '</coordinates>' + '\n'
f1.write(s)
f1.write('      </LineString>' + '\n')
f1.write('    </Placemark>' + '\n')
f1.write('  </Document>' + '\n')
f1.write('</kml>' + '\n')


# f1.write('
f.close()
f1.close()