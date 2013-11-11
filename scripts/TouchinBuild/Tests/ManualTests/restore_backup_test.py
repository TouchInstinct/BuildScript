from CommandBuilders.RestoreBackupCommandBuilder import RestoreBackupCommandBuilder

line = "restore from backup 'BuildSample'"

builder = RestoreBackupCommandBuilder()
command = builder.getCommandFor(line)

command.execute()



