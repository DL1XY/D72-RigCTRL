from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Band, Power
from d72.cmds.pc import PC

class PCSet(SerialCommand):

    config = PC()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.band != Band.BAND_A and self.config.band != Band.BAND_B:
            raise ValueError (f"Band {self.config.band} outside valid range, should be {Band.BAND_A.value} or {Band.BAND_B.value}")
        if self.config.power not in Power:
            raise ValueError (f"Power {self.config.power} outside valid range, should be between {Power.HIGH.value} and {Power.EXTRA_LOW.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.band},{self.config.power}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = PCSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
