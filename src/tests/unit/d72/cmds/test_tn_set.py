import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.tn_set import TNSet
from d72.cmds.tn import TN
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

class TestTNSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = TNSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
    # Band
    def test_exception_band(self):
        self.cmd.config = TN()
        self.cmd.config.band = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Band {NegativeTest.MINUS_ONE} outside valid range, should be between 0 and 3"
        ) 

    # TNC
    def test_exception_tnc(self):
        self.cmd.config = TN()
        self.cmd.config.tnc = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"TNC -1 outside valid range, should be between 0 and 2"
        )
    
   