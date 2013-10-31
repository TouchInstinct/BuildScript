from CommandBuilders.CleanBuildCommandBuilder import CleanBuildCommandBuilder

buildUtilPath = '/Applications/Xamarin\ Studio.app/Contents/MacOS/mdtool'
line = "clean 'BuildSample/BuildSample.sln' for 'Release|iPhone'"

builder = CleanBuildCommandBuilder(buildUtilPath, 'clean')

command = builder.getCommandFor(line)
command.execute()