import sys
import os
import stat
import argparse
from distutils.core import setup

print sys.argv
parser = argparse.ArgumentParser()
parser.add_argument('install')
args = parser.parse_known_args()[0]

packageName = 'TouchinBuild'
version = '0.0.13'

setup(name= packageName,
	version= version,

	py_modules=['TouchinBuild.taskRunner'],
	packages= ['TouchinBuild.Core', 'TouchinBuild.Core.LineConveyor',
				'TouchinBuild.utils', 'TouchinBuild.utils.SettingsProvider',
				'TouchinBuild.parsers', 'TouchinBuild.parsers.CopyParser', 'TouchinBuild.parsers.ParserBackup', 'TouchinBuild.parsers.InsideParser', 'TouchinBuild.parsers.SettingsParser',
				'TouchinBuild.commands', 'TouchinBuild.commands.CleanBuildCommands',
				'TouchinBuild.CommandBuilders'],

	url = 'http://touchin.ru',
	license = 'BSD License',
	description = 'Build tool for Touchin',
	author = 'Rustam Zaitov',
	author_email = 'rustam.zaitov [at] touchin.ru',
	maintainer= 'Rustam Zaitov',
	maintainer_email='rustam.zaitov [at] touchin.ru',
)

if args.install == 'install':
	libPath = os.path.join(sys.prefix, 'lib')
	dirsNames = os.listdir(libPath)
	pythonDir = [name for name in dirsNames if name.startswith('python')][0]
	executable = os.path.join(libPath, pythonDir, 'site-packages', packageName, 'taskRunner.py')

	symlink = '/usr/local/bin/tibuild'
	try:
		os.unlink(symlink)
	except OSError:
		print 'warning: symlink file {0} is not exist'.format(symlink)

	st = os.stat(executable)
	os.chmod(executable, st.st_mode | stat.S_IEXEC)
	os.symlink(executable, symlink)