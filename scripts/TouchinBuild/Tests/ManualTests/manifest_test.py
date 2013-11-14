from CommandBuilders.PatchManifestCommandBuilder import PatchManifestCommandBuilder

line = "inside 'BuildSample/DroidApp/Properties/AndroidManifest.xml' set android:versionCode to '777'"

builder = PatchManifestCommandBuilder()

command = builder.getCommandFor(line)
command.execute()
