from distutils.core import setup

setup(name= 'TouchinBuild',
	version= '0.0.10',
	py_modules=['TouchinBuild.taskRunner'],
	packages= ['TouchinBuild.Core', 'TouchinBuild.Core.LineConveyor',
				'TouchinBuild.utils', 'TouchinBuild.utils.SettingsProvider',
				'TouchinBuild.parsers', 'TouchinBuild.parsers.CopyParser', 'TouchinBuild.parsers.BackupParser', 'TouchinBuild.parsers.InsideParser', 'TouchinBuild.parsers.SettingsParser',
				'TouchinBuild.commands', 'TouchinBuild.commands.CleanBuildCommands',
				'TouchinBuild.CommandBuilders'],
	url = 'http://touchin.ru',
	license = 'BSD License',
	description = 'Build tool for Touchin',
	author = 'Rustam Zaitov',
	author_email = 'rustam.zaitov [at] touchin.ru',
	maintainer= 'Rustam Zaitov',
	maintainer_email='rustam.zaitov [at] touchin.ru'
)
