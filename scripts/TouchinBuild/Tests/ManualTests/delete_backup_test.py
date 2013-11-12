from CommandBuilders.DeleteBackupCommandBuilder import DeleteBackupCommandBuilder

line = "delete backup"

cmdBuilder = DeleteBackupCommandBuilder()
command = cmdBuilder.getCommandFor(line)

command.execute()