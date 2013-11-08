from CommandBuilders.PatchCsprojCommandBuilder import PatchCsprojCommandBuilder

line = "inside 'BuildSample/BuildSample/CoolApp.csproj' set OutputPath to 'Output' for 'Release|iPhone'"

builder = PatchCsprojCommandBuilder()
command = builder.getCommandFor(line)
command.execute()