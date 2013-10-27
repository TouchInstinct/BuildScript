from CommandBuilders.CopyCommandBuilder import CopyCommandBuilder
from ManualTests.path_provider import PathProvider

line1 = "copy 'BuildSample/BuildSample.sln' to 'BuildSample/BuildSample.txt'"
line2 = "copy 'BuildSample/BuildSample.sln' to '~/tmp/BuildSample.sln'"

baseDir = '../'
path_provider = PathProvider(baseDir)

copyCmdBuilder = CopyCommandBuilder(path_provider)

copyCmdToRel = copyCmdBuilder.getCommandFor(line1)
copyCmdToRel.execute()

copyCmdToAbs = copyCmdBuilder.getCommandFor(line2)
copyCmdToAbs.execute()
