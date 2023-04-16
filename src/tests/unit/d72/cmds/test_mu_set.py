import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.mu_set import MUSet
from d72.cmds.mu import MU
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestMUSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = MUSet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
    
    # lampTimer
    def test_exception_lampTimer(self):
        self.cmd.config = MU()
        self.cmd.config.lampTimer = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Lamp timer -1 outside valid range, should be between 2 and A"
        )
    
    # contrast
    def test_exception_contrast_too_long(self):
        self.cmd.config = MU()
        self.cmd.config.contrast = "12"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Contrast {self.cmd.config.contrast} is invalid, should be 0 to F"
        )

    def test_exception_contrast_wrong_characters(self):
        self.cmd.config = MU()
        self.cmd.config.contrast = "#"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Contrast {self.cmd.config.contrast} is invalid, should be 0 to F"
        )
    
    def test_exception_contrast_none(self):
        self.cmd.config = MU()
        self.cmd.config.contrast = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )
    
    # batterySaver
    def test_exception_batterySaver(self):
        self.cmd.config = MU()
        self.cmd.config.batterySaver = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Battery saver -1 outside valid range, should be between 0 and A"    
        )

    # apo
    def test_exception_apo(self):
        self.cmd.config = MU()
        self.cmd.config.apo = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"APO -1 outside valid range, should be between 0 and 3"    
        )
    
    # audioRadioGPS
    def test_exception_audioRadioGPS(self):
        self.cmd.config = MU()
        self.cmd.config.audioRadioGPS = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Audio/Radio/GPS -1 outside valid range, should be between 0 and 3"    
        )

    # vhfAIP
    def test_exception_vhfAIP(self):
        self.cmd.config = MU()
        self.cmd.config.vhfAIP = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"VHF AIP -1 invalid, should be 0 or 1"    
        )
    
    # uhfAIP
    def test_exception_uhfAIP(self):
        self.cmd.config = MU()
        self.cmd.config.uhfAIP = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"UHF AIP -1 invalid, should be 0 or 1"    
        )
    
    # vox
    def test_exception_vox(self):
        self.cmd.config = MU()
        self.cmd.config.vox = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"VOX -1 invalid, should be 0 or 1"    
        )
    
    # voxGain
    def test_exception_voxGain_too_long(self):
        self.cmd.config = MU()
        self.cmd.config.voxGain = "12"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"VOX gain {self.cmd.config.voxGain} is invalid, should be 0 to 9"
        )

    def test_exception_voxGain_wrong_characters(self):
        self.cmd.config = MU()
        self.cmd.config.voxGain = "#"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"VOX gain {self.cmd.config.voxGain} is invalid, should be 0 to 9"
        )
    
    def test_exception_voxGain_none(self):
        self.cmd.config = MU()
        self.cmd.config.voxGain = None
        with self.assertRaises(TypeError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"expected string or bytes-like object"
        )
    
    # voxDelay
    def test_exception_voxDelay(self):
        self.cmd.config = MU()
        self.cmd.config.voxDelay = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"VOX delay -1 outside valid range, should be between 0 and 6"    
        )
    
    # voxOnBusy
    def test_exception_voxOnBusy(self):
        self.cmd.config = MU()
        self.cmd.config.voxOnBusy = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"VOX on busy -1 invalid, should be 0 or 1"    
        )
    
    # beatShift
    def test_exception_beatShift(self):
        self.cmd.config = MU()
        self.cmd.config.beatShift = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Beat shift -1 outside valid range, should be between 0 and 7"    
        )
    
    # txInhibit
    def test_exception_txInhibit(self):
        self.cmd.config = MU()
        self.cmd.config.txInhibit = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"TX inhibit -1 invalid, should be 0 or 1"    
        )
    
    # balance
    def test_exception_balance(self):
        self.cmd.config = MU()
        self.cmd.config.balance = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Balance -1 outside valid range, should be between 0 and 4"    
        )
    
    # recall
    def test_exception_recall(self):
        self.cmd.config = MU()
        self.cmd.config.recall = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Recall -1 invalid, should be 0 or 1"    
        )
    
    # scanResume
    def test_exception_scanResume(self):
        self.cmd.config = MU()
        self.cmd.config.scanResume = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Scan resume -1 outside valid range, should be between 0 and 2"    
        )
    
    # timeRestart
    def test_exception_timeRestart(self):
        self.cmd.config = MU()
        self.cmd.config.timeRestart = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Time restart -1 outside valid range, should be between 1 and A"    
        )
    
    # carrierRestart
    def test_exception_carrierRestart(self):
        self.cmd.config = MU()
        self.cmd.config.carrierRestart = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Carrier restart -1 outside valid range, should be between 1 and A"    
        )
    
    # autoOffset
    def test_exception_autoOffset(self):
        self.cmd.config = MU()
        self.cmd.config.autoOffset = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Auto offset -1 invalid, should be 0 or 1"    
        )