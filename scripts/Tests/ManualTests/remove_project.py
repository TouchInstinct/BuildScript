from CommandBuilders.RemoveProjectCommandBuilder import RemoveProjectCommandBuilder

line = "inside 'BuildSample/BuildSample.sln' remove NotCompileApp project"

builder = RemoveProjectCommandBuilder()
command = builder.getCommandFor(line)

command.execute()