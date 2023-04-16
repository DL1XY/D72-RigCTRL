import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.ba_set import BASet
from d72.cmds.ba import BA
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestBASet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = BASet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception(self):
        self.cmd.config = BA()
        self.cmd.config.batteryType = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Battery type {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )

    def test_exception_batteryType_str(self):
        self.cmd.config = BA()
        self.cmd.config.batteryType = 'fail'
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'str' and 'EnumMeta'"
        )
    
    def test_exception_batteryType_empty(self):
        self.cmd.config = BA()
        self.cmd.config.batteryType = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )