# -*- coding: utf-8 -*-

"""
**************************STANDALONE SCRIPT********************************
*                                                                         *
*          Used for side processing for QGIS PROJECT Suit.                *
*                                                                         *
***************************************************************************
"""

############################################
from qgis.core import *
from PyQt5.QtCore import QVariant
import os,sys
import processing
import shutil
import fileinput
import xml.etree.ElementTree as ET
from zipfile import ZipFile
import pandas as pd
import time
from .lib_tools import *
############################################

# QA - DEFINITIONS ################
## Set
def setQALayer(): #
	# Erase the contents of the dpi layer, create it if necessary and add to the project.
	try:
		qalayer = prj.mapLayersByName("QA")[0]
	except IndexError:
		qalayer = QgsVectorLayer('Point?crs=epsg:31370&field=Reason:string(254)', 'QA Issues' ,"memory")
		prj.addMapLayer(qalayer)
		################ adicionar geometria para identificação visual

def setQALayerLn():
	# Erase the contents of the QA layer, create it if necessary and add to the project.
	try:
		qalayerln = prj.mapLayersByName("QA - Linear")[0]
	except IndexError:
		qalayerln = QgsVectorLayer('LineString?crs=epsg:31370&field=reason:string(254)', 'QA Issues Linear' , "memory")
		prj.addMapLayer(qalayerln)
		################ adicionar geometria para identificação visual

## Reset
def resetQALayer(pProcessName): #resetQALayer(None)
	# Erase the contents of the dpi layer, create it if necessary and add to the project.
	try:
		qalayer = prj.mapLayersByName("QA")[0]
	except IndexError:
		qalayer = QgsVectorLayer('Point?crs=epsg:31370&field=Reason:string(254)', 'QA Issues' ,"memory")
		prj.addMapLayer(qalayer)
		################ adicionar geometria para identificação visual

	qalayer.startEditing()
	for ft in qalayer.getFeatures():
		if pProcessName == None or ft.attributes()[0] == pProcessName:
			qalayer.deleteFeature(ft.id())  
	qalayer.commitChanges()

def resetQALayerLn(pProcessName):
	# Erase the contents of the QA layer, create it if necessary and add to the project.
	try:
		qalayerln = prj.mapLayersByName("QA - Linear")[0]
	except IndexError:
		qalayerln = QgsVectorLayer('LineString?crs=epsg:31370&field=reason:string(254)', 'QA Issues Linear' , "memory")
		prj.addMapLayer(qalayerln)
		################ adicionar geometria para identificação visual
		
	qalayerln.startEditing()
	for ft in qalayerln.getFeatures():
		if pProcessName == None or ft.attributes()[0] == pProcessName:
			qalayerln.deleteFeature(ft.id())                
	qalayerln.commitChanges()

## Create Errors
def createErr(feat, errmsg):
	qalayer = prj.mapLayersByName('QA')[0]
	outGeom = QgsFeature()
	outGeom.setGeometry(feat.geometry())
	outGeom.setAttributes([errmsg])
	qalayer.dataProvider().addFeatures([outGeom])

def createErrLn(feat, errmsg):
	qalayerln = prj.mapLayersByName('QA - Linear')[0]
	outGeom = QgsFeature()
	outGeom.setGeometry(feat.geometry())
	outGeom.setAttributes([errmsg])
	qalayerln.dataProvider().addFeatures([outGeom])

def closeQA():
	print('Issues') #rodar um processamento de buffer para cada ponto/linha dentro do lyr de qa

## ( import.py ) FUNÇAO QUE DETECTA SE ALGUMA LABEL NÃO TEM COINCIDENCIA DENTRO DO JOIN
def check_enclosures(source,f_index,idx):    #dp|ab|d-hh / 'field index' / if ab:'Label':'Indentifier'
	#checks if critical fields are filled in
	for f in source.getFeatures():
		if f.attributes()[f.fields().indexFromName(f_index)] == None:
			createErr(f, "Error: No match found for id#{} | {} \n Please verify enclosures tables.".format(f.attributes()[f.fields().indexFromName('ID')], f.attributes()[f.fields().indexFromName(idx)]))

