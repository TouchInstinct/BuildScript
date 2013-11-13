import abc


class PreprocessorBase:
	__metaclass__ = abc.ABCMeta

	def __init__(self):
		pass

	@abc.abstractmethod
	def processText(self, line, conveyorProcessor):
		pass