from commands.ShCommand import ShTextCommand

calendarCommand = ShTextCommand('cal 12 2013')
calendarCommand.execute()

touchCommand = ShTextCommand('touch ../tmp.txt')
touchCommand.execute()
