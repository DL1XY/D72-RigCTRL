from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
import re
from d72.cmds.ms import MS

class MSSet(SerialCommand):

    config = MS()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if not re.match('^[a-zA-Z0-9]{1,8}$', self.config.msg):
            raise ValueError (f"Message {self.config.msg} is invalid")    
        return self._receiver.action(f"{self.config.cmd} {self.config.msg}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = MSSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
