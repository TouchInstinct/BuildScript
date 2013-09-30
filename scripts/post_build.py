import testflight as tf

def PublishToTestFlight(config):
	api_token = config['api_token']
	team_token = config['team_token']

	publisher = tf.TestFlightPublisher(api_token, team_token)
	publisher.Publish(config)


def PrintToConsole(config):
	print 'Sample post build action!'