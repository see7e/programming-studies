# -*- coding: utf-8 -*-

import os
import time
#qgis
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import *
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from qgis.gui import QgsMapLayerComboBox, QgsFieldComboBox
import re
#core
from .modulos import lib_tools
from .modulos import lib_qa
#import
from .modulos import lib_import

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
	os.path.dirname(__file__), 'PluginProcessSuit_dialog_base.ui')) # Create with PyQt

class UnifiberProcessSuitDialog(QtWidgets.QDialog, FORM_CLASS):
	def __init__(self, parent=None):
		"""Constructor."""
		super(UnifiberProcessSuitDialog, self).__init__(parent)
		# Set up the user interface from Designer through FORM_CLASS.
		# After self.setupUi() you can access any designer object by doing
		# self.<objectname>, and you can use autoconnect slots - see
		# http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
		# #widgets-and-dialogs-with-auto-connect
		#setup
		self.setupUi(self)
		#self.Export_setUp()
		#self.ProgressBar()
		#import
		self.UpdateTitleButton.clicked.connect(self.projetTitle)
		self.StartImpButton.clicked.connect(self.startImporting)
		self.StartClearButton.clicked.connect(self.StartClearing)
		#qa
		self.QAButton.clicked.connect(self.QA)
		#labels
		self.DCablesButton.clicked.connect(self.DistCablesLabel)
		self.FCablesButton.clicked.connect(self.FeederCablesLabel)
		self.DDuctsLabelButton.clicked.connect(self.DDuctsLabel)
		#other
		self.tirarLetrasButton.clicked.connect(self.UpdateFields)
		#self.ExportDXFButton.clicked.connect(self.ExportDXF)

	# setups
	def QA(self):
		lib_qa.qa_ative_module()
	#import
	def projetTitle(self):
		lib_tools.titleDialog("Title","Insert Value: ","<title>")
	def startImporting(self):
		lib_import.imp_all()
	def startClearing(self):
		lib_tools.clear_all()
