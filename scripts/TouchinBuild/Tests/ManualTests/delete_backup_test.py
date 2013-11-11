from CommandBuilders.DeleteBackupCommandBuilder import DeleteBackupCommandBuilder

line = "delete backup 'BuildSample'"

cmdBuilder = DeleteBackupCommandBuilder()
command = cmdBuilder.getCommandFor(line)

command.execute()