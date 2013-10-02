import os
import inspect
cur_abs_dir_path = os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0])
print('testflight_command', cur_abs_dir_path)

import sys
parent = os.path.split(cur_abs_dir_path)[0]
if parent not in sys.path:
	sys.path.append(parent)

import build_command as bcmd
import testflight as tf

class PublishToTestFlightCommand(bcmd.BuildCommand):
	def __init__(self, api_token, team_token, notes):
		self._publisher = tf.TestFlightPublisherBase(api_token, team_token, notes)

	def Execute(self):
		self._publisher.Publish()

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	parser.add_argument('-at', '--api_token', required=True, help='api token')
	parser.add_argument('-tt', '--team_token', required=True, help='team token')
	parser.add_argument('-n', '--notes', default=tf.TestFlightPublisherBase.DefaultNotes, help='upload notes')

	args = parser.parse_args()

	cmd = PublishToTestFlightCommand(args.api_token, args.team_token, args.notes)
	cmd.Execute()