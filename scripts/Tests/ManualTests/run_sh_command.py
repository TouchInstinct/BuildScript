from commands.ShCommand import ShCommand

calendarCommand = ShCommand('cal 12 2013')
calendarCommand.execute()

touchCommand = ShCommand('touch ../tmp.txt')
touchCommand.execute()
