import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.ty_get import TYGet
from d72.cmds.serial_receiver import SerialReceiver

class TestTYGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps=SerialReceiver())
        self.rcvr.action = MagicMock(return_value="OK")    
        self.cmd = TYGet(self.rcvr)
    
    def test_execute_success(self):
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  