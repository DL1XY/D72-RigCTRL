import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.tt_set import TTSet
from d72.cmds.serial_receiver import SerialReceiver

class TestTTSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps=SerialReceiver())
        self.rcvr.action = MagicMock(return_value="OK")    
        self.cmd = TTSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  