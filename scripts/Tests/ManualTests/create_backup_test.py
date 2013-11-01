from CommandBuilders.CreateBackupCommandBuilder import CreateBackupCommandBuilder
from Tests.ManualTests.path_provider import PathProvider

line = "create backup for 'BuildSample'"

baseDir = '../'
path_provider = PathProvider(baseDir)

cmdBuilder = CreateBackupCommandBuilder(path_provider)
command = cmdBuilder.getCommandFor(line)

command.execute()