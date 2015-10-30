'''
found at http://pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
'''
# The top argument for walk
import os

topdir = '.\\in\\book'

# The extension to search for
exten = '.pdf'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            print(os.path.join(dirpath, name))
