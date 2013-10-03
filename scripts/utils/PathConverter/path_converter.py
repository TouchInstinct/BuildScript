import utils.PathConverter.converter_base as cB
import os


class PathConverter(cB.ConverterBase):
	def __init__(self, sln_path):
		self._sln_dir = os.path.dirname(sln_path)

	def Convert(self, rel_path):
		return os.path.join(self._sln_dir, rel_path)