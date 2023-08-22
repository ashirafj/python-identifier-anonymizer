import unittest
import anonymizer
import textwrap

def canonical(code):
    return textwrap.dedent(code).strip()

class Comparisons:
    def assertAnonEqual(self, code, expected_code, expected_map):
        code = canonical(code)
        expected_code = canonical(expected_code)
        anonymized_code, identifier_map = anonymizer.anonymize(code)
        anonymized_code = anonymized_code.rstrip()
        self.assertEqual(anonymized_code, expected_code)
        self.assertEqual(identifier_map, expected_map)

class MyTest(unittest.TestCase, Comparisons):
    def test_ListComp(self):
        # ListComp
        code = """
        my_list = [1, 2, 3]
        selected_list = [x for x in my_list if x > 1]
        """
        expected_code = """
        VAR00 = [1, 2, 3]
        VAR01 = [VAR02 for VAR02 in VAR00 if VAR02 > 1]
        """
        expected_map = {
            "VAR00": "my_list",
            "VAR01": "selected_list",
            "VAR02": "x",
        }

        self.assertAnonEqual(code, expected_code, expected_map)

    def test_DictComp(self):
        # DictComp
        code = """
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        selected_dict = {k: v for k, v in my_dict.items() if v > 1}
        """
        expected_code = """
        VAR00 = {'a': 1, 'b': 2, 'c': 3}
        VAR01 = {VAR02: VAR03 for VAR02, VAR03 in VAR00.items() if VAR03 > 1}
        """
        expected_map = {
            "VAR00": "my_dict",
            "VAR01": "selected_dict",
            "VAR02": "k",
            "VAR03": "v",
        }

        self.assertAnonEqual(code, expected_code, expected_map)
    
    def test_SetComp(self):
        # SetComp
        code = """
        my_set = {1, 2, 3}
        selected_set = {x for x in my_set if x > 1}
        """
        expected_code = """
        VAR00 = {1, 2, 3}
        VAR01 = {VAR02 for VAR02 in VAR00 if VAR02 > 1}
        """
        expected_map = {
            "VAR00": "my_set",
            "VAR01": "selected_set",
            "VAR02": "x",
        }
        
        self.assertAnonEqual(code, expected_code, expected_map)

    def test_GeneratorExp(self):
        # GeneratorExp
        code = """
        my_list = [1, 2, 3]
        selected_list = (x for x in my_list if x > 1)
        """
        expected_code = """
        VAR00 = [1, 2, 3]
        VAR01 = (VAR02 for VAR02 in VAR00 if VAR02 > 1)
        """
        expected_map = {
            "VAR00": "my_list",
            "VAR01": "selected_list",
            "VAR02": "x",
        }

        self.assertAnonEqual(code, expected_code, expected_map)
    
    def test_FormattedValue(self):
        # FormattedValue
        code = """
        a = 2.2
        msg = 'Hello'
        print(msg, a)
        print(f'{msg}! a = {a}.')
        """
        expected_code = """
        VAR00 = 2.2
        VAR01 = 'Hello'
        print(VAR01, VAR00)
        print(f'{VAR01}! a = {VAR00}.')
        """
        expected_map = {
            "VAR00": "a",
            "VAR01": "msg",
        }

        self.assertAnonEqual(code, expected_code, expected_map)

if __name__ == '__main__':
    unittest.main()
