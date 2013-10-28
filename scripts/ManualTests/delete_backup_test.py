from CommandBuilders.DeleteBackupCommandBuilder import DeleteBackupCommandBuilder
from ManualTests.path_provider import PathProvider

line = "delete backup"

baseDir = '../'
path_provider = PathProvider(baseDir)

cmdBuilder = DeleteBackupCommandBuilder(path_provider)
command = cmdBuilder.getCommandFor(line)

command.execute()