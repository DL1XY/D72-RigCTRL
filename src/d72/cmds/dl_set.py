from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import BandMode
from d72.cmds.dl import DL

class DLSet(SerialCommand):

    config = DL()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.bandMode not in BandMode:
            raise ValueError (f"Band mode {self.config.bandMode} outside valid range, should be {BandMode.DUAL.value} or {BandMode.SINGLE.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.bandMode}") 

if __name__ == "__main__":
    cfg = DL()
    cfg.bandMode = BandMode.DUAL  
    rcv = SerialReceiver()
    cmd = DLSet(rcv)
    cmd.config =cfg
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
