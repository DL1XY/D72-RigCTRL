from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
import re
from d72.cmds.me import ME

class MEGet(SerialCommand):

    config = ME()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):        
        if not re.match('^[0-9]{3}$', self.config.channel):
            raise ValueError (f"Channel {self.config.channel} is invalid")        
        return self._receiver.action(f"{self.config.cmd} {self.config.channel}") 

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = MEGet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)
    inv.execute_commands()

