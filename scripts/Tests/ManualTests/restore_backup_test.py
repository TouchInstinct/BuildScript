from CommandBuilders.RestoreBackupCommandBuilder import RestoreBackupCommandBuilder

line = "restore from backup"

builder = RestoreBackupCommandBuilder()
command = builder.getCommandFor(line)

command.execute()



