import os

class PathProvider:
	def __init__(self, base_dir):
		self._base_dir = base_dir

	def ResolveAbsPath(self, rel_path):
		abs_path = os.path.join(self._base_dir, rel_path)
		return abs_path

