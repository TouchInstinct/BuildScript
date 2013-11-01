from CommandBuilders.PatchCsprojCommandBuilder import PatchCsprojCommandBuilder
from Tests.ManualTests.path_provider import PathProvider
from commands.ValueProvider import ValueProvider

config = {'sln_config' : 'Release|iPhone'}
line = "inside 'BuildSample/BuildSample/CoolApp.csproj' set OutputPath to 'Output'"

base_dir = '../'
path_provider = PathProvider(base_dir)
value_provider = ValueProvider(config)

builder = PatchCsprojCommandBuilder(config, path_provider, value_provider)
command = builder.getCommandFor(line)
command.execute()