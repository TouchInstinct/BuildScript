from CommandBuilders.CreateBackupCommandBuilder import CreateBackupCommandBuilder

line = "create backup"

cmdBuilder = CreateBackupCommandBuilder()
command = cmdBuilder.getCommandFor(line)

command.execute()