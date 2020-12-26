layer = iface.activeLayer()

#layer.renderer().symbol().setSize(6)
#layer.triggerRepaint()

#layer.renderer().symbol().setColor(QColor("blue"))
#layer.triggerRepaint()

layer.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
layer.triggerRepaint()
