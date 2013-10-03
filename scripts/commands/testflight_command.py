import commands.build_command as bcmd
import utils.testflight.testflight_publisher as tf


class PublishToTestFlightCommand(bcmd.BuildCommand):
	def __init__(self, api_token, team_token, notes):
		self._publisher = tf.TestFlightPublisherBase(api_token, team_token, notes)

	def Execute(self):
		self._publisher.Publish()