# -*- coding: utf-8 -*-

"""
**************************STANDALONE SCRIPT********************************
*                                                                         *
*          Used for side processing for QGIS PROJECT Suit.                *
*                                                                         *
***************************************************************************
"""

############################################
import os
import processing
#qgs imports
from qgis.core import *
from PyQt5.QtCore import QVariant #for modifing fields values
from PyQt5.QtWidgets import *
from qgis.gui import *
#from qgis.gui import QgsMapCanvas
from qgis.utils import iface
import os, fnmatch #def find_file(pattern, path)
import time

#DEF
prj = QgsProject.instance()
prjTitle = prj.title()
root = prj.layerTreeRoot()
##paths
prj_path = prj.readPath("./")
############################################

# PROCESSING ################
## UI - ASKING DIALOG
"""expects a title to change Projct Title"""
def titleDialog(t,l,placeholder):   #t:<str>|l:<str>|placeholder:<str>
	qid = QInputDialog()
	title = t                   #"Title"
	label = l                   #"Insert Value: "
	mode = QLineEdit.Normal
	default = placeholder       #"<title>"
	tit, ok = QInputDialog.getText(qid, title, label, mode, default)
	prj.setTitle(tit)
	prjTitle = prj.title()
	return prjTitle

## LAYERS - ADD LYRS IN GROUP(creates new one)
def addLyrstoGrp(new,groupName,layers,lyrs_path):   #new:<T/F>|groupName:<str>|layers:<arry>|lyrs_path:<str>
	if new == True:
		groupName="Name"
		group = root.addGroup(groupName)     #if group don't exists
	else:
		group = root.findGroup(groupName)   #if group exist
	#layers = ["layer_name1","layer_name2","layer_name3","...","layer_name"]

		#defines path to find storaged layers
		#gis.stackexchange.com/questions/290938/adding-layer-to-group-in-layers-panel-using-pyqgis
	for shape_name in layers:
		lyrs_path = lyrs_path + shape_name + ".shp"
		vlayer = QgsVectorLayer(lyrs_path, shape_name,"ogr")
		prj.addMapLayer(vlayer, False)
		group.addLayer(vlayer)
		#print(vlayer.name() + ' added')  #optional
		lyrs_path = prj_path + "/lyrs/"    #resets path

## LAYERS - Copy FUNCTIONS
class CopyFeatures:
	def __init__(self, iface):
		# save reference to the QGIS interface
		self.iface = iface
		
	def copyAll(self,source,target): #src:<lyr>|trg:<lyr>
		source.selectAll()
		self.iface.copySelectionToClipboard(source)

		target.startEditing()
		self.iface.pasteFromClipboard(target)
		target.commitChanges()

	def copyByExp(self,source,target,exp):   #src:<lyr>|trg:<lyr>|exp:'str'
		source.selectByExpression(exp)
		self.iface.copySelectionToClipboard(source)

		target.startEditing()
		self.iface.pasteFromClipboard(target)
		target.commitChanges()

## LAYERS - clearSelection FUNCTION
def ClearSelection():   #void
	canvas = QgsMapCanvas()
	for l in canvas.layers():
		if isinstance(l, QgsMapLayer):
			l.removeSelection()
	canvas.refresh()

## LAYERS - SPATIAL INDEX
def verfySI(layers):
	for layer in layers:
		if (layer.dataProvider().hasSpatialIndex() == 1):
			processing.run("native:createspatialindex", {'INPUT': layer})
		if (layer.dataProvider().hasSpatialIndex() == 2):
			print( F'   >the {layer.name()} has a spatial index' )

## LAYERS - CLEAR ALL
def clear_all():
    export_group = "export"
    temp_group = "_temp"

    group_layer = root.findGroup(export_group)
    group_layer2 = root.findGroup(temp_group)
    root.removeChildNode(group_layer)
    root.removeChildNode(group_layer2)

    # Get all layers in the project
    layers = prj.mapLayers().values()

    time.sleep(5)
    # Loop over each layer and delete all features
    for layer in layers:
        if layer.name() != "aerial_enc" and layer.name()!="dp_enc" and layer.name()!="dhh_enc":
            with edit(layer):
                layer.deleteFeatures(layer.allFeatureIds())

## FILE - FIND IN FOLDER
def find_file(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result[0] # retorna a primeira ocorrencia
file_path = find_file('*.csv', prj_path) # extenção | caminho
print(file_path)