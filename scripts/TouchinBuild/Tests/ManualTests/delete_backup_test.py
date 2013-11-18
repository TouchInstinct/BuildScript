from CommandBuilders.BuilderBackupCommands.DeleteBackupCommandBuilder import DeleteBackupCommandBuilder

line = "delete backup"

cmdBuilder = DeleteBackupCommandBuilder(None)
command = cmdBuilder.getCommandFor(line)

command.execute()