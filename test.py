import subprocess
import unittest

class CompareErrorMessages(unittest.TestCase):
    def test_missing_file(self):
        args = ['./lss.sh', 'foo']
        msg = subprocess.check_output(args, stderr=subprocess.STDOUT)
        args2 = ['ls', 'foo']
        msg2 = subprocess.check_output(args2, stderr=subprocess.STDOUT)
        self.assertEqual(msg, msg2)
