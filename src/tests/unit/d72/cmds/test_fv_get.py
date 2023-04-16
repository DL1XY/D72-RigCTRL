import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.fv_get import FVGet
from d72.cmds.fv import FV
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestFVGet(unittest.TestCase):
    
    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = FVGet(self.rcvr)

    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
    
    def test_exception(self):
        self.cmd.config = FV()
        self.cmd.config.firmwareType = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Firmware type -1 outside valid range, should be between 0 or 1"
        )