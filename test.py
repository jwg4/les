import os
import subprocess
import unittest

class CompareErrorMessages(unittest.TestCase):
    def test_missing_file_return_code_the_same_as_ls(self):
        DEVNULL = open(os.devnull, 'wb')
        args = ['./lss.sh', 'foo']
        ret = subprocess.call(args, stderr=DEVNULL)
        args2 = ['ls', 'foo']
        ret2 = subprocess.call(args2, stderr=DEVNULL)
        self.assertEqual(ret == 0, ret2 == 0)

    def get_output(self, args):
        try:
            msg = subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            msg = e.output
        return msg

    def test_missing_file_message_code_the_same_as_ls(self):
        args = ['./lss.sh', 'foo']
        msg = self.get_output(args)
        args2 = ['ls', 'foo']
        msg2 = self.get_output(args2)
        self.assertEqual(msg, msg2)
