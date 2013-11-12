from CommandBuilders.CreateBackupCommandBuilder import CreateBackupCommandBuilder

line = "create backup for '.'"

cmdBuilder = CreateBackupCommandBuilder()
command = cmdBuilder.getCommandFor(line)

command.execute()