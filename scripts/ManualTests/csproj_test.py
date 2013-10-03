import path_provider
import commands.patch_csproj_command as csproj
config = {
	'csproj group:CoolApp key:rel_path': 'BuildSample/CoolApp.csproj',
	'csproj group:CoolApp key:CodesignProvision': '@codesign_provision',
	'csproj group:CoolApp key:CodesignKey': '@codesign_key',

	'codesign_provision': 'MyProvisioningValue',
	'codesign_key': 'MyCodesignValue'
}

base_dir = '/Users/rzaitov/Documents/Apps/BuildScript',
provider = path_provider.PathProvider(base_dir)

patcher = csproj.PatchCsproj(config, provider)
patcher.Execute()
