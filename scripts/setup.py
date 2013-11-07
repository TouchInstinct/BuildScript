from distutils.core import setup

setup(name= 'TouchinBuild',
	version= '0.0.10',
	packages= ['Core', 'Core.LineConveyor',
				'utils', 'utils.SettingsProvider',
				'parser', 'parser.CopyParser', 'parser.BackupParser', 'parser.InsideParser', 'parser.SettingsParser',
				'commands', 'commands.CleanBuildCommands',
				'CommandBuilders'],
	url = 'http://touchin.ru',
	license = 'All rights reserved.',
	description = 'Build tool for Touchin',
	author = 'Rustam Zaitov',
	author_email = 'rustam.zaitov@touchin.ru'
)
