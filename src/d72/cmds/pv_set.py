import re
from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import ProgrammableVFOBand
from d72.cmds.pv import PV

class PVSet(SerialCommand):

    config = PV()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if not re.match('^[0-9]{4}$', self.config.lowerFrequency):
            raise ValueError (f"Lower frequency {self.config.lowerFrequency} is invalid")    
        if not re.match('^[0-9]{4}$', self.config.upperFrequency):
            raise ValueError (f"Upper frequency {self.config.upperFrequency} is invalid")
        if self.config.vfoBand not in ProgrammableVFOBand:
            raise ValueError (f"VFO band {self.config.vfoBand} outside valid range, should be between {ProgrammableVFOBand.A_BAND_136.value} and {ProgrammableVFOBand.B_BAND_400.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.vfoBand},{self.config.lowerFrequency},{self.config.upperFrequency}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = PVSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
