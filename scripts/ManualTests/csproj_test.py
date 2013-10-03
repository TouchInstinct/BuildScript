import path_provider
import commands.patch_csproj_command as csproj

config = {
	'csproj app:CoolApp rel_path': 'BuildSample/BuildSample/CoolApp.csproj',
	'csproj app:CoolApp key:CodesignProvision': '@codesign_provision',
	'csproj app:CoolApp key:CodesignKey': '@codesign_key',

	'codesign_provision': 'MyProvisioningValue',
	'codesign_key': 'MyCodesignValue',
	'sln_config': 'Release|iPhone'
}

base_dir = '/Users/rzaitov/Documents/Apps/BuildScript'
provider = path_provider.PathProvider(base_dir)

patcher = csproj.PatchCsproj(config, provider)
patcher.Execute()
