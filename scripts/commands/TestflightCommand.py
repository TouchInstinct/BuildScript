from utils.testflight.TestflightPublisher import TestFlightPublisher


class PublishToTestFlightCommand:
	def __init__(self, api_token, team_token, notes):
		self._publisher = TestFlightPublisher(api_token, team_token, notes)

	def execute(self):
		self._publisher.Publish()