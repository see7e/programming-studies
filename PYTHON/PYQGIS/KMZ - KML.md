---
title: KMZ | KML
tags: studies, programação
use: Documentation
languages: python
dependences: QGis
---

# KML
## [Exporting shapefile to KML with set line width using PyQGIS](https://gis.stackexchange.com/questions/346392/exporting-shapefile-to-kml-with-set-line-width-using-pyqgis)
```py
for layer in layers:
name=layer.name()
if "Feeder" in name:
    output_layer = r"(path/to/file)" +  name + ".kml"
    QgsVectorFileWriter.writeAsVectorFormat(layer, output_layer, "utf-8", layer.crs())
```
## Styling
