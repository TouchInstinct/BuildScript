from CommandBuilders.CreateBackupCommandBuilder import CreateBackupCommandBuilder

line = "create backup for 'BuildSample'"

cmdBuilder = CreateBackupCommandBuilder()
command = cmdBuilder.getCommandFor(line)

command.execute()