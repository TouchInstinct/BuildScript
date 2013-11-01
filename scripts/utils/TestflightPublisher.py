from subprocess import call


class TestFlightPublisher:
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