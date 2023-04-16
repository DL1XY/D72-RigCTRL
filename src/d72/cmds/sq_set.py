from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Band, Squelch
from d72.cmds.sq import SQ

class SQSet(SerialCommand):

    config = SQ()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.band != Band.BAND_A and self.config.band != Band.BAND_B:
            raise ValueError (f"Band {self.config.band} outside valid range, should be {Band.BAND_A.value} or {Band.BAND_B.value}")
        if self.config.squelch not in Squelch:
            raise ValueError (f"Squelch {self.config.squelch} outside valid range, should be between {Squelch.VAL_0.value} and {Squelch.VAL_5.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.band},{self.config.squelch}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = SQSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()

