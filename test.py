import subprocess
import unittest

class CompareErrorMessages(unittest.TestCase):
    def test_missing_file(self):
        args = ['./lss.sh', 'foo']
        ret = subprocess.call(args)
        args2 = ['ls', 'foo']
        ret2 = subprocess.call(args2)
        self.assertEqual(ret == 0, ret2 == 0)
