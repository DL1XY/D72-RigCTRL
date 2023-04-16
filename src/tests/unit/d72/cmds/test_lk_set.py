import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.lk_set import LKSet
from d72.cmds.lk import LK
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestLKSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = LKSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception_status(self):
        self.cmd.config = LK()
        self.cmd.config.status = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Status -1 outside valid range, should be 0 or 1"
        ) 

    def test_exception_keylock(self):
        self.cmd.config = LK()
        self.cmd.config.lock = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Key lock -1 outside valid range, should be between 0 and 2"
        ) 