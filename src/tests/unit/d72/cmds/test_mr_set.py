import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.mr_set import MRSet
from d72.cmds.mr import MR
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestMNSet(unittest.TestCase):
    
    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = MRSet(self.rcvr)

    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
    
    def test_exception_band(self):
        self.cmd.config = MR()
        self.cmd.config.band = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Band -1 outside valid range, should be 0 or 1"
        )
    
    # channel      
    def test_exception_channel_too_long(self):
        self.cmd.config = MR()
        self.cmd.config.channel = "1234"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )

    def test_exception_channel_too_short(self):
        self.cmd.config = MR()
        self.cmd.config.channel = "01"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )

    def test_exception_channel_invalid_characters(self):
        self.cmd.config = MR()
        self.cmd.config.channel = "ABC"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )
    
    def test_exception_channel_none(self):
        self.cmd.config = MR()
        self.cmd.config.channel = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )

   