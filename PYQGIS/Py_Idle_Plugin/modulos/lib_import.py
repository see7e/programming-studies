# -*- coding: utf-8 -*-

"""
**************************STANDALONE SCRIPT********************************
*                                                                         *
*          Used for side processing for QGIS PROJECT Suit.                *
*                                                                         *
***************************************************************************
"""

############################################
import os,sys
from qgis.core import *
from PyQt5.QtCore import QVariant
from qgis.utils import iface
import processing
import time
#modules
from .lib_tools import *
#create instance
copyFeatures = CopyFeatures(iface)
from .lib_qa import *
############################################

def imp_all():

	#0.0 DEFINITIONS
	start_time = time.time()    #Timer
	prjTitle = prj.title()
	try:
		qalayer = prj.mapLayersByName("QA")[0]
		qalayer = prj.mapLayersByName("QA - Linear")[0]
	except IndexError:
		setQALayer()
		setQALayerLn()

	progression = 0 #index management

	#0.1 set directories structure
	prj_path = prj.readPath("./")
	qgis_layers_path = prj_path + "/shp_base"
	export_layers_path = prj_path + "/shp_exp/"
	_temp_path = prj_path+"/_temp/"

	#0.2 Set QA
	try:
		qalayer = prj.mapLayersByName("QA")[0]
		qalayer = prj.mapLayersByName("QA - Linear")[0]
	except IndexError:
		setQALayer()
		setQALayerLn()

	# 1.0 LAYERS MANAGEMENT
	## 1.1 EXPORTED SHAPES TO "export" GROUP
	print('> Imports')
	if progression == 0:
		groupName="export"
		group = root.addGroup(groupName)

		vlyrMap = ["A-Cable", "A-Duct", "A-Subduct", "A-Box",
					"Ar-Duct", "Ar-Route", "BE","CO", "AP", "D-Cable",
					"D-Duct", "HLDDuct","D-HH", "DP", "Drop Cable",
					"Fc-Route","HP", "F-Cable", "Pole",
					"Rs", "T-Box", "BK"]

		#1.1.1 #https://gis.stackexchange.com/questions/290938/adding-layer-to-group-in-layers-panel-using-pyqgis
		for shape in vlyrMap:
			export_layers_path = export_layers_path + shape + ".shp"
			vlayer = QgsVectorLayer(export_layers_path, shape,"ogr")
			prj.addMapLayer(vlayer, False)
			group.addLayer(vlayer)
			
			#print(vlayer.name() + ' added')  #debug
			export_layers_path = prj_path + "/shp_exp/"    #reset path
		
		progression += 1 #jump
	else:
		#progression = progression + 1 #jump
		print('[i1.1] - Import shp skipped')

	## 1.2 DEFINE LAYERS IN PROJECT
	print('> Layers Management')
		#set the layers variable = a list of all the layer objects open in the QGIS interface
	if progression == 1:
		#lyrs
		co_lyr = prj.mapLayersByName('CO')[0]
		dp_lyr = prj.mapLayersByName('DP')[0]
		dhh_lyr = prj.mapLayersByName('DHH')[0]
		Rs_lyr = prj.mapLayersByName('Rs')[0]
		poleCl_lyr = prj.mapLayersByName('Pole-Cl')[0]
		fcCl_lyr = prj.mapLayersByName('Fc-Cl')[0]
		terminationBox_lyr = prj.mapLayersByName('T-Box')[0]
		drops_lyr = prj.mapLayersByName('Drops')[0]
		dCables_lyr = prj.mapLayersByName('D-Cable')[0]
		feedCable_lyr = prj.mapLayersByName('F-Cable')[0]
		multFus_lyr = prj.mapLayersByName('MultiFus')[0]
		dDucts_lyr = prj.mapLayersByName('D-Ducts')[0]
		be_lyr = prj.mapLayersByName('BE')[0]
		pole_lyr = prj.mapLayersByName('Pole')[0]
		hp_lyr = prj.mapLayersByName('HPs')[0]
		bk_lyr = prj.mapLayersByName('BK')[0]
		#csv
		a_enc_lyr = prj.mapLayersByName('a_enc')[0]
		dp_enc_lyr = prj.mapLayersByName('dp_enc')[0]
		dhh_enc_lyr = prj.mapLayersByName('dhh_enc')[0]

		layers = prj.mapLayers().values()
		valid_exp_lrys = []
		for layer in layers:
			#print(layer.name()) #debug
			#export
			if layer.name() == "CO" and layer.isValid():
				export_co_lyr = layer
				valid_exp_lrys.append(export_co_lyr)
			if layer.name() == "AP" and layer.isValid():
				export_ap_lyr = layer
				valid_exp_lrys.append(export_ap_lyr)
			if layer.name() == "DP" and layer.isValid():
				export_dp_lyr = layer
				valid_exp_lrys.append(export_dp_lyr)
			if layer.name() == "D-HH" and layer.isValid():
				export_dhh_lyr = layer
				valid_exp_lrys.append(export_dhh_lyr)
			if layer.name() == "Rs" and layer.isValid():
				export_Rs_lyr = layer
				valid_exp_lrys.append(export_Rs_lyr)
			if layer.name() == "A-Box" and layer.isValid():
				export_ab_lyr = layer
				valid_exp_lrys.append(export_ab_lyr)
			if layer.name() == "T-Box" and layer.isValid():
				export_terminationBox_lyr = layer
				valid_exp_lrys.append(export_terminationBox_lyr)
			if layer.name() == "A-Cable" and layer.isValid():
				export_aCable_lyr = layer
				valid_exp_lrys.append(export_aCable_lyr)
			if layer.name() == "A-Duct" and layer.isValid():
				export_aDuct_lyr = layer
				valid_exp_lrys.append(export_aDuct_lyr)
			if layer.name() == "A-Subduct" and layer.isValid():
				export_aSubDuct_lyr = layer
				valid_exp_lrys.append(export_aSubDuct_lyr)
			if layer.name() == "D-Cable" and layer.isValid():
				export_dCables_lyr = layer
				valid_exp_lrys.append(export_dCables_lyr)
			if layer.name() == "F-Cable" and layer.isValid():
				export_fCable_lyr = layer
				valid_exp_lrys.append(export_fCable_lyr)
			if layer.name() == "Ar-Route" and layer.isValid():
				export_aRoute_lyr = layer
				valid_exp_lrys.append(export_aRoute_lyr)
			if layer.name() == "Fc-Route" and layer.isValid():
				export_fRoute_lyr = layer
				valid_exp_lrys.append(export_fRoute_lyr)
			if layer.name() == "D-Duct" and layer.isValid():
				export_dDucts_lyr = layer
				valid_exp_lrys.append(export_dDucts_lyr)
			if layer.name() == "BE" and layer.isValid():
				export_be_lyr = layer
				valid_exp_lrys.append(export_be_lyr)
			if layer.name() == "Pole" and layer.isValid():
				export_Pole_lyr = layer
				valid_exp_lrys.append(export_Pole_lyr)
			if layer.name() == "HP" and layer.isValid():
				export_hp_lyr = layer
				valid_exp_lrys.append(export_hp_lyr)

			if layer.name() == "BK" and layer.isValid():
				export_bk_lyr = layer
				valid_exp_lrys.append(export_bk_lyr)

		verfySI(layers)
		p_list = []
		filter = ["DP","Rs","A-Box","T-Box","CO","AP","D-HH","BE","HP","BK"]
		for i in valid_exp_lrys:
			for p in filter:
				if i.name() == p:
					p_list.append(i)
		#print(p_list)

		l_list = []
		filter = ["A-Cable", "Ar-Route", "Fc-Route","A-Duct", "A-Subduct", "F-Cable","D-Duct"]
		for i in valid_exp_lrys:
			for l in filter:
				if i.name() == l:
					l_list.append(i)
		#print(l_list)
		progression += 1 #jump
	else:
		#progression = progression + 1 #jump
		print('[i1.2] - Layers Defnition skipped')

	## 1.3 FIX GEOMETRIES
	print('> Fix Geometries')
	if progression == 2:
		_temp_groupName="_temp"
		_tempGroup = root.addGroup(_temp_groupName)

		#processing calfunctions
		#JUNTA TODOS OS PONTOS
		ALL_PT = processing.run("native:mergevectorlayers",
		{'LAYERS':p_list,
		'CRS':QgsCoordinateReferenceSystem('EPSG:31370'),
		'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT})
		
		SNAP_PONTOS = processing.run('native:snapgeometries', {
			'BEHAVIOR': 2,  # Prefer aligning nodes, don't insert new vertices
			'INPUT': ALL_PT['OUTPUT'],
			'REFERENCE_LAYER': export_Pole_lyr,
			'TOLERANCE': 0.15,
			#'OUTPUT': parameters['Snapped_aerialboxes']
			'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
		})

		#ATUALIZA O CAMPO ID
		ALL_PT = processing.run("native:fieldcalculator", 
		{'INPUT':SNAP_PONTOS['OUTPUT'],
		'FIELD_NAME':'ID',
		'FIELD_TYPE':2,
		'FIELD_LENGTH':250,
		'FIELD_PRECISION':0,
		'FORMULA':"$ID",
		'OUTPUT':_temp_path+'Points_Final.shp'
		})
		vlayer = QgsVectorLayer(_temp_path+'Points_Final.shp', 'Points_Final', "ogr")
		prj.addMapLayer(vlayer, False)
		_tempGroup.addLayer(vlayer)

		for i in valid_exp_lrys:
			if i.name() == "D-Cable":
				#FIX AS (dist) CABLES AOS ALL_PT
				DIST_CABLES = processing.run("native:fixgeometries", 
				{'INPUT':export_dCables_lyr,
				'OUTPUT':QgsProcessing.TEMPORARY_OUTPUT})

				#ATRAI AS (dist) CABLES AOS ALL_PT
				DIST_CABLES = processing.run("native:snapgeometries", 
				{'INPUT':DIST_CABLES['OUTPUT'],
				'REFERENCE_LAYER':ALL_PT['OUTPUT'],
				'TOLERANCE':0.2,
				'BEHAVIOR':0,
				'OUTPUT':QgsProcessing.TEMPORARY_OUTPUT})

				#CAMPOS DE ORIGEM E DESTINO
				DIST_CABLES = processing.run("native:fieldcalculator", 
				{'INPUT':DIST_CABLES['OUTPUT'],
				'FIELD_NAME':'ORIGEM',
				'FIELD_TYPE':2,
				'FIELD_LENGTH':250,
				'FIELD_PRECISION':0,
				'FORMULA':"aggregate(\r\nlayer:= 'Points_Final',\r\naggregate:='concatenate',\r\nexpression:= to_string(ID),\r\nconcatenator:=',',\r\nfilter:=intersects($geometry, start_point(geometry(@parent))))\r\n",'OUTPUT':'TEMPORARY_OUTPUT'})

				DIST_CABLES = processing.run("native:fieldcalculator", 
				{'INPUT':DIST_CABLES['OUTPUT'],
				'FIELD_NAME':'DESTINO',
				'FIELD_TYPE':2,
				'FIELD_LENGTH':250,
				'FIELD_PRECISION':0,
				'FORMULA':"aggregate(\r\nlayer:= 'Points_Final',\r\naggregate:='concatenate',\r\nexpression:= to_string(ID),\r\nconcatenator:=',',\r\nfilter:=intersects($geometry, end_point(geometry(@parent))))\r\n",'OUTPUT':'TEMPORARY_OUTPUT'})

				DIST_CABLES = processing.run("native:addfieldtoattributestable", 
				{'INPUT':DIST_CABLES['OUTPUT'],
				'FIELD_NAME':'Label',
				'FIELD_TYPE':2,
				'FIELD_LENGTH':150,
				'FIELD_PRECISION':0,
				'OUTPUT':_temp_path+'Cable_Dist.shp'
				})
				vlayer = QgsVectorLayer(_temp_path+'Cable_Dist.shp', 'Cable_Dist', "ogr")
				prj.addMapLayer(vlayer, False)
				_tempGroup.addLayer(vlayer)

		#ADICIONA (others) CABLES AOS ALL_PT
		OTHR_CABLES = processing.run("native:mergevectorlayers", 
		{'LAYERS':l_list,
		'CRS':QgsCoordinateReferenceSystem('EPSG:31370'),
		'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT})

		OTHR_CABLES = processing.run("native:fixgeometries", 
		{'INPUT':OTHR_CABLES['OUTPUT'],
		'OUTPUT':QgsProcessing.TEMPORARY_OUTPUT})

		OTHR_CABLES = processing.run("native:snapgeometries", 
		{'INPUT':OTHR_CABLES['OUTPUT'],
		'REFERENCE_LAYER':ALL_PT['OUTPUT'],
		'TOLERANCE':0.2,
		'BEHAVIOR':0,
		'OUTPUT':_temp_path+'Cable_others.shp'
		})
		vlayer = QgsVectorLayer(_temp_path+'Cable_others.shp', 'Cable_others', "ogr")
		prj.addMapLayer(vlayer, False)
		_tempGroup.addLayer(vlayer)

		_temp_othrCable_lyr = prj.mapLayersByName('Cable_others')[0]
		_temp_othrCable_lyr.setProviderEncoding(u'UTF-8')
		_temp_othrCable_lyr.dataProvider().setEncoding(u'UTF-8')
		check_null_length(_temp_othrCable_lyr,'GeoLength')

		_temp_points_lyr = prj.mapLayersByName('Points_Final')[0]
		try:
			_temp_distCable_lyr = prj.mapLayersByName('Cable_Dist')[0]
			_temp_distCable_lyr.setProviderEncoding(u'UTF-8')
			_temp_distCable_lyr.dataProvider().setEncoding(u'UTF-8')
			check_null_length(_temp_distCable_lyr,'GeoLength')
			Check_dCables.dp_connections(_temp_distCable_lyr,'Points_Final')
		except:
			print('     [ERROR] Missing d-Cables')
		progression += 1 #jump
	else:
		#progression = progression + 1 #jump
		print('[i1.3] - Fix Geometries skipped')

	## 1.4 CREATE JOIN IN LAYER
	print('> Join Layers')
		#gis.stackexchange.com/questions/133573/joining-table-field-with-shapefile-using-pyqgis
		#gis.stackexchange.com/questions/267732/joining-layers-with-pyqgis-3
	if progression == 3:

		### 1.4.1 remove info in origin lyrs
		toRemove = [export_ab_lyr, export_dp_lyr, export_dhh_lyr]
		for f_lyr in toRemove:
			for f in f_lyr.getFeatures():
				f_lyr.startEditing()
				f_lyr.deleteFeature(f.id())

		### 1.4.2 GET INFO
		#ab
		copyFeatures.copyByExp(_temp_points_lyr,export_ab_lyr,'\"layer\"= \'A-Box\'')
		#ClearSelection()

		#DP
		copyFeatures.copyByExp(_temp_points_lyr,export_dp_lyr,'\"layer\"= \'DP\'')
		#ClearSelection()
		
		#D-HH
		copyFeatures.copyByExp(_temp_points_lyr,export_dhh_lyr,'\"layer\"= \'D-HH\'')
		ClearSelection()

		### 1.4.3 Set properties for the join
		#DP
		shpField='Label'
		csvField='Label'
		joinObject = QgsVectorLayerJoinInfo()

		joinObject.setJoinFieldName(csvField)
		joinObject.setTargetFieldName(shpField)
		joinObject.setJoinLayerId(dp_enc_lyr.id())
		joinObject.setUsingMemoryCache(True)
		joinObject.setJoinLayer(dp_enc_lyr)
		export_dp_lyr.addJoin(joinObject)
		#check invalid joins
		check_enclosures(export_dp_lyr,'dp_enc_Type','Label')

		#AB
		shpField='Label'
		csvField='Label'
		joinObject = QgsVectorLayerJoinInfo()

		joinObject.setJoinFieldName(csvField)
		joinObject.setTargetFieldName(shpField)
		joinObject.setJoinLayerId(a_enc_lyr.id())
		joinObject.setUsingMemoryCache(True)
		joinObject.setJoinLayer(a_enc_lyr)
		export_ab_lyr.addJoin(joinObject)
		#check invalid joins
		check_enclosures(export_ab_lyr,'ab_enclosures_Type','Label')

		#DHH
		shpField='Label'
		csvField='Label'
		joinObject = QgsVectorLayerJoinInfo()

		joinObject.setJoinFieldName(csvField)
		joinObject.setTargetFieldName(shpField)
		joinObject.setJoinLayerId(dhh_enc_lyr.id())
		joinObject.setUsingMemoryCache(True)
		joinObject.setJoinLayer(dhh_enc_lyr)
		export_dhh_lyr.addJoin(joinObject)
		#check invalid joins
		check_enclosures(export_dhh_lyr,'dhh_enc_Type','Label')

		progression += 1 #jump
	else:
		print('[i1.4] - Join in Layers skipped')

	## 1.5 COPY INFO FROM EXP LYRS FOR EACH LAYER
	print('> Copies')
		#opensourceoptions.com/blog/pyqgis-select-features-from-a-vector-layer/
	if progression == 4:

		#joint lyrs
		#Pole-Cl
		copyFeatures.copyByExp(export_ab_lyr,poleCl_lyr,'\"a_enc_Type\"= \'type1\' OR \"a_enc_Type\"= \'type2\'')
		#FC-Cl
		copyFeatures.copyByExp(export_ab_lyr,fcCl_lyr,'\"a_enc_Type\"= \'type3\'')
		#DP
		copyFeatures.copyAll(export_dp_lyr,dp_lyr)
		#update fields
		dp_lyr.startEditing()
		
		try:
			lb_idx = dp_lyr.fields().lookupField('Label')
		except:
			print('lookupField(\'Label\') doesn\'t exists')

		x = 1
		for f in dp_lyr.getFeatures():
			if x < 10:
				value = F'{prjTitle}-DP-0{x}'
			else:
				value = F'{prjTitle}-DP-{x}'
			x += 1

			#name = f.attributes()[f.fields().indexFromName('Label')]
			#value = prjTitle +'-'+ name

			atts = {lb_idx: value}
			dp_lyr.changeAttributeValues(f.id(), atts)
		dp_lyr.commitChanges()
		dp_lyr = prj.mapLayersByName('DP')[0]     #update value

		#DHH
		copyFeatures.copyAll(export_dhh_lyr,dhh_lyr)
		ClearSelection()

		############################
		#Distribution Cables
		try:
			copyFeatures.copyAll(_temp_distCable_lyr,dCables_lyr)
			ClearSelection()
		except:
			print('     [ERROR] Missing D-Cables')
		############################

		#Rs
		copyFeatures.copyByExp(_temp_points_lyr,Rs_lyr,'\"layer\"= \'Rs\'')
		#ClearSelection()

		#D-Ducts
		copyFeatures.copyByExp(_temp_othrCable_lyr,dDucts_lyr,'\"layer\"= \'D-Duct\'')
		#ClearSelection()

		#Drops
		copyFeatures.copyByExp(_temp_othrCable_lyr,drops_lyr,'\"layer\"= \'A-Cable\'')
		copyFeatures.copyByExp(_temp_othrCable_lyr,drops_lyr,'\"layer\"= \'A-Subduct\'')
		#ClearSelection()

		#Pole
		copyFeatures.copyAll(export_Pole_lyr,pole_lyr)
		#ClearSelection()

		#Multifus
		copyFeatures.copyByExp(_temp_othrCable_lyr,multFus_lyr,'\"layer\"= \'A-Duct\'')
		check_multf_length(multFus_lyr,'length')
		#ClearSelection()

		#CO
		copyFeatures.copyByExp(_temp_points_lyr,co_lyr,'\"layer\"= \'CO\'')
		copyFeatures.copyByExp(_temp_points_lyr,co_lyr,'\"layer\"= \'AP\'')
		#ClearSelection()

		#BE
		copyFeatures.copyByExp(_temp_points_lyr,be_lyr,'\"layer\"= \'BE\'')
		#ClearSelection()

		#T-Box
		copyFeatures.copyByExp(_temp_points_lyr,terminationBox_lyr,'\"layer\"= \'T-Box\'')
		#ClearSelection()

		#fCable
		copyFeatures.copyByExp(_temp_othrCable_lyr,feedCable_lyr,'\"layer\"= \'F-Cable\'')
		#ClearSelection()

		#HP
		copyFeatures.copyByExp(_temp_points_lyr,hp_lyr,'\"layer\"= \'HP\'')
		#ClearSelection()

		#BK
		copyFeatures.copyByExp(_temp_points_lyr,bk_lyr,'\"layer\"= \'BK\'')
		ClearSelection()

		progression += 1 #jump
	else:
		print('[i1.5] - Layer Copies skipped')

	iface.messageBar().clearWidgets()

	print('========================================')
	print("--- END in %s seconds ---" % (time.time() - start_time))
	print('========================================')