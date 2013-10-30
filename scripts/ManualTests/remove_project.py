from CommandBuilders.RemoveProjectCommandBuilder import RemoveProjectCommandBuilder

line = "inside 'BuildSample/BuildSample.sln' remove NotCompile project"

builder = RemoveProjectCommandBuilder()
command = builder.getCommandFor(line)

command.execute()