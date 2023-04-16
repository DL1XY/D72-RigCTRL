from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import DTMF
from d72.cmds.dt import DT

class DTSet(SerialCommand):

    config = DT()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.dtmf not in DTMF:
            raise ValueError (f"DTMF {self.config.dtmf} outside valid range, should be between {DTMF.DTMF_0.value} and {DTMF.DTMF_HZ_1633.value}")
        return self._receiver.action(f"{self.config.cmd} {self.config.dtmf}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = DTSet(rcv)    
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
