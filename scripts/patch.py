import re
import os

def RewriteFile(file_to_rewrite, content):
	file_to_rewrite.seek(0)
	file_to_rewrite.write(content)
	file_to_rewrite.truncate()
	file_to_rewrite.close()


def PatchSlnForIos(build_config):

	sln_file = open(build_config['sln_path'], 'r+')
	content = sln_file.read()

	condesign_key_patt = r'<CodesignKey>.*?</CodesignKey>'
	condesign_key_node = r'<CodesignKey>{0}</CodesignKey>'.format(build_config['codesign_key'])
	content = re.sub(condesign_key_patt, condesign_key_node, content)

	RewriteFile(sln_file, content)

def PatchInfoPlist(build_config):

	sln_dir = os.path.dirname(build_config['sln_path'])
	abs_info_plist_path = os.path.join(sln_dir, build_config['info_plist_rel_path'])

	info_plist_file = open(abs_info_plist_path, 'r+')
	content = info_plist_file.read()

	version_patt = r'\s*<key>CFBundleVersion</key>\s+<string>[\d\.]+</string>'
	version_node = r'\n\t<key>CFBundleVersion</key>\n\t<string>{0}</string>'.format(build_config['version'])
	content = re.sub(version_patt, version_node, content)

	RewriteFile(info_plist_file, content)

def PathcIos(build_config):

	PatchSlnForIos(build_config)
	PatchInfoPlist(build_config)

def PathcAndroid(build_config):
	print('start patch ios')

