import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.dl_set import DLSet
from d72.cmds.dl import DL
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestDLSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = DLSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception(self):
        self.cmd.config = DL()
        self.cmd.config.bandMode = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Band mode {NegativeTest.MINUS_ONE} outside valid range, should be 0 or 1"
        )
