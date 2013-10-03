import unittest
from utils.sln import sln_toolkit_base as sln


class TestRemoveProjectSections(unittest.TestCase):

	def test_RemoveProjectSections(self):
		toolkit = sln.SolutionToolkitBase()
		patched_content = toolkit.RemoveProjectSectionsFrom(TestRemoveProjectSections.sln_content_original, ['NotCompileApp'])
		self.assertEqual(TestRemoveProjectSections.sln_content_patched, patched_content)

	sln_content_original = r"""
Microsoft Visual Studio Solution File, Format Version 11.00
# Visual Studio 2010
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "CoolApp", "BuildSample\CoolApp.csproj", "{E7393DD4-5E5F-456A-89AB-000EC63BD901}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "NotCompileApp", "NotCompileApp\NotCompileApp.csproj", "{3DE4FDFA-1502-44CF-9B73-78B6D730C59F}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Domain", "Domain\Domain.csproj", "{BD5EC0A1-EDC9-4D90-BACF-AE54F26148C1}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|iPhoneSimulator = Debug|iPhoneSimulator
		Release|iPhoneSimulator = Release|iPhoneSimulator
		Debug|iPhone = Debug|iPhone
		Release|iPhone = Release|iPhone
	EndGlobalSection
"""

	sln_content_patched = r"""
Microsoft Visual Studio Solution File, Format Version 11.00
# Visual Studio 2010
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "CoolApp", "BuildSample\CoolApp.csproj", "{E7393DD4-5E5F-456A-89AB-000EC63BD901}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Domain", "Domain\Domain.csproj", "{BD5EC0A1-EDC9-4D90-BACF-AE54F26148C1}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|iPhoneSimulator = Debug|iPhoneSimulator
		Release|iPhoneSimulator = Release|iPhoneSimulator
		Debug|iPhone = Debug|iPhone
		Release|iPhone = Release|iPhone
	EndGlobalSection
"""