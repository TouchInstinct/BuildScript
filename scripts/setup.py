from distutils.core import setup

setup(name= 'TouchinBuild',
	version= '0.0.10',
	packages= ['Core', 'Core.LineConveyor',
				'utils', 'utils.SettingsProvider',
				'parsers', 'parsers.CopyParser', 'parsers.BackupParser', 'parsers.InsideParser', 'parsers.SettingsParser',
				'commands', 'commands.CleanBuildCommands',
				'CommandBuilders'],
	url = 'http://touchin.ru',
	license = 'BSD License',
	description = 'Build tool for Touchin',
	author = 'Rustam Zaitov',
	author_email = 'rustam.zaitov [at] touchin.ru',
	maintainer= 'Rustam Zaitov',
	maintainer_email='rustam.zaitov [at] touchin.ru'
)
