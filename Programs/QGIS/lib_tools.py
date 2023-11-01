# -*- coding: utf-8 -*-

"""
************************* STANDALONE SCRIPT *******************************
*                                                                         *
*                      Used for side processing                           *
*                                                                         *
***************************************************************************
"""
############################################
import re
import time
import shutil
import os,sys
import fnmatch	# FIND_FILE IN FOLDER
import openpyxl	# import enclosures (xlsx) tables
import fileinput
import processing
import pandas as pd
#from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

#qgs imports
from qgis.core import (
	QgsField,
	QgsFields,
	QgsProject,
	QgsFeature,
	QgsPointXY,
	QgsWkbTypes,
	QgsMapLayer,
	QgsGeometry,
	QgsExpression,
	QgsProcessing,
	QgsVectorLayer,
	QgsFeatureRequest,
	QgsVectorFileWriter,
	QgsExpressionContext,
	QgsVectorLayerJoinInfo,
	QgsExpressionContextUtils,
	QgsExpressionContextScope,
	QgsCoordinateReferenceSystem
)
from qgis.gui import QgsMapCanvas
from qgis.utils import iface

#PyQt
from PyQt5.QtCore import QVariant #for modifing fields values
from PyQt5.QtWidgets import (
	QInputDialog,
	QLineEdit
)

############################################

# DEF
PRJ = QgsProject.instance()
ROOT = PRJ.layerTreeRoot()
# set directories structure
PRJ_PATH = PRJ.readPath("./")
QGS_LYRS_PATH = F"{PRJ_PATH}/shp"

############################################

# PROCESSING ################
## UI - ASKING DIALOGS
def titleDialog(title:str,label:str,placeholder:str):
	""" Dialog box to ask for the title of the project file
	:param t: title of the dialog box
	:param l: label of the dialog box
	:param placeholder: placeholder of the dialog box
	Return type: str
	Usage: TITLE = titleDialog("Title","Insert Value: ","ProjectTitle")
	"""
	qid = QInputDialog()
	mode = QLineEdit.Normal
	tit, ok = QInputDialog.getText(qid, title, label, mode, placeholder)
	PRJ.setTitle(tit)
	prjTitle = PRJ.title()
	return prjTitle


def custom_variable_dialog(title:str,label:str,placeholder:str):
	""" Dialog box to ask for a custom project variable. Pops if not existis
	(with ``placeholder`` as variable name)
	:param t: title of the dialog box
	:param l: label of the dialog box
	:param placeholder: placeholder of the dialog box, must equals the var name
	Return type: str
	Usage: CUSTOM_VAR = custom_variable_dialog("Title","Insert Value: ","VAR_01")
	"""
	qid = QInputDialog()
	mode = QLineEdit.Normal
	if not QgsExpressionContextUtils.projectScope(PRJ).variable(placeholder):
		variable, ok = QInputDialog.getText(qid, title, label, mode, placeholder)
		return variable
	else:
		return QgsExpressionContextUtils.projectScope(PRJ).variable(placeholder)


## FIND_FILE IN FOLDER
class PathFinder:
	def __init_(self):
		pass


	#import fnmatch
	def find_file(self, pattern, path, i):
		count = 0  # Counter for matching files
		for root, dirs, files in os.walk(path):
			for name in files:
				if fnmatch.fnmatch(name, pattern):
					if count == i:
						return os.path.join(root, name)
					count += 1
		return None  # No matching file found or invalid index


