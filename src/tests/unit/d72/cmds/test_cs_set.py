import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.cs_set import CSSet
from d72.cmds.cs import CS
from d72.cmds.serial_receiver import SerialReceiver

class TestCSSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = CSSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception_callsign_too_long(self):
        self.cmd.config = CS()
        self.cmd.config.callsign = "ABCDEFG"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Callsign {self.cmd.config.callsign} is invalid"
        )

    def test_exception_callsign_wrong_characters(self):
        self.cmd.config = CS()
        self.cmd.config.callsign = "DL1XY-"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Callsign {self.cmd.config.callsign} is invalid"
        )
    
    def test_exception_callsign_none(self):
        self.cmd.config = CS()
        self.cmd.config.callsign = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )