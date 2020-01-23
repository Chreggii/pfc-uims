import unittest

import sys
from pathlib import Path

import os

from configuration.configuration_model import get_value_from_data, find_js_files, is_new_pull_available, GitRepo, \
    pull_from_remote, get_value_from_origin_name, get_all_model_names

ROOT_DIR = os.path.abspath(os.curdir)

sys.path.append(ROOT_DIR + '/backend/configuration')


class ModelTest(unittest.TestCase):

    clone_url = "https://github.com/sarahzu/Visual-Components-Testcase-2.git"
    local_repo_path = ROOT_DIR + "/testing/local"
    git_repo = GitRepo(local_repo_path, clone_url)

    def test_pull_from_remote(self):
        return_value = pull_from_remote(ROOT_DIR + "/testing/local")
        expected_value = False
        self.assertEqual(expected_value, return_value)

    def test_get_value_from_origin_name(self):
        value_origin = "aum.mfa.out.PublicVehicles"
        node_path_string = "value.1.value"
        return_value = get_value_from_origin_name(value_origin, node_path_string)
        expected_value = 3300
        self.assertEqual(return_value, expected_value)

    def test_get_value_from_data(self):
        input_or_output_file = "out"
        filename = "aum.mfa.out.PublicVehicles"
        value_origin_tree_notes = ["value", "1", "value"]
        return_value = get_value_from_data(input_or_output_file, filename, value_origin_tree_notes)
        expected_value = 3300
        self.assertEqual(return_value, expected_value)

    def test_get_all_model_names(self):
        model_path = ROOT_DIR + "/backend/tests/out"
        return_value = get_all_model_names(model_path)
        expected_value = ["aum.mfa.out.EndOfLifeMgmt", "aum.mfa.out.Energy", "aum.mfa.out.Industry"]
        self.assertEqual(return_value.sort(), expected_value.sort())

    def test_find_js_files(self):
        return_value = find_js_files(ROOT_DIR + "/backend/tests/files")
        expected_value = [{'name': 'PieChart', 'filename': 'demoVisComp',
                           'path': ROOT_DIR + '/backend/tests/files/demoVisComp.js',
                           'parameters': [
                               {'name': 'breakpoint', 'type': 'integer', 'defaultValue': '480', 'dependentOn': ''},
                               {'name': 'chartWidth', 'type': 'integer', 'defaultValue': '200', 'dependentOn': ''},
                               {'name': 'legendPosition', 'type': 'string', 'defaultValue': 'bottom',
                                'dependentOn': ''},
                               {'name': 'modelA', 'type': 'dynamic', 'defaultValue': 'aum.mfa.out.PublicVehicles',
                                'dependentOn': ''},
                               {'name': 'modelB', 'type': 'dynamic', 'defaultValue': 'aum.mfa.out.PrivateVehicles',
                                'dependentOn': ''},
                               {'name': 'modelC', 'type': 'dynamic', 'defaultValue': 'aum.mfa.out.OtherBuildings',
                                'dependentOn': ''},
                               {'name': 'modelD', 'type': 'dynamic', 'defaultValue': 'aum.mfa.out.ResidentialBuildings',
                                'dependentOn': ''},
                               {'name': 'modelE', 'type': 'dynamic', 'defaultValue': 'aum.mfa.out.Industry',
                                'dependentOn': ''}, {'name': 'valueA', 'type': 'dependent', 'defaultValue': '44',
                                                     'dependentOn': 'valueA--modelA--value.10.value'},
                               {'name': 'valueB', 'type': 'dependent', 'defaultValue': '55',
                                'dependentOn': 'valueB--modelB--value.10.value'},
                               {'name': 'valueC', 'type': 'dependent', 'defaultValue': '55',
                                'dependentOn': 'valueC--modelC--value.10.value'},
                               {'name': 'valueD', 'type': 'dependent', 'defaultValue': '43',
                                'dependentOn': 'valueD--modelD--value.10.value'},
                               {'name': 'valueE', 'type': 'dependent', 'defaultValue': '22',
                                'dependentOn': 'valueE--modelE--value.10.value'},
                               {'name': 'click', 'type': 'dependent', 'defaultValue': '777',
                                'dependentOn': 'click--getValue--value.1.value'},
                               {'name': 'getValue', 'type': 'callback', 'defaultValue': 'onButtonClicked',
                                'dependentOn': ''}]}]
        self.assertEqual(return_value, expected_value)

    def test_is_new_pull_available(self):
        # no pull available
        local_repo_path = ROOT_DIR + "/testing/github"
        return_value = is_new_pull_available(local_repo_path)
        expected_value = False
        self.assertEqual(return_value, expected_value)

        # pull available
        local_repo_path = ROOT_DIR + "/testing/github2"
        return_value = is_new_pull_available(local_repo_path)
        expected_value = True
        self.assertEqual(return_value, expected_value)

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