#  LAYERS ######################################################################
## LAYERS - ADDLAYERS CLASS
class AddLayers():
	def __init__(self):
		pass


	def addGroup(self, group_name:str):
		'''Slight variation of root.addGroup()'''
		group = ROOT.findGroup(group_name) if not ROOT.findGroup(group_name) == None else ROOT.addGroup(group_name)
		#print(group)	#debug
		return group
	

	def add_shp_to_group(self, group_name:str, lyr=None, lyr_name=None, lyr_path=None):
		'''Add layers once at a time'''
		group = self.addGroup(group_name)
		
		vlayer = lyr if lyr is not None else QgsVectorLayer(lyr_path, lyr_name, "ogr")

		if vlayer.isValid():
			if group_name:  # Check if the groupName is provided (not None).
				PRJ.addMapLayer(vlayer, False)
				group.addLayer(vlayer)
				print(F"	{vlayer.name()} added to {group_name} group.")  # Debug message.
			else:
				PRJ.addMapLayer(vlayer)  # Assuming you want to add the layer directly to the project.
				print(F"	{vlayer.name()} added.")  # Debug message.
		else:
			print(F"	Invalid layer: {lyr_name} or {lyr_path}")  # Debug message for invalid layers.


	def add_shps_to_group(self, lyrs_path:str, vlyr_map:list, group_name:str):
		'''Add layers in loop'''
		#https://gis.stackexchange.com/questions/290938/adding-layer-to-group-in-layers-panel-using-pyqgis
		loop_path = lyrs_path
		group = self.addGroup(group_name)

		for shape in vlyr_map:
			try:
				loop_path = loop_path + shape + ".shp" # ERSI Shapefile
			except:
				loop_path = loop_path + shape + ".gpkg" # GeoPackage
			vlayer = QgsVectorLayer(loop_path, shape,"ogr")
			if vlayer.isValid() and group_name is not None:
				#print(vlayer) #debug
				PRJ.addMapLayer(vlayer, False)
				group.addLayer(vlayer)
				print(F"	{vlayer.name()} added to {group_name} group.")	#debug
			elif vlayer.isValid():
				PRJ.addMapLayer(vlayer)
				print(F"	{vlayer.name()} added.")	#debug
			loop_path = lyrs_path    #reset path


	def clean_attribute_name(self, name):
		'''Function to clean up attribute names'''
		return name.strip().replace(';', '_').replace(' ', '_')


	# NOT READY YET
	#def shp_from_csv(self, csv_file_path, layer_name, group_name):
	#	'''Create a shapefile from a xlsx file'''
	#	# Verify group existance
	#	group = self.addGroup(group_name)
	#	# Read the data from the CSV file using pandas
	#	df = pd.read_csv(csv_file_path)
	#	# Create an empty noGeometry layer with the desired attributes
	#	tlayer = QgsVectorLayer('None?name=' + layer_name, 'memory')
	#	PRJ.addMapLayer(tlayer, False)
	#	group.addLayer(tlayer)
	#	
	#	# Add attributes to the layer
	#	provider = tlayer.dataProvider()
	#	fields = [QgsField(self.clean_attribute_name(attr), QVariant.String) for attr in df.columns]
	#	provider.addAttributes(fields)
	#	tlayer.updateFields()
	#	# Add features with no geometry to the memory layer using the data from the DataFrame
	#	for index, row in df.iterrows():
	#		feature = QgsFeature()
	#		for attr in df.columns:
	#			feature.setAttribute(self.clean_attribute_name(attr), row[attr])
	#		# Add the feature to the layer (no geometry is set for each feature)
	#		tlayer.addFeature(feature)
	#	# Return the added layer
	#	return tlayer  # Return the newly created layer """


## LAYERS - Manipulations
### Copy FUNCTIONS
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


### JOIN LYRS
def join_lyrs(source_lyr, target_lyr, source_field:str, target_field:str, fields:list=None):
	""" Join layers by field
	:param source_lyr: source layer
	:param target_lyr: target layer
	:param source_field: source field
	:param target_field: target field
	:param fields: fields to be joined
	Return type: None
	"""
	joinObject = QgsVectorLayerJoinInfo()

	joinObject.setJoinFieldName(source_field) #csvField
	joinObject.setTargetFieldName(target_field) #shpField
	joinObject.setJoinLayerId(source_lyr.id()) #aerial_enclosures_lyr
	joinObject.setUsingMemoryCache(True)
	joinObject.setJoinFieldNamesSubset(fields) if fields else None #['field1', 'field2']
	joinObject.setJoinLayer(source_lyr) #aerial_enclosures_lyr
	target_lyr.addJoin(joinObject) #export_ab_lyr


### UPDATE VALUES
def update_values(layer, field, filter='"ID"', value=None, func=None):
	""" Update values in a layer
	:param layer: layer to be updated
	:param field: field to be updated
	:param filter: filter to be applied
	:param value: value to be set
	:param func: function to be applied
	Return type: None
	Usage: update_values(layer, field, filter='"ID"', value=None, func=None)
	"""
	try:
		idxEdgeId = layer.fields().lookupField(field)
	except:
		print(f'lookupField({field}) doesn\'t exists')
		raise IndexError
	if value is None and func is None:
		print('No value or function provided')
		raise ValueError	
	layer.startEditing()
	for f in layer.getFeatures(filter):
		value = func(f) if func is not None else value
		layer.changeAttributeValues(f.id(), {idxEdgeId: value})
	layer.commitChanges()


### clearSelection
def ClearSelection():   #void
	canvas = QgsMapCanvas()
	for l in canvas.layers():
		if isinstance(l, QgsMapLayer):
			l.removeSelection()
	canvas.refresh()


### SPATIAL INDEX
def verify_spatial_index(layers):
	""" Verify if layers has a spatial index
	:param layers: list of layers
	Return type: None
	Usage: verify_spatial_index(layers)
	"""
	for layer in layers:
		if (layer.dataProvider().hasSpatialIndex() == 1):
			processing.run("native:createspatialindex", {'INPUT': layer})
		#if (layer.dataProvider().hasSpatialIndex() == 2):
		#	print(F"	the {layer.name()} has a spatial index")


#  FILES #######################################################################
## FILES - OUTPUT FILE (.txt/.csv)
#to_review
def layer_to_file(layer, output_path:str, indexes:list):
	# open the output file
	with open(output_path, 'w') as file:
		# get the fields in the layer
		fields = layer.fields()

		# if indexes has more than one element, join them with commas
		index = ';'.join(indexes)
		head = [field.name() for field in fields if field.name() == index]
		file.write("\t".join(head) + "\n")

		# get the features in the layer and write the attribute values for each feature
		# follow the same order of the fields as above
		for idx in indexes:
			for feature in layer.getFeatures():
				values = [str(feature[field.name()]) for field in fields if field.name() == idx]
				file.write("\t".join(values) + "\n")
