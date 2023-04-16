import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.gm_set import GMSet
from d72.cmds.gm import GM
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest

class TestGMSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = GMSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception(self):
        self.cmd.config = GM()
        self.cmd.config.radioGpsMode = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Radio/GPS mode -1 outside valid range, should be 0 or 1"
        )
