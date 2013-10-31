from CommandBuilders.CleanBuildCommandBuilder import CleanBuildCommandBuilder

buildUtilPath = '/Applications/Xamarin\ Studio.app/Contents/MacOS/mdtool'
line = "build 'BuildSample/BuildSample.sln' for 'Release|iPhone'"

builder = CleanBuildCommandBuilder(buildUtilPath, 'build')

command = builder.getCommandFor(line)
command.execute()