## CHECK GEOMETRIES (decidir se a verificação deve ser feita antes ou depois das cópias)
### ( import.py ) <export - D-Cable>/<export - D-Duct> garantir que nao tenha nenhuma geometria nula
def check_null_length(source,idx):
	#checks the length field if not null
	for fLn in source.getFeatures():
		if fLn.attributes()[fLn.fields().indexFromName(idx)] == None or fLn.attributes()[fLn.fields().indexFromName(idx)] == 0:
			createErrLn(fLn,"Feature (fid #{} | Type {}) tem comprimento igual a NULL.".format(fLn["ID"], fLn["Type"]))

### ( import.py ) <MultiFus> garantir que nao tenha nenhum trecho acima de 600m
def check_multf_length(layer,idx):
	for fLn in layer.getFeatures():
		if fLn.attributes()[fLn.fields().indexFromName(idx)] > 600:
			createErrLn(fLn,"Multifu (fid #{}) tem comprimento acima dos 600m.".format(fLn["ID"]))

### ( LABELINGS ) adiciona a lista de QA os erros de ligação dos elementos quando executado o(s) script(s)
def find_start_end_points(script,layer,idx1,idx2):
	for fLn in layer.getFeatures():
		if fLn.attributes()[fLn.fields().indexFromName(idx1)] == '' or fLn.attributes()[fLn.fields().indexFromName(idx2)] == '':
			createErrLn(fLn,"{} | Não encontrado start or end pont, por favor cheque as conexões da linha (fid #{}).".format(script,fLn["ID"]))

### ( qa_ative.py ) Aerial Boxes
class Check_aerialBoxes():
	def __init__(self) -> None:
		pass
	def check_type(source,target,type):   #source:<lyr>|target:'str'|type:'str'
		x = 0
		for f in source.getFeatures(QgsFeatureRequest().setFilterExpression ('intersecting_geom_count(\'{}\')=0 AND \"aerial_enclosures_Type\"=\'{}\''.format(target,type))):
			x += 1
			if x != 0:
				msg = "Error: Tipo ({}) de equipamento em instalação indevida ( fid #{} | {}).".format(type,f["ID"],f["Label"])
				createErr(f,msg)

	#### <export - Aerial Box> e <Riser> nao podem coincidir
	def check_for_risers(source,target):   #source:<lyr>|target:'str'|type:'str'
		x = 0
		for f in source.getFeatures(QgsFeatureRequest().setFilterExpression (F'intersecting_geom_count(\'{target}\') != 0')):
			x += 1
			if x != 0:
				msg = "Error: Riser posicionado de maneira indevida (sobreposto à {} fid #{}), reposicione ou remova-o.".format(f["Label"],f["ID"])
				createErr(f,msg)

### ( qa_ative.py ) F-Cables()
class Check_fCables():
	def __init__(self) -> None:
		pass
	def max_ft_qtd(source):
		x = 0
		for fLn in source.getFeatures():
			x += 1
			if x > 23:
				msg = F"Error: Máximo de cabos de Feeder atingidos (total atual - {x} und)."
				createErr(fLn,msg)

