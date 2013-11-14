from commands.CommandBase import CommandBase
from utils.TestflightPublisher import TestFlightPublisher


class TestflightCommand(CommandBase):
	def __init__(self, pathToFile,  api_token, team_token, notes):
		CommandBase.__init__(self)

		assert pathToFile is not None

		self.__pathToFile = pathToFile
		self.__publisher = TestFlightPublisher(api_token, team_token, notes)

	def execute(self):
		self.__publisher.Publish(self.__pathToFile)
