from CommandBuilders.PatchManifestCommandBuilder import PatchManifestCommandBuilder

line = "inside 'BuildSample/DroidApp/Properties/AndroidManifest.xml' set android:versionCode to '7.7.7'"

builder = PatchManifestCommandBuilder()

command = builder.getCommandFor(line)
command.execute()
