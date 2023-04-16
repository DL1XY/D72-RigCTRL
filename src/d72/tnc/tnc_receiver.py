import serial

class TncReceiver:

    def __init__(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.port = '/dev/ttyUSB0'
        self.ser.bytesize = 8
        self.ser.parity = 'N'
        self.ser.stopbits = 1
        self.ser.timeout = None
        self.ser.xonxoff = 0
        self.ser.rtscts = 0


    def action(self, cmd:str) -> None:        
        cmd = f"{cmd}\r"
        if not self.ser.is_open:
            self.ser.open()
        print(self.ser)
        print(f'serial write cmd:{cmd}')        
        self.ser.write(cmd.encode())

        print(f'serial read')        
        rcvd = ""
        while True:
            c = self.ser.readline()            
            
        print (f"received data:{rcvd}")
     
  