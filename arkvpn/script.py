"""This class allows to make actions on a certain script"""

import subprocess
import os

import constant

class Script(object):
    def __init__(self, script):
        self.script = script
        self._path = os.path.join(constant.SCRIPT_DIR, script)
        self.process = None

    def start_script(self):
        self.process = subprocess.Popen(self._path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def stop_script(self):
        self.process.kill()

    def get_path(self):
        return self._path