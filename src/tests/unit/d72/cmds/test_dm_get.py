import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.dm_get import DMGet
from d72.cmds.dm import DM
from d72.cmds.serial_receiver import SerialReceiver

class TestDMGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = DMGet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    

    def test_exception_channel_too_long(self):
        self.cmd.config = DM()
        self.cmd.config.channel = "111"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )

    def test_exception_channel_wrong_characters(self):
        self.cmd.config = DM()
        self.cmd.config.channel = "DL1XY-"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Channel {self.cmd.config.channel} is invalid"
        )
    
    def test_exception_channel_none(self):
        self.cmd.config = DM()
        self.cmd.config.channel = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )
  