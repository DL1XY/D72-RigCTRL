import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.me_get import MEGet
from d72.cmds.me import ME
from d72.cmds.serial_receiver import SerialReceiver

class TestMEGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = MEGet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    

    def test_exception_channel_too_long(self):
        self.cmd.config = ME()
        self.cmd.config.channel = "1111"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )

    def test_exception_channel_wrong_characters(self):
        self.cmd.config = ME()
        self.cmd.config.channel = "XYZ"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )
    
    def test_exception_channel_none(self):
        self.cmd.config = ME()
        self.cmd.config.channel = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )
  