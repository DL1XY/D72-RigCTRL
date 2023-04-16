import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.pv_set import PVSet
from d72.cmds.pv import PV
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestPVSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = PVSet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
    def test_exception_vfoband(self):
        self.cmd.config = PV()
        self.cmd.config.vfoBand = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"VFO band -1 outside valid range, should be between 0 and 5"
        )
    
    def test_exception_vfoband_none(self):
        self.cmd.config = PV()
        self.cmd.config.vfoBand = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )

    # lowerFrequency
    def test_exception_lowerFrequency_too_long(self):
        self.cmd.config = PV()
        self.cmd.config.lowerFrequency = "122434"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Lower frequency {self.cmd.config.lowerFrequency} is invalid"
        )

    def test_exception_lowerFrequency_too_short(self):
        self.cmd.config = PV()
        self.cmd.config.lowerFrequency = "123"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Lower frequency {self.cmd.config.lowerFrequency} is invalid"
        )
    
    def test_exception_lowerFrequency_wrong_characters(self):
        self.cmd.config = PV()
        self.cmd.config.lowerFrequency = "#"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Lower frequency {self.cmd.config.lowerFrequency} is invalid"
        )
    
    def test_exception_lowerFrequency_none(self):
        self.cmd.config = PV()
        self.cmd.config.lowerFrequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )

    # upperFrequency
    def test_exception_upperFrequency_too_long(self):
        self.cmd.config = PV()
        self.cmd.config.upperFrequency = "121243"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Upper frequency {self.cmd.config.upperFrequency} is invalid"
        )

    def test_exception_upperFrequency_too_short(self):
        self.cmd.config = PV()
        self.cmd.config.upperFrequency = "123"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Upper frequency {self.cmd.config.upperFrequency} is invalid"
        )

    def test_exception_upperFrequency_wrong_characters(self):
        self.cmd.config = PV()
        self.cmd.config.upperFrequency = "#"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Upper frequency {self.cmd.config.upperFrequency} is invalid"
        )
    
    def test_exception_upperFrequency_none(self):
        self.cmd.config = PV()
        self.cmd.config.upperFrequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )