import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.sq_set import SQSet
from d72.cmds.sq import SQ
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestSQGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps=SerialReceiver())
        self.rcvr.action = MagicMock(return_value="OK")    
        self.cmd = SQSet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
    # band
    def test_exception_band(self):
        self.cmd.config = SQ()
        self.cmd.config.band = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            "Band -1 outside valid range, should be 0 or 1"
        )
    
    # Squelch     
    def test_exception_band_low(self):
        self.cmd.config = SQ()
        self.cmd.config.squelch = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Squelch {self.cmd.config.squelch} outside valid range, should be between 0 and 5"
        )

    def test_exception_squelch_high(self):
        self.cmd.config = SQ()
        self.cmd.config.squelch = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Squelch {self.cmd.config.squelch} outside valid range, should be between 0 and 5"
        )

    def test_exception_squelch_none(self):
        self.cmd.config = SQ()
        self.cmd.config.squelch = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            "unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
