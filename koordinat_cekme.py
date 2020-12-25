# Gis verisinde python ile koordinat çekme

layer = iface.activeLayer()
""" Verinin kaydedilmesini istediğiniz yolu giriniz. 
Örnek* = C:gis/xyz.txt
"""
output_file = open('Örnek*', 'w')
for f in layer.getFeatures():
    geom = f.geometry()
    writeLine = str(f['name']) + ',' + str(geom.asPoint().y()) + ',' + str(geom.asPoint().x()) + ',' + str(geom.asPoint().x()) + '\n'
    output_file.write(writeLine)
output_file.close
