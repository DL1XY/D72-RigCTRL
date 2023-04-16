import re
from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from d72.cmds.cs import CS

class CSSet(SerialCommand):

    config = CS()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        if not re.match('^[a-zA-Z0-9]{1,6}$', self.config.callsign):
            raise ValueError (f"Callsign {self.config.callsign} is invalid") 
        return self._receiver.action(f"{self.config.cmd} {self.config.callsign}")     

if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = CSSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()  
