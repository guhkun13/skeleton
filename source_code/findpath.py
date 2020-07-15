import os

PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)

paths = PATH.split('/')
print(paths)
print(paths[3])
