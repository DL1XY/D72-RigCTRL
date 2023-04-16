import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.bl_get import BLGet
from d72.cmds.serial_receiver import SerialReceiver

class TestBLGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = BLGet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
