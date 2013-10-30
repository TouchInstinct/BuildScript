from CommandBuilders.PatchCsprojCommandBuilder import PatchCsprojCommandBuilder
from ManualTests.path_provider import PathProvider
from commands.ValueProvider import ValueProvider

config = {}
line = "inside 'BuildSample/BuildSample/CoolApp.csproj' set OutputPath to 'Output'"

base_dir = '../'
path_provider = PathProvider(base_dir)
value_provider = ValueProvider(config)

builder = PatchCsprojCommandBuilder(config, path_provider, value_provider)
command = builder.getCommandFor(line)