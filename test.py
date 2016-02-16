import subprocess
import unittest

class CompareErrorMessages(unittest.TestCase):
    def test_missing_file_return_code_the_same_as_ls(self):
        args = ['./lss.sh', 'foo']
        ret = subprocess.call(args)
        args2 = ['ls', 'foo']
        ret2 = subprocess.call(args2)
        self.assertEqual(ret == 0, ret2 == 0)

    def test_missing_file_message_code_the_same_as_ls(self):
        args = ['./lss.sh', 'foo']
        try:
            subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            msg = e.output
        args2 = ['ls', 'foo']
        try:
            subprocess.check_output(args2, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            msg2 = e.output
        self.assertEqual(msg, msg2)
