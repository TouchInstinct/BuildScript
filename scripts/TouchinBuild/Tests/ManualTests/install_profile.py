from CommandBuilders.InstallProfileCommandBuilder import InstallProfileCommandBuilder

line = "install profile 'BuildSample/BuildSample/Profiles/8F606DAE-F9C9-4A19-8EFF-34B990D76C28.mobileprovision'"

builder = InstallProfileCommandBuilder()
command = builder.getCommandFor(line)

command.execute()