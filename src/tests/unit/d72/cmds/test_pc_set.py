import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.pc_set import PCSet
from d72.cmds.pc import PC
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestPCSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = PCSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()  

    # Band     
    def test_exception_band(self):
        self.cmd.config = PC()
        self.cmd.config.band = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Band -1 outside valid range, should be 0 or 1"
        )

    
    def test_exception_band_none(self):
        self.cmd.config = PC()
        self.cmd.config.band = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )

    # Power     
    def test_exception_band(self):
        self.cmd.config = PC()
        self.cmd.config.power = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Power -1 outside valid range, should be between 0 and 2"
        )

    
    def test_exception_band_none(self):
        self.cmd.config = PC()
        self.cmd.config.power = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )