import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.bt_set import BTSet
from d72.cmds.bt import BT
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestBTSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = BTSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception(self):
        self.cmd.config = BT()
        self.cmd.config.burstTone = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Burst tone -1 outside valid range, should be between 0 and 3"
        )