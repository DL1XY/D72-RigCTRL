import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.ba_get import BAGet
from d72.cmds.serial_receiver import SerialReceiver

class TestBAGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = BAGet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  