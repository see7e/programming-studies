import os
prj = QgsProject.instance()
##paths
prj_path = prj.readPath("./")

import os, fnmatch
def find_file(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result[0] # retorna a primeira ocorrencia
file_path = find_file('*.csv', prj_path) # extenção | caminho
print(file_path)

##for ESRI its almost always going to be:
##Lat = Y Long = X

uri = F"file:///{file_path}?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",";", "X", "Y","epsg:31370")

#Make a vector layer
eq_layer=QgsVectorLayer(uri,"eq-data","delimitedtext")

#Check if layer is valid
if not eq_layer.isValid():
    print ("Layer not loaded")

#Add CSV data    
prj.addMapLayer(eq_layer)
