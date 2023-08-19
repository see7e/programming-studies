"""
Model exported as python.
Name : model
Group : 
With QGIS : 32204
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
import processing


class Model(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('2', 'export - CO', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('1', 'export - Aerial Boxes', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('3', 'export - D-Cables', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('4', 'export - D-Ducts', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('exporthp', 'export - HP', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('export3', 'export - DP', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('export2', 'export - Riser', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('export', 'export - F-Cables', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('7', 'export - Termination Box', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('6', 'export - Paal', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('5', 'export - DopCables', types=[QgsProcessing.TypeVectorLine], defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Better Geometries
        alg_params = {
            'aerialboxes': parameters['1'],
            'co': parameters['2'],
            'dcables': parameters['3'],
            'dducts': parameters['4'],
            'dropcables': parameters['5'],
            'exportdp': parameters['export3'],
            'exporthps': parameters['exporthp'],
            'exportpaal': parameters['6'],
            'exportriser': parameters['export2'],
            'exportterminationbox': parameters['7'],
            'fcables': parameters['export'],
            'Snapped_aerialboxes': QgsProcessing.TEMPORARY_OUTPUT,
            'Snapped_dcables': QgsProcessing.TEMPORARY_OUTPUT,
            'Snapped_dducts': QgsProcessing.TEMPORARY_OUTPUT,
            'Snapped_dropcables': QgsProcessing.TEMPORARY_OUTPUT,
            'Snapped_fcables': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['BetterGeometries'] = processing.run('script:Better Geometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return 'model'

    def displayName(self):
        return 'model'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Model()
