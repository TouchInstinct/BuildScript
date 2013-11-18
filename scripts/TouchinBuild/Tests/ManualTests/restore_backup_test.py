from CommandBuilders.BuilderBackupCommands.RestoreBackupCommandBuilder import RestoreBackupCommandBuilder

line = "restore from backup"

builder = RestoreBackupCommandBuilder(None)
command = builder.getCommandFor(line)

command.execute()



