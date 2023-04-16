from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Band
from d72.cmds.cc import CC

class CCGet(SerialCommand):

    config = CC()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.band != Band.BAND_A.value and self.config.band.value != Band.BAND_B.value:
            raise ValueError (f"Band {self.config.band} outside valid range, should be {Band.BAND_A.value} or {Band.BAND_B.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.band}") 

if __name__ == "__main__":
    cfg = CC()
    cfg.band = Band.BAND_B    
    rcv = SerialReceiver()
    cmd = CCGet(rcv)
    cmd.config =cfg
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()