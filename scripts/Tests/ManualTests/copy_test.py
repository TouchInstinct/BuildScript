from CommandBuilders.CopyCommandBuilder import CopyCommandBuilder
from Tests.ManualTests.path_provider import PathProvider

line1 = "copy 'BuildSample/BuildSample.sln' to 'BuildSample/BuildSample.txt'"
line2 = "copy 'BuildSample/BuildSample/Profiles/8F606DAE-F9C9-4A19-8EFF-34B990D76C28.mobileprovision' to '~/Library/MobileDevice/Provisioning Profiles/BuildScript.mobileprovision'"

baseDir = '../'
path_provider = PathProvider(baseDir)

copyCmdBuilder = CopyCommandBuilder(path_provider)

#copyCmdToRel = copyCmdBuilder.getCommandFor(line1)
#copyCmdToRel.execute()

copyCmdToAbs = copyCmdBuilder.getCommandFor(line2)
copyCmdToAbs.execute()
