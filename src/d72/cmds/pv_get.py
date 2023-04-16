from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import ProgrammableVFOBand
from d72.cmds.pv import PV

class PVGet(SerialCommand):

    config = PV()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):        
        if self.config.vfoBand not in ProgrammableVFOBand:
            raise ValueError (f"VFO band {self.config.vfoBand} outside valid range, should be between {ProgrammableVFOBand.A_BAND_136.value} and {ProgrammableVFOBand.B_BAND_400.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.vfoBand}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = PVGet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()