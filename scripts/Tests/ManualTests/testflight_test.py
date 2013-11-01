from CommandBuilders.TestflightCommandBuilder import TestflightCommandBuilder

line = "publish 'Output/Appstore/Artifacts/BuildSample-1.2.3.ipa' to testflight notes = 'Hello' api_token = '0e6925075d4fc10fed0e7bbf43fa6894_NjQ0OTI2MjAxMi0wOS0yNSAxMTo0MDozNi40OTY5MjU' team_token = 'c5c3cf7a6dae2bea4382dfbd181a2075_Mjc4ODkwMjAxMy0wOS0yOSAxNDowOTo1OC40Mzg5MTY'"

builder = TestflightCommandBuilder()

command = builder.getCommandFor(line)
command.execute()