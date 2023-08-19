"""
Model exported as python.
Name : Better Geometries
Group : 
With QGIS : 32204
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class BetterGeometries(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_aerialboxes', 'snapped_aerialBoxes', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=''))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_dcables', 'snapped_dCables', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_fcables', 'snapped_fCables', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=''))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_dropcables', 'snapped_dropCables', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=''))
        self.addParameter(QgsProcessingParameterFeatureSink('Snapped_dducts', 'snapped_dDucts', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=''))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(12, model_feedback)
        results = {}
        outputs = {}

        # Snap AerialBox to Paal
        alg_params = {
            'BEHAVIOR': 2,  # Prefer aligning nodes, don't insert new vertices
            'INPUT': 'export___Aerial_Box_7e1866a9_d55d_4c7e_87b4_07e7c651728d',
            'REFERENCE_LAYER': 'export___Paal_ab750646_b2e2_4742_8bf2_e9bc85c5f760',
            'TOLERANCE': 0.005,
            'OUTPUT': parameters['Snapped_aerialboxes']
        }
        outputs['SnapAerialboxToPaal'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Snapped_aerialboxes'] = outputs['SnapAerialboxToPaal']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Snap DDuct to DP
        alg_params = {
            'BEHAVIOR': 4,  # Move end points only, prefer aligning nodes
            'INPUT': 'export___D_Duct_69c1c123_d834_4ad8_9073_85f602aa49a8',
            'REFERENCE_LAYER': outputs['SnapAerialboxToPaal']['OUTPUT'],
            'TOLERANCE': 0.005,
            'OUTPUT': parameters['Snapped_dducts']
        }
        outputs['SnapDductToDp'] = processing.run('native:snapgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Snapped_dducts'] = outputs['SnapDductToDp']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Fix D-Cables geometries
        alg_params = {
            'INPUT': 'export___D_Cable_29486728_20a0_4231_883c_b23b38530ba0',
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
            'REFERENCE_LAYER': 'export___Paal_ab750646_b2e2_4742_8bf2_e9bc85c5f760',
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
            'REFERENCE_LAYER': 'export___Termination_Box_1b3f45f4_6b47_4063_85b6_b0de567f89ef',
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
            'REFERENCE_LAYER': 'export___Riser_2a4b89ea_93eb_422c_869b_b01e5be24ec3',
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
            'REFERENCE_LAYER': 'export___DP_1505044e_194c_4a77_a91a_32d65481b0e3',
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
            'INPUT': 'export___F_Cable_7c53677b_65f2_4108_9aa3_68cc091ef4a4',
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
            'REFERENCE_LAYER': 'CO_9c5c692a_528a_4c37_9d9d_a9b3fdd97ada',
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
            'INPUT': 'export___Drop_Cable_da123931_204c_4602_a345_519be17abbb7',
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
            'REFERENCE_LAYER': 'export___Paal_ab750646_b2e2_4742_8bf2_e9bc85c5f760',
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
            'REFERENCE_LAYER': 'HPs_041cfde7_d0b4_48b1_94ce_9372e09c725e',
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
