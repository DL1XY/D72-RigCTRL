import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.ms_set import MSSet
from d72.cmds.ms import MS
from d72.cmds.serial_receiver import SerialReceiver

class TestMSSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = MSSet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    

    def test_exception_channel_too_long(self):
        self.cmd.config = MS()
        self.cmd.config.msg = "ABCD12345"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Message {self.cmd.config.msg} is invalid"
        )

    def test_exception_channel_wrong_characters(self):
        self.cmd.config = MS()
        self.cmd.config.msg = ";*(#)"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Message {self.cmd.config.msg} is invalid"
        )
    
    def test_exception_channel_none(self):
        self.cmd.config = MS()
        self.cmd.config.msg = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )
  