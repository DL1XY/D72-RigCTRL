import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.vm_get import VMGet
from d72.cmds.vm import VM
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestVMGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = VMGet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
    # Band
    def test_exception_band(self):
        self.cmd.config = VM()
        self.cmd.config.band = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Band -1 outside valid range, should be 0 or 1"
        ) 