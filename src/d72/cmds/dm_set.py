import re
from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.dm import DM

class DMSet(SerialCommand):

    config = DM()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if not re.match('^[0-9]{1}$', self.config.channel):
            raise ValueError (f"Channel {self.config.channel} is invalid")  
        if not re.match('^[A-F0-9 ]{16}$', self.config.dtmf):
            raise ValueError (f"DTMF code {self.config.dtmf} is invalid")    
        return self._receiver.action(f"{self.config.cmd} {self.config.channel},{self.config.dtmf}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = DMSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
