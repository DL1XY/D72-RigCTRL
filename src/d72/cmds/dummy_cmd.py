from serial_command import SerialCommand
from serial_receiver import SerialReceiver
from serial_invoker import SerialInvoker

class DummyCmd(SerialCommand):   
    ctrlc="\x03\x03\x03"
    
    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self) -> str:        
        return self._receiver.action(f"CS DL1XY") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = DummyCmd(rcv)    
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
