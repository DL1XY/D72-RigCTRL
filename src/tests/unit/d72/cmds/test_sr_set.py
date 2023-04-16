import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.sr_set import SRSet
from d72.cmds.sr import SR
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestSRSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = SRSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
    # reset
    def test_exception_reset(self):
        self.cmd.config = SR()
        self.cmd.config.reset = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Reset value -1 outside valid range, should be bewteen 0 and 2"
        )
    
   