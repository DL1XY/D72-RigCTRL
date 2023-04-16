import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.mn_get import MNGet
from d72.cmds.mn import MN
from d72.cmds.serial_receiver import SerialReceiver

class TestMNGet(unittest.TestCase):
    
    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = MNGet(self.rcvr)

    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
    
     # channel      
    def test_exception_channel_too_long(self):
        self.cmd.config = MN()
        self.cmd.config.channel = "1234"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )

    def test_exception_channel_too_short(self):
        self.cmd.config = MN()
        self.cmd.config.channel = "01"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )

    def test_exception_channel_invalid_characters(self):
        self.cmd.config = MN()
        self.cmd.config.channel = "ABC"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )
    
    def test_exception_channel_none(self):
        self.cmd.config = MN()
        self.cmd.config.channel = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )