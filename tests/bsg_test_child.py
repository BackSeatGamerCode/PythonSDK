import sys
sys.path.append('..')

from BSGPythonSDK import *


class BSGTestChild(BSGPythonSDK):
    def get_event(self, redemption):
        return HelloWorldEvent()
