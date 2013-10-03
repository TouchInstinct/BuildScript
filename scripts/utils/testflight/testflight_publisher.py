import os
from utils import testflight as tf


class TestFlightPublisher(tf.TestFlightPublisherBase):
	def __init__(self, config):
		self._config = config

		api_token = config['tf_api_token']
		team_token = config['tf_team_token']
		notes = config.get('ft_notes', None)

		tf.TestFlightPublisherBase.__init__(self, api_token, team_token, notes)

	def Publish(self):
		sln_path = self._config['sln_path']
		sln_dir = os.path.dirname(sln_path)

		ipa_rel_path = 'BuildSample/bin/iPhone/Release/BuildSample-{0}.ipa'.format(self._config['version'])
		ipa_abs_path = os.path.join(sln_dir, ipa_rel_path)

		return tf.TestFlightPublisherBase.Publish(self, ipa_abs_path)