### ( qa_ative.py ) D-Cables()
class Check_dCables():
	def __init__(self) -> None:
		pass
	#### ( import.py ) verificar se (algum dp foi movido) os <export - D-Cable> nao intersecta com <export - DP>
	def dp_connections(source,target):   #source:<lyr>|target:'str'
		x = 0
		for fLn in source.getFeatures(QgsFeatureRequest().setFilterExpression (F'intersecting_geom_count(\'{target}\')=1 ')):
			x += 1
			if x != 0:
				msg = "Error: Sem conexão entre o Cabo (fid #{}) e o DP.".format(fLn["ID"])
				createErrLn(fLn,msg)

	#### verificar cruzamentos entre o <facade-route> e o <d-cable> que tenha o type != 'Rectractanet 96FO'
	def check_routes(source,target,type):   #source:<lyr>(export - Façade Route)|target:'str'(Cable_others)|type:'str'(Rectractanet 96FO)
		y = 0
		for fLn in source.getFeatures(QgsFeatureRequest().setFilterExpression (F'aggregate(layer:=\'{target}\',aggregate:=\'max\',expression:=\"layer\", \
									 											filter:= overlaps($geometry, geometry(@parent))) = \'{source}\' \
																				AND Type != \'{type}\'')):
			y += 1
			if y != 0:
				msg = "Error: Tipo({}) de cabo em instalação indevida, veriricar encaminhamento aéreo ou em fachada ( fid #{} | {}).".format(type,fLn["ID"],fLn["Label"])
				createErrLn(fLn,msg)

### ( qa_ative.py ) D-Ducts
class Check_dDucts():
	def __init__(self) -> None:
		pass
	#### checar ducts para MDUs (!= 'DB')
	def mdu_ducts(source,target):   #source:<lyr>|target:'str' ('TerminationBox')
		x = 0
		for fLn in source.getFeatures(QgsFeatureRequest().setFilterExpression ('intersecting_geom_count(\'{}\') != 0 AND \"Type\" != \'DB\''.format(target))):
			x += 1
			if x != 0:
				msg = "Error: Tipo({}) de cabo em instalação indevida, veriricar encaminhamento aéreo ou em fachada ( fid #{} | {}).".format(type,fLn["ID"],fLn["Label"])
				createErrLn(fLn,msg)

### ( qa_ative.py ) verificar <TerminationBox>
def check_temBoxes(source,target):   #source:<lyr>|target:'str'('Drops')
	x = 0
	for f in source.getFeatures(QgsFeatureRequest().setFilterExpression (F'(intersecting_geom_count(\'{target}\') > 8 AND \"Spec\" = 1) OR \
																			(intersecting_geom_count(\'{target}\') >= 8 AND intersecting_geom_count(\'{target}\') <= 24 AND \"Spec\" = 4) OR \
																			(intersecting_geom_count(\'{target}\') > 24 AND \"Spec\" = 5) ')):
		x+=1
		if x != 0:
			msg = "Error: Equipamento (fid #{}) com limite de conexões atingidas.".format(f["ID"])
			createErr(f,msg)


#################IMPORT#####################
#modules
#from .qa_control import *
############################################

def qa_ative_module():
    # DEFINITIONS
    start_time = time.time()    #Timer
    try:
        qalayer = prj.mapLayersByName("QA")[0]
        qalayer = prj.mapLayersByName("QA - Linear")[0]
    except IndexError:
        setQALayer()
        setQALayerLn()

    # LAYERS
    layers = prj.mapLayers().values()
    for layer in layers:
        #lyrs
        if layer.name() == "FacadeClosure" and layer.isValid():
            facadeClosure_lyr = layer
        if layer.name() == "TerminationBox" and layer.isValid():
            terminationBox_lyr = layer
	    #export
        if layer.name() == "export - Aerial Box" and layer.isValid():
            export_ab_lyr = layer

    ## CLOSURES
    Check_aerialBoxes.check_type(facadeClosure_lyr,'Paal','OFDC-A4')
    Check_aerialBoxes.check_for_risers(export_ab_lyr,'export - Riser')

    check_temBoxes(terminationBox_lyr,'Drops')
    ## CABLES
    Check_dCables.check_routes(export_fRoute_lyr,'Cable_others','Rectractanet 96FO')
    ## DUCTS
    Check_dDucts.mdu_ducts(dDucts_lyr,'TerminationBox')

    print('========================================')
    print("--- END in %s seconds ---" % (time.time() - start_time))
    print('========================================')