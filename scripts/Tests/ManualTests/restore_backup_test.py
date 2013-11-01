from CommandBuilders.RestoreBackupCommandBuilder import RestoreBackupCommandBuilder
from Tests.ManualTests.path_provider import PathProvider

line = "restore from backup"

baseDir = '../'
path_provider = PathProvider(baseDir)

builder = RestoreBackupCommandBuilder(path_provider)
command = builder.getCommandFor(line)

command.execute()



