from d72.cmds.serial_command import SerialCommand
from d72.cmds.serial_receiver import SerialReceiver
from d72.cmds.serial_invoker import SerialInvoker
from dateutil import parser as date_parser
from d72.cmds.rt import RT

class RTSet(SerialCommand):

    config = RT()

    def __init__(self, receiver: SerialReceiver) -> None:
        self._receiver = receiver

    def execute(self):
        date = f"{self.config.year}{self.config.month}{self.config.day}{self.config.hour}{self.config.minute}{self.config.second}"
        date_parser.parse(date)
        self._receiver.action(f"{self.config.cmd} {date}") 
    
if __name__ == "__main__":
    rcv = SerialReceiver()
    cmd = RTSet(rcv)
    inv = SerialInvoker()
    inv.store_command(cmd)       
    inv.execute_commands()
