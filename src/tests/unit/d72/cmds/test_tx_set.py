import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.tx_set import TXSet
from d72.cmds.serial_receiver import SerialReceiver

class TestTXSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps=SerialReceiver())
        self.rcvr.action = MagicMock(return_value="OK")    
        self.cmd = TXSet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  