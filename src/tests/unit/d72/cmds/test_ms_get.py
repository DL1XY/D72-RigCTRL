import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.ms_get import MSGet
from d72.cmds.serial_receiver import SerialReceiver

class TestBAGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = MSGet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
