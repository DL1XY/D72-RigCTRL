from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import FirmwareType
from d72.cmds.fv import FV

class FVGet(SerialCommand):

    config = FV()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.firmwareType not in FirmwareType:
            raise ValueError (f"Firmware type {self.config.firmwareType} outside valid range, should be between {FirmwareType.MAIN.value} or {FirmwareType.TNC.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.firmwareType}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = FVGet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()  

    
