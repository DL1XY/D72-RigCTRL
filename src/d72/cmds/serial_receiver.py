from serial import Serial
from serial.serialutil import SerialException
from kivy.utils import platform

if platform == 'android':
    pass
    # from usb4a import usb
    # from usbserial4a import serial4a
else:
    from serial import Serial
    from serial import SerialException

class SerialReceiver:

    def __init__(self):
        """
        self.device_name_list = []
        self.serial_port = None
        self.read_thread = None
        self.port_thread_lock = threading.Lock()
        
        if platform == 'android':
            device = usb.get_usb_device(device_name)
            if not device:
                raise SerialException(
                    "Device {} not present!".format(device_name)
                )
            if not usb.has_usb_permission(device):
                usb.request_usb_permission(device)
                return
            self.serial_port = serial4a.get_serial_port(
                device_name,
                9600,
                8,
                'N',
                1,
                timeout=1
            )
            self.serial_port.xonxoff = 0
            self.serial_port.rtscts = 0
        else:
            self.serial_port = Serial(
                device_name,
                9600,
                8,
                'N',
                1,
                timeout=1
            )
            self.serial_port.xonxoff = 0
            self.serial_port.rtscts = 0
        
        if self.serial_port.is_open and not self.read_thread:
            self.read_thread = threading.Thread(target = self.read_msg_thread)
            self.read_thread.start()
        """
        if platform == 'android':
            pass
        else:
            self.ser = Serial()
            self.ser.baudrate = 9600
            self.ser.port = '/dev/ttyUSB0'
            self.ser.bytesize = 8
            self.ser.parity = 'N'
            self.ser.stopbits = 1
            self.ser.timeout = None
            self.ser.xonxoff = 0
            self.ser.rtscts = 0


    def action(self, cmd:str) -> str:        
        cmd = f"{cmd}\r"
        if platform == 'android':
                pass            
        else:
            try:
                if not self.ser.is_open:
                    self.ser.open()
                print(self.ser)
                print(f'serial write cmd:{cmd}')        
                self.ser.write(cmd.encode())

                print(f'serial read')        
                rcvd = ""
                while True:
                    c = self.ser.read()            
                    if len(c) == 0 or c == b'\r':
                        break
                    rcvd+= c.decode()
                print (f"received data:{rcvd}")
                return rcvd
            except SerialException:
                print(f"SerialException connecting serial")
            except:
                print(f"Error connecting serial")

    def close(self):
        if self.ser.is_open:
            self.ser.close()

        