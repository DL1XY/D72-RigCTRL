import re
from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Band
from d72.cmds.mr import MR

class MRSet(SerialCommand):

    config = MR()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self) -> None:
        if not re.match('^[0-9]{3}$', self.config.channel):
            raise ValueError (f"Channel {self.config.channel} is invalid")    
        if self.config.band != Band.BAND_A and self.config.band != Band.BAND_B:
            raise ValueError (f"Band {self.config.band} outside valid range, should be {Band.BAND_A.value} or {Band.BAND_B.value}")
        self._receiver.action(f"{self.config.cmd} {self.config.band},{self.config.channel}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = MRSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
