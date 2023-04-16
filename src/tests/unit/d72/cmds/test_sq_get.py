import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.sq_get import SQGet
from d72.cmds.sq import SQ
from d72.cmds.attributes import NegativeTest
from d72.cmds.serial_receiver import SerialReceiver

''' Test class for getting SO '''
class TestSQGet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps=SerialReceiver())
        self.rcvr.action = MagicMock(return_value="OK")    
        self.cmd = SQGet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()    
  
    def test_exception(self):
        self.cmd.config = SQ()
        self.cmd.config.band = NegativeTest.MINUS_ONE
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            "Band -1 outside valid range, should be 0 or 1"
        )