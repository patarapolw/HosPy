# import os,sys

# __all__ = []

# for filename in os.listdir(os.path.dirname(__file__)):
# 	module, ext = os.path.splitext(filename)
# 	if module[0] not in ('.', '_'):
# 		if ext == '.py':
# 			if module not in ('__init__'):
# 				__all__ += [module]
# 		if os.path.isdir(filename):
# 			__all__ += [module]

# del os,sys

from . import login, mainWindow, preferences, personnel, patient