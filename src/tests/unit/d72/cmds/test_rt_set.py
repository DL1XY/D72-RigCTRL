import unittest
from unittest.mock import Mock, MagicMock
from d72.cmds.rt_set import RTSet
from d72.cmds.rt import RT
from d72.cmds.serial_receiver import SerialReceiver
from dateutil.parser._parser import ParserError
class TestRTSet(unittest.TestCase):

    def setUp(self):
        self.rcvr = Mock(wraps = SerialReceiver())
        self.rcvr.action = MagicMock (return_value="OK")    
        self.cmd = RTSet(self.rcvr)
    
    def test_execute_success(self):       
        self.cmd.execute()
        self.rcvr.action.assert_called_once()  

    # year
    def test_exception_year_wrong_characters(self):
        self.cmd.config = RT()
        self.cmd.config.year = "ABC"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: ABC0308174000"
        )  
    
    def test_exception_year_too_long(self):
        self.cmd.config = RT()
        self.cmd.config.year = "20000"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        ) 
    
    def test_exception_year_too_short(self):
        self.cmd.config = RT()
        self.cmd.config.year = "10"
        with self.assertRaises(ParserError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"hour must be in 0..23: 100308174000"
        )
  
    def test_exception_year_none(self):
        self.cmd.config = RT()
        self.cmd.config.year = None
        with self.assertRaises(ParserError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: None0308174000"
        )
    
    # month
    def test_exception_month_wrong_characters(self):
        self.cmd.config = RT()
        self.cmd.config.month = "AB"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 2023AB08174000"
        )  
    
    def test_exception_month_too_long(self):
        self.cmd.config = RT()
        self.cmd.config.month = "123"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        ) 
    
    def test_exception_month_too_short(self):
        self.cmd.config = RT()
        self.cmd.config.month = "1"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        )
  
    def test_exception_month_none(self):
        self.cmd.config = RT()
        self.cmd.config.month = None
        with self.assertRaises(ParserError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 2023None08174000"
        )
    
    # day
    def test_exception_day_wrong_characters(self):
        self.cmd.config = RT()
        self.cmd.config.day = "AB"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 202303AB174000"
        )  
    
    def test_exception_day_too_long(self):
        self.cmd.config = RT()
        self.cmd.config.day = "123"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        ) 
    
    def test_exception_day_too_short(self):
        self.cmd.config = RT()
        self.cmd.config.day = "1"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        )
  
    def test_exception_day_none(self):
        self.cmd.config = RT()
        self.cmd.config.day = None
        with self.assertRaises(ParserError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 202303None174000"
        )
    
    # hour
    def test_exception_hour_wrong_characters(self):
        self.cmd.config = RT()
        self.cmd.config.hour = "AB"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 20230308AB4000"
        )  
    
    def test_exception_hour_too_long(self):
        self.cmd.config = RT()
        self.cmd.config.hour = "123"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        ) 
    
    def test_exception_hour_too_short(self):
        self.cmd.config = RT()
        self.cmd.config.hour = "1"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        )
  
    def test_exception_hour_none(self):
        self.cmd.config = RT()
        self.cmd.config.hour = None
        with self.assertRaises(ParserError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 20230308None4000"
        )
    
    # minutes
    def test_exception_minutes_wrong_characters(self):
        self.cmd.config = RT()
        self.cmd.config.minute = "AB"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 2023030817AB00"
        )  
    
    def test_exception_minutes_too_long(self):
        self.cmd.config = RT()
        self.cmd.config.minute = "123"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        ) 
    
    def test_exception_minutes_too_short(self):
        self.cmd.config = RT()
        self.cmd.config.minute = "1"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        )
  
    def test_exception_minutes_none(self):
        self.cmd.config = RT()
        self.cmd.config.minute = None
        with self.assertRaises(ParserError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 2023030817None00"
        )

    # second
    def test_exception_second_wrong_characters(self):
        self.cmd.config = RT()
        self.cmd.config.second = "&$"
        with self.assertRaises(ValueError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 202303081740&$"
        )  
    
    def test_exception_second_too_long(self):
        self.cmd.config = RT()
        self.cmd.config.second = "123"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        ) 
    
    def test_exception_second_too_short(self):
        self.cmd.config = RT()
        self.cmd.config.second = "1"
        with self.assertRaises(OverflowError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"signed integer is greater than maximum"
        )
  
    def test_exception_second_none(self):
        self.cmd.config = RT()
        self.cmd.config.second = None
        with self.assertRaises(ParserError) as exception_context:
            self.cmd.execute()
        
        self.assertEqual(
            str(exception_context.exception),
            f"Unknown string format: 202303081740None"
        )