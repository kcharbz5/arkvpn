import os

path = os.path.abspath(__file__)
path = os.path.dirname(os.path.split(path)[0])


SCRIPT_DIR = os.path.join(path, "scripts/")
IMG_DIR = os.path.join(path, "img/")