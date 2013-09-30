import testflight as tf

def PublishToTestFlight(config):
	publisher = tf.TestFlightPublisher(config)
	publisher.Publish()

def PrintToConsole(config):
	print 'Sample post build action!'