import math

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

with open('Data1.txt') as f, open('data_out.kml', 'w') as f1:
    AY, AX, BY, BX = [float(f.readline()) for _ in range(4)]
    Mag = [float(line) for line in f if is_float(line)]

    Ts = (max(Mag) + min(Mag)) / 2
    delta = math.sqrt((BX - AX)**2 + (BY - AY)**2) / len(Mag)
    kut = math.atan(BY - AY) / (BX - AX)

    coordinates = ''.join(f"{i * delta * math.cos(kut) - (mag - Ts) * 0.00002 * math.sin(kut) + AX},"
                          f"{i * delta * math.sin(kut) + (mag - Ts) * 0.00002 * math.cos(kut) + AY},0 "
                          for i, mag in enumerate(Mag))

    kml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.2">
  <Document>
    <Placemark>
      <name>Міст Патона</name>
      <description>Графік магнітного поля</description>
      <Style>
        <LineStyle>
          <color>A600FF00</color>
          <width>3</width>
        </LineStyle>
      </Style>
      <LineString>
        <extrude>1</extrude>
        <coordinates>{coordinates}</coordinates>
      </LineString>
    </Placemark>
  </Document>
</kml>
"""

    f1.write(kml_content)

