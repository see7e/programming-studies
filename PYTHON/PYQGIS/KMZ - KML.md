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
## [Styling](https://gis.stackexchange.com/questions/370386/exporting-to-kml-file-with-specifying-some-symbology-icon-styles)
In order to do this, you will have to create an additional field, `OGR_STYLE` to provide the instructions for each feature. See [this answer](#houskas-answer) for how to do this for line colours; for symbols you'll have to use a `SYMBOL(...)` tag instead as documented in the first link above.

The `SYMBOL(...)` tag documentation refers to predefined OGR symbol IDs, and cursorily describes using system-specific symbols with a `.bmp` file as an example. If you're dead-set on using a range of Google symbols, you'll have to explore whether you can pass a URL to a `.png` instead of a local `.bmp` file. Alternatively, you could use one of the predefined OGR symbol IDs and then post-process the `.kml` file to replace that with the symbol you want.

### [Houska's Answer](https://gis.stackexchange.com/questions/297494/styling-kml-through-libkml-layer-creation-options)
Your secret weapon is to create a field in your layer called `OGR_STYLE`. The ogr LIBKML driver then interprets this to style the output `<placemark>`s. The relevant documentation is at [https://www.gdal.org/ogr\_feature\_style.html](https://www.gdal.org/ogr_feature_style.html), [https://www.gdal.org/drv\_libkml.html](https://www.gdal.org/drv_libkml.html), and of course [https://www.gdal.org/ogr2ogr.html](https://www.gdal.org/ogr2ogr.html) for invocation (though it works from Python too).

If `OGR_STYLE` is of the form "@stylename", it will get converted into `<styleUrl>#stylename</styleUrl>` in KML. You can than define the styling for it in KML as you wish.

Alternately, if `OGR_STYLE` uses the language described in the first link above, it is (reasonably) translated into `<lineStyle>`,`<polyStyle>` etc. For instance, for a lineString layer, I just tested (with an export from QGIS desktop, actually) and `OGR_STYLE` set to `PEN(c:#0000ff,w:5px)` turns into

```xml
 <LineStyle>
     <color>ffff0000</color>
     <width>5</width>
 </LineStyle>
```

For polygons, you'll use `BRUSH(fc:...)` for the fill in addition to `PEN(c:...)` for the border.

You don't mention it, but if you are displaying your layer in e.g. QGIS desktop, you might wonder if you can carry over the QGIS displayed styling directly. That styling is not stored in the layer data, so you can't using `ogr2ogr`. With the right settings, you can try to do so if exporting from QGIS or using PyQGIS calls. However, the styling capabilities of different visualization engines (QGIS, Google Earth, etc.) are sufficiently incompatible that this works well only in the simplest of cases. I've found it best to either create the target styling in OGR-style language in the OGR\_STYLE field, or to do it as a named `<styleUrl>` in KML.