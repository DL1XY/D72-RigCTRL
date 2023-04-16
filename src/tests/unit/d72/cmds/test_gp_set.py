import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.gp_set import LKSet
from d72.cmds.gp import GP
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestGPSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = LKSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception_status(self):
        self.cmd.config = GP()
        self.cmd.config.status = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Status -1 outside valid range, should be 0 or 1"
        ) 

    def test_exception_igps(self):
        self.cmd.config = GP()
        self.cmd.config.igps = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Internal GPS -1 outside valid range, should be 0 or 1"
        ) 