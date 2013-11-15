from CommandBuilders.BuilderBackupCommands.CreateBackupCommandBuilder import CreateBackupCommandBuilder

line = "create backup"

cmdBuilder = CreateBackupCommandBuilder(None)
command = cmdBuilder.getCommandFor(line)

command.execute()