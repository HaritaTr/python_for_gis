from qgis.PyQt.QtCore import QVariant

v1 = QgsVectorLayer("Point", "noktalarim", "memory")
pr = v1.dataProvider()
pr.addAttributes([QgsField("isim", QVariant.String),
                  QgsField("yas", QVariant.Int),
                  QgsField("boy", QVariant.Double)])
v1.updateFields()
QgsProject.instance().addMapLayer(v1)

f = QgsFeature()
f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(32.9, 39.9)))
f.setAttributes(["Erdem", 35, 2.1])
pr.addFeature(f)
v1.updateExtents()
