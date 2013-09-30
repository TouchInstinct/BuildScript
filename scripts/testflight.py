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

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	parser.add_argument('-at', '--api_token', required=True, help='api token')
	parser.add_argument('-tt', '--team_token', required=True, help='team token')
	parser.add_argument('-n', '--notes', default=TestFlightPublisherBase.DefaultNotes, help='upload notes')

	args = parser.parse_args()

	publisher = TestFlightPublisherBase(args.api_token, args.team_token, args.notes)
	publisher.Publish(args.path)



