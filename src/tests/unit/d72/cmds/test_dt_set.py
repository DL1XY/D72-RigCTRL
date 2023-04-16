import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.dt_set import DTSet
from d72.cmds.dt import DT
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.attributes import NegativeTest, DTMF

class TestDTSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = DTSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()
  
    def test_exception(self):
        self.cmd.config = DT()
        self.cmd.config.dtmf = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"DTMF {NegativeTest.MINUS_ONE} outside valid range, should be between {DTMF.DTMF_0.value} and {DTMF.DTMF_HZ_1633.value}"
        )
