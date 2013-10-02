from subprocess import call
import os

class TestFlightPublisherBase:
	DefaultNotes = 'This build was uploaded via the upload API'

	def __init__(self, api_token, team_token, notes=DefaultNotes):
		self._api_token = api_token
		self._team_token = team_token
		self._notes = notes

	def Publish(self, pathToFile):
		cmd_text_pattern = "curl http://testflightapp.com/api/builds.json -F file=@'{0}' -F api_token='{1}' -F team_token='{2}' -F notes='{3}'"
		cmd_text = cmd_text_pattern.format(pathToFile, self._api_token, self._team_token, self._notes)

		ret_code = call(cmd_text, shell=True)
		return ret_code

class TestFlightPublisher(TestFlightPublisherBase):
	def __init__(self, config):
		self._config = config

		api_token = config['tf_api_token']
		team_token = config['tf_team_token']
		notes = config.get('ft_notes', None)

		TestFlightPublisherBase.__init__(self, api_token, team_token, notes)

	def Publish(self):
		sln_path = self._config['sln_path']
		sln_dir = os.path.dirname(sln_path)

		ipa_rel_path = 'BuildSample/bin/iPhone/Release/BuildSample-{0}.ipa'.format(self._config['version'])
		ipa_abs_path = os.path.join(sln_dir, ipa_rel_path)

		return TestFlightPublisherBase.Publish(self, ipa_abs_path)