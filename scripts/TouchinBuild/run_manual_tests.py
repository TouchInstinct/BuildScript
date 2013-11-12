import os
scriptFilePath = os.path.abspath(__file__)

scriptDir = os.path.dirname(scriptFilePath)
baseDir = os.path.join(scriptDir, os.pardir, os.pardir)

baseDirAbsPath = os.path.abspath(baseDir)
os.chdir(baseDirAbsPath)
print 'current working dir: {0}'.format(baseDirAbsPath)

#import Tests.ManualTests.csproj_test
#import ManualTests.info_plist_test
#import ManualTests.copy_test
#import Tests.ManualTests.create_backup_test
#import Tests.ManualTests.delete_backup_test
import Tests.ManualTests.restore_backup_test
#import ManualTests.csproj_test
#import ManualTests.run_sh_command
#import ManualTests.make_dirs
#import ManualTests.remove_project
#import ManualTests.infoplist_test
#import ManualTests.clean_test
#import Tests.ManualTests.testflight_test
#import Tests.ManualTests.install_profile
#import Tests.ManualTests.macros_include_test
#import Tests.ManualTests.resolve_settings