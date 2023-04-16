from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.attributes import BurstTone
from d72.cmds.bt import BT

class BTSet(SerialCommand):

    config = BT()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if self.config.burstTone not in BurstTone:
            raise ValueError (f"Burst tone {self.config.burstTone} outside valid range, should be between {BurstTone.FREQ_HZ_1000.value} and {BurstTone.FREQ_HZ_2100.value}")
        self._receiver.action(f"{self.config.cmd} {self.config.burstTone}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = BTSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
