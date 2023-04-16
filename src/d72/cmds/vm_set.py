from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Band, MemoryVFOMode
from d72.cmds.vm import VM

class VMSet(SerialCommand):

    config = VM()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.band != Band.BAND_A and self.config.band != Band.BAND_B:
            raise ValueError (f"Band {self.config.band} outside valid range, should be {Band.BAND_A.value} or {Band.BAND_B.value}")
        if self.config.memoryVFOMode not in MemoryVFOMode:
            raise ValueError (f"Memory VFO mode {self.config.memoryVFOMode} outside valid range, should be between {MemoryVFOMode.VFO.value} and {MemoryVFOMode.WX.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.band},{self.config.memoryVFOMode}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = VMSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()  
