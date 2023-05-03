from qgis.core import QgsProcessingFeedback

class MyFeedBack(QgsProcessingFeedback):

    def setProgressText(self, text):
        print(text)

    def pushInfo(self, info):
        print(info)

    def pushCommandInfo(self, info):
        print(info)

    def pushDebugInfo(self, info):
        print(info)

    def pushConsoleInfo(self, info):
        print(info)

    def reportError(self, error, fatalError=False):
        print(error)
    

result = processing.run(name, params, feedback=MyFeedBack())