import testflight

def PublishToTestFlight(config):
	cmd_text_pattern = "curl http://testflightapp.com/api/builds.json -F file=@'{0}' -F api_token='{1}' -F team_token='{2}' -F notes='This build was uploaded via the upload API'"
	cmd_text = cmd_text_pattern.format(config[''])

def PrintToConsole(config):
	print 'Sample post build action!'