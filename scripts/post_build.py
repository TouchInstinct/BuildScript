from subprocess import call
import os
import testflight

def PublishToTestFlight(config):
	sln_path = config['sln_path']
	sln_dir = os.path.dirname(sln_path)

	cmd_text_pattern = "curl http://testflightapp.com/api/builds.json -F file=@'{0}' -F api_token='{1}' -F team_token='{2}' -F notes='This build was uploaded via the upload API'"
	ipa_rel_path = 'BuildSample/bin/iPhone/Release/BuildSample-{0}.ipa'.format(config['version'])
	ipa_abs_path = os.path.join(sln_dir, ipa_rel_path)

	api_token = config['api_token']
	team_token = config['team_token']
	cmd_text = cmd_text_pattern.format(ipa_abs_path, api_token, team_token)

	ret_code = call(cmd_text, shell=True)

def PrintToConsole(config):
	print 'Sample post build action!'