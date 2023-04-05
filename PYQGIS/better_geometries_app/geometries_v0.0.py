"""
Model exported as python.
Name : Better Geometries
Group : 
With QGIS : 32204
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class BetterGeometries(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        #self.addParameter(QgsProcessingParameterVectorLayer(NAME, DESCRIPTION, types=[VECTOR_GEOMETRY], defaultValue=None))
        """
        # Better Geometries callFunction
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
        """
        self.addParameter(QgsProcessingParameterVectorLayer('aerialboxes', 'export - Aerial Boxes', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('co', 'export - CO', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('dcables', 'export - D-Cables', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('dducts', 'export - D-Ducts', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('dropcables', 'export - DropCables', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('exportpaal', 'export - Paal', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('exportterminationbox', 'export - Termination Box', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('fcables', 'export - F-Cables', types=[QgsProcessing.TypeVectorLine], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('exportriser', 'export - Riser', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('exportdp', 'export - DP', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer('exporthps', 'export - HPs', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_aerialboxes', 'snapped_aerialBoxes', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_dcables', 'snapped_dCables', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_fcables', 'snapped_fCables', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_dropcables', 'snapped_dropCables', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_dducts', 'snapped_dDucts', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(12, model_feedback)
        results = {}
        outputs = {}

        # Snap AerialBox to Paal
        alg_params = {
            'BEHAVIOR': 2,  # Prefer aligning nodes, don't insert new vertices
            'INPUT': parameters['aerialboxes'],
            'REFERENCE_LAYER': parameters['aerialboxes'],
            'TOLERANCE': 0.005,
            'OUTPUT': parameters['Snapped_aerialboxes']
        }
        outputs['SnapAerialboxToPaal'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Snapped_aerialboxes'] = outputs['SnapAerialboxToPaal']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Snap DDuct to aerial Boxes
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': parameters['dducts'],
            'REFERENCE_LAYER': outputs['SnapAerialboxToPaal']['OUTPUT'],
            'TOLERANCE': 0.005,
            'OUTPUT': parameters['Snapped_dducts']
        }
        outputs['SnapDductToAerialBoxes'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Snapped_dducts'] = outputs['SnapDductToAerialBoxes']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Fix D-Cables geometries
        alg_params = {
            'INPUT': parameters['dcables'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FixDcablesGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Snap (fx)DCables to Paal
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': outputs['FixDcablesGeometries']['OUTPUT'],
            'REFERENCE_LAYER': parameters['exportpaal'],
            'TOLERANCE': 0.005,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['SnapFxdcablesToPaal'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Snap (fx)DCable to TermBox
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': outputs['SnapFxdcablesToPaal']['OUTPUT'],
            'REFERENCE_LAYER': parameters['exportterminationbox'],
            'TOLERANCE': 0.005,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['SnapFxdcableToTermbox'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Snap (fx)DCable to Riser
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': outputs['SnapFxdcableToTermbox']['OUTPUT'],
            'REFERENCE_LAYER': parameters['exportriser'],
            'TOLERANCE': 0.005,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['SnapFxdcableToRiser'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # Snap(fx) DCable to DP
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': outputs['SnapFxdcableToRiser']['OUTPUT'],
            'REFERENCE_LAYER': parameters['exportdp'],
            'TOLERANCE': 0.005,
            'OUTPUT': parameters['Snapped_dcables']
        }
        outputs['SnapfxDcableToDp'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Snapped_dcables'] = outputs['SnapfxDcableToDp']['OUTPUT']

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Fix F-Cables geometries
        alg_params = {
            'INPUT': parameters['fcables'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FixFcablesGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # Snap (fx) FCable to CO
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': outputs['FixFcablesGeometries']['OUTPUT'],
            'REFERENCE_LAYER': parameters['co'],
            'TOLERANCE': 0.005,
            'OUTPUT': parameters['Snapped_fcables']
        }
        outputs['SnapFxFcableToCo'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Snapped_fcables'] = outputs['SnapFxFcableToCo']['OUTPUT']

        feedback.setCurrentStep(9)
        if feedback.isCanceled():
            return {}

        # Fix DropCable geometries
        alg_params = {
            'INPUT': parameters['dropcables'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FixDropcableGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(10)
        if feedback.isCanceled():
            return {}

        # Snap dropCable to Paal
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': outputs['FixDropcableGeometries']['OUTPUT'],
            'REFERENCE_LAYER': parameters['exportpaal'],
            'TOLERANCE': 0.005,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['SnapDropcableToPaal'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(11)
        if feedback.isCanceled():
            return {}

        # Snap (fx)dropCable to HP
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': outputs['SnapDropcableToPaal']['OUTPUT'],
            'REFERENCE_LAYER': parameters['exporthps'],
            'TOLERANCE': 0.005,
            'OUTPUT': parameters['Snapped_dropcables']
        }
        outputs['SnapFxdropcableToHp'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Snapped_dropcables'] = outputs['SnapFxdropcableToHp']['OUTPUT']
        return results

    def name(self):
        return 'Better Geometries'

    def displayName(self):
        return 'Better Geometries'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return BetterGeometries()
