import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.cc_set import CCSet
from d72.cmds.cc import CC
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestCCSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = CCSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()  

    # Band     
    def test_exception_band_low(self):
        self.cmd.config = CC()
        self.cmd.config.band = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Band {NegativeTest.MINUS_ONE} outside valid range, should be between 0 and 3"
        )

    def test_exception_band_high(self):
        self.cmd.config = CC()
        self.cmd.config.band = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Band {NegativeTest.PLUS_MILLION} outside valid range, should be between 0 and 3"
        )

    def test_exception_band_none(self):
        self.cmd.config = CC()
        self.cmd.config.band = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )

    # frequency     
    def test_exception_frequency_too_long(self):
        self.cmd.config = CC()
        self.cmd.config.frequency = "0123456789012345678"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Frequency {self.cmd.config.frequency} is invalid"
        )

    def test_exception_frequency_too_short(self):
        self.cmd.config = CC()
        self.cmd.config.frequency = "012"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Frequency {self.cmd.config.frequency} is invalid"
        )

    def test_exception_frequency_invalid_characters(self):
        self.cmd.config = CC()
        self.cmd.config.frequency = "AABBCCDDEE"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Frequency {self.cmd.config.frequency} is invalid"
        )
    
    def test_exception_frequency_none(self):
        self.cmd.config = CC()
        self.cmd.config.frequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )

    # StepSize     
    def test_exception_stepsize_low(self):
        self.cmd.config = CC()
        self.cmd.config.stepSize = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Step size {NegativeTest.MINUS_ONE} outside valid range, should be between 0 and A"
        )

    def test_exception_stepsize_high(self):
        self.cmd.config = CC()
        self.cmd.config.stepSize = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Step size {NegativeTest.PLUS_MILLION} outside valid range, should be between 0 and A"
        )

    def test_exception_stepsize_none(self):
        self.cmd.config = CC()
        self.cmd.config.stepSize = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
     # Shift      
    def test_exception_shift_low(self):
        self.cmd.config = CC()
        self.cmd.config.shift = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Shift {NegativeTest.MINUS_ONE} outside valid range, should be between 0 and 3"
        )

    def test_exception_shift_high(self):
        self.cmd.config = CC()
        self.cmd.config.shift = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Shift {NegativeTest.PLUS_MILLION} outside valid range, should be between 0 and 3"
        )

    def test_exception_shift_none(self):
        self.cmd.config = CC()
        self.cmd.config.shift = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # reverse      
    def test_exception_reverse_low(self):
        self.cmd.config = CC()
        self.cmd.config.reverse = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Reverse {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )

    def test_exception_reverse_high(self):
        self.cmd.config = CC()
        self.cmd.config.reverse = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Reverse {NegativeTest.PLUS_MILLION} outside valid range, should be 0 or 1"
        )

    def test_exception_reverse_none(self):
        self.cmd.config = CC()
        self.cmd.config.reverse = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # toneStatus      
    def test_exception_toneStatus_low(self):
        self.cmd.config = CC()
        self.cmd.config.toneStatus = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Tone status {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )

    def test_exception_toneStatus_high(self):
        self.cmd.config = CC()
        self.cmd.config.toneStatus = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Tone status {NegativeTest.PLUS_MILLION} outside valid range, should be 0 or 1"
        )

    def test_exception_toneStatus_none(self):
        self.cmd.config = CC()
        self.cmd.config.toneStatus = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # ctcssStatus      
    def test_exception_ctcssStatus_low(self):
        self.cmd.config = CC()
        self.cmd.config.ctcssStatus = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"CTCSS status {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )

    def test_exception_ctcssStatus_high(self):
        self.cmd.config = CC()
        self.cmd.config.ctcssStatus = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"CTCSS status {NegativeTest.PLUS_MILLION} outside valid range, should be 0 or 1"
        )

    def test_exception_ctcssStatus_none(self):
        self.cmd.config = CC()
        self.cmd.config.ctcssStatus = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # dcsStatus      
    def test_exception_dcsStatus_low(self):
        self.cmd.config = CC()
        self.cmd.config.dcsStatus = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"DCS status {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )

    def test_exception_dcsStatus_high(self):
        self.cmd.config = CC()
        self.cmd.config.dcsStatus = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"DCS status {NegativeTest.PLUS_MILLION} outside valid range, should be 0 or 1"
        )

    def test_exception_dcsStatus_none(self):
        self.cmd.config = CC()
        self.cmd.config.dcsStatus = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # splitTone      
    def test_exception_splitTone_low(self):
        self.cmd.config = CC()
        self.cmd.config.splitTone = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Split tone {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )

    def test_exception_splitTone_high(self):
        self.cmd.config = CC()
        self.cmd.config.splitTone = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Split tone {NegativeTest.PLUS_MILLION} outside valid range, should be 0 or 1"
        )

    def test_exception_splitTone_none(self):
        self.cmd.config = CC()
        self.cmd.config.splitTone = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # toneFrequency      
    def test_exception_toneFrequency_low(self):
        self.cmd.config = CC()
        self.cmd.config.toneFrequency = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Tone frequency {NegativeTest.MINUS_ONE} outside valid range, should be between 01 and 42"
        )

    def test_exception_toneFrequency_high(self):
        self.cmd.config = CC()
        self.cmd.config.toneFrequency = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Tone frequency {NegativeTest.PLUS_MILLION} outside valid range, should be between 01 and 42"
        )

    def test_exception_toneFrequency_none(self):
        self.cmd.config = CC()
        self.cmd.config.toneFrequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # ctcssFrequency      
    def test_exception_ctcssFrequency_low(self):
        self.cmd.config = CC()
        self.cmd.config.ctcssFrequency = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"CTCSS frequency {NegativeTest.MINUS_ONE} outside valid range, should be between 01 and 42"
        )

    def test_exception_ctcssFrequency_high(self):
        self.cmd.config = CC()
        self.cmd.config.ctcssFrequency = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"CTCSS frequency {NegativeTest.PLUS_MILLION} outside valid range, should be between 01 and 42"
        )

    def test_exception_ctcssFrequency_none(self):
        self.cmd.config = CC()
        self.cmd.config.ctcssFrequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # dcsFrequency      
    def test_exception_dcsFrequency_low(self):
        self.cmd.config = CC()
        self.cmd.config.dcsFrequency = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"DCS frequency {NegativeTest.MINUS_ONE} outside valid range, should be between 000 and 754"
        )

    def test_exception_dcsFrequency_high(self):
        self.cmd.config = CC()
        self.cmd.config.dcsFrequency = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"DCS frequency {NegativeTest.PLUS_MILLION} outside valid range, should be between 000 and 754"
        )

    def test_exception_dcsFrequency_none(self):
        self.cmd.config = CC()
        self.cmd.config.dcsFrequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )
    
    # crossTone      
    def test_exception_crossTone_low(self):
        self.cmd.config = CC()
        self.cmd.config.crossTone = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Cross tone {NegativeTest.MINUS_ONE} outside valid range, should be between 0 and 3"
        )

    def test_exception_crossTone_high(self):
        self.cmd.config = CC()
        self.cmd.config.crossTone = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Cross tone {NegativeTest.PLUS_MILLION} outside valid range, should be between 0 and 3"
        )

    def test_exception_crossTone_none(self):
        self.cmd.config = CC()
        self.cmd.config.crossTone = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )

    # offsetFrequency     
    def test_exception_offsetFrequency_too_long(self):
        self.cmd.config = CC()
        self.cmd.config.offsetFrequency = "0123456789012345678"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Offset frequency {self.cmd.config.offsetFrequency} is invalid"
        )

    def test_exception_offsetFrequency_too_short(self):
        self.cmd.config = CC()
        self.cmd.config.offsetFrequency = "012"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Offset frequency {self.cmd.config.offsetFrequency} is invalid"
        )

    def test_exception_offsetFrequency_invalid_characters(self):
        self.cmd.config = CC()
        self.cmd.config.offsetFrequency = "AABBCCDD"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Offset frequency {self.cmd.config.offsetFrequency} is invalid"
        )
    
    def test_exception_offsetFrequency_none(self):
        self.cmd.config = CC()
        self.cmd.config.offsetFrequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )
    # mode      
    def test_exception_mode_low(self):
        self.cmd.config = CC()
        self.cmd.config.mode = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Mode {NegativeTest.MINUS_ONE} outside valid range, should be between 0 and 2"
        )

    def test_exception_mode_high(self):
        self.cmd.config = CC()
        self.cmd.config.mode = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Mode {NegativeTest.PLUS_MILLION} outside valid range, should be between 0 and 2"
        )

    def test_exception_mode_none(self):
        self.cmd.config = CC()
        self.cmd.config.mode = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )

     # txFrequency     
    def test_exception_txFrequency_too_long(self):
        self.cmd.config = CC()
        self.cmd.config.txFrequency = "0123456789012345678"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"TX frequency {self.cmd.config.txFrequency} is invalid"
        )

    def test_exception_txFrequency_too_short(self):
        self.cmd.config = CC()
        self.cmd.config.txFrequency = "012"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"TX frequency {self.cmd.config.txFrequency} is invalid"
        )

    def test_exception_txFrequency_invalid_characters(self):
        self.cmd.config = CC()
        self.cmd.config.txFrequency = "AABBCCDDEE"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"TX frequency {self.cmd.config.txFrequency} is invalid"
        )
    
    def test_exception_txFrequency_none(self):
        self.cmd.config = CC()
        self.cmd.config.txFrequency = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )

    # lockout      
    def test_exception_lockout_low(self):
        self.cmd.config = CC()
        self.cmd.config.lockout = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Lock out {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )

    def test_exception_lockout_high(self):
        self.cmd.config = CC()
        self.cmd.config.lockout = NegativeTest.PLUS_MILLION
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Lock out {NegativeTest.PLUS_MILLION} outside valid range, should be 0 or 1"
        )

    def test_exception_lockout_none(self):
        self.cmd.config = CC()
        self.cmd.config.lockout = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"unsupported operand type(s) for 'in': 'NoneType' and 'EnumMeta'"
        )