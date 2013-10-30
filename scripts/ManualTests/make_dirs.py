from CommandBuilders.MakeDirsCommandBuilder import MakeDirsCommandBuilder

line = "create dirs '../Output/mySuperConfigName/Artifacts'"

builder = MakeDirsCommandBuilder()

command = builder.getCommandFor(line)
command.execute()