from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import Reset
from d72.cmds.sr import SR

class SRSet(SerialCommand):

    config = SR()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.reset not in Reset:
            raise ValueError(f"Reset value {self.config.reset} outside valid range, should be bewteen {Reset.VFO.value} and {Reset.FULL.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.reset}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = SRSet(rcv)    
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()

