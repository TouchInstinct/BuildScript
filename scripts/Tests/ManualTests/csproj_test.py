from CommandBuilders.PatchCsprojCommandBuilder import PatchCsprojCommandBuilder
from commands.ValueProvider import ValueProvider

config = {'sln_config' : 'Release|iPhone'}
line = "inside 'BuildSample/BuildSample/CoolApp.csproj' set OutputPath to 'Output'"

value_provider = ValueProvider(config)

builder = PatchCsprojCommandBuilder(config, value_provider)
command = builder.getCommandFor(line)
command.execute()