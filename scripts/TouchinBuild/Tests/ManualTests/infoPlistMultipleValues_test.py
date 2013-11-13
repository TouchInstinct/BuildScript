from CommandBuilders.PatchInfoPlistArrayCommandBuilder import PatchInfoPlistArrayCommandBuilder

line = "inside 'BuildSample/BuildSample/Info.plist' set UISupportedInterfaceOrientations to 'value1:value2:value3'"

cmdBuilder = PatchInfoPlistArrayCommandBuilder()
command = cmdBuilder.getCommandFor(line)
command.execute()

