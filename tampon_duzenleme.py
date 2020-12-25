url = "C:/Users/gnser/Desktop/python.zip"
iface.addVectorLayer(url, "points", "ogr")
layer = iface.activeLayer()
result = processing.runAndLoadResults("native:buffer",
    {'INPUT':layer, 'DISTANCE':0.001, 'SEGMENTS':5, 'END_CAP_STYLE':0, 'JOIN_STYLE':0, 'MITER_LIMIT':2, 
    'DISSOLIVE':False, 'OUTPUT':'memory:buffered'})
    
