import os
import sys

module_dirpath = os.path.dirname(os.path.abspath(__file__))
source_dirpath = os.path.join(module_dirpath, '..', 'src')
print(source_dirpath)
sys.path.insert(0, source_dirpath)
