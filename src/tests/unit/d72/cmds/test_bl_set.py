import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.bl_set import BLSet
from d72.cmds.bl import BL
from d72.cmds.serial_receiver import SerialReceiver

class TestBLSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = BLSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception_backlightstatus_too_low(self):
        self.cmd.config = BL()
        self.cmd.config.backlightStatus = -1
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Backlight status -1 outside valid range, should be between 0 and 8"
        )
    
    def test_exception_backlightstatus_too_high(self):
        self.cmd.config = BL()
        self.cmd.config.backlightStatus = 9
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Backlight status 9 outside valid range, should be between 0 and 8"
        )
    
    def test_exception_backlightstatus_str(self):
        self.cmd.config = BL()
        self.cmd.config.backlightStatus = 'fail'
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"invalid literal for int() with base 10: 'fail'"
        )
    
    def test_exception_backlightstatus_empty(self):
        self.cmd.config = BL()
        self.cmd.config.backlightStatus = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"int() argument must be a string, a bytes-like object or a number, not 'NoneType'"
        )